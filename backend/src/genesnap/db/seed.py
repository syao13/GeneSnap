"""Seed the curated variant database with known clinically significant variants."""

import json
import sqlite3
from datetime import date
from pathlib import Path

from genesnap.db.connection import SCHEMA_SQL
from genesnap.db.variants import GENOTYPE_INTERPRETATIONS, VARIANTS

TODAY = date.today().isoformat()


def seed_database(db_path: Path) -> None:
    """Create and seed the database with curated variants."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA_SQL)

    _insert_variants(conn)
    _insert_genotype_interpretations(conn)

    conn.commit()
    conn.close()

    cursor = sqlite3.connect(db_path).execute("SELECT COUNT(*) FROM variants")
    count = cursor.fetchone()[0]
    cursor.close()
    print(f"Seeded {count} variants into {db_path}")


def _insert_variants(conn: sqlite3.Connection) -> None:
    """Insert all curated variants."""
    for v in VARIANTS:
        conn.execute(
            """INSERT OR REPLACE INTO variants
            (rsid, gene, category, name, significance, description,
             risk_allele, normal_allele, chromosome, position, source,
             external_ids, publications, clinvar_stars, odds_ratio, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                v["rsid"],
                v["gene"],
                v["category"],
                v["name"],
                v["significance"],
                v["description"],
                v.get("risk_allele"),
                v.get("normal_allele"),
                v["chromosome"],
                v["position"],
                v["source"],
                json.dumps(v.get("external_ids")) if v.get("external_ids") else None,
                json.dumps(v.get("publications")) if v.get("publications") else None,
                v.get("clinvar_stars", 0),
                v.get("odds_ratio"),
                TODAY,
            ),
        )


def _insert_genotype_interpretations(conn: sqlite3.Connection) -> None:
    """Insert genotype interpretations for all variants."""
    for interp in GENOTYPE_INTERPRETATIONS:
        conn.execute(
            """INSERT OR REPLACE INTO genotype_interpretations
            (rsid, genotype, interpretation, risk_level)
            VALUES (?, ?, ?, ?)""",
            (interp["rsid"], interp["genotype"], interp["interpretation"], interp["risk_level"]),
        )


if __name__ == "__main__":
    from genesnap.config import settings

    seed_database(settings.db_path)
