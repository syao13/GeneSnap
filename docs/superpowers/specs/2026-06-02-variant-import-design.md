# Variant Import Pipeline — Design Spec

**Date:** 2026-06-02
**Status:** Approved

## Problem

The curated variant database contains ~803 hand-written variants across 9 Python files. Coverage is intentionally selective but leaves large gaps: the 23andMe chip has ~600k SNPs, ClinVar has ~40k pathogenic/LP variants with strong review status, and the GWAS Catalog has ~60k genome-wide significant associations. Users with clinically relevant variants outside the curated set see no results.

## Goal

Expand coverage to ~100k variants without manual curation, without copying entire databases, while keeping the app stateless and fast at query time.

## Non-Goals

- Automated/scheduled refresh (manual for now)
- Replacing the existing curated Python files
- Changing the app runtime (no new services, no schema changes)
- AI-generated interpretations
- AncestryDNA or other chip formats

---

## Architecture

A standalone ETL script (`backend/scripts/import_variants.py`) runs outside the app on demand. It downloads bulk data from three sources, filters to clinically significant variants, generates template-based interpretations, and bulk-inserts into the existing SQLite DB using `INSERT OR IGNORE` so curated data is never overwritten.

```
backend/scripts/
├── import_variants.py          # CLI entry point
├── sources/
│   ├── __init__.py
│   ├── clinvar.py              # parse_clinvar_vcf()
│   ├── gwas.py                 # parse_gwas_tsv()
│   └── pharmgkb.py             # parse_pharmgkb_annotations()
└── data/
    └── star_allele_rsids.json  # haplotype→rsID+alleles lookup for star alleles
```

The app (`analyzer.py`, `queries.py`, schema) requires zero changes. It reads more rows from SQLite and that's it.

---

## Data Sources

### ClinVar
- **File:** `clinvar.vcf.gz` from NCBI FTP (GRCh37 build, ~50MB compressed)
- **URL:** `https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz`
- **Auto-downloaded** by the script

### GWAS Catalog
- **File:** Full associations TSV from EBI (~200MB)
- **URL:** `https://www.ebi.ac.uk/gwas/api/search/downloads/full`
- **Auto-downloaded** by the script

### PharmGKB
- **File:** `clinical_annotations.tsv` from PharmGKB downloads page
- **Requires free account registration** at pharmgkb.org
- **Passed manually** via `--pharmgkb` flag

`star_allele_rsids.json` stores rsID plus both alleles so genotype interpretations can be generated without an additional lookup:

```json
{
  "CYP2C19*2": {"rsid": "rs4244285", "risk_allele": "A", "ref_allele": "G"},
  "CYP2D6*4":  {"rsid": "rs3892097", "risk_allele": "A", "ref_allele": "G"}
}
```

---

## Filtering Criteria

### ClinVar

Include if ALL of:
- `CLNSIG` contains `Pathogenic`, `Likely_pathogenic`, or `drug_response`
- `CLNREVSTAT` is one of: `criteria_provided_multiple_submitters` (★★), `reviewed_by_expert_panel` (★★★), `practice_guideline` (★★★★)
- `ID` field starts with `rs` (has a parseable rsID)

Exclude:
- `Conflicting_interpretations_of_pathogenicity`
- Variants without an rsID (structural variants, insertions/deletions with no rs number)

Expected yield: ~15,000–40,000 variants.

### GWAS Catalog

Include if ALL of:
- `P-VALUE` < 5×10⁻⁸ (genome-wide significant)
- `SNPS` field contains a single rsID
- `STRONGEST SNP-RISK ALLELE` is parseable (format: `rs1234-A`)
- `INITIAL SAMPLE SIZE` ≥ 1,000

Deduplicate: keep only the most significant p-value row per rsID per trait. For multiple traits per rsID, keep the strongest association for the `variants` row; store others in `external_ids`.

Expected yield: ~30,000–60,000 unique rsIDs.

### PharmGKB

Include if ALL of:
- `Level of Evidence` is `1A` or `1B` (CPIC guideline-level)
- `Variant/Haplotypes` is either a direct rsID or a star allele name present in `star_allele_rsids.json`

Exclude:
- Level 2A/2B/3/4 (lower evidence; high-value variants from these levels are already in the curated pharma files)
- Haplotype names not in the bundled lookup (logged as warnings, not errors)

Expected yield: ~300–500 variants (most already exist in curated files and will be skipped by `INSERT OR IGNORE`).

---

## Categorization

| Source | Logic | Category |
|---|---|---|
| ClinVar | `CLNSIG` contains `drug_response` | `pharmacogenomics` |
| ClinVar | All other (pathogenic/LP) | `health_risk` |
| GWAS | Gene in pharma allowlist (CYP*, UGT*, VKORC1, DPYD, TPMT, SLCO1B1, etc.) | `pharmacogenomics` |
| GWAS | Trait text matches disease/cancer/syndrome keywords | `health_risk` |
| GWAS | Everything else | `trait` |
| PharmGKB | Always | `pharmacogenomics` |

The pharma gene allowlist covers: `CYP2D6`, `CYP2C19`, `CYP2C9`, `CYP3A4`, `CYP3A5`, `CYP1A2`, `CYP2B6`, `UGT1A1`, `UGT2B7`, `VKORC1`, `DPYD`, `TPMT`, `NUDT15`, `SLCO1B1`, `IFNL3`, `HLA-B`, `HLA-A`, `G6PD`, `CACNA1S`, `RYR1`.

Health risk keywords: `cancer`, `disease`, `syndrome`, `disorder`, `carcinoma`, `leukemia`, `diabetes`, `hypertension`, `infarction`, `stroke`, `thrombosis`, `anemia`, `fibrosis`.

---

## Template Interpretation Generation

Auto-imported variants get template-based per-genotype interpretations, not hand-written prose. Quality is intentionally lower than curated entries but factually correct.

### ClinVar — Pathogenic / Likely Pathogenic

```
{REF}{REF} → risk_level=normal
  "You do not carry this {GENE} variant associated with {CONDITION}."

{REF}{ALT} → risk_level=increased_risk
  "You carry one copy of this {SIGNIFICANCE} {GENE} variant associated with
   {CONDITION} (ClinVar {STARS}). Consider discussing with a healthcare provider."

{ALT}{ALT} → risk_level=high_risk
  "You carry two copies of this {SIGNIFICANCE} {GENE} variant associated with
   {CONDITION} (ClinVar {STARS}). Clinical confirmation is recommended."
```

`Pathogenic` uses "strongly recommended"; `Likely_pathogenic` uses "recommended".

### ClinVar — Drug Response

```
{REF}{REF} → risk_level=normal
  "Standard {GENE} function expected for {DRUG} metabolism."

{REF}{ALT} → risk_level=increased_risk
  "You carry one copy of a {GENE} drug response variant affecting {DRUG}.
   Consult your prescriber if taking this medication."

{ALT}{ALT} → risk_level=high_risk
  "You carry two copies of a {GENE} drug response variant affecting {DRUG}.
   Prescriber consultation is strongly recommended."
```

### GWAS Catalog

```
{REF}{REF} → risk_level=normal
  "You do not carry the {TRAIT} risk allele in {GENE}."

{REF}{ALT} → risk_level=increased_risk
  "You carry one copy of the {GENE} risk allele associated with {TRAIT}
   (OR: ~{OR_HET}x above baseline, p={PVAL}, population-level association)."

{ALT}{ALT} → risk_level=increased_risk  ← never high_risk for GWAS
  "You carry two copies of the {GENE} risk allele associated with {TRAIT}
   (OR: {OR}x above baseline, p={PVAL}, population-level association)."
```

OR for het genotype is approximated as `1 + (OR - 1) / 2` when OR > 1. For protective alleles (OR < 1), risk and reference alleles are swapped so the "risk allele" always has OR ≥ 1.

### PharmGKB

```
{REF}{REF} → risk_level=normal
  "You do not carry {STAR_ALLELE}. Normal {GENE} function expected for {DRUG}."

{REF}{ALT} → risk_level=increased_risk
  "You carry one copy of {STAR_ALLELE}, associated with {PHENOTYPE} for {DRUG}.
   Consult prescriber if taking {DRUG}. (CPIC Level {LEVEL})"

{ALT}{ALT} → risk_level=high_risk
  "You carry two copies of {STAR_ALLELE} ({PHENOTYPE}). CPIC Level {LEVEL}
   guideline recommends review of {DRUG} therapy."
```

### X-chromosome / Mitochondrial edge case

For variants on chromosomes X or MT, insert the `variants` row but skip `genotype_interpretations` entirely. The analyzer already has a fallback at `analyzer.py:77` for variants with no matching interpretation:

```python
interpretation = f"Genotype {snp.genotype} — no specific interpretation available for this variant."
risk_level = RiskLevel.NORMAL
```

This is cleaner than inserting a `--` sentinel row (which would only match actual no-call genotypes) and requires no special handling in the import script.

---

## Significance Field Mapping

Auto-imported variants map to the existing `Significance` enum:

| Source value | `significance` field |
|---|---|
| ClinVar `Pathogenic` | `pathogenic` |
| ClinVar `Likely_pathogenic` | `likely_pathogenic` |
| ClinVar `drug_response` | `drug_response` |
| GWAS association | `association` |
| PharmGKB 1A/1B | `drug_response` |

---

## Source Field Values

Auto-imported variants use distinct `source` values so tiers are queryable:

| Tier | `source` value |
|---|---|
| Hand-curated Python files | `clinvar`, `pharmgkb`, `gwas_catalog` (existing) |
| ClinVar bulk import | `clinvar_import` |
| GWAS Catalog bulk import | `gwas_import` |
| PharmGKB bulk import | `pharmgkb_import` |

---

## seed.py Change

`seed.py` currently uses `INSERT OR REPLACE` unconditionally. Change to `INSERT OR IGNORE` by default with an opt-in `--force` flag:

```python
def seed_database(db_path: Path, force: bool = False) -> None:
    ...

def _insert_variants(conn, force: bool = False) -> None:
    op = "INSERT OR REPLACE" if force else "INSERT OR IGNORE"
    conn.execute(f"{op} INTO variants ...")
```

This ensures re-running `seed.py` after an import doesn't wipe imported data. `--force` is available when intentionally refreshing curated entries.

---

## CLI Interface

```bash
# Full import (ClinVar + GWAS auto-downloaded, PharmGKB path provided)
uv run scripts/import_variants.py --pharmgkb path/to/clinical_annotations.tsv

# Skip a source
uv run scripts/import_variants.py --skip-gwas --skip-pharmgkb

# Dry run — prints counts, no DB writes
uv run scripts/import_variants.py --dry-run

# Use existing downloaded files (skip re-download)
uv run scripts/import_variants.py --clinvar-file path/to/clinvar.vcf.gz
```

Sample output:
```
Downloading ClinVar VCF (GRCh37)... 47MB
Parsing ClinVar: 38,412 passed filters, 21 skipped (X/MT)
Downloading GWAS Catalog TSV... 198MB
Parsing GWAS: 54,209 passed filters, 3,118 deduplicated
Parsing PharmGKB: 287 passed filters, 14 haplotypes not in lookup (skipped)
Inserting into /path/to/genesnap.db...
  38,412 ClinVar | 54,209 GWAS | 287 PharmGKB
  803 skipped (already curated) | 0 errors
Done. DB now contains 92,105 variants (was 803).
```

---

## Testing

Unit tests use small fixture files — no network calls, no real DB writes (in-memory SQLite).

```
tests/test_import/
├── fixtures/
│   ├── sample_clinvar.vcf          # ~20 lines covering all filter cases
│   ├── sample_gwas.tsv             # ~20 rows covering all category types
│   └── sample_pharmgkb.tsv         # Mix of rsIDs and star allele entries
├── test_clinvar.py
├── test_gwas.py
└── test_pharmgkb.py
```

Key cases per source:

**ClinVar:**
- Variant passing all filters → correct `VariantDict` + 3 `InterpretationDict` rows
- 1-star variant → excluded
- `Conflicting_interpretations` → excluded
- X-chromosome variant → `VariantDict` produced, no `InterpretationDict` rows

**GWAS:**
- Passes filters → correct category via keyword heuristic
- Gene in pharma allowlist → `pharmacogenomics` regardless of trait text
- Multi-SNP haplotype row → excluded
- Duplicate rsID+trait → deduplication keeps lowest p-value
- Sample size < 1000 → excluded
- Protective allele (OR < 1) → risk and ref alleles swapped so risk_allele always has OR ≥ 1

**PharmGKB:**
- rsID entry at Level 1A → accepted
- Star allele in lookup → resolved to rsID, accepted
- Star allele not in lookup → skipped with warning, no crash
- Level 2A entry → excluded

**Integration (seed.py change):**
- Curated variant in DB, import runs → `source` field unchanged after `INSERT OR IGNORE`
- `--force` flag → curated entry overwritten by import (intentional)

---

## Expected Coverage After Import

| Source | New variants | Category mix |
|---|---|---|
| ClinVar import | ~38,000 | health_risk + pharmacogenomics |
| GWAS import | ~54,000 | health_risk + trait + small pharma |
| PharmGKB import | ~250 (net new) | pharmacogenomics |
| Existing curated | 803 (unchanged) | all three |
| **Total** | **~93,000** | |

---

## What Does Not Change

- `analyzer.py` — unchanged
- `queries.py` — unchanged (already fetches all variants and filters in Python)
- `db/connection.py` and `SCHEMA_SQL` — no new columns
- `models/schemas.py` — unchanged
- Curated Python files in `db/variants/` — unchanged, take precedence
- Docker / deployment — unchanged (DB file path stays the same)
