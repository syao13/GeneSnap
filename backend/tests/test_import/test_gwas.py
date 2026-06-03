"""Tests for GWAS Catalog TSV parser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from sources.gwas import parse_gwas_tsv

FIXTURES = Path(__file__).parent / "fixtures"

# Minimal rsid_alleles dict (from ClinVar) for tests that need interpretations
KNOWN_ALLELES: dict[str, tuple[str, str]] = {
    "rs7903146": ("C", "T"),
    "rs1045485": ("G", "C"),
    "rs1042725": ("T", "C"),
    "rs9923231": ("G", "A"),
}


def test_includes_large_sample_health_risk() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs7903146" in rsids


def test_excludes_multi_snp_row() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs1234567" not in rsids


def test_excludes_small_sample() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs762551" not in rsids
    assert "rs2222222" not in rsids


def test_pharma_gene_categorized_correctly() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    vkorc1 = next((v for v, _ in results if v["rsid"] == "rs9923231"), None)
    assert vkorc1 is not None
    assert vkorc1["category"] == "pharmacogenomics"


def test_disease_keyword_is_health_risk() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    t2d = next((v for v, _ in results if v["rsid"] == "rs7903146"), None)
    assert t2d is not None
    assert t2d["category"] == "health_risk"


def test_height_is_trait() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    height = next((v for v, _ in results if v["rsid"] == "rs1042725"), None)
    assert height is not None
    assert height["category"] == "trait"


def test_protective_allele_swapped() -> None:
    """OR=0.5 for A allele means A is protective; risk and ref should be swapped."""
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    vkorc1 = next((v for v, _ in results if v["rsid"] == "rs9923231"), None)
    assert vkorc1 is not None
    # Original: STRONGEST SNP-RISK ALLELE = rs9923231-A, OR=0.5
    # After swap: risk_allele should be G (the non-A allele, OR = 1/0.5 = 2.0)
    assert vkorc1["risk_allele"] == "G"
    assert vkorc1["odds_ratio"] is not None
    assert vkorc1["odds_ratio"] > 1.0


def test_known_alleles_generates_interpretations() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    t2d = next((v, i) for v, i in results if v["rsid"] == "rs7903146")
    _, interps = t2d
    assert len(interps) == 3


def test_unknown_alleles_skips_interpretations() -> None:
    """GWAS variant with no entry in rsid_alleles -> no interpretation rows."""
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", {}))
    t2d = next((v, i) for v, i in results if v["rsid"] == "rs7903146")
    _, interps = t2d
    assert interps == []


def test_source_is_gwas_import() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    assert all(v["source"] == "gwas_import" for v, _ in results)
