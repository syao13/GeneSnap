"""Seed the curated variant database with known clinically significant variants."""

import json
import sqlite3
from datetime import date
from pathlib import Path

from genesnap.db.connection import SCHEMA_SQL
from genesnap.db.variants import GENOTYPE_INTERPRETATIONS, VARIANTS

TODAY = date.today().isoformat()


def seed_database(db_path: Path, force: bool = False) -> None:
    """Create and seed the database with curated variants.

    Args:
        db_path: Path to the SQLite database file.
        force: If True, use INSERT OR REPLACE (overwrites existing rows).
               Default False uses INSERT OR IGNORE (preserves existing rows).
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA_SQL)

    _insert_variants(conn, force=force)
    _insert_genotype_interpretations(conn, force=force)

    conn.commit()
    conn.close()

    cursor = sqlite3.connect(db_path).execute("SELECT COUNT(*) FROM variants")
    count = cursor.fetchone()[0]
    cursor.close()
    print(f"Seeded {count} variants into {db_path}")


def _insert_variants(conn: sqlite3.Connection, force: bool = False) -> None:
    op = "INSERT OR REPLACE" if force else "INSERT OR IGNORE"
    for v in VARIANTS:
        conn.execute(
            f"""{op} INTO variants
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


def _insert_genotype_interpretations(conn: sqlite3.Connection, force: bool = False) -> None:
    op = "INSERT OR REPLACE" if force else "INSERT OR IGNORE"
    for interp in GENOTYPE_INTERPRETATIONS:
        conn.execute(
            f"""{op} INTO genotype_interpretations
            (rsid, genotype, interpretation, risk_level)
            VALUES (?, ?, ?, ?)""",
            (interp["rsid"], interp["genotype"], interp["interpretation"], interp["risk_level"]),
        )


if __name__ == "__main__":
    import argparse

    from genesnap.config import settings

    parser = argparse.ArgumentParser(description="Seed the curated variant database.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing rows (INSERT OR REPLACE). Default is INSERT OR IGNORE.",
    )
    args = parser.parse_args()
    seed_database(settings.db_path, force=args.force)
