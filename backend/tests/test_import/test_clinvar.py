"""Tests for ClinVar VCF parser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from sources.clinvar import parse_clinvar_vcf

FIXTURES = Path(__file__).parent / "fixtures"


def _results(path: Path = FIXTURES / "sample_clinvar.vcf") -> list:
    variants, _ = parse_clinvar_vcf(path)
    return variants


def test_passes_pathogenic_3star() -> None:
    rsids = {v["rsid"] for v, _ in _results()}
    assert "rs6025" in rsids


def test_excludes_single_star() -> None:
    rsids = {v["rsid"] for v, _ in _results()}
    assert "rs9999999" not in rsids


def test_excludes_conflicting() -> None:
    rsids = {v["rsid"] for v, _ in _results()}
    assert "rs8888888" not in rsids


def test_excludes_missing_rs() -> None:
    assert not any(v["gene"] == "GENE3" for v, _ in _results())


def test_pathogenic_has_three_interpretations() -> None:
    rs6025 = next((v, i) for v, i in _results() if v["rsid"] == "rs6025")
    variant, interps = rs6025
    assert len(interps) == 3
    assert variant["significance"] == "pathogenic"
    assert variant["category"] == "health_risk"
    assert variant["source"] == "clinvar_import"


def test_pathogenic_genotype_strings() -> None:
    _, interps = next((v, i) for v, i in _results() if v["rsid"] == "rs6025")
    genotypes = {r["genotype"] for r in interps}
    # REF=G ALT=A → GG, AG (sorted), AA
    assert genotypes == {"GG", "AG", "AA"}


def test_drug_response_is_pharmacogenomics() -> None:
    rs1799853 = next((v, i) for v, i in _results() if v["rsid"] == "rs1799853")
    variant, interps = rs1799853
    assert variant["category"] == "pharmacogenomics"
    assert variant["significance"] == "drug_response"
    assert len(interps) == 3


def test_x_chrom_has_variant_but_no_interpretations() -> None:
    rs5978 = next(((v, i) for v, i in _results() if v["rsid"] == "rs5978"), None)
    assert rs5978 is not None
    variant, interps = rs5978
    assert variant["chromosome"] == "X"
    assert interps == []


def test_clinvar_stars_mapped_correctly() -> None:
    by_rsid = {v["rsid"]: v for v, _ in _results()}
    assert by_rsid["rs6025"]["clinvar_stars"] == 3          # reviewed_by_expert_panel
    assert by_rsid["rs80357906"]["clinvar_stars"] == 4      # practice_guideline
    assert by_rsid["rs1799853"]["clinvar_stars"] == 2       # multiple_submitters


def test_condition_strips_not_provided() -> None:
    tp53 = next((v for v, _ in _results() if v["rsid"] == "rs63750447"), None)
    assert tp53 is not None
    assert "Li-Fraumeni" in tp53["name"]
    assert "not_provided" not in tp53["name"]


def test_returns_rsid_alleles_dict() -> None:
    _, rsid_alleles = parse_clinvar_vcf(FIXTURES / "sample_clinvar.vcf")
    assert "rs6025" in rsid_alleles
    assert rsid_alleles["rs6025"] == ("G", "A")
