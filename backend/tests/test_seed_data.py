"""Validation tests for the curated variant seed data."""

import re

from genesnap.db.variants import GENOTYPE_INTERPRETATIONS, VARIANTS
from genesnap.models.schemas import Category, RiskLevel, Significance

VALID_CATEGORIES = {e.value for e in Category}
VALID_SIGNIFICANCES = {e.value for e in Significance}
VALID_RISK_LEVELS = {e.value for e in RiskLevel}
VALID_CHROMOSOMES = {str(i) for i in range(1, 23)} | {"X", "Y", "MT"}
RSID_PATTERN = re.compile(r"^rs\d+$")


class TestVariantCount:
    def test_at_least_200_variants(self):
        assert len(VARIANTS) >= 200, f"Expected 200+ variants, got {len(VARIANTS)}"

    def test_at_least_200_interpretations(self):
        assert len(GENOTYPE_INTERPRETATIONS) >= 200


class TestNoDuplicates:
    def test_no_duplicate_rsids(self):
        rsids = [v["rsid"] for v in VARIANTS]
        dupes = {r for r in rsids if rsids.count(r) > 1}
        assert not dupes, f"Duplicate rsids: {dupes}"

    def test_no_duplicate_interpretation_rsid_genotype_pairs(self):
        pairs = [(i["rsid"], i["genotype"]) for i in GENOTYPE_INTERPRETATIONS]
        dupes = {p for p in pairs if pairs.count(p) > 1}
        assert not dupes, f"Duplicate (rsid, genotype) pairs: {dupes}"


class TestInterpretationCoverage:
    def test_every_variant_has_at_least_2_interpretations(self):
        interp_counts: dict[str, int] = {}
        for i in GENOTYPE_INTERPRETATIONS:
            interp_counts[i["rsid"]] = interp_counts.get(i["rsid"], 0) + 1

        missing = {
            rsid: count
            for v in VARIANTS
            if (rsid := v["rsid"]) and (count := interp_counts.get(rsid, 0)) < 2
        }
        assert not missing, f"Variants with <2 interpretations: {missing}"

    def test_all_interpretation_rsids_match_a_variant(self):
        variant_rsids = {v["rsid"] for v in VARIANTS}
        orphans = {i["rsid"] for i in GENOTYPE_INTERPRETATIONS if i["rsid"] not in variant_rsids}
        assert not orphans, f"Orphan interpretation rsids: {orphans}"


class TestEnumValues:
    def test_all_categories_valid(self):
        invalid = {
            v["rsid"]: v["category"] for v in VARIANTS if v["category"] not in VALID_CATEGORIES
        }
        assert not invalid, f"Invalid categories: {invalid}"

    def test_all_significances_valid(self):
        invalid = {
            v["rsid"]: v["significance"]
            for v in VARIANTS
            if v["significance"] not in VALID_SIGNIFICANCES
        }
        assert not invalid, f"Invalid significances: {invalid}"

    def test_all_risk_levels_valid(self):
        invalid = {
            (i["rsid"], i["genotype"]): i["risk_level"]
            for i in GENOTYPE_INTERPRETATIONS
            if i["risk_level"] not in VALID_RISK_LEVELS
        }
        assert not invalid, f"Invalid risk_levels: {invalid}"


class TestVariantFields:
    def test_rsid_format(self):
        invalid = [v["rsid"] for v in VARIANTS if not RSID_PATTERN.match(v["rsid"])]
        assert not invalid, f"Invalid rsid format: {invalid}"

    def test_chromosome_valid(self):
        invalid = {
            v["rsid"]: v["chromosome"] for v in VARIANTS if v["chromosome"] not in VALID_CHROMOSOMES
        }
        assert not invalid, f"Invalid chromosomes: {invalid}"

    def test_position_positive(self):
        invalid = {v["rsid"]: v["position"] for v in VARIANTS if v["position"] <= 0}
        assert not invalid, f"Non-positive positions: {invalid}"

    def test_clinvar_stars_in_range(self):
        invalid = {
            v["rsid"]: v["clinvar_stars"] for v in VARIANTS if not 0 <= v["clinvar_stars"] <= 4
        }
        assert not invalid, f"clinvar_stars out of 0-4 range: {invalid}"

    def test_required_fields_present(self):
        required = [
            "rsid",
            "gene",
            "category",
            "name",
            "significance",
            "description",
            "chromosome",
            "position",
            "source",
        ]
        for v in VARIANTS:
            for field in required:
                assert field in v, f"{v.get('rsid', '?')} missing field: {field}"


class TestCategoryCoverage:
    """Ensure variants span all three categories."""

    def test_has_health_risk_variants(self):
        count = sum(1 for v in VARIANTS if v["category"] == "health_risk")
        assert count >= 50, f"Expected 50+ health_risk, got {count}"

    def test_has_pharmacogenomics_variants(self):
        count = sum(1 for v in VARIANTS if v["category"] == "pharmacogenomics")
        assert count >= 30, f"Expected 30+ pharmacogenomics, got {count}"

    def test_has_trait_variants(self):
        count = sum(1 for v in VARIANTS if v["category"] == "trait")
        assert count >= 20, f"Expected 20+ trait, got {count}"


def test_seed_database(tmp_path):
    """Seed a fresh database and verify variant count."""
    import sqlite3

    from genesnap.db.seed import seed_database

    db_path = tmp_path / "test.db"
    seed_database(db_path)

    conn = sqlite3.connect(db_path)
    (variant_count,) = conn.execute("SELECT COUNT(*) FROM variants").fetchone()
    (interp_count,) = conn.execute("SELECT COUNT(*) FROM genotype_interpretations").fetchone()
    conn.close()

    assert variant_count >= 200, f"Expected 200+ seeded variants, got {variant_count}"
    assert interp_count >= 200, f"Expected 200+ seeded interpretations, got {interp_count}"
