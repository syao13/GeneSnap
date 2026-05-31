"""SQLite database connection management."""

import aiosqlite

from genesnap.config import settings

_db: aiosqlite.Connection | None = None


async def get_db() -> aiosqlite.Connection:
    """Get the database connection, initializing if needed."""
    global _db
    if _db is None:
        _db = await aiosqlite.connect(settings.db_path)
        _db.row_factory = aiosqlite.Row
    return _db


async def init_db() -> None:
    """Initialize the database and create tables if they don't exist."""
    db = await get_db()
    await db.executescript(SCHEMA_SQL)
    await _migrate(db)
    await db.commit()


async def _migrate(db: aiosqlite.Connection) -> None:
    """Add columns that may be missing from older databases."""
    cursor = await db.execute("PRAGMA table_info(variants)")
    columns = {row[1] for row in await cursor.fetchall()}

    if "clinvar_stars" not in columns:
        await db.execute("ALTER TABLE variants ADD COLUMN clinvar_stars INTEGER NOT NULL DEFAULT 0")
    if "odds_ratio" not in columns:
        await db.execute("ALTER TABLE variants ADD COLUMN odds_ratio REAL")


async def close_db() -> None:
    """Close the database connection."""
    global _db
    if _db is not None:
        await _db.close()
        _db = None


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS variants (
    rsid TEXT PRIMARY KEY,
    gene TEXT NOT NULL,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    significance TEXT NOT NULL,
    description TEXT NOT NULL,
    risk_allele TEXT,
    normal_allele TEXT,
    chromosome TEXT NOT NULL,
    position INTEGER NOT NULL,
    source TEXT NOT NULL,
    external_ids TEXT,
    publications TEXT,
    clinvar_stars INTEGER NOT NULL DEFAULT 0,
    odds_ratio REAL,
    last_updated TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS genotype_interpretations (
    rsid TEXT NOT NULL,
    genotype TEXT NOT NULL,
    interpretation TEXT NOT NULL,
    risk_level TEXT NOT NULL,
    FOREIGN KEY (rsid) REFERENCES variants(rsid),
    PRIMARY KEY (rsid, genotype)
);

CREATE TABLE IF NOT EXISTS api_cache (
    cache_key TEXT PRIMARY KEY,
    response_json TEXT NOT NULL,
    fetched_at TEXT NOT NULL,
    expires_at TEXT NOT NULL
);
"""
