"""PharmGKB clinical annotations parser: filters to CPIC Level 1A/1B."""

import csv
import json
from collections.abc import Iterator
from datetime import date
from pathlib import Path

from sources.templates import pharmgkb_interpretations

from genesnap.db.variants._types import InterpretationDict, VariantDict

TODAY = date.today().isoformat()

ALLOWED_LEVELS = {"1A", "1B"}


def _load_star_alleles(json_path: Path) -> dict[str, dict[str, str]]:
    with open(json_path) as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def parse_pharmgkb_annotations(
    tsv_path: Path,
    star_allele_path: Path,
) -> Iterator[tuple[VariantDict, list[InterpretationDict]]]:
    """Parse PharmGKB clinical_annotations.tsv or clinicalVariants.tsv.

    Supports both column naming conventions:
      - clinical_annotations.tsv: "Variant/Haplotypes", "Level of Evidence", "Drug(s)", "Phenotype(s)"
      - clinicalVariants.tsv:     "variant",             "level of evidence", "chemicals",  "phenotypes"

    Multi-allele rows (comma-separated star alleles like "CYP2C9*1, CYP2C9*3") are skipped —
    these describe diplotypes rather than single variants. Only single rsIDs and single star
    alleles are processed. Star alleles are resolved via star_allele_rsids.json.
    """
    star_alleles = _load_star_alleles(star_allele_path)
    seen_rsids: set[str] = set()

    with open(tsv_path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            # Support both column naming conventions
            level = (
                row.get("Level of Evidence")
                or row.get("level of evidence")
                or ""
            ).strip()
            if level not in ALLOWED_LEVELS:
                continue

            variant_field = (
                row.get("Variant/Haplotypes")
                or row.get("variant")
                or ""
            ).strip()
            gene = row.get("Gene") or row.get("gene") or ""
            gene = gene.strip()
            drug = (row.get("Drug(s)") or row.get("chemicals") or "").strip().lower()
            phenotype = (row.get("Phenotype(s)") or row.get("phenotypes") or "").strip()

            # Skip multi-allele rows (diplotype descriptions like "CYP2C9*1, CYP2C9*3")
            if "," in variant_field:
                continue

            # Resolve rsID and alleles
            if variant_field.startswith("rs"):
                rsid = variant_field
                # For direct rsIDs, look up alleles in star_alleles by rsid match
                allele_entry = next(
                    (v for v in star_alleles.values() if v["rsid"] == rsid),
                    None,
                )
                if allele_entry is None:
                    continue  # No allele data available; can't generate interpretations
                ref = allele_entry["ref_allele"]
                alt = allele_entry["risk_allele"]
                star_allele_name = ""
            else:
                # Star allele name
                if variant_field not in star_alleles:
                    print(f"Warning: star allele '{variant_field}' not in lookup, skipping.")
                    continue
                entry = star_alleles[variant_field]
                rsid = entry["rsid"]
                ref = entry["ref_allele"]
                alt = entry["risk_allele"]
                star_allele_name = variant_field

            if rsid in seen_rsids:
                continue
            seen_rsids.add(rsid)

            name = f"{star_allele_name or gene} - {drug}"
            description = (
                f"CPIC Level {level} annotation for {gene} and {drug}. "
                f"Associated phenotype: {phenotype}. Imported from PharmGKB."
            )

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": "pharmacogenomics",
                "name": name,
                "significance": "drug_response",
                "description": description,
                "risk_allele": alt,
                "normal_allele": ref,
                "chromosome": "",  # PharmGKB doesn't include coordinates
                "position": 0,
                "source": "pharmgkb_import",
                "clinvar_stars": 0,
                "odds_ratio": None,
                "publications": None,
                "external_ids": None,
            }

            interps = pharmgkb_interpretations(
                rsid=rsid, ref=ref, alt=alt, gene=gene,
                drug=drug, phenotype=phenotype,
                level=level, star_allele=star_allele_name,
                is_sex_chrom=False,
            )

            yield variant, interps
