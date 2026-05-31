"""Pydantic models for API request/response schemas."""

from enum import StrEnum

from pydantic import BaseModel


class Category(StrEnum):
    HEALTH_RISK = "health_risk"
    PHARMACOGENOMICS = "pharmacogenomics"
    TRAIT = "trait"


class Significance(StrEnum):
    PATHOGENIC = "pathogenic"
    LIKELY_PATHOGENIC = "likely_pathogenic"
    RISK_FACTOR = "risk_factor"
    DRUG_RESPONSE = "drug_response"
    ASSOCIATION = "association"


class RiskLevel(StrEnum):
    NORMAL = "normal"
    CARRIER = "carrier"
    INCREASED_RISK = "increased_risk"
    HIGH_RISK = "high_risk"


class SNP(BaseModel):
    """A single SNP from a raw data file."""

    rsid: str
    chromosome: str
    position: int
    genotype: str


class CuratedVariant(BaseModel):
    """A variant from the curated database."""

    rsid: str
    gene: str
    category: Category
    name: str
    significance: Significance
    description: str
    risk_allele: str | None = None
    normal_allele: str | None = None
    chromosome: str
    position: int
    source: str
    external_ids: dict[str, str] | None = None
    publications: list[str] | None = None
    clinvar_stars: int = 0
    odds_ratio: float | None = None


class GenotypeInterpretation(BaseModel):
    """Interpretation for a specific genotype of a variant."""

    rsid: str
    genotype: str
    interpretation: str
    risk_level: RiskLevel


class VariantMatch(BaseModel):
    """A matched variant from analysis - user's SNP + curated data."""

    snp: SNP
    variant: CuratedVariant
    interpretation: str
    risk_level: RiskLevel
    publications: list[str]
    score: float = 0.0


class AnalysisSummary(BaseModel):
    """Summary statistics for the analysis."""

    total_snps_parsed: int
    total_variants_found: int
    health_risk_count: int
    pharmacogenomics_count: int
    trait_count: int
    high_risk_count: int


class AnalysisResult(BaseModel):
    """Complete analysis result returned by the upload endpoint."""

    summary: AnalysisSummary
    health_risks: list[VariantMatch]
    pharmacogenomics: list[VariantMatch]
    traits: list[VariantMatch]


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    variant_count: int
