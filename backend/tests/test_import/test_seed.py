"""Tests for seed.py INSERT OR IGNORE / force behaviour."""

import sqlite3
from pathlib import Path

from genesnap.db.seed import seed_database


def test_seed_does_not_overwrite_existing_variant(tmp_path: Path) -> None:
    """Default seed (no force) must not replace a variant already in the DB."""
    db_path = tmp_path / "test.db"
    # First seed populates the DB
    seed_database(db_path)

    # Manually corrupt one row
    conn = sqlite3.connect(db_path)
    conn.execute("UPDATE variants SET description = 'SENTINEL' WHERE rsid = 'rs429358'")
    conn.commit()
    conn.close()

    # Second seed without --force must leave SENTINEL intact
    seed_database(db_path)

    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT description FROM variants WHERE rsid = 'rs429358'").fetchone()
    conn.close()
    assert row is not None
    assert row[0] == "SENTINEL"


def test_seed_force_overwrites_existing_variant(tmp_path: Path) -> None:
    """seed_database(force=True) must replace existing rows."""
    db_path = tmp_path / "test.db"
    seed_database(db_path)

    conn = sqlite3.connect(db_path)
    conn.execute("UPDATE variants SET description = 'SENTINEL' WHERE rsid = 'rs429358'")
    conn.commit()
    conn.close()

    seed_database(db_path, force=True)

    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT description FROM variants WHERE rsid = 'rs429358'").fetchone()
    conn.close()
    assert row is not None
    assert row[0].startswith("One of two SNPs")
