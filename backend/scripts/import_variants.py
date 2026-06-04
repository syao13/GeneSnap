#!/usr/bin/env python3
"""Bulk import variants from ClinVar, GWAS Catalog, and PharmGKB into the genesnap DB.

Usage:
    uv run scripts/import_variants.py --pharmgkb path/to/clinical_annotations.tsv
    uv run scripts/import_variants.py --skip-gwas --skip-pharmgkb
    uv run scripts/import_variants.py --dry-run
    uv run scripts/import_variants.py --clinvar-file path/to/clinvar.vcf.gz
"""

import argparse
import json
import sqlite3
import sys
import tempfile
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

# Add scripts/ directory to path so sources/ sub-package is importable
sys.path.insert(0, str(Path(__file__).parent))

from sources.clinvar import parse_clinvar_vcf
from sources.gwas import parse_gwas_tsv
from sources.pharmgkb import parse_pharmgkb_annotations

CLINVAR_URL = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz"
GWAS_URL = "https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations-full.zip"
STAR_ALLELES_PATH = Path(__file__).parent / "data" / "star_allele_rsids.json"

TODAY = date.today().isoformat()


def _download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    urllib.request.urlretrieve(url, dest)
    size_mb = dest.stat().st_size / 1_000_000
    print(f"  -> {dest.name} ({size_mb:.0f}MB)")


def _insert_batch(
    conn: sqlite3.Connection,
    variants: list,
    interpretations: list,
) -> tuple[int, int]:
    """Insert a batch of variants and interpretations using INSERT OR IGNORE.

    Returns (inserted, skipped).
    """
    inserted = 0
    skipped = 0
    for v in variants:
        result = conn.execute(
            """INSERT OR IGNORE INTO variants
            (rsid, gene, category, name, significance, description,
             risk_allele, normal_allele, chromosome, position, source,
             external_ids, publications, clinvar_stars, odds_ratio, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                v["rsid"], v["gene"], v["category"], v["name"], v["significance"],
                v["description"], v.get("risk_allele"), v.get("normal_allele"),
                v["chromosome"], v["position"], v["source"],
                json.dumps(v["external_ids"]) if v.get("external_ids") is not None else None,
                json.dumps(v["publications"]) if v.get("publications") is not None else None,
                v.get("clinvar_stars", 0), v.get("odds_ratio"), TODAY,
            ),
        )
        if result.rowcount > 0:
            inserted += 1
        else:
            skipped += 1

    for interp in interpretations:
        conn.execute(
            """INSERT OR IGNORE INTO genotype_interpretations
            (rsid, genotype, interpretation, risk_level) VALUES (?, ?, ?, ?)""",
            (interp["rsid"], interp["genotype"], interp["interpretation"], interp["risk_level"]),
        )

    return inserted, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pharmgkb", type=Path, help="Path to PharmGKB clinical_annotations.tsv")
    parser.add_argument(
        "--clinvar-file", type=Path, help="Use existing ClinVar VCF (skip download)"
    )
    parser.add_argument("--gwas-file", type=Path, help="Use existing GWAS TSV (skip download)")
    parser.add_argument("--skip-clinvar", action="store_true")
    parser.add_argument("--skip-gwas", action="store_true")
    parser.add_argument("--skip-pharmgkb", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Parse and count only, no DB writes")
    parser.add_argument("--db", type=Path, help="Override DB path (default: from settings)")
    args = parser.parse_args()

    # Resolve DB path
    if args.db:
        db_path = args.db
    else:
        from genesnap.config import settings
        db_path = settings.db_path

    if not args.dry_run and not db_path.exists():
        print(f"Error: DB not found at {db_path}. Run seed.py first.")
        sys.exit(1)

    conn: sqlite3.Connection | None = None if args.dry_run else sqlite3.connect(db_path)

    total_inserted = 0
    total_skipped = 0
    rsid_alleles: dict[str, tuple[str, str]] = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # --- ClinVar ---
        if not args.skip_clinvar:
            clinvar_path = args.clinvar_file or tmp / "clinvar.vcf.gz"
            if not args.clinvar_file:
                _download(CLINVAR_URL, clinvar_path)

            print("Parsing ClinVar VCF...")
            clinvar_results, rsid_alleles = parse_clinvar_vcf(clinvar_path)

            variants_batch = [v for v, _ in clinvar_results]
            interps_batch = [i for _, interps in clinvar_results for i in interps]
            x_mt_skipped = sum(
                1 for v, interps in clinvar_results
                if not interps and v.get("chromosome", "") in {"X", "Y", "MT"}
            )

            if conn is not None:
                ins, skp = _insert_batch(conn, variants_batch, interps_batch)
                conn.commit()
            else:
                ins, skp = len(variants_batch), 0

            print(
                f"  ClinVar: {ins} inserted, {skp} skipped (already in DB), "
                f"{x_mt_skipped} sex/MT chrom (no interpretations)"
            )
            total_inserted += ins
            total_skipped += skp

        # --- GWAS Catalog ---
        if not args.skip_gwas:
            gwas_path = args.gwas_file
            if not gwas_path:
                zip_path = tmp / "gwas_catalog.zip"
                _download(GWAS_URL, zip_path)
                print("  Extracting GWAS TSV from ZIP...")
                with zipfile.ZipFile(zip_path) as zf:
                    tsv_names = [n for n in zf.namelist() if n.endswith(".tsv")]
                    if not tsv_names:
                        raise RuntimeError("No TSV found inside GWAS ZIP")
                    gwas_path = tmp / tsv_names[0]
                    zf.extract(tsv_names[0], tmp)

            print("Parsing GWAS Catalog TSV...")
            variants_batch = []
            interps_batch = []
            for variant, interps in parse_gwas_tsv(gwas_path, rsid_alleles):
                variants_batch.append(variant)
                interps_batch.extend(interps)

            if conn is not None:
                ins, skp = _insert_batch(conn, variants_batch, interps_batch)
                conn.commit()
            else:
                ins, skp = len(variants_batch), 0

            print(f"  GWAS: {ins} inserted, {skp} skipped (already in DB)")
            total_inserted += ins
            total_skipped += skp

        # --- PharmGKB ---
        if not args.skip_pharmgkb:
            if not args.pharmgkb:
                print(
                    "Skipping PharmGKB (no --pharmgkb path provided). "
                    "Download clinical_annotations.tsv from pharmgkb.org and re-run with "
                    "--pharmgkb path/to/clinical_annotations.tsv"
                )
            else:
                print("Parsing PharmGKB annotations...")
                variants_batch = []
                interps_batch = []
                for variant, interps in parse_pharmgkb_annotations(
                    args.pharmgkb, STAR_ALLELES_PATH
                ):
                    variants_batch.append(variant)
                    interps_batch.extend(interps)

                if conn is not None:
                    ins, skp = _insert_batch(conn, variants_batch, interps_batch)
                    conn.commit()
                else:
                    ins, skp = len(variants_batch), 0

                print(f"  PharmGKB: {ins} inserted, {skp} skipped (already in DB)")
                total_inserted += ins
                total_skipped += skp

    if conn is not None:
        cursor = conn.execute("SELECT COUNT(*) FROM variants")
        total_in_db = cursor.fetchone()[0]
        conn.close()
        print(
            f"\nDone. {total_inserted} new variants inserted, {total_skipped} skipped. "
            f"DB now contains {total_in_db} variants."
        )
    else:
        print(
            f"\nDry run complete. Would insert {total_inserted} variants "
            f"(skipped {total_skipped} already in DB)."
        )


if __name__ == "__main__":
    main()
