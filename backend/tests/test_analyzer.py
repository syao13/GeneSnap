"""Tests for the SNP analysis engine."""

import sqlite3
from pathlib import Path

import aiosqlite
import pytest

from genesnap.analysis.analyzer import SIGNIFICANCE_WEIGHT, analyze_snps, compute_score
from genesnap.db.connection import SCHEMA_SQL
from genesnap.db.seed import (
    _insert_genotype_interpretations,
    _insert_variants,
)
from genesnap.models.schemas import (
    SNP,
    AnalysisResult,
    Category,
    CuratedVariant,
    RiskLevel,
    Significance,
)

TEST_DB = Path(__file__).parent / "test_analyzer.db"


@pytest.fixture
async def test_db() -> aiosqlite.Connection:
    """Create and seed a test database."""
    # Create with sync sqlite3 first
    if TEST_DB.exists():
        TEST_DB.unlink()
    conn_sync = sqlite3.connect(TEST_DB)
    conn_sync.executescript(SCHEMA_SQL)
    _insert_variants(conn_sync)
    _insert_genotype_interpretations(conn_sync)
    conn_sync.commit()
    conn_sync.close()

    # Open async connection
    db = await aiosqlite.connect(TEST_DB)
    db.row_factory = aiosqlite.Row
    yield db
    await db.close()
    TEST_DB.unlink(missing_ok=True)


class TestAnalyzeSnps:
    """Tests for the analyze_snps function."""

    async def test_returns_analysis_result(self, test_db: aiosqlite.Connection) -> None:
        """Should return an AnalysisResult model."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG")]
        result = await analyze_snps(test_db, snps)
        assert isinstance(result, AnalysisResult)

    async def test_matches_known_variant(self, test_db: aiosqlite.Connection) -> None:
        """Should identify a known pathogenic variant."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG")]
        result = await analyze_snps(test_db, snps)

        assert result.summary.total_variants_found == 1
        assert len(result.health_risks) == 1
        assert result.health_risks[0].variant.gene == "F5"
        assert result.health_risks[0].variant.name == "Factor V Leiden"

    async def test_correct_genotype_interpretation(self, test_db: aiosqlite.Connection) -> None:
        """Should look up the correct genotype interpretation."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG")]
        result = await analyze_snps(test_db, snps)

        match = result.health_risks[0]
        assert match.risk_level == RiskLevel.INCREASED_RISK
        assert "5-10x" in match.interpretation

    async def test_unknown_genotype_fallback(self, test_db: aiosqlite.Connection) -> None:
        """Should handle genotypes not in the interpretation table."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="XX")]
        result = await analyze_snps(test_db, snps)

        assert len(result.health_risks) == 1
        match = result.health_risks[0]
        assert match.risk_level == RiskLevel.NORMAL
        assert "no specific interpretation" in match.interpretation.lower()

    async def test_no_matches_for_unknown_snps(self, test_db: aiosqlite.Connection) -> None:
        """Should return empty results for SNPs not in the curated DB."""
        snps = [
            SNP(rsid="rs999999999", chromosome="1", position=1, genotype="AA"),
            SNP(rsid="rs888888888", chromosome="2", position=2, genotype="GG"),
        ]
        result = await analyze_snps(test_db, snps)

        assert result.summary.total_snps_parsed == 2
        assert result.summary.total_variants_found == 0
        assert len(result.health_risks) == 0
        assert len(result.pharmacogenomics) == 0
        assert len(result.traits) == 0

    async def test_categorizes_variants_correctly(self, test_db: aiosqlite.Connection) -> None:
        """Should place variants in the correct category lists."""
        snps = [
            SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG"),  # health
            SNP(rsid="rs1799853", chromosome="10", position=96702047, genotype="CT"),  # pharma
            SNP(rsid="rs4988235", chromosome="2", position=136608646, genotype="GG"),  # trait
        ]
        result = await analyze_snps(test_db, snps)

        assert len(result.health_risks) == 1
        assert result.health_risks[0].variant.category == Category.HEALTH_RISK

        assert len(result.pharmacogenomics) == 1
        assert result.pharmacogenomics[0].variant.category == Category.PHARMACOGENOMICS

        assert len(result.traits) == 1
        assert result.traits[0].variant.category == Category.TRAIT

    async def test_summary_counts_correct(self, test_db: aiosqlite.Connection) -> None:
        """Should produce accurate summary counts."""
        snps = [
            SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AA"),  # high_risk
            SNP(rsid="rs7903146", chromosome="10", position=114758349, genotype="TT"),  # high_risk
            SNP(rsid="rs1799853", chromosome="10", position=96702047, genotype="CT"),  # pharma
            SNP(rsid="rs4988235", chromosome="2", position=136608646, genotype="GG"),  # trait
            SNP(rsid="rs999999", chromosome="1", position=1, genotype="AA"),  # unknown
        ]
        result = await analyze_snps(test_db, snps)

        assert result.summary.total_snps_parsed == 5
        assert result.summary.total_variants_found == 4
        assert result.summary.health_risk_count == 2
        assert result.summary.pharmacogenomics_count == 1
        assert result.summary.trait_count == 1
        assert result.summary.high_risk_count == 2

    async def test_sorts_by_risk_level(self, test_db: aiosqlite.Connection) -> None:
        """Should sort results within each category by risk level (highest first)."""
        snps = [
            SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="GG"),  # normal
            SNP(rsid="rs7903146", chromosome="10", position=114758349, genotype="TT"),  # high_risk
            SNP(rsid="rs334", chromosome="11", position=5248232, genotype="AT"),  # carrier
        ]
        result = await analyze_snps(test_db, snps)

        risk_levels = [m.risk_level for m in result.health_risks]
        # high_risk should come before carrier, carrier before normal
        assert risk_levels.index(RiskLevel.HIGH_RISK) < risk_levels.index(RiskLevel.CARRIER)
        assert risk_levels.index(RiskLevel.CARRIER) < risk_levels.index(RiskLevel.NORMAL)

    async def test_empty_snps_list(self, test_db: aiosqlite.Connection) -> None:
        """Should handle empty input gracefully."""
        result = await analyze_snps(test_db, [])

        assert result.summary.total_snps_parsed == 0
        assert result.summary.total_variants_found == 0
        assert result.health_risks == []
        assert result.pharmacogenomics == []
        assert result.traits == []

    async def test_includes_publications(self, test_db: aiosqlite.Connection) -> None:
        """Should include publication PMIDs from the curated variant."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG")]
        result = await analyze_snps(test_db, snps)

        assert len(result.health_risks[0].publications) > 0
        assert "7989264" in result.health_risks[0].publications

    async def test_score_is_computed(self, test_db: aiosqlite.Connection) -> None:
        """Should compute a non-zero score for variants with evidence data."""
        snps = [SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="AG")]
        result = await analyze_snps(test_db, snps)

        match = result.health_risks[0]
        assert match.score > 0
        # Factor V Leiden: pathogenic(10) * (1+3 stars) * 7.0 OR = 280
        assert match.score == 280.0

    async def test_score_used_for_secondary_sort(self, test_db: aiosqlite.Connection) -> None:
        """Within same risk level, higher-scored variant should come first."""
        snps = [
            # Both are health_risk, both will be "normal" risk level with GG genotype
            SNP(rsid="rs6025", chromosome="1", position=169519049, genotype="GG"),
            SNP(rsid="rs9939609", chromosome="16", position=53820527, genotype="TT"),
        ]
        result = await analyze_snps(test_db, snps)

        # Both should be normal risk, but rs6025 has a much higher score
        assert len(result.health_risks) == 2
        assert result.health_risks[0].snp.rsid == "rs6025"
        assert result.health_risks[0].score > result.health_risks[1].score


class TestComputeScore:
    """Tests for the compute_score function."""

    def _make_variant(
        self,
        significance: str = "pathogenic",
        clinvar_stars: int = 0,
        odds_ratio: float | None = None,
    ) -> CuratedVariant:
        return CuratedVariant(
            rsid="rs_test",
            gene="TEST",
            category=Category.HEALTH_RISK,
            name="Test variant",
            significance=Significance(significance),
            description="Test",
            chromosome="1",
            position=1,
            source="test",
            clinvar_stars=clinvar_stars,
            odds_ratio=odds_ratio,
        )

    def test_basic_pathogenic(self) -> None:
        """Pathogenic with 0 stars, no OR = 10 * 1 * 1.0 = 10."""
        v = self._make_variant("pathogenic", clinvar_stars=0, odds_ratio=None)
        assert compute_score(v) == 10.0

    def test_stars_multiply(self) -> None:
        """Stars increase the score multiplicatively: 10 * (1+4) = 50."""
        v = self._make_variant("pathogenic", clinvar_stars=4, odds_ratio=None)
        assert compute_score(v) == 50.0

    def test_odds_ratio_multiply(self) -> None:
        """OR multiplies the score: 10 * 1 * 5.0 = 50."""
        v = self._make_variant("pathogenic", clinvar_stars=0, odds_ratio=5.0)
        assert compute_score(v) == 50.0

    def test_all_three_factors(self) -> None:
        """All factors combined: 10 * (1+3) * 7.0 = 280."""
        v = self._make_variant("pathogenic", clinvar_stars=3, odds_ratio=7.0)
        assert compute_score(v) == 280.0

    def test_low_odds_ratio_floors_to_one(self) -> None:
        """OR below 1.0 (protective) should be treated as 1.0."""
        v = self._make_variant("risk_factor", clinvar_stars=0, odds_ratio=0.5)
        # 5 * 1 * 1.0 = 5.0 (not 5 * 1 * 0.5 = 2.5)
        assert compute_score(v) == 5.0

    def test_significance_weights(self) -> None:
        """Each significance level should have the correct weight."""
        for sig, expected_weight in SIGNIFICANCE_WEIGHT.items():
            v = self._make_variant(sig.value, clinvar_stars=0, odds_ratio=None)
            assert compute_score(v) == float(expected_weight)
