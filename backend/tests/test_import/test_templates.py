"""Tests for genotype interpretation template generation."""

import sys
from pathlib import Path

# Add scripts/ to path so sources/ is importable
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from sources.templates import (
    clinvar_interpretations,
    gwas_interpretations,
    make_genotypes,
    pharmgkb_interpretations,
)


def test_make_genotypes_alphabetical_het() -> None:
    ref_ref, het, alt_alt = make_genotypes("G", "A")
    assert ref_ref == "GG"
    assert het == "AG"   # alphabetical: A < G
    assert alt_alt == "AA"


def test_make_genotypes_tc() -> None:
    ref_ref, het, alt_alt = make_genotypes("C", "T")
    assert ref_ref == "CC"
    assert het == "CT"   # alphabetical: C < T
    assert alt_alt == "TT"


def test_clinvar_pathogenic_returns_three_rows() -> None:
    rows = clinvar_interpretations(
        rsid="rs6025",
        ref="G",
        alt="A",
        gene="F5",
        condition="Thrombophilia due to activated protein C resistance",
        significance="pathogenic",
        stars=3,
        is_sex_chrom=False,
    )
    assert len(rows) == 3
    genotypes = {r["genotype"] for r in rows}
    assert genotypes == {"GG", "AG", "AA"}


def test_clinvar_pathogenic_risk_levels() -> None:
    rows = clinvar_interpretations(
        rsid="rs6025", ref="G", alt="A", gene="F5",
        condition="Thrombosis", significance="pathogenic", stars=3, is_sex_chrom=False,
    )
    by_geno = {r["genotype"]: r["risk_level"] for r in rows}
    assert by_geno["GG"] == "normal"
    assert by_geno["AG"] == "increased_risk"
    assert by_geno["AA"] == "high_risk"


def test_clinvar_sex_chrom_returns_empty() -> None:
    rows = clinvar_interpretations(
        rsid="rs5978", ref="G", alt="A", gene="F9",
        condition="Hemophilia B", significance="pathogenic", stars=3, is_sex_chrom=True,
    )
    assert rows == []


def test_clinvar_drug_response_uses_drug_framing() -> None:
    rows = clinvar_interpretations(
        rsid="rs1799853", ref="C", alt="T", gene="CYP2C9",
        condition="Warfarin response", significance="drug_response", stars=2, is_sex_chrom=False,
    )
    assert len(rows) == 3
    het_row = next(r for r in rows if r["genotype"] == "CT")
    assert "warfarin" in het_row["interpretation"].lower()
    assert het_row["risk_level"] == "increased_risk"


def test_gwas_caps_at_increased_risk() -> None:
    rows = gwas_interpretations(
        rsid="rs7903146", ref="C", alt="T", gene="TCF7L2",
        trait="Type 2 diabetes", odds_ratio=1.4, pval=3.2e-35, is_sex_chrom=False,
    )
    assert len(rows) == 3
    risk_levels = {r["risk_level"] for r in rows}
    assert "high_risk" not in risk_levels
    assert "increased_risk" in risk_levels


def test_gwas_sex_chrom_returns_empty() -> None:
    rows = gwas_interpretations(
        rsid="rs999", ref="A", alt="G", gene="XGENE",
        trait="Some trait", odds_ratio=1.2, pval=1e-10, is_sex_chrom=True,
    )
    assert rows == []


def test_pharmgkb_returns_three_rows_with_drug_name() -> None:
    rows = pharmgkb_interpretations(
        rsid="rs4244285", ref="G", alt="A", gene="CYP2C19",
        drug="clopidogrel", phenotype="Poor Metabolizer",
        level="1A", star_allele="CYP2C19*2", is_sex_chrom=False,
    )
    assert len(rows) == 3
    het_row = next(r for r in rows if r["genotype"] == "AG")
    assert "clopidogrel" in het_row["interpretation"]
    assert "CYP2C19*2" in het_row["interpretation"]


def test_pharmgkb_homozygous_is_high_risk() -> None:
    rows = pharmgkb_interpretations(
        rsid="rs4244285", ref="G", alt="A", gene="CYP2C19",
        drug="clopidogrel", phenotype="Poor Metabolizer",
        level="1A", star_allele="CYP2C19*2", is_sex_chrom=False,
    )
    alt_alt = next(r for r in rows if r["genotype"] == "AA")
    assert alt_alt["risk_level"] == "high_risk"
