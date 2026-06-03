"""ClinVar VCF parser: filters to pathogenic/LP/drug_response with >=2 review stars."""

import gzip
from datetime import date
from pathlib import Path

from sources.templates import clinvar_interpretations

from genesnap.db.variants._types import InterpretationDict, VariantDict

TODAY = date.today().isoformat()

SEX_CHROMS = {"X", "Y", "MT"}

ALLOWED_CLNSIG = {
    "Pathogenic",
    "Likely_pathogenic",
    "drug_response",
    "Pathogenic/Likely_pathogenic",
}
EXCLUDED_CLNSIG_SUBSTRINGS = {"Conflicting_interpretations"}

REVSTAT_STARS: dict[str, int] = {
    "practice_guideline": 4,
    "reviewed_by_expert_panel": 3,
    "criteria_provided,_multiple_submitters,_no_conflicts": 2,
}

CLNSIG_TO_SIGNIFICANCE: dict[str, str] = {
    "Pathogenic": "pathogenic",
    "Likely_pathogenic": "likely_pathogenic",
    "Pathogenic/Likely_pathogenic": "pathogenic",
    "drug_response": "drug_response",
}


def _parse_info(info_str: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for field in info_str.split(";"):
        if "=" in field:
            k, v = field.split("=", 1)
            result[k] = v
    return result


def _pick_clnsig(raw: str) -> str | None:
    """Pick the most actionable significance from a pipe-separated CLNSIG string."""
    for val in raw.split("|"):
        if any(excl in val for excl in EXCLUDED_CLNSIG_SUBSTRINGS):
            return None
        if val in ALLOWED_CLNSIG:
            return val
    return None


def _pick_revstat_stars(raw: str) -> int | None:
    """Return star count for the best review status in a pipe-separated CLNREVSTAT string."""
    for allowed, stars in REVSTAT_STARS.items():
        if allowed in raw:
            return stars
    return None


def _clean_condition(clndn: str) -> str:
    """Pick first non-'not_provided' condition and replace underscores."""
    parts = [p for p in clndn.split("|") if p.lower() not in {"not_provided", "not_specified"}]
    raw = parts[0] if parts else clndn.split("|")[0]
    return raw.replace("_", " ").strip()


def _pick_gene(geneinfo: str) -> str:
    first = geneinfo.split("|")[0]
    return first.split(":")[0].strip() or "UNKNOWN"


def parse_clinvar_vcf(
    vcf_path: Path,
) -> tuple[list[tuple[VariantDict, list[InterpretationDict]]], dict[str, tuple[str, str]]]:
    """Parse ClinVar VCF, returning filtered variants and a ref/alt allele lookup.

    Returns:
        (variants_and_interps, rsid_alleles) where rsid_alleles maps rsid -> (ref, alt).
        rsid_alleles is passed to parse_gwas_tsv and parse_pharmgkb_annotations so
        they can generate genotype interpretations.
    """
    rsid_alleles: dict[str, tuple[str, str]] = {}
    results: list[tuple[VariantDict, list[InterpretationDict]]] = []

    opener = gzip.open if str(vcf_path).endswith(".gz") else open
    with opener(vcf_path, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            parts = line.strip().split("\t")
            if len(parts) < 8:
                continue

            chrom, pos_str, _var_id, ref, alt, _qual, _filt, info_str = parts[:8]

            # Skip multi-allelic
            if "," in alt:
                continue

            info = _parse_info(info_str)

            # rsID from INFO RS= field (not ID column, which is ClinVar VariationID)
            rs_num = info.get("RS", "")
            if not rs_num:
                continue
            rsid = f"rs{rs_num}"

            clnsig_raw = info.get("CLNSIG", "")
            clnsig = _pick_clnsig(clnsig_raw)
            if clnsig is None:
                continue

            revstat_raw = info.get("CLNREVSTAT", "")
            stars = _pick_revstat_stars(revstat_raw)
            if stars is None:
                continue

            condition = _clean_condition(info.get("CLNDN", "not_provided"))
            gene = _pick_gene(info.get("GENEINFO", "UNKNOWN:0"))
            significance = CLNSIG_TO_SIGNIFICANCE.get(clnsig, "risk_factor")
            is_sex = chrom in SEX_CHROMS
            category = "pharmacogenomics" if significance == "drug_response" else "health_risk"
            stars_display = "★" * stars + "☆" * (4 - stars)

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": category,
                "name": f"{gene} - {condition}",
                "significance": significance,
                "description": (
                    f"{significance.replace('_', ' ').title()} variant in {gene} "
                    f"associated with {condition} (ClinVar {stars_display}). "
                    "Imported from ClinVar."
                ),
                "risk_allele": alt,
                "normal_allele": ref,
                "chromosome": chrom,
                "position": int(pos_str),
                "source": "clinvar_import",
                "clinvar_stars": stars,
                "odds_ratio": None,
                "publications": None,
                "external_ids": None,
            }

            interps = clinvar_interpretations(
                rsid=rsid, ref=ref, alt=alt, gene=gene,
                condition=condition, significance=significance,
                stars=stars, is_sex_chrom=is_sex,
            )

            rsid_alleles[rsid] = (ref, alt)
            results.append((variant, interps))

    return results, rsid_alleles
