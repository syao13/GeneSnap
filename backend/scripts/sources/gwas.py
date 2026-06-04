"""GWAS Catalog TSV parser: filters to genome-wide significant associations."""

import csv
import re
from collections.abc import Iterator
from datetime import date
from pathlib import Path

from sources.templates import gwas_interpretations

from genesnap.db.variants._types import InterpretationDict, VariantDict

TODAY = date.today().isoformat()

SEX_CHROMS = {"X", "Y", "MT"}
MIN_SAMPLE_SIZE = 1000
PVAL_THRESHOLD = 5e-8

PHARMA_GENES = {
    "CYP2D6", "CYP2C19", "CYP2C9", "CYP3A4", "CYP3A5", "CYP1A2", "CYP2B6",
    "UGT1A1", "UGT2B7", "VKORC1", "DPYD", "TPMT", "NUDT15", "SLCO1B1",
    "IFNL3", "HLA-B", "HLA-A", "G6PD", "CACNA1S", "RYR1",
}
HEALTH_RISK_KEYWORDS = {
    "cancer", "disease", "syndrome", "disorder", "carcinoma", "leukemia",
    "diabetes", "hypertension", "infarction", "stroke", "thrombosis",
    "anemia", "fibrosis", "tumor", "tumour", "melanoma", "sclerosis",
}


def _parse_sample_size(s: str) -> int:
    stripped = [n.replace(",", "") for n in re.findall(r"[\d,]+", s)]
    nums = [int(n) for n in stripped if n]
    return max(nums) if nums else 0


def _parse_pval(s: str) -> float | None:
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def _parse_or(s: str) -> float | None:
    try:
        v = float(s)
        return v if v > 0 else None
    except (ValueError, TypeError):
        return None


def _parse_gene(mapped_gene: str) -> str:
    gene = mapped_gene.strip()
    for sep in [" - ", " x ", ", ", ";"]:
        if sep in gene:
            gene = gene.split(sep)[0].strip()
    return gene or "UNKNOWN"


def _categorize(gene: str, trait: str) -> str:
    if gene in PHARMA_GENES:
        return "pharmacogenomics"
    if any(kw in trait.lower() for kw in HEALTH_RISK_KEYWORDS):
        return "health_risk"
    return "trait"


def parse_gwas_tsv(
    tsv_path: Path,
    rsid_alleles: dict[str, tuple[str, str]],
) -> Iterator[tuple[VariantDict, list[InterpretationDict]]]:
    """Parse GWAS Catalog full associations TSV.

    Args:
        tsv_path: Path to the GWAS Catalog TSV file.
        rsid_alleles: Dict of rsid->(ref,alt) from ClinVar. Used to generate
                      genotype interpretations. Variants not in this dict still
                      get a variants row but no interpretation rows.
    """
    seen_rsids: set[str] = set()

    with open(tsv_path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            # Parse and filter SNPS field -- must be a single rsID
            snps_field = row.get("SNPS", "").strip()
            if " " in snps_field or not snps_field.startswith("rs"):
                continue
            rsid = snps_field

            if rsid in seen_rsids:
                continue

            # Parse p-value
            pval = _parse_pval(row.get("P-VALUE", ""))
            if pval is None or pval >= PVAL_THRESHOLD:
                continue

            # Parse sample size
            sample_size = _parse_sample_size(row.get("INITIAL SAMPLE SIZE", ""))
            if sample_size < MIN_SAMPLE_SIZE:
                continue

            # Parse risk allele from "rs1234-T" format
            strongest = row.get("STRONGEST SNP-RISK ALLELE", "")
            if "-" not in strongest:
                continue
            risk_allele_from_gwas = strongest.split("-", 1)[1].strip()
            if not risk_allele_from_gwas or risk_allele_from_gwas in {"?", "N"}:
                continue

            chrom = row.get("CHR_ID", "").strip()
            pos_str = row.get("CHR_POS", "").strip()
            if not pos_str.isdigit():
                continue

            gene = _parse_gene(row.get("MAPPED_GENE", "UNKNOWN"))
            trait = row.get("DISEASE/TRAIT", "").strip()
            or_val = _parse_or(row.get("OR or BETA", ""))
            is_sex = chrom in SEX_CHROMS
            category = _categorize(gene, trait)

            # Get ref/alt from ClinVar lookup
            alleles = rsid_alleles.get(rsid)
            if alleles:
                ref: str | None
                alt: str | None
                ref, alt = alleles
            else:
                ref, alt = None, None

            # Handle protective alleles (OR < 1): swap so risk_allele always has OR >= 1
            risk_allele = risk_allele_from_gwas
            normal_allele = ref
            if or_val is not None and or_val < 1.0 and ref is not None:
                risk_allele = ref
                normal_allele = risk_allele_from_gwas
                alt = ref
                ref = risk_allele_from_gwas
                or_val = round(1.0 / or_val, 3) if or_val > 0 else None

            seen_rsids.add(rsid)

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": category,
                "name": f"{gene} - {trait}",
                "significance": "association",
                "description": (
                    f"Associated with {trait} in {gene} "
                    f"(OR: {or_val:.2f}x, p={pval:.2e}, GWAS Catalog)."
                    if or_val else
                    f"Associated with {trait} in {gene} (p={pval:.2e}, GWAS Catalog)."
                ),
                "risk_allele": risk_allele,
                "normal_allele": normal_allele,
                "chromosome": chrom,
                "position": int(pos_str),
                "source": "gwas_import",
                "clinvar_stars": 0,
                "odds_ratio": or_val,
                "publications": None,
                "external_ids": None,
            }

            interps: list[InterpretationDict] = []
            if ref is not None and not is_sex:
                interps = gwas_interpretations(
                    rsid=rsid, ref=ref, alt=alt,  # type: ignore[arg-type]
                    gene=gene, trait=trait,
                    odds_ratio=or_val, pval=pval,
                    is_sex_chrom=is_sex,
                )

            yield variant, interps
