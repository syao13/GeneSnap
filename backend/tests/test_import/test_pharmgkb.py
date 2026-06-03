"""Tests for PharmGKB clinical annotations parser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from sources.pharmgkb import parse_pharmgkb_annotations

FIXTURES = Path(__file__).parent / "fixtures"
STAR_ALLELES = Path(__file__).parent.parent.parent / "scripts" / "data" / "star_allele_rsids.json"


def test_includes_direct_rsid_level_1a() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs4244285" in rsids


def test_includes_level_1b() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs1799853" in rsids


def test_resolves_star_allele_to_rsid() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    # CYP2D6*4 -> rs3892097
    assert "rs3892097" in rsids


def test_skips_unknown_star_allele() -> None:
    # CYP2D6*99 is not in lookup -- should not raise, and name not in results
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    assert not any("*99" in v["name"] for v, _ in results)


def test_excludes_level_2a() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs7412" not in rsids


def test_all_are_pharmacogenomics() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    assert all(v["category"] == "pharmacogenomics" for v, _ in results)


def test_all_are_drug_response() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    assert all(v["significance"] == "drug_response" for v, _ in results)


def test_three_interpretation_rows() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    for v, interps in results:
        assert len(interps) == 3, f"{v['rsid']} should have 3 interpretation rows"


def test_drug_name_in_interpretation() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    cyp2c19 = next((v, i) for v, i in results if v["rsid"] == "rs4244285")
    _, interps = cyp2c19
    het = next(r for r in interps if r["risk_level"] == "increased_risk")
    assert "clopidogrel" in het["interpretation"]


def test_source_is_pharmgkb_import() -> None:
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    assert all(v["source"] == "pharmgkb_import" for v, _ in results)
