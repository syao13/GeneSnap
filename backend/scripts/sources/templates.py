"""Shared template functions for generating per-genotype interpretations."""

from math import floor, log10

from genesnap.db.variants._types import InterpretationDict


def make_genotypes(ref: str, alt: str) -> tuple[str, str, str]:
    """Return (hom_ref, het, hom_alt) genotype strings.

    Het is alphabetically sorted to match 23andMe reporting convention.
    """
    return ref + ref, "".join(sorted([ref, alt])), alt + alt


def clinvar_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    condition: str,
    significance: str,
    stars: int,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a ClinVar variant."""
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)
    stars_display = "★" * stars + "☆" * (4 - stars)

    if significance == "drug_response":
        drug = condition.lower().replace(" response", "").replace(" metabolism", "").strip()
        return [
            {
                "rsid": rsid,
                "genotype": ref_ref,
                "interpretation": f"Standard {gene} function expected for {drug} metabolism.",
                "risk_level": "normal",
            },
            {
                "rsid": rsid,
                "genotype": het,
                "interpretation": (
                    f"You carry one copy of a {gene} drug response variant affecting {drug}. "
                    "Consult your prescriber if taking this medication."
                ),
                "risk_level": "increased_risk",
            },
            {
                "rsid": rsid,
                "genotype": alt_alt,
                "interpretation": (
                    f"You carry two copies of a {gene} drug response variant affecting {drug}. "
                    "Prescriber consultation is strongly recommended."
                ),
                "risk_level": "high_risk",
            },
        ]

    sig_display = significance.replace("_", " ")
    strength = "strongly recommended" if significance == "pathogenic" else "recommended"
    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": f"You do not carry this {gene} variant associated with {condition}.",
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of this {sig_display} {gene} variant associated with "
                f"{condition} (ClinVar {stars_display}). "
                "Consider discussing with a healthcare provider."
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of this {sig_display} {gene} variant associated with "
                f"{condition} (ClinVar {stars_display}). "
                f"Clinical confirmation is {strength}."
            ),
            "risk_level": "high_risk",
        },
    ]


def gwas_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    trait: str,
    odds_ratio: float | None,
    pval: float | None,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a GWAS association.

    GWAS variants are capped at increased_risk — never high_risk.
    """
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)

    if odds_ratio is not None:
        or_str = f"{odds_ratio:.1f}x"
        or_het = 1 + (odds_ratio - 1) / 2 if odds_ratio > 1 else odds_ratio
        or_het_str = f"{or_het:.1f}x"
    else:
        or_str = or_het_str = "unknown"

    if pval is not None and pval > 0:
        exp = floor(log10(pval))
        mantissa = pval / (10**exp)
        pval_str = f"{mantissa:.1f}×10⁻{abs(exp)}"  # noqa: RUF001
    else:
        pval_str = "unknown"

    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": f"You do not carry the {trait} risk allele in {gene}.",
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of the {gene} risk allele associated with {trait} "
                f"(OR: ~{or_het_str} above baseline, p={pval_str}, population-level association)."
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of the {gene} risk allele associated with {trait} "
                f"(OR: {or_str} above baseline, p={pval_str}, population-level association)."
            ),
            "risk_level": "increased_risk",
        },
    ]


def pharmgkb_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    drug: str,
    phenotype: str,
    level: str,
    star_allele: str,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a PharmGKB annotation."""
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)
    label = star_allele if star_allele else gene

    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": (
                f"You do not carry {label}. Normal {gene} function expected for {drug}."
            ),
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of {label}, associated with {phenotype} for {drug}. "
                f"Consult prescriber if taking {drug}. (CPIC Level {level})"
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of {label} ({phenotype}). "
                f"CPIC Level {level} guideline recommends review of {drug} therapy."
            ),
            "risk_level": "high_risk",
        },
    ]
