"""Core analysis engine: match uploaded SNPs against curated variant database."""

import aiosqlite

from genesnap.db.queries import get_genotype_interpretations, get_matching_variants
from genesnap.models.schemas import (
    SNP,
    AnalysisResult,
    AnalysisSummary,
    Category,
    CuratedVariant,
    RiskLevel,
    Significance,
    VariantMatch,
)

RISK_LEVEL_ORDER = {
    RiskLevel.HIGH_RISK: 0,
    RiskLevel.INCREASED_RISK: 1,
    RiskLevel.CARRIER: 2,
    RiskLevel.NORMAL: 3,
}

SIGNIFICANCE_WEIGHT = {
    Significance.PATHOGENIC: 10,
    Significance.LIKELY_PATHOGENIC: 8,
    Significance.RISK_FACTOR: 5,
    Significance.DRUG_RESPONSE: 4,
    Significance.ASSOCIATION: 2,
}


def compute_score(variant: CuratedVariant) -> float:
    """Compute a composite evidence score for a variant.

    Formula: significance_weight * (1 + clinvar_stars) * max(odds_ratio, 1.0)

    - significance_weight: pathogenic(10) > likely_pathogenic(8)
      > risk_factor(5) > drug_response(4) > association(2)
    - clinvar_stars: 0-4, multiplied as (1 + stars) giving range 1-5
    - odds_ratio: effect size from GWAS; defaults to 1.0 when unavailable
    """
    sig_weight = SIGNIFICANCE_WEIGHT.get(variant.significance, 1)
    star_factor = 1 + variant.clinvar_stars
    or_factor = max(variant.odds_ratio, 1.0) if variant.odds_ratio is not None else 1.0
    return round(sig_weight * star_factor * or_factor, 1)


async def analyze_snps(db: aiosqlite.Connection, snps: list[SNP]) -> AnalysisResult:
    """Analyze a list of SNPs against the curated variant database.

    Cross-references all SNPs with known variants, looks up genotype-specific
    interpretations, categorizes matches, and sorts by risk level then score.
    """
    if not snps:
        return _empty_result()

    rsid_to_snp = {snp.rsid: snp for snp in snps}
    rsid_set = set(rsid_to_snp.keys())

    variants = await get_matching_variants(db, rsid_set)
    interpretations = await get_genotype_interpretations(db, rsid_set)

    health_risks: list[VariantMatch] = []
    pharmacogenomics: list[VariantMatch] = []
    traits: list[VariantMatch] = []
    high_risk_count = 0

    for variant in variants:
        snp = rsid_to_snp[variant.rsid]
        interp_key = (variant.rsid, snp.genotype)

        if interp_key in interpretations:
            interp = interpretations[interp_key]
            interpretation = interp.interpretation
            risk_level = interp.risk_level
        else:
            interpretation = (
                f"Genotype {snp.genotype} — no specific interpretation available for this variant."
            )
            risk_level = RiskLevel.NORMAL

        if risk_level == RiskLevel.HIGH_RISK:
            high_risk_count += 1

        score = compute_score(variant)

        match = VariantMatch(
            snp=snp,
            variant=variant,
            interpretation=interpretation,
            risk_level=risk_level,
            publications=variant.publications or [],
            score=score,
        )

        if variant.category == Category.HEALTH_RISK:
            health_risks.append(match)
        elif variant.category == Category.PHARMACOGENOMICS:
            pharmacogenomics.append(match)
        else:
            traits.append(match)

    def sort_key(m: VariantMatch) -> tuple[int, float]:
        return (RISK_LEVEL_ORDER.get(m.risk_level, 99), -m.score)

    health_risks.sort(key=sort_key)
    pharmacogenomics.sort(key=sort_key)
    traits.sort(key=sort_key)

    summary = AnalysisSummary(
        total_snps_parsed=len(snps),
        total_variants_found=len(variants),
        health_risk_count=len(health_risks),
        pharmacogenomics_count=len(pharmacogenomics),
        trait_count=len(traits),
        high_risk_count=high_risk_count,
    )

    return AnalysisResult(
        summary=summary,
        health_risks=health_risks,
        pharmacogenomics=pharmacogenomics,
        traits=traits,
    )


def _empty_result() -> AnalysisResult:
    """Return an empty analysis result."""
    return AnalysisResult(
        summary=AnalysisSummary(
            total_snps_parsed=0,
            total_variants_found=0,
            health_risk_count=0,
            pharmacogenomics_count=0,
            trait_count=0,
            high_risk_count=0,
        ),
        health_risks=[],
        pharmacogenomics=[],
        traits=[],
    )
