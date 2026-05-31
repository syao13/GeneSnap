"""SQL query functions for the curated variant database."""

import json

import aiosqlite

from genesnap.models.schemas import (
    Category,
    CuratedVariant,
    GenotypeInterpretation,
    RiskLevel,
    Significance,
)


async def get_matching_variants(db: aiosqlite.Connection, rsids: set[str]) -> list[CuratedVariant]:
    """Look up curated variants matching a set of rsIDs.

    Fetches all curated variants (small table) and filters in Python to
    avoid SQLite's SQL variable limit with large uploads (600k+ SNPs).
    """
    if not rsids:
        return []

    cursor = await db.execute("SELECT * FROM variants")
    rows = await cursor.fetchall()

    return [_row_to_variant(row) for row in rows if row["rsid"] in rsids]


async def get_genotype_interpretations(
    db: aiosqlite.Connection, rsids: set[str]
) -> dict[tuple[str, str], GenotypeInterpretation]:
    """Get genotype interpretations for a set of rsIDs.

    Returns a dict keyed by (rsid, genotype). Fetches all rows and filters
    in Python to avoid SQLite's SQL variable limit.
    """
    if not rsids:
        return {}

    cursor = await db.execute("SELECT * FROM genotype_interpretations")
    rows = await cursor.fetchall()

    return {
        (row["rsid"], row["genotype"]): GenotypeInterpretation(
            rsid=row["rsid"],
            genotype=row["genotype"],
            interpretation=row["interpretation"],
            risk_level=RiskLevel(row["risk_level"]),
        )
        for row in rows
        if row["rsid"] in rsids
    }


async def get_variant_count(db: aiosqlite.Connection) -> int:
    """Get total number of curated variants."""
    cursor = await db.execute("SELECT COUNT(*) FROM variants")
    row = await cursor.fetchone()
    return int(row[0]) if row else 0


def _row_to_variant(row: aiosqlite.Row) -> CuratedVariant:
    """Convert a database row to a CuratedVariant model."""
    external_ids = json.loads(row["external_ids"]) if row["external_ids"] else None
    publications = json.loads(row["publications"]) if row["publications"] else None

    return CuratedVariant(
        rsid=row["rsid"],
        gene=row["gene"],
        category=Category(row["category"]),
        name=row["name"],
        significance=Significance(row["significance"]),
        description=row["description"],
        risk_allele=row["risk_allele"],
        normal_allele=row["normal_allele"],
        chromosome=row["chromosome"],
        position=int(row["position"]),
        source=row["source"],
        external_ids=external_ids,
        publications=publications,
        clinvar_stars=int(row["clinvar_stars"]),
        odds_ratio=float(row["odds_ratio"]) if row["odds_ratio"] is not None else None,
    )
