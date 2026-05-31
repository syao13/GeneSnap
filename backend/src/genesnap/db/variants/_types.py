"""TypedDict definitions for variant seed data."""

from typing import TypedDict


class VariantDict(TypedDict, total=False):
    rsid: str
    gene: str
    category: str
    name: str
    significance: str
    description: str
    risk_allele: str | None
    normal_allele: str | None
    chromosome: str
    position: int
    source: str
    external_ids: dict[str, str] | None
    publications: list[str] | None
    clinvar_stars: int
    odds_ratio: float | None


class InterpretationDict(TypedDict):
    rsid: str
    genotype: str
    interpretation: str
    risk_level: str
