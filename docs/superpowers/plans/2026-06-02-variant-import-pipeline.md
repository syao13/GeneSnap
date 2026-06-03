# Variant Import Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a standalone ETL script that bulk-imports ~93,000 variants from ClinVar, GWAS Catalog, and PharmGKB into the existing SQLite DB, expanding coverage from ~803 curated entries without changing the app at all.

**Architecture:** A `backend/scripts/` directory contains the CLI entry point (`import_variants.py`) and three source parsers (`clinvar.py`, `gwas.py`, `pharmgkb.py`) plus shared template generation (`templates.py`). ClinVar is parsed first to build a `rsid→(ref,alt)` allele lookup that GWAS and PharmGKB use to generate genotype interpretations. All inserts use `INSERT OR IGNORE` so hand-curated data is never overwritten. `seed.py` is updated from `INSERT OR REPLACE` to `INSERT OR IGNORE` by default with a `--force` opt-in.

**Tech Stack:** Python 3.12, sqlite3 (stdlib), gzip (stdlib), csv (stdlib), argparse (stdlib), uv for running scripts. Tests use pytest with in-memory SQLite and local fixture files — no network calls.

---

## File Map

**New files:**
- `backend/scripts/__init__.py` — empty, makes scripts importable
- `backend/scripts/sources/__init__.py` — empty
- `backend/scripts/sources/templates.py` — `make_genotypes()`, `clinvar_interpretations()`, `gwas_interpretations()`, `pharmgkb_interpretations()`
- `backend/scripts/sources/clinvar.py` — `parse_clinvar_vcf()` → yields `(VariantDict, list[InterpretationDict])` + returns `rsid_alleles` dict
- `backend/scripts/sources/gwas.py` — `parse_gwas_tsv()` → yields `(VariantDict, list[InterpretationDict])`
- `backend/scripts/sources/pharmgkb.py` — `parse_pharmgkb_annotations()` → yields `(VariantDict, list[InterpretationDict])`
- `backend/scripts/import_variants.py` — CLI entry point, orchestrates download + parse + insert
- `backend/scripts/data/star_allele_rsids.json` — `{"CYP2C19*2": {"rsid": "rs4244285", "risk_allele": "A", "ref_allele": "G"}, ...}`
- `backend/tests/test_import/__init__.py` — empty
- `backend/tests/test_import/fixtures/sample_clinvar.vcf` — 8 test VCF lines
- `backend/tests/test_import/fixtures/sample_gwas.tsv` — 7 test TSV rows
- `backend/tests/test_import/fixtures/sample_pharmgkb.tsv` — 5 test rows
- `backend/tests/test_import/test_templates.py`
- `backend/tests/test_import/test_clinvar.py`
- `backend/tests/test_import/test_gwas.py`
- `backend/tests/test_import/test_pharmgkb.py`
- `backend/tests/test_import/test_seed.py`

**Modified files:**
- `backend/src/genesnap/db/seed.py` — `INSERT OR REPLACE` → `INSERT OR IGNORE` by default; add `force: bool = False` param; update `__main__` block

---

## Task 1: Update seed.py to use INSERT OR IGNORE by default

**Files:**
- Modify: `backend/src/genesnap/db/seed.py`
- Test: `backend/tests/test_import/test_seed.py`

- [ ] **Step 1: Create the test file and write failing tests**

Create `backend/tests/test_import/__init__.py` (empty) and `backend/tests/test_import/test_seed.py`:

```python
"""Tests for seed.py INSERT OR IGNORE / force behaviour."""

import json
import sqlite3
from pathlib import Path

import pytest

from genesnap.db.connection import SCHEMA_SQL
from genesnap.db.seed import seed_database


def _make_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA_SQL)
    conn.commit()
    return conn


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
    assert row[0] != "SENTINEL"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd backend && uv run pytest tests/test_import/test_seed.py -v
```

Expected: `FAILED` — `seed_database` does not accept `force` param yet.

- [ ] **Step 3: Update seed.py**

Replace the entire file content:

```python
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
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd backend && uv run pytest tests/test_import/test_seed.py -v
```

Expected: `2 passed`

- [ ] **Step 5: Run full test suite to check nothing broke**

```bash
cd backend && uv run pytest -v
```

Expected: all previously passing tests still pass.

- [ ] **Step 6: Commit**

```bash
git add backend/src/genesnap/db/seed.py backend/tests/test_import/__init__.py backend/tests/test_import/test_seed.py
git commit -m "feat: change seed.py to INSERT OR IGNORE by default, add --force flag"
```

---

## Task 2: Create scripts directory structure and star_allele_rsids.json

**Files:**
- Create: `backend/scripts/__init__.py`
- Create: `backend/scripts/sources/__init__.py`
- Create: `backend/scripts/data/star_allele_rsids.json`

- [ ] **Step 1: Create empty init files**

Create `backend/scripts/__init__.py` — empty file.
Create `backend/scripts/sources/__init__.py` — empty file.

- [ ] **Step 2: Create star_allele_rsids.json**

Create `backend/scripts/data/star_allele_rsids.json`:

```json
{
  "CYP2C19*2":  {"rsid": "rs4244285",   "risk_allele": "A", "ref_allele": "G"},
  "CYP2C19*3":  {"rsid": "rs4986893",   "risk_allele": "A", "ref_allele": "G"},
  "CYP2C19*17": {"rsid": "rs12248560",  "risk_allele": "T", "ref_allele": "C"},
  "CYP2D6*4":   {"rsid": "rs3892097",   "risk_allele": "A", "ref_allele": "G"},
  "CYP2D6*10":  {"rsid": "rs1065852",   "risk_allele": "T", "ref_allele": "C"},
  "CYP2D6*17":  {"rsid": "rs28371706",  "risk_allele": "C", "ref_allele": "T"},
  "CYP2D6*41":  {"rsid": "rs28371725",  "risk_allele": "A", "ref_allele": "G"},
  "CYP2C9*2":   {"rsid": "rs1799853",   "risk_allele": "T", "ref_allele": "C"},
  "CYP2C9*3":   {"rsid": "rs1057910",   "risk_allele": "C", "ref_allele": "A"},
  "CYP2C9*5":   {"rsid": "rs28371686",  "risk_allele": "C", "ref_allele": "G"},
  "CYP2C9*6":   {"rsid": "rs9332131",   "risk_allele": "A", "ref_allele": "G"},
  "CYP2B6*6":   {"rsid": "rs3745274",   "risk_allele": "T", "ref_allele": "G"},
  "DPYD*2A":    {"rsid": "rs3918290",   "risk_allele": "A", "ref_allele": "G"},
  "DPYD*13":    {"rsid": "rs55886062",  "risk_allele": "A", "ref_allele": "G"},
  "TPMT*2":     {"rsid": "rs1800462",   "risk_allele": "A", "ref_allele": "G"},
  "TPMT*3B":    {"rsid": "rs1800460",   "risk_allele": "A", "ref_allele": "G"},
  "TPMT*3C":    {"rsid": "rs1142345",   "risk_allele": "C", "ref_allele": "T"},
  "NUDT15*3":   {"rsid": "rs116855232", "risk_allele": "T", "ref_allele": "C"},
  "SLCO1B1*5":  {"rsid": "rs4149056",   "risk_allele": "C", "ref_allele": "T"},
  "UGT1A1*6":   {"rsid": "rs4148323",   "risk_allele": "A", "ref_allele": "G"},
  "CYP3A5*3":   {"rsid": "rs776746",    "risk_allele": "A", "ref_allele": "G"},
  "VKORC1*2":   {"rsid": "rs9923231",   "risk_allele": "A", "ref_allele": "G"},
  "HLA-B*57:01": {"rsid": "rs2395029",  "risk_allele": "G", "ref_allele": "T"},
  "HLA-B*58:01": {"rsid": "rs9263726",  "risk_allele": "C", "ref_allele": "G"},
  "IFNL3*rs12979860": {"rsid": "rs12979860", "risk_allele": "T", "ref_allele": "C"}
}
```

- [ ] **Step 3: Commit**

```bash
git add backend/scripts/ 
git commit -m "feat: add scripts directory structure and PharmGKB star allele lookup"
```

---

## Task 3: Create templates.py and tests

**Files:**
- Create: `backend/scripts/sources/templates.py`
- Test: `backend/tests/test_import/test_templates.py`

- [ ] **Step 1: Write failing tests**

Create `backend/tests/test_import/test_templates.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd backend && uv run pytest tests/test_import/test_templates.py -v
```

Expected: `ImportError` or `ModuleNotFoundError` — templates.py doesn't exist yet.

- [ ] **Step 3: Create templates.py**

Create `backend/scripts/sources/templates.py`:

```python
"""Shared template functions for generating per-genotype interpretations."""

from math import floor, log10

from genesnap.db.variants._types import InterpretationDict


def make_genotypes(ref: str, alt: str) -> tuple[str, str, str]:
    """Return (hom_ref, het, hom_alt) genotype strings.

    Het is alphabetically sorted to match 23andMe reporting convention.
    """
    return ref + ref, "".join(sorted([ref, alt])), alt + alt


def clinvar_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    condition: str,
    significance: str,
    stars: int,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a ClinVar variant."""
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)
    stars_display = "★" * stars + "☆" * (4 - stars)

    if significance == "drug_response":
        drug = condition.lower().replace(" response", "").replace(" metabolism", "").strip()
        return [
            {
                "rsid": rsid,
                "genotype": ref_ref,
                "interpretation": f"Standard {gene} function expected for {drug} metabolism.",
                "risk_level": "normal",
            },
            {
                "rsid": rsid,
                "genotype": het,
                "interpretation": (
                    f"You carry one copy of a {gene} drug response variant affecting {drug}. "
                    "Consult your prescriber if taking this medication."
                ),
                "risk_level": "increased_risk",
            },
            {
                "rsid": rsid,
                "genotype": alt_alt,
                "interpretation": (
                    f"You carry two copies of a {gene} drug response variant affecting {drug}. "
                    "Prescriber consultation is strongly recommended."
                ),
                "risk_level": "high_risk",
            },
        ]

    sig_display = significance.replace("_", " ")
    strength = "strongly recommended" if significance == "pathogenic" else "recommended"
    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": f"You do not carry this {gene} variant associated with {condition}.",
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of this {sig_display} {gene} variant associated with "
                f"{condition} (ClinVar {stars_display}). "
                "Consider discussing with a healthcare provider."
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of this {sig_display} {gene} variant associated with "
                f"{condition} (ClinVar {stars_display}). "
                f"Clinical confirmation is {strength}."
            ),
            "risk_level": "high_risk",
        },
    ]


def gwas_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    trait: str,
    odds_ratio: float | None,
    pval: float | None,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a GWAS association.

    GWAS variants are capped at increased_risk — never high_risk.
    """
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)

    if odds_ratio is not None:
        or_str = f"{odds_ratio:.1f}x"
        or_het = 1 + (odds_ratio - 1) / 2 if odds_ratio > 1 else odds_ratio
        or_het_str = f"{or_het:.1f}x"
    else:
        or_str = or_het_str = "unknown"

    if pval is not None and pval > 0:
        exp = floor(log10(pval))
        mantissa = pval / (10**exp)
        pval_str = f"{mantissa:.1f}×10⁻{abs(exp)}"
    else:
        pval_str = "unknown"

    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": f"You do not carry the {trait} risk allele in {gene}.",
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of the {gene} risk allele associated with {trait} "
                f"(OR: ~{or_het_str} above baseline, p={pval_str}, population-level association)."
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of the {gene} risk allele associated with {trait} "
                f"(OR: {or_str} above baseline, p={pval_str}, population-level association)."
            ),
            "risk_level": "increased_risk",
        },
    ]


def pharmgkb_interpretations(
    *,
    rsid: str,
    ref: str,
    alt: str,
    gene: str,
    drug: str,
    phenotype: str,
    level: str,
    star_allele: str,
    is_sex_chrom: bool,
) -> list[InterpretationDict]:
    """Generate three genotype interpretation rows for a PharmGKB annotation."""
    if is_sex_chrom:
        return []

    ref_ref, het, alt_alt = make_genotypes(ref, alt)
    label = star_allele if star_allele else gene

    return [
        {
            "rsid": rsid,
            "genotype": ref_ref,
            "interpretation": (
                f"You do not carry {label}. Normal {gene} function expected for {drug}."
            ),
            "risk_level": "normal",
        },
        {
            "rsid": rsid,
            "genotype": het,
            "interpretation": (
                f"You carry one copy of {label}, associated with {phenotype} for {drug}. "
                f"Consult prescriber if taking {drug}. (CPIC Level {level})"
            ),
            "risk_level": "increased_risk",
        },
        {
            "rsid": rsid,
            "genotype": alt_alt,
            "interpretation": (
                f"You carry two copies of {label} ({phenotype}). "
                f"CPIC Level {level} guideline recommends review of {drug} therapy."
            ),
            "risk_level": "high_risk",
        },
    ]
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd backend && uv run pytest tests/test_import/test_templates.py -v
```

Expected: `9 passed`

- [ ] **Step 5: Commit**

```bash
git add backend/scripts/sources/templates.py backend/tests/test_import/test_templates.py
git commit -m "feat: add genotype interpretation template functions"
```

---

## Task 4: Create ClinVar parser and tests

**Files:**
- Create: `backend/scripts/sources/clinvar.py`
- Create: `backend/tests/test_import/fixtures/sample_clinvar.vcf`
- Test: `backend/tests/test_import/test_clinvar.py`

**Background — ClinVar VCF format:**
- The `ID` column contains the ClinVar VariationID (a number), NOT the rsID
- The rsID is in the `INFO` field as `RS=<number>` (without "rs" prefix)
- `CLNSIG` contains significance, pipe-separated when multiple alleles, e.g. `Pathogenic` or `Pathogenic/Likely_pathogenic`
- `CLNREVSTAT` contains the review status string with underscores and commas, e.g. `criteria_provided,_multiple_submitters,_no_conflicts`
- `CLNDN` contains the condition name with underscores, pipe-separated if multiple conditions
- `GENEINFO` format: `GENENAME:GENEID` or `GENE1:ID1|GENE2:ID2` — take the first gene name

- [ ] **Step 1: Create the fixture VCF**

Create `backend/tests/test_import/fixtures/sample_clinvar.vcf`:

```
##fileformat=VCFv4.1
##INFO=<ID=CLNSIG,Number=.,Type=String,Description="Clinical significance">
##INFO=<ID=CLNREVSTAT,Number=.,Type=String,Description="Review status">
##INFO=<ID=CLNDN,Number=.,Type=String,Description="Disease name">
##INFO=<ID=GENEINFO,Number=1,Type=String,Description="Gene info">
##INFO=<ID=RS,Number=1,Type=Integer,Description="dbSNP ID">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO
1	169519049	929301	G	A	.	.	RS=6025;CLNSIG=Pathogenic;CLNREVSTAT=reviewed_by_expert_panel;CLNDN=Thrombophilia_due_to_activated_protein_C_resistance;GENEINFO=F5:2153
17	41276045	17661	G	A	.	.	RS=80357906;CLNSIG=Pathogenic;CLNREVSTAT=practice_guideline;CLNDN=Hereditary_breast_and_ovarian_cancer_syndrome;GENEINFO=BRCA1:672
10	96702047	12345	C	T	.	.	RS=1799853;CLNSIG=drug_response;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNDN=Warfarin_response;GENEINFO=CYP2C9:1559
1	1000000	99999	G	A	.	.	RS=9999999;CLNSIG=Pathogenic;CLNREVSTAT=criteria_provided,_single_submitter;CLNDN=Some_disease;GENEINFO=GENE1:12345
1	2000000	88888	G	A	.	.	RS=8888888;CLNSIG=Conflicting_interpretations_of_pathogenicity;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNDN=Some_disease;GENEINFO=GENE2:12346
1	3000000	77777	G	A	.	.	CLNSIG=Pathogenic;CLNREVSTAT=reviewed_by_expert_panel;CLNDN=Some_disease;GENEINFO=GENE3:12347
X	154931326	55555	G	A	.	.	RS=5978;CLNSIG=Pathogenic;CLNREVSTAT=reviewed_by_expert_panel;CLNDN=Hemophilia_B;GENEINFO=F9:2158
17	7577538	44444	C	T	.	.	RS=63750447;CLNSIG=Pathogenic;CLNREVSTAT=practice_guideline;CLNDN=Li-Fraumeni_syndrome|not_provided;GENEINFO=TP53:7157
```

Lines and what they test:
1. rs6025 — Pathogenic, 3★, autosomal → included, 3 interpretation rows
2. rs80357906 — Pathogenic, 4★, autosomal → included (will be skipped by INSERT OR IGNORE in the real DB)
3. rs1799853 — drug_response, 2★ → included as pharmacogenomics
4. rs9999999 — 1★ only → excluded
5. rs8888888 — Conflicting → excluded
6. No RS= in INFO → excluded
7. rs5978 — X-linked, 3★ → included in variants, zero interpretation rows
8. rs63750447 — multiple CLNDN with "not_provided" → condition picks first non-"not_provided"

- [ ] **Step 2: Write failing tests**

Create `backend/tests/test_import/test_clinvar.py`:

```python
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
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd backend && uv run pytest tests/test_import/test_clinvar.py -v
```

Expected: `ImportError` — clinvar.py doesn't exist yet.

- [ ] **Step 4: Create clinvar.py**

Create `backend/scripts/sources/clinvar.py`:

```python
"""ClinVar VCF parser: filters to pathogenic/LP/drug_response with >=2 review stars."""

import gzip
from datetime import date
from pathlib import Path

from genesnap.db.variants._types import InterpretationDict, VariantDict

from sources.templates import clinvar_interpretations

TODAY = date.today().isoformat()

SEX_CHROMS = {"X", "Y", "MT"}

ALLOWED_CLNSIG = {"Pathogenic", "Likely_pathogenic", "drug_response", "Pathogenic/Likely_pathogenic"}
EXCLUDED_CLNSIG_SUBSTRINGS = {"Conflicting_interpretations"}

REVSTAT_STARS: dict[str, int] = {
    "practice_guideline": 4,
    "reviewed_by_expert_panel": 3,
    "criteria_provided,_multiple_submitters,_no_conflicts": 2,
}

CLNSIG_TO_SIGNIFICANCE: dict[str, str] = {
    "Pathogenic": "pathogenic",
    "Likely_pathogenic": "likely_pathogenic",
    "Pathogenic/Likely_pathogenic": "pathogenic",
    "drug_response": "drug_response",
}


def _parse_info(info_str: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for field in info_str.split(";"):
        if "=" in field:
            k, v = field.split("=", 1)
            result[k] = v
    return result


def _pick_clnsig(raw: str) -> str | None:
    """Pick the most actionable significance from a pipe-separated CLNSIG string."""
    for val in raw.split("|"):
        if any(excl in val for excl in EXCLUDED_CLNSIG_SUBSTRINGS):
            return None
        if val in ALLOWED_CLNSIG:
            return val
    return None


def _pick_revstat_stars(raw: str) -> int | None:
    """Return star count for the best review status in a pipe-separated CLNREVSTAT string."""
    for allowed, stars in REVSTAT_STARS.items():
        if allowed in raw:
            return stars
    return None


def _clean_condition(clndn: str) -> str:
    """Pick first non-'not_provided' condition and replace underscores."""
    parts = [p for p in clndn.split("|") if p.lower() not in {"not_provided", "not_specified"}]
    raw = parts[0] if parts else clndn.split("|")[0]
    return raw.replace("_", " ").strip()


def _pick_gene(geneinfo: str) -> str:
    first = geneinfo.split("|")[0]
    return first.split(":")[0].strip() or "UNKNOWN"


def parse_clinvar_vcf(
    vcf_path: Path,
) -> tuple[list[tuple[VariantDict, list[InterpretationDict]]], dict[str, tuple[str, str]]]:
    """Parse ClinVar VCF, returning filtered variants and a ref/alt allele lookup.

    Returns:
        (variants_and_interps, rsid_alleles) where rsid_alleles maps rsid → (ref, alt).
        rsid_alleles is passed to parse_gwas_tsv and parse_pharmgkb_annotations so
        they can generate genotype interpretations.
    """
    rsid_alleles: dict[str, tuple[str, str]] = {}
    results: list[tuple[VariantDict, list[InterpretationDict]]] = []

    opener = gzip.open if str(vcf_path).endswith(".gz") else open
    with opener(vcf_path, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            parts = line.strip().split("\t")
            if len(parts) < 8:
                continue

            chrom, pos_str, _var_id, ref, alt, _qual, _filt, info_str = parts[:8]

            # Skip multi-allelic
            if "," in alt:
                continue

            info = _parse_info(info_str)

            # rsID from INFO RS= field (not ID column, which is ClinVar VariationID)
            rs_num = info.get("RS", "")
            if not rs_num:
                continue
            rsid = f"rs{rs_num}"

            clnsig_raw = info.get("CLNSIG", "")
            clnsig = _pick_clnsig(clnsig_raw)
            if clnsig is None:
                continue

            revstat_raw = info.get("CLNREVSTAT", "")
            stars = _pick_revstat_stars(revstat_raw)
            if stars is None:
                continue

            condition = _clean_condition(info.get("CLNDN", "not_provided"))
            gene = _pick_gene(info.get("GENEINFO", "UNKNOWN:0"))
            significance = CLNSIG_TO_SIGNIFICANCE.get(clnsig, "risk_factor")
            is_sex = chrom in SEX_CHROMS
            category = "pharmacogenomics" if significance == "drug_response" else "health_risk"
            stars_display = "★" * stars + "☆" * (4 - stars)

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": category,
                "name": f"{gene} – {condition}",
                "significance": significance,
                "description": (
                    f"{significance.replace('_', ' ').title()} variant in {gene} "
                    f"associated with {condition} (ClinVar {stars_display}). "
                    "Imported from ClinVar."
                ),
                "risk_allele": alt,
                "normal_allele": ref,
                "chromosome": chrom,
                "position": int(pos_str),
                "source": "clinvar_import",
                "clinvar_stars": stars,
                "odds_ratio": None,
                "publications": None,
                "external_ids": None,
            }

            interps = clinvar_interpretations(
                rsid=rsid, ref=ref, alt=alt, gene=gene,
                condition=condition, significance=significance,
                stars=stars, is_sex_chrom=is_sex,
            )

            rsid_alleles[rsid] = (ref, alt)
            results.append((variant, interps))

    return results, rsid_alleles
```

- [ ] **Step 5: Run tests — expect PASS**

```bash
cd backend && uv run pytest tests/test_import/test_clinvar.py -v
```

Expected: `10 passed`

- [ ] **Step 6: Commit**

```bash
git add backend/scripts/sources/clinvar.py \
        backend/tests/test_import/fixtures/sample_clinvar.vcf \
        backend/tests/test_import/test_clinvar.py
git commit -m "feat: add ClinVar VCF parser with filtering and template interpretations"
```

---

## Task 5: Create GWAS Catalog parser and tests

**Files:**
- Create: `backend/scripts/sources/gwas.py`
- Create: `backend/tests/test_import/fixtures/sample_gwas.tsv`
- Test: `backend/tests/test_import/test_gwas.py`

**Background — GWAS Catalog TSV format:**
- Tab-separated with a header row
- Key columns: `DISEASE/TRAIT`, `INITIAL SAMPLE SIZE`, `STRONGEST SNP-RISK ALLELE` (format: `rs1234-T`), `SNPS`, `MAPPED_GENE`, `P-VALUE`, `OR or BETA`, `CHR_ID`, `CHR_POS`
- `SNPS` can be space-separated for multi-SNP rows (e.g. `rs1234 rs5678`) — exclude these
- GWAS doesn't provide REF allele; use `rsid_alleles` dict (from ClinVar) when available, otherwise skip interpretations

- [ ] **Step 1: Create the fixture TSV**

Create `backend/tests/test_import/fixtures/sample_gwas.tsv` (lines separated by actual tabs):

```
DATE ADDED TO CATALOG	PUBMEDID	FIRST AUTHOR	DATE	JOURNAL	LINK	STUDY	DISEASE/TRAIT	INITIAL SAMPLE SIZE	REPLICATION SAMPLE SIZE	REGION	CHR_ID	CHR_POS	REPORTED GENE(S)	MAPPED_GENE	UPSTREAM_GENE_ID	DOWNSTREAM_GENE_ID	SNP_GENE_IDS	UPSTREAM_GENE_DISTANCE	DOWNSTREAM_GENE_DISTANCE	STRONGEST SNP-RISK ALLELE	SNPS	MERGED	SNP_ID_CURRENT	CONTEXT	INTERGENIC	RISK ALLELE FREQUENCY	P-VALUE	PVALUE_MLOG	P-VALUE (TEXT)	OR or BETA	95% CI (TEXT)	PLATFORM [SNPS PASSING QC]	CNV	MAPPED_TRAIT	MAPPED_TRAIT_URI	STUDY ACCESSION	GENOTYPING TECHNOLOGY
2010-01-01	17463246	Doe J	2007-01-14	Nature Genetics	http://example.com	GWAS of T2D	Type 2 diabetes	10000 European individuals		10q25.2	10	114758349	TCF7L2	TCF7L2			12345			rs7903146-T	rs7903146	0	7903146	intron_variant	0	0.30	3.2e-35	34.5		1.4	[1.35-1.45]	Illumina	N	type 2 diabetes mellitus	http://www.ebi.ac.uk/efo/EFO_0001360	GCST000123	Genome-wide genotyping array
2010-01-01	20453838	Smith A	2008-05-01	Nature	http://example.com	Breast cancer GWAS	Breast cancer	50000 cases		17q21	17	41276045	BRCA1	BRCA1			672			rs1045485-C	rs1045485	0	1045485	missense_variant	0	0.10	5.1e-9	8.3		1.2	[1.15-1.25]	Illumina	N	breast carcinoma	http://www.ebi.ac.uk/efo/EFO_0000305	GCST000456	Genome-wide genotyping array
2010-01-01	18391952	Jones B	2008-09-01	Nature Genetics	http://example.com	Height GWAS	Height	200000 individuals		12q14	12	66259591	HMGA2	HMGA2			8091			rs1042725-C	rs1042725	0	1042725	3_prime_UTR_variant	0	0.47	1e-10	10.0		1.1	[1.08-1.12]	Illumina	N	body height	http://www.ebi.ac.uk/efo/EFO_0004339	GCST000789	Genome-wide genotyping array
2010-01-01	19228618	Clark C	2009-02-01	NEJM	http://example.com	Warfarin dose	Warfarin dose	3000 individuals		16p11.2	16	31096368	VKORC1	VKORC1			79001			rs9923231-A	rs9923231	0	9923231	upstream_gene_variant	0	0.37	1e-50	50.0		0.5	[0.45-0.55]	Illumina	N	warfarin	http://www.ebi.ac.uk/efo/EFO_0000694	GCST001111	Genome-wide genotyping array
2010-01-01	12345678	Multi A	2005-01-01	Science	http://example.com	Multi-SNP study	Some trait	5000 individuals		1p36	1	1000000	GENE1	GENE1			11111			rs1234567-T	rs1234567 rs7654321	0	1234567	intron_variant	0	0.20	1e-8	8.0		1.3	[1.25-1.35]	Illumina	N	some trait	http://www.ebi.ac.uk/efo/EFO_9999999	GCST002222	Genome-wide genotyping array
2010-01-01	22768372	Brew D	2012-06-01	PLOS Genetics	http://example.com	Caffeine study	Caffeine consumption	500 individuals		15q24	15	75041917	CYP1A2	CYP1A2			1544			rs762551-C	rs762551	0	762551	intron_variant	0	0.27	1e-15	15.0		1.5	[1.4-1.6]	Illumina	N	caffeine consumption	http://www.ebi.ac.uk/efo/EFO_0006786	GCST003333	Genome-wide genotyping array
2010-01-01	11111111	Edge E	2006-01-01	Genetics	http://example.com	Tiny study	Tiny trait	200 individuals		2p16	2	20000000	GENE2	GENE2			22222			rs2222222-A	rs2222222	0	2222222	intron_variant	0	0.15	1e-9	9.0		1.2	[1.1-1.3]	Illumina	N	tiny trait	http://www.ebi.ac.uk/efo/EFO_8888888	GCST004444	Genome-wide genotyping array
```

Rows and what they test:
1. rs7903146 — Type 2 diabetes, large sample, TCF7L2 → health_risk, included
2. rs1045485 — Breast cancer, large sample → health_risk, included
3. rs1042725 — Height trait → trait category, included
4. rs9923231 — Warfarin dose, VKORC1 (pharma gene), OR=0.5 (protective → swap alleles) → pharmacogenomics
5. Multi-SNP row (rs1234567 rs7654321 in SNPS) → excluded
6. rs762551 — CYP1A2 pharma gene, sample size 500 (<1000) → excluded
7. rs2222222 — tiny study, sample 200 → excluded

- [ ] **Step 2: Write failing tests**

Create `backend/tests/test_import/test_gwas.py`:

```python
"""Tests for GWAS Catalog TSV parser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from sources.gwas import parse_gwas_tsv

FIXTURES = Path(__file__).parent / "fixtures"

# Minimal rsid_alleles dict (from ClinVar) for tests that need interpretations
KNOWN_ALLELES: dict[str, tuple[str, str]] = {
    "rs7903146": ("C", "T"),
    "rs1045485": ("G", "C"),
    "rs1042725": ("T", "C"),
    "rs9923231": ("G", "A"),
}


def test_includes_large_sample_health_risk() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs7903146" in rsids


def test_excludes_multi_snp_row() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs1234567" not in rsids


def test_excludes_small_sample() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
    assert "rs762551" not in rsids
    assert "rs2222222" not in rsids


def test_pharma_gene_categorized_correctly() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    vkorc1 = next((v for v, _ in results if v["rsid"] == "rs9923231"), None)
    assert vkorc1 is not None
    assert vkorc1["category"] == "pharmacogenomics"


def test_disease_keyword_is_health_risk() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    t2d = next((v for v, _ in results if v["rsid"] == "rs7903146"), None)
    assert t2d is not None
    assert t2d["category"] == "health_risk"


def test_height_is_trait() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    height = next((v for v, _ in results if v["rsid"] == "rs1042725"), None)
    assert height is not None
    assert height["category"] == "trait"


def test_protective_allele_swapped() -> None:
    """OR=0.5 for A allele means A is protective; risk and ref should be swapped."""
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    vkorc1 = next((v for v, _ in results if v["rsid"] == "rs9923231"), None)
    assert vkorc1 is not None
    # Original: STRONGEST SNP-RISK ALLELE = rs9923231-A, OR=0.5
    # After swap: risk_allele should be G (the non-A allele, OR = 1/0.5 = 2.0)
    assert vkorc1["risk_allele"] == "G"
    assert vkorc1["odds_ratio"] is not None
    assert vkorc1["odds_ratio"] > 1.0


def test_known_alleles_generates_interpretations() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    t2d = next((v, i) for v, i in results if v["rsid"] == "rs7903146")
    _, interps = t2d
    assert len(interps) == 3


def test_unknown_alleles_skips_interpretations() -> None:
    """GWAS variant with no entry in rsid_alleles → no interpretation rows."""
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", {}))
    t2d = next((v, i) for v, i in results if v["rsid"] == "rs7903146")
    _, interps = t2d
    assert interps == []


def test_source_is_gwas_import() -> None:
    results = list(parse_gwas_tsv(FIXTURES / "sample_gwas.tsv", KNOWN_ALLELES))
    assert all(v["source"] == "gwas_import" for v, _ in results)
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd backend && uv run pytest tests/test_import/test_gwas.py -v
```

Expected: `ImportError` — gwas.py doesn't exist.

- [ ] **Step 4: Create gwas.py**

Create `backend/scripts/sources/gwas.py`:

```python
"""GWAS Catalog TSV parser: filters to genome-wide significant associations."""

import csv
import re
from datetime import date
from pathlib import Path
from typing import Iterator

from genesnap.db.variants._types import InterpretationDict, VariantDict

from sources.templates import gwas_interpretations

TODAY = date.today().isoformat()

SEX_CHROMS = {"X", "Y", "MT"}
MIN_SAMPLE_SIZE = 1000
PVAL_THRESHOLD = 5e-8

PHARMA_GENES = {
    "CYP2D6", "CYP2C19", "CYP2C9", "CYP3A4", "CYP3A5", "CYP1A2", "CYP2B6",
    "UGT1A1", "UGT2B7", "VKORC1", "DPYD", "TPMT", "NUDT15", "SLCO1B1",
    "IFNL3", "HLA-B", "HLA-A", "G6PD", "CACNA1S", "RYR1",
}
HEALTH_RISK_KEYWORDS = {
    "cancer", "disease", "syndrome", "disorder", "carcinoma", "leukemia",
    "diabetes", "hypertension", "infarction", "stroke", "thrombosis",
    "anemia", "fibrosis", "tumor", "tumour", "melanoma", "sclerosis",
}


def _parse_sample_size(s: str) -> int:
    nums = [int(n.replace(",", "")) for n in re.findall(r"[\d,]+", s)]
    return max(nums) if nums else 0


def _parse_pval(s: str) -> float | None:
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def _parse_or(s: str) -> float | None:
    try:
        v = float(s)
        return v if v > 0 else None
    except (ValueError, TypeError):
        return None


def _parse_gene(mapped_gene: str) -> str:
    gene = mapped_gene.strip()
    for sep in [" - ", " x ", ", ", ";"]:
        if sep in gene:
            gene = gene.split(sep)[0].strip()
    return gene or "UNKNOWN"


def _categorize(gene: str, trait: str) -> str:
    if gene in PHARMA_GENES:
        return "pharmacogenomics"
    if any(kw in trait.lower() for kw in HEALTH_RISK_KEYWORDS):
        return "health_risk"
    return "trait"


def parse_gwas_tsv(
    tsv_path: Path,
    rsid_alleles: dict[str, tuple[str, str]],
) -> Iterator[tuple[VariantDict, list[InterpretationDict]]]:
    """Parse GWAS Catalog full associations TSV.

    Args:
        tsv_path: Path to the GWAS Catalog TSV file.
        rsid_alleles: Dict of rsid→(ref,alt) from ClinVar. Used to generate
                      genotype interpretations. Variants not in this dict still
                      get a variants row but no interpretation rows.
    """
    seen_rsids: set[str] = set()

    with open(tsv_path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            # Parse and filter SNPS field — must be a single rsID
            snps_field = row.get("SNPS", "").strip()
            if " " in snps_field or not snps_field.startswith("rs"):
                continue
            rsid = snps_field

            if rsid in seen_rsids:
                continue

            # Parse p-value
            pval = _parse_pval(row.get("P-VALUE", ""))
            if pval is None or pval >= PVAL_THRESHOLD:
                continue

            # Parse sample size
            sample_size = _parse_sample_size(row.get("INITIAL SAMPLE SIZE", ""))
            if sample_size < MIN_SAMPLE_SIZE:
                continue

            # Parse risk allele from "rs1234-T" format
            strongest = row.get("STRONGEST SNP-RISK ALLELE", "")
            if "-" not in strongest:
                continue
            risk_allele_from_gwas = strongest.split("-", 1)[1].strip()
            if not risk_allele_from_gwas or risk_allele_from_gwas in {"?", "N"}:
                continue

            chrom = row.get("CHR_ID", "").strip()
            pos_str = row.get("CHR_POS", "").strip()
            if not pos_str.isdigit():
                continue

            gene = _parse_gene(row.get("MAPPED_GENE", "UNKNOWN"))
            trait = row.get("DISEASE/TRAIT", "").strip()
            or_val = _parse_or(row.get("OR or BETA", ""))
            is_sex = chrom in SEX_CHROMS
            category = _categorize(gene, trait)

            # Get ref/alt from ClinVar lookup
            alleles = rsid_alleles.get(rsid)
            if alleles:
                ref, alt = alleles
            else:
                ref, alt = None, None

            # Handle protective alleles (OR < 1): swap so risk_allele always has OR >= 1
            risk_allele = risk_allele_from_gwas
            normal_allele = ref if ref else None
            if or_val is not None and or_val < 1.0 and ref is not None:
                # Risk allele from GWAS is actually protective; swap
                risk_allele = ref
                normal_allele = risk_allele_from_gwas
                alt = ref
                ref = risk_allele_from_gwas
                or_val = round(1.0 / or_val, 3) if or_val > 0 else None

            seen_rsids.add(rsid)

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": category,
                "name": f"{gene} – {trait}",
                "significance": "association",
                "description": (
                    f"Associated with {trait} in {gene} "
                    f"(OR: {or_val:.2f}x, p={pval:.2e}, GWAS Catalog)."
                    if or_val else
                    f"Associated with {trait} in {gene} (p={pval:.2e}, GWAS Catalog)."
                ),
                "risk_allele": risk_allele,
                "normal_allele": normal_allele,
                "chromosome": chrom,
                "position": int(pos_str),
                "source": "gwas_import",
                "clinvar_stars": 0,
                "odds_ratio": or_val,
                "publications": None,
                "external_ids": None,
            }

            interps: list[InterpretationDict] = []
            if ref is not None and not is_sex:
                interps = gwas_interpretations(
                    rsid=rsid, ref=ref, alt=alt,  # type: ignore[arg-type]
                    gene=gene, trait=trait,
                    odds_ratio=or_val, pval=pval,
                    is_sex_chrom=is_sex,
                )

            yield variant, interps
```

- [ ] **Step 5: Run tests — expect PASS**

```bash
cd backend && uv run pytest tests/test_import/test_gwas.py -v
```

Expected: `10 passed`

- [ ] **Step 6: Commit**

```bash
git add backend/scripts/sources/gwas.py \
        backend/tests/test_import/fixtures/sample_gwas.tsv \
        backend/tests/test_import/test_gwas.py
git commit -m "feat: add GWAS Catalog TSV parser with categorization and interpretation templates"
```

---

## Task 6: Create PharmGKB parser and tests

**Files:**
- Create: `backend/scripts/sources/pharmgkb.py`
- Create: `backend/tests/test_import/fixtures/sample_pharmgkb.tsv`
- Test: `backend/tests/test_import/test_pharmgkb.py`

**Background — PharmGKB clinical_annotations.tsv format:**
- Tab-separated with header
- Key columns: `Variant/Haplotypes` (rsID or star allele), `Gene`, `Level of Evidence`, `Drug(s)`, `Phenotype(s)`
- Filter to Level 1A and 1B only
- Star alleles resolved via `star_allele_rsids.json`; unresolved ones are skipped with a warning

- [ ] **Step 1: Create the fixture TSV**

Create `backend/tests/test_import/fixtures/sample_pharmgkb.tsv`:

```
Clinical Annotation ID	Variant/Haplotypes	Gene	Level of Evidence	Level Override	Level Modifiers	Score	Phenotype Category	PMID(s)	Evidence Count	Drug(s)	Phenotype(s)	Notes	Specialty Population	Latest History Date (YYYY-MM-DD)	URL
1001	rs4244285	CYP2C19	1A			10.0	Efficacy	20802479	25	clopidogrel	Reduced Function		NA	2023-01-01	https://www.pharmgkb.org/clinicalAnnotation/1001
1002	CYP2D6*4	CYP2D6	1A			9.0	Efficacy	16958828	30	codeine	Poor Metabolizer		NA	2023-01-01	https://www.pharmgkb.org/clinicalAnnotation/1002
1003	rs1799853	CYP2C9	1B			8.0	Dosage	9399854	20	warfarin	Decreased Metabolism		NA	2023-01-01	https://www.pharmgkb.org/clinicalAnnotation/1003
1004	CYP2D6*99	CYP2D6	1A			7.0	Efficacy	99999999	5	codeine	Unknown		NA	2023-01-01	https://www.pharmgkb.org/clinicalAnnotation/1004
1005	rs7412	APOE	2A			5.0	Efficacy	7842013	15	statins	Altered Response		NA	2023-01-01	https://www.pharmgkb.org/clinicalAnnotation/1005
```

Rows and what they test:
1. rs4244285 — direct rsID, Level 1A → included
2. CYP2D6*4 — star allele in lookup → resolved to rs3892097, included
3. rs1799853 — direct rsID, Level 1B → included
4. CYP2D6*99 — star allele NOT in lookup → skipped with warning
5. rs7412 — Level 2A → excluded

- [ ] **Step 2: Write failing tests**

Create `backend/tests/test_import/test_pharmgkb.py`:

```python
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
    # CYP2D6*4 → rs3892097
    assert "rs3892097" in rsids


def test_skips_unknown_star_allele(capsys: object) -> None:
    list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    # CYP2D6*99 is not in lookup — should not raise, and rsid not in results
    results = list(parse_pharmgkb_annotations(FIXTURES / "sample_pharmgkb.tsv", STAR_ALLELES))
    rsids = {v["rsid"] for v, _ in results}
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
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd backend && uv run pytest tests/test_import/test_pharmgkb.py -v
```

Expected: `ImportError` — pharmgkb.py doesn't exist.

- [ ] **Step 4: Create pharmgkb.py**

Create `backend/scripts/sources/pharmgkb.py`:

```python
"""PharmGKB clinical annotations parser: filters to CPIC Level 1A/1B."""

import csv
import json
from datetime import date
from pathlib import Path
from typing import Iterator

from genesnap.db.variants._types import InterpretationDict, VariantDict

from sources.templates import pharmgkb_interpretations

TODAY = date.today().isoformat()

ALLOWED_LEVELS = {"1A", "1B"}


def _load_star_alleles(json_path: Path) -> dict[str, dict[str, str]]:
    with open(json_path) as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def parse_pharmgkb_annotations(
    tsv_path: Path,
    star_allele_path: Path,
) -> Iterator[tuple[VariantDict, list[InterpretationDict]]]:
    """Parse PharmGKB clinical_annotations.tsv, yielding Level 1A/1B variants.

    Star alleles are resolved to rsIDs via star_allele_rsids.json.
    Unresolvable haplotypes are skipped with a printed warning.
    """
    star_alleles = _load_star_alleles(star_allele_path)
    seen_rsids: set[str] = set()

    with open(tsv_path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            level = row.get("Level of Evidence", "").strip()
            if level not in ALLOWED_LEVELS:
                continue

            variant_field = row.get("Variant/Haplotypes", "").strip()
            gene = row.get("Gene", "").strip()
            drug = row.get("Drug(s)", "").strip().lower()
            phenotype = row.get("Phenotype(s)", "").strip()

            # Resolve rsID and alleles
            if variant_field.startswith("rs"):
                rsid = variant_field
                # For direct rsIDs, look up alleles in star_alleles by rsid match
                allele_entry = next(
                    (v for v in star_alleles.values() if v["rsid"] == rsid),
                    None,
                )
                if allele_entry is None:
                    continue  # No allele data available; can't generate interpretations
                ref = allele_entry["ref_allele"]
                alt = allele_entry["risk_allele"]
                star_allele_name = ""
            else:
                # Star allele name
                if variant_field not in star_alleles:
                    print(f"Warning: star allele '{variant_field}' not in lookup, skipping.")
                    continue
                entry = star_alleles[variant_field]
                rsid = entry["rsid"]
                ref = entry["ref_allele"]
                alt = entry["risk_allele"]
                star_allele_name = variant_field

            if rsid in seen_rsids:
                continue
            seen_rsids.add(rsid)

            name = f"{star_allele_name or gene} – {drug}"
            description = (
                f"CPIC Level {level} annotation for {gene} and {drug}. "
                f"Associated phenotype: {phenotype}. Imported from PharmGKB."
            )

            variant: VariantDict = {
                "rsid": rsid,
                "gene": gene,
                "category": "pharmacogenomics",
                "name": name,
                "significance": "drug_response",
                "description": description,
                "risk_allele": alt,
                "normal_allele": ref,
                "chromosome": "",  # PharmGKB doesn't include coordinates
                "position": 0,
                "source": "pharmgkb_import",
                "clinvar_stars": 0,
                "odds_ratio": None,
                "publications": None,
                "external_ids": None,
            }

            interps = pharmgkb_interpretations(
                rsid=rsid, ref=ref, alt=alt, gene=gene,
                drug=drug, phenotype=phenotype,
                level=level, star_allele=star_allele_name,
                is_sex_chrom=False,
            )

            yield variant, interps
```

- [ ] **Step 5: Run tests — expect PASS**

```bash
cd backend && uv run pytest tests/test_import/test_pharmgkb.py -v
```

Expected: `10 passed`

- [ ] **Step 6: Fix: PharmGKB variants with chromosome="" and position=0**

The `variants` table has `chromosome TEXT NOT NULL` and `position INTEGER NOT NULL`. PharmGKB doesn't include coordinates. The ClinVar VCF likely has these variants (same rsIDs as in the pharma gene star alleles), so the INSERT OR IGNORE will skip PharmGKB variants that already exist in the DB from ClinVar. For genuinely new PharmGKB-only variants, set chromosome to `""` and position to `0` — the schema allows this since both are TEXT/INTEGER (no CHECK constraint). Verify the schema allows it:

```bash
cd backend && python3 -c "
import sqlite3
from genesnap.db.connection import SCHEMA_SQL
conn = sqlite3.connect(':memory:')
conn.executescript(SCHEMA_SQL)
conn.execute(\"INSERT INTO variants (rsid,gene,category,name,significance,description,chromosome,position,source,last_updated,clinvar_stars) VALUES ('rsTest','G1','health_risk','N','pathogenic','D','',0,'test','2026-01-01',0)\")
conn.commit()
print('OK')
"
```

Expected output: `OK`

- [ ] **Step 7: Commit**

```bash
git add backend/scripts/sources/pharmgkb.py \
        backend/tests/test_import/fixtures/sample_pharmgkb.tsv \
        backend/tests/test_import/test_pharmgkb.py
git commit -m "feat: add PharmGKB clinical annotations parser with star allele resolution"
```

---

## Task 7: Create import_variants.py CLI entry point

**Files:**
- Create: `backend/scripts/import_variants.py`

- [ ] **Step 1: Create import_variants.py**

Create `backend/scripts/import_variants.py`:

```python
#!/usr/bin/env python3
"""Bulk import variants from ClinVar, GWAS Catalog, and PharmGKB into the genesnap DB.

Usage:
    uv run scripts/import_variants.py --pharmgkb path/to/clinical_annotations.tsv
    uv run scripts/import_variants.py --skip-gwas --skip-pharmgkb
    uv run scripts/import_variants.py --dry-run
    uv run scripts/import_variants.py --clinvar-file path/to/clinvar.vcf.gz
"""

import argparse
import json
import sqlite3
import sys
import tempfile
import urllib.request
from datetime import date
from pathlib import Path

# Add scripts/ directory to path so sources/ sub-package is importable
sys.path.insert(0, str(Path(__file__).parent))

from sources.clinvar import parse_clinvar_vcf
from sources.gwas import parse_gwas_tsv
from sources.pharmgkb import parse_pharmgkb_annotations

CLINVAR_URL = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz"
GWAS_URL = "https://www.ebi.ac.uk/gwas/api/search/downloads/full"
STAR_ALLELES_PATH = Path(__file__).parent / "data" / "star_allele_rsids.json"

TODAY = date.today().isoformat()


def _download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    urllib.request.urlretrieve(url, dest)
    size_mb = dest.stat().st_size / 1_000_000
    print(f"  → {dest.name} ({size_mb:.0f}MB)")


def _insert_batch(
    conn: sqlite3.Connection,
    variants: list,
    interpretations: list,
    dry_run: bool,
) -> tuple[int, int]:
    """Insert a batch of variants and interpretations. Returns (inserted, skipped)."""
    if dry_run:
        return len(variants), 0

    inserted = 0
    skipped = 0
    for v in variants:
        result = conn.execute(
            """INSERT OR IGNORE INTO variants
            (rsid, gene, category, name, significance, description,
             risk_allele, normal_allele, chromosome, position, source,
             external_ids, publications, clinvar_stars, odds_ratio, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                v["rsid"], v["gene"], v["category"], v["name"], v["significance"],
                v["description"], v.get("risk_allele"), v.get("normal_allele"),
                v["chromosome"], v["position"], v["source"],
                json.dumps(v.get("external_ids")) if v.get("external_ids") else None,
                json.dumps(v.get("publications")) if v.get("publications") else None,
                v.get("clinvar_stars", 0), v.get("odds_ratio"), TODAY,
            ),
        )
        if result.rowcount > 0:
            inserted += 1
        else:
            skipped += 1

    for interp in interpretations:
        conn.execute(
            """INSERT OR IGNORE INTO genotype_interpretations
            (rsid, genotype, interpretation, risk_level) VALUES (?, ?, ?, ?)""",
            (interp["rsid"], interp["genotype"], interp["interpretation"], interp["risk_level"]),
        )

    return inserted, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pharmgkb", type=Path, help="Path to PharmGKB clinical_annotations.tsv")
    parser.add_argument("--clinvar-file", type=Path, help="Use existing ClinVar VCF (skip download)")
    parser.add_argument("--gwas-file", type=Path, help="Use existing GWAS TSV (skip download)")
    parser.add_argument("--skip-clinvar", action="store_true")
    parser.add_argument("--skip-gwas", action="store_true")
    parser.add_argument("--skip-pharmgkb", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Parse and count only, no DB writes")
    parser.add_argument("--db", type=Path, help="Override DB path (default: from settings)")
    args = parser.parse_args()

    # Resolve DB path
    if args.db:
        db_path = args.db
    else:
        from genesnap.config import settings
        db_path = settings.db_path

    if not db_path.exists():
        print(f"Error: DB not found at {db_path}. Run seed.py first.")
        sys.exit(1)

    conn = None if args.dry_run else sqlite3.connect(db_path)

    total_inserted = 0
    total_skipped = 0
    rsid_alleles: dict[str, tuple[str, str]] = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # --- ClinVar ---
        if not args.skip_clinvar:
            clinvar_path = args.clinvar_file or tmp / "clinvar.vcf.gz"
            if not args.clinvar_file:
                _download(CLINVAR_URL, clinvar_path)

            print("Parsing ClinVar VCF...")
            clinvar_results, rsid_alleles = parse_clinvar_vcf(clinvar_path)

            variants_batch, interps_batch = [], []
            x_mt_skipped = 0
            for variant, interps in clinvar_results:
                variants_batch.append(variant)
                interps_batch.extend(interps)
                if not interps and variant["chromosome"] in {"X", "Y", "MT"}:
                    x_mt_skipped += 1

            if conn:
                ins, skp = _insert_batch(conn, variants_batch, interps_batch, dry_run=False)
                conn.commit()
            else:
                ins, skp = len(variants_batch), 0

            print(
                f"  ClinVar: {ins} inserted, {skp} skipped (already in DB), "
                f"{x_mt_skipped} sex/MT chrom (no interpretations)"
            )
            total_inserted += ins
            total_skipped += skp

        # --- GWAS Catalog ---
        if not args.skip_gwas:
            gwas_path = args.gwas_file or tmp / "gwas_catalog.tsv"
            if not args.gwas_file:
                _download(GWAS_URL, gwas_path)

            print("Parsing GWAS Catalog TSV...")
            variants_batch, interps_batch = [], []
            for variant, interps in parse_gwas_tsv(gwas_path, rsid_alleles):
                variants_batch.append(variant)
                interps_batch.extend(interps)

            if conn:
                ins, skp = _insert_batch(conn, variants_batch, interps_batch, dry_run=False)
                conn.commit()
            else:
                ins, skp = len(variants_batch), 0

            print(f"  GWAS: {ins} inserted, {skp} skipped (already in DB)")
            total_inserted += ins
            total_skipped += skp

        # --- PharmGKB ---
        if not args.skip_pharmgkb:
            if not args.pharmgkb:
                print(
                    "Skipping PharmGKB (no --pharmgkb path provided). "
                    "Download clinical_annotations.tsv from pharmgkb.org and re-run with "
                    "--pharmgkb path/to/clinical_annotations.tsv"
                )
            else:
                print("Parsing PharmGKB annotations...")
                variants_batch, interps_batch = [], []
                for variant, interps in parse_pharmgkb_annotations(
                    args.pharmgkb, STAR_ALLELES_PATH
                ):
                    variants_batch.append(variant)
                    interps_batch.extend(interps)

                if conn:
                    ins, skp = _insert_batch(conn, variants_batch, interps_batch, dry_run=False)
                    conn.commit()
                else:
                    ins, skp = len(variants_batch), 0

                print(f"  PharmGKB: {ins} inserted, {skp} skipped (already in DB)")
                total_inserted += ins
                total_skipped += skp

    if conn:
        cursor = conn.execute("SELECT COUNT(*) FROM variants")
        total_in_db = cursor.fetchone()[0]
        conn.close()
        print(
            f"\nDone. {total_inserted} new variants inserted, {total_skipped} skipped. "
            f"DB now contains {total_in_db} variants."
        )
    else:
        print(
            f"\nDry run complete. Would insert {total_inserted} variants "
            f"(skipped {total_skipped} already in DB)."
        )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Smoke test the CLI help**

```bash
cd backend && uv run scripts/import_variants.py --help
```

Expected: prints usage with all flags listed (`--pharmgkb`, `--clinvar-file`, `--dry-run`, etc.) and exits 0.

- [ ] **Step 3: Smoke test dry-run with skip flags (no downloads, no DB needed)**

```bash
cd backend && uv run scripts/import_variants.py \
  --skip-gwas --skip-pharmgkb \
  --clinvar-file tests/test_import/fixtures/sample_clinvar.vcf \
  --dry-run
```

Expected output (exact numbers may vary by fixture):
```
Parsing ClinVar VCF...
  ClinVar: 6 inserted, 0 skipped (already in DB), 1 sex/MT chrom (no interpretations)

Dry run complete. Would insert 6 variants (skipped 0 already in DB).
```

- [ ] **Step 4: Run full test suite to make sure nothing is broken**

```bash
cd backend && uv run pytest -v
```

Expected: all tests pass (including the new test_import tests).

- [ ] **Step 5: Run ruff and mypy**

```bash
cd backend && uv run ruff check scripts/ && uv run ruff format --check scripts/
```

Fix any lint issues, then:

```bash
cd backend && uv run mypy scripts/ --ignore-missing-imports
```

Fix any type errors.

- [ ] **Step 6: Commit**

```bash
git add backend/scripts/import_variants.py
git commit -m "feat: add import_variants.py CLI entry point for bulk variant import"
```

---

## Full Test Run Verification

After all tasks are complete:

- [ ] **Run the complete test suite**

```bash
cd backend && uv run pytest -v
```

Expected: all tests pass with no failures.

- [ ] **Verify smoke test with real fixture data end-to-end**

```bash
cd backend && uv run python -c "
import sqlite3, tempfile
from pathlib import Path
from genesnap.db.connection import SCHEMA_SQL
from genesnap.db.seed import seed_database

# Create a fresh DB and seed it
with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
    db_path = Path(f.name)
seed_database(db_path)
before = sqlite3.connect(db_path).execute('SELECT COUNT(*) FROM variants').fetchone()[0]
print(f'Before import: {before} variants')
"
```

Then run the import against fixture files:

```bash
cd backend && uv run scripts/import_variants.py \
  --clinvar-file tests/test_import/fixtures/sample_clinvar.vcf \
  --gwas-file tests/test_import/fixtures/sample_gwas.tsv \
  --pharmgkb tests/test_import/fixtures/sample_pharmgkb.tsv \
  --db /tmp/test_genesnap.db
```

(First run `seed_database` to create the DB, or use `uv run src/genesnap/db/seed.py` to seed `/tmp/test_genesnap.db`.)

Expected: output shows variants from all three sources inserted, curated entries skipped.
