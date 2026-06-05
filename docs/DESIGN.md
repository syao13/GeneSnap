# GeneSnap - Design Document

## 1. Project Overview

**GeneSnap** is a web application that parses raw genetic testing data (starting with 23andMe), identifies clinically significant SNP variants, and provides annotated results with links to scientific literature and databases.

### Goals
- Upload and parse 23andMe raw data files (~577K-967K SNPs depending on chip version)
- Identify clinically significant variants across three categories:
  - **Health Risk**: Disease-associated variants (BRCA1/2, APOE, Factor V Leiden, etc.)
  - **Pharmacogenomics**: Drug response variants (CYP2D6, CYP2C19, VKORC1, etc.)
  - **Traits**: Well-established trait associations (lactose intolerance, caffeine metabolism, etc.)
- Display annotated results with clinical significance, risk context, and linked research papers
- Enrich results with live data from ClinVar, Ensembl, PharmGKB, GWAS Catalog, and PubMed

### Non-Goals (for now)
- Multi-user authentication / accounts
- Support for other providers (AncestryDNA, MyHeritage) - will be added later
- Polygenic risk scores (complex multi-SNP calculations)
- Clinical-grade diagnostic reporting (this is an informational tool, not medical advice)

---

## 2. Architecture

```
┌─────────────────────────────────────┐
│           React Frontend            │
│  ┌───────────┐  ┌────────────────┐  │
│  │  Upload   │  │   Results      │  │
│  │  Page     │  │   Dashboard    │  │
│  └───────────┘  └────────────────┘  │
│                  ┌────────────────┐  │
│                  │ Variant Detail │  │
│                  └────────────────┘  │
└──────────────┬──────────────────────┘
               │ REST API (JSON)
┌──────────────▼──────────────────────┐
│         FastAPI Backend             │
│  ┌──────────┐  ┌─────────────────┐  │
│  │  Parser  │  │    Analysis     │  │
│  │  Module  │  │    Engine       │  │
│  └──────────┘  └────────┬────────┘  │
│                          │          │
│  ┌───────────────────────▼───────┐  │
│  │     Enrichment Services       │  │
│  │  ClinVar│Ensembl│PharmGKB│PM  │  │
│  └───────────────────────────────┘  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     SQLite (Curated Variants DB)    │
│  - Known pathogenic variants        │
│  - Pharmacogenomics annotations     │
│  - Trait associations               │
│  - Cached API responses             │
└─────────────────────────────────────┘
```

### Data Flow

1. User uploads 23andMe raw `.txt` file via the React frontend
2. Backend parses the file, extracting rsID/chromosome/position/genotype per SNP
3. Analysis engine cross-references all SNPs against the local curated variant DB
4. Matched variants are categorized (health/pharma/trait) and ranked by significance
5. Results returned to frontend for display
6. User can click individual variants to trigger live API enrichment (papers, latest annotations)

---

## 3. Tech Stack

### Backend
| Component | Choice | Rationale |
|-----------|--------|-----------|
| Language | Python 3.12+ | Requested; strong bioinformatics ecosystem |
| Framework | FastAPI | Async support, auto OpenAPI docs, Pydantic validation, better than Flask for API-first design |
| Package Manager | uv | Fast, modern Python package manager |
| Database | SQLite via aiosqlite | No server needed, portable, sufficient for curated variant DB |
| ORM | None (raw SQL with helper functions) | SQLite is simple enough; avoids ORM overhead |
| HTTP Client | httpx | Async HTTP for API enrichment calls |
| Testing | pytest + pytest-asyncio | TDD approach, async test support |
| Linting/Format | ruff | Fast, replaces flake8 + black + isort in one tool |
| Type Checking | mypy (strict) | Catch bugs early, especially for data processing |

### Frontend
| Component | Choice | Rationale |
|-----------|--------|-----------|
| Framework | React 18 + TypeScript | Requested; strong ecosystem |
| Build Tool | Vite | Fast dev server, simple config |
| Styling | Tailwind CSS | Rapid UI development, no custom CSS files |
| HTTP Client | fetch (native) | Simple enough for our needs |
| Testing | Vitest + React Testing Library | Fast, Vite-native testing |
| Linting | ESLint + Prettier | Standard for React/TS projects |

---

## 4. Backend Design

### 4.1 Project Structure

```
backend/
├── pyproject.toml              # uv project config, dependencies, ruff/mypy config
├── uv.lock
├── src/
│   └── genesnap/
│       ├── __init__.py
│       ├── main.py             # FastAPI app entry point, CORS, lifespan
│       ├── config.py           # Settings (API keys, DB path, etc.)
│       ├── api/
│       │   ├── __init__.py
│       │   ├── upload.py       # POST /api/upload - file upload + analysis
│       │   ├── variants.py     # GET /api/variants/{rsid} - variant detail
│       │   └── enrichment.py   # GET /api/enrich/{rsid} - live API enrichment
│       ├── parsers/
│       │   ├── __init__.py
│       │   ├── base.py         # Abstract base parser (for future providers)
│       │   └── twentythreeandme.py  # 23andMe raw data parser
│       ├── analysis/
│       │   ├── __init__.py
│       │   └── analyzer.py     # Core analysis: match SNPs to curated DB
│       ├── services/
│       │   ├── __init__.py
│       │   ├── clinvar.py      # ClinVar E-utilities client
│       │   ├── ensembl.py      # Ensembl VEP REST client
│       │   ├── pharmgkb.py     # PharmGKB API client
│       │   ├── gwas.py         # GWAS Catalog API client
│       │   └── pubmed.py       # PubMed E-utilities client
│       ├── db/
│       │   ├── __init__.py
│       │   ├── connection.py   # SQLite connection management
│       │   ├── queries.py      # SQL query functions
│       │   └── seed.py         # Seed script to populate curated variants
│       └── models/
│           ├── __init__.py
│           └── schemas.py      # Pydantic models for API request/response
├── data/
│   ├── curated_variants.sql    # SQL to create + populate variant tables
│   └── genesnap.db             # SQLite database (generated, gitignored)
└── tests/
    ├── __init__.py
    ├── conftest.py             # Shared fixtures (test DB, sample data, async client)
    ├── fixtures/
    │   └── sample_23andme.txt  # Sample 23andMe raw data for testing
    ├── test_parsers.py         # Parser unit tests
    ├── test_analyzer.py        # Analysis engine tests
    ├── test_api.py             # API endpoint integration tests
    └── test_services.py        # External service client tests (mocked)
```

### 4.2 23andMe Parser

**Input format** (tab-delimited, comments start with `#`):
```
# This data file generated by 23andMe at: ...
# rsid  chromosome  position  genotype
rs548049170	1	69869	TT
rs13328684	1	74792	--
rs9283150	1	565508	AG
```

**Parser output** - list of `SNP` objects:
```python
@dataclass
class SNP:
    rsid: str           # e.g., "rs548049170"
    chromosome: str     # e.g., "1", "X", "MT"
    position: int       # e.g., 69869
    genotype: str       # e.g., "TT", "AG", "--"
```

**Key considerations**:
- Skip comment lines (`#`) and the header line
- Handle `--` (no-call) genotypes - skip these in analysis
- Filter out internal IDs (`i` prefix) - only process `rs` prefixed IDs
- Stream-parse the file (don't load all 600K+ lines into memory at once)
- Validate chromosome values (1-22, X, Y, MT)
- All coordinates are GRCh37/hg19

### 4.3 Curated Variant Database (SQLite)

**Schema**:

```sql
CREATE TABLE variants (
    rsid TEXT PRIMARY KEY,           -- e.g., "rs6025"
    gene TEXT NOT NULL,              -- e.g., "F5"
    category TEXT NOT NULL,          -- "health_risk" | "pharmacogenomics" | "trait"
    name TEXT NOT NULL,              -- Human-readable name, e.g., "Factor V Leiden"
    significance TEXT NOT NULL,      -- "pathogenic" | "likely_pathogenic" | "risk_factor" | "drug_response" | "association"
    description TEXT NOT NULL,       -- What this variant indicates
    risk_allele TEXT,                -- The risk/effect allele, e.g., "A"
    normal_allele TEXT,              -- The reference/normal allele, e.g., "G"
    chromosome TEXT NOT NULL,
    position INTEGER NOT NULL,
    source TEXT NOT NULL,            -- "clinvar" | "pharmgkb" | "gwas_catalog" | "manual"
    external_ids TEXT,               -- JSON: {"clinvar": "12345", "omim": "600160"}
    publications TEXT,               -- JSON array of PMIDs: ["12345678", "23456789"]
    last_updated TEXT NOT NULL       -- ISO 8601 date
);

CREATE TABLE genotype_interpretations (
    rsid TEXT NOT NULL,
    genotype TEXT NOT NULL,          -- e.g., "AA", "AG", "GG"
    interpretation TEXT NOT NULL,    -- What this specific genotype means
    risk_level TEXT NOT NULL,        -- "normal" | "carrier" | "increased_risk" | "high_risk"
    FOREIGN KEY (rsid) REFERENCES variants(rsid),
    PRIMARY KEY (rsid, genotype)
);

CREATE TABLE api_cache (
    cache_key TEXT PRIMARY KEY,      -- e.g., "clinvar:rs6025"
    response_json TEXT NOT NULL,
    fetched_at TEXT NOT NULL,        -- ISO 8601 timestamp
    expires_at TEXT NOT NULL         -- Cache expiry
);
```

**Initial seed data** (~200-500 variants covering):
- ACMG Secondary Findings gene list variants (84 genes)
- Top PharmGKB clinical annotations (CPIC Level A drug-gene pairs)
- Well-established GWAS associations (genome-wide significant, replicated)
- See Section 6 for the priority variant list

### 4.4 Analysis Engine

```python
class AnalysisResult:
    summary: AnalysisSummary       # Total SNPs, matched count, breakdown by category
    health_risks: list[VariantMatch]
    pharmacogenomics: list[VariantMatch]
    traits: list[VariantMatch]

class VariantMatch:
    snp: SNP                        # From uploaded file
    variant: CuratedVariant         # From database
    interpretation: str             # Genotype-specific interpretation
    risk_level: str                 # normal / carrier / increased_risk / high_risk
    publications: list[str]         # PMIDs for key papers
```

**Analysis flow**:
1. Parse uploaded file into list of `SNP` objects
2. Extract all rsIDs into a set
3. Query curated DB: `SELECT * FROM variants WHERE rsid IN (?...)`
4. For each match, look up the genotype interpretation
5. Sort by significance/risk level (high risk first)
6. Return categorized results

**Performance target**: < 3 seconds for a full 23andMe file (~600K SNPs)

### 4.5 Enrichment Services

These are called **on-demand** when a user clicks a specific variant for more detail. Not called during initial analysis (too slow for 100+ variants).

| Service | Purpose | Rate Limit | Caching |
|---------|---------|------------|---------|
| ClinVar | Clinical significance, review status | 10/sec (with API key) | 7 days |
| Ensembl VEP | Variant consequences, population freq | 15/sec | 7 days |
| PharmGKB | Drug interactions, dosing guidelines | 2/sec | 7 days |
| GWAS Catalog | Trait associations, effect sizes | ~10/sec | 7 days |
| PubMed | Related papers, abstracts | 10/sec (with API key) | 30 days |

All responses cached in `api_cache` table to avoid redundant calls.

### 4.6 API Endpoints

```
POST /api/upload
  - Accepts: multipart/form-data (file upload)
  - Returns: AnalysisResult JSON
  - Parses file, runs analysis, returns categorized results

GET /api/variants/{rsid}
  - Returns: CuratedVariant with genotype interpretations
  - From local DB only (fast)

GET /api/enrich/{rsid}
  - Returns: EnrichmentResult (ClinVar + Ensembl + PubMed data)
  - Calls external APIs (or returns cached), merges results
  - May be slow on first call (~2-5 sec)

GET /api/health
  - Returns: {"status": "ok", "variant_count": 350}
  - Health check endpoint
```

---

## 5. Frontend Design

### 5.1 Project Structure

```
frontend/
├── package.json
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── index.html
├── public/
├── src/
│   ├── main.tsx                 # Entry point
│   ├── App.tsx                  # Router setup
│   ├── api/
│   │   └── client.ts            # API client functions
│   ├── components/
│   │   ├── FileUpload.tsx        # Drag-and-drop file upload
│   │   ├── AnalysisSummary.tsx   # Overview cards (counts, categories)
│   │   ├── VariantTable.tsx      # Sortable/filterable variant list
│   │   ├── VariantDetail.tsx     # Expanded view with enrichment data
│   │   ├── RiskBadge.tsx         # Color-coded risk level indicator
│   │   └── Layout.tsx            # Page layout wrapper
│   ├── pages/
│   │   ├── HomePage.tsx          # Upload page
│   │   └── ResultsPage.tsx       # Analysis results
│   ├── types/
│   │   └── index.ts              # TypeScript types matching API schemas
│   └── utils/
│       └── format.ts             # Formatting helpers
└── tests/
    ├── FileUpload.test.tsx
    └── VariantTable.test.tsx
```

### 5.2 Pages

**Home / Upload Page**:
- Clean landing with brief explanation
- Drag-and-drop zone for .txt file upload
- File validation (check for 23andMe format header)
- Upload progress indicator
- Disclaimer: "This tool is for informational purposes only. Not medical advice."

**Results Page**:
- **Summary cards**: Total SNPs analyzed, variants found, breakdown by category
- **Three tabs**: Health Risks | Pharmacogenomics | Traits
- **Variant table** (per tab):
  - Columns: Gene, Variant Name, Your Genotype, Risk Level, Significance
  - Color-coded risk badges (green=normal, yellow=carrier, orange=increased, red=high)
  - Sortable by risk level
  - Click row to expand detail panel
- **Variant detail panel** (expanded):
  - Full description and interpretation
  - "Load latest research" button (triggers enrichment API)
  - Linked papers from PubMed (title, authors, journal, year, link)
  - External links: ClinVar page, OMIM, PharmGKB

### 5.3 UI Wireframe (text-based)

```
┌────────────────────────────────────────────────────────┐
│  Genesnap                                              │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ 12 Found │  │  4 High  │  │  3 Pharma│             │
│  │ Variants │  │  Risk    │  │  Relevant│             │
│  └──────────┘  └──────────┘  └──────────┘             │
│                                                        │
│  [Health Risks]  [Pharmacogenomics]  [Traits]          │
│  ─────────────────────────────────────────             │
│  Gene    Variant           Genotype  Risk              │
│  ────    ───────           ────────  ────              │
│  APOE    Alzheimer Risk    e3/e4     ⚠ Increased      │
│  F5      Factor V Leiden   AG        ⚠ Carrier        │
│  BRCA1   Breast Cancer     AA        ✓ Normal         │
│  MTHFR   C677T             CT        ⚠ Carrier        │
│                                                        │
│  ▼ APOE - Alzheimer Risk (expanded)                   │
│  ┌──────────────────────────────────────────┐         │
│  │ Your genotype: e3/e4                      │         │
│  │ One copy of the e4 allele is associated   │         │
│  │ with increased risk of late-onset         │         │
│  │ Alzheimer's disease.                      │         │
│  │                                           │         │
│  │ [Load Latest Research]                    │         │
│  │                                           │         │
│  │ Key Papers:                               │         │
│  │ • Corder et al. (1993) Science            │         │
│  │ • Farrer et al. (1997) JAMA               │         │
│  │                                           │         │
│  │ Links: ClinVar | OMIM | SNPedia           │         │
│  └──────────────────────────────────────────┘         │
└────────────────────────────────────────────────────────┘
```

---

## 6. Priority Variant List (Initial Seed Data)

### Health Risk Variants
| rsID | Gene | Condition | Significance |
|------|------|-----------|-------------|
| rs429358 + rs7412 | APOE | Alzheimer's disease risk | risk_factor |
| rs6025 | F5 | Factor V Leiden (thrombophilia) | pathogenic |
| rs1799963 | F2 | Prothrombin G20210A (thrombophilia) | pathogenic |
| rs1801133 | MTHFR | C677T (folate metabolism) | risk_factor |
| rs1801131 | MTHFR | A1298C (folate metabolism) | risk_factor |
| rs9939609 | FTO | Obesity risk | association |
| rs7903146 | TCF7L2 | Type 2 diabetes risk | risk_factor |
| rs1800562 | HFE | Hereditary hemochromatosis (C282Y) | pathogenic |
| rs1799945 | HFE | Hereditary hemochromatosis (H63D) | risk_factor |
| rs334 | HBB | Sickle cell trait | pathogenic |
| rs80357906 | BRCA1 | Breast/ovarian cancer (185delAG) | pathogenic |
| rs80357713 | BRCA2 | Breast/ovarian cancer (6174delT) | pathogenic |
| rs28897696 | MUTYH | Colorectal cancer risk | pathogenic |

### Pharmacogenomics Variants
| rsID | Gene | Drug Response | Significance |
|------|------|--------------|-------------|
| rs1799853 | CYP2C9 | Warfarin metabolism (*2) | drug_response |
| rs1057910 | CYP2C9 | Warfarin metabolism (*3) | drug_response |
| rs9923231 | VKORC1 | Warfarin sensitivity | drug_response |
| rs4244285 | CYP2C19 | Clopidogrel metabolism (*2) | drug_response |
| rs4986893 | CYP2C19 | Clopidogrel metabolism (*3) | drug_response |
| rs12248560 | CYP2C19 | Clopidogrel metabolism (*17) | drug_response |
| rs4149056 | SLCO1B1 | Statin myopathy risk | drug_response |
| rs1142345 | TPMT | Thiopurine toxicity (*3C) | drug_response |
| rs1800460 | TPMT | Thiopurine toxicity (*3B) | drug_response |
| rs3918290 | DPYD | 5-FU toxicity | drug_response |
| rs8175347 | UGT1A1 | Irinotecan toxicity (*28) | drug_response |
| rs762551 | CYP1A2 | Caffeine metabolism | drug_response |
| rs1801280 | NAT2 | Isoniazid metabolism (*5) | drug_response |

### Trait Variants
| rsID | Gene | Trait | Significance |
|------|------|-------|-------------|
| rs4988235 | MCM6/LCT | Lactose tolerance/intolerance | association |
| rs1815739 | ACTN3 | Muscle fiber type (sprint/endurance) | association |
| rs671 | ALDH2 | Alcohol flush reaction | association |
| rs601338 | FUT2 | Secretor status (norovirus resistance) | association |
| rs1800497 | DRD2/ANKK1 | Dopamine receptor density | association |
| rs53576 | OXTR | Oxytocin receptor (empathy) | association |
| rs1695 | GSTP1 | Detoxification capacity | association |
| rs1042713 | ADRB2 | Beta-2 adrenergic receptor | association |
| rs4680 | COMT | Catechol-O-methyltransferase (stress response) | association |
| rs1800955 | DRD4 | Novelty seeking | association |

---

## 7. Development Practices

### Tooling
- **uv** for Python dependency management and virtual environments
- **ruff** for linting and formatting (configured in `pyproject.toml`)
- **mypy** for static type checking (strict mode)
- **pytest** with TDD approach - write tests first, then implement
- **pre-commit** hooks for ruff + mypy on every commit

### TDD Workflow
For each feature:
1. Write failing test(s) describing expected behavior
2. Implement minimum code to pass
3. Refactor while keeping tests green
4. Repeat

### Git Strategy
- Feature branches off `main`
- Conventional commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`
- Small, focused commits

### Configuration
- Environment variables via `.env` file (not committed)
- `config.py` with pydantic-settings for validation
- Required: `NCBI_API_KEY` (free, for higher rate limits on ClinVar/PubMed)
- Optional: other API keys as needed

---

## 8. Implementation Phases

### Phase 1: Foundation (Core Backend)
- [ ] Project scaffolding (uv, ruff, mypy, pytest config)
- [ ] 23andMe parser with tests
- [ ] SQLite database setup + seed script with initial ~40 variants
- [ ] Analysis engine with tests
- [ ] `POST /api/upload` endpoint with tests

### Phase 2: Frontend MVP
- [ ] React + Vite + TypeScript + Tailwind setup
- [ ] File upload component
- [ ] Results page with summary cards and variant table
- [ ] Variant detail panel (local data only)
- [ ] Connect frontend to backend API

### Phase 3: Live Enrichment
- [ ] ClinVar service client
- [ ] PubMed service client
- [ ] Ensembl VEP service client
- [ ] PharmGKB service client
- [ ] GWAS Catalog service client
- [ ] API cache layer
- [ ] Enrichment API endpoint
- [ ] Frontend "Load Latest Research" integration

### Phase 4: Polish & Expand
- [ ] Expand curated variant DB (200+ variants)
- [ ] Improve UI/UX (loading states, error handling, responsive design)
- [ ] Add medical disclaimer and genetic counseling recommendations
- [ ] Docker setup for portability
- [ ] Add AncestryDNA parser (future provider)

---

## 9. Key Decisions & Trade-offs

| Decision | Choice | Alternative | Why |
|----------|--------|-------------|-----|
| FastAPI over Flask | FastAPI | Flask | Auto docs, async, Pydantic validation, better DX |
| SQLite over PostgreSQL | SQLite | PostgreSQL | No server needed, portable, sufficient for curated data |
| No ORM | Raw SQL | SQLAlchemy | Simpler for a small schema; avoids abstraction overhead |
| On-demand enrichment | Lazy load | Batch on upload | Enriching 50+ variants on upload would be too slow (rate limits) |
| Curated DB + live APIs | Hybrid | API-only or DB-only | Fast initial results + fresh data when user drills down |
| Vite over CRA | Vite | Create React App | CRA is deprecated; Vite is faster and simpler |
| Tailwind over CSS modules | Tailwind | CSS Modules, MUI | Rapid prototyping, consistent design, no component library lock-in |

---

## 10. Limitations & Disclaimers

The application must clearly communicate:
1. **Not a diagnostic tool** - Results are informational only, not medical advice
2. **Genotyping ≠ sequencing** - Consumer SNP arrays test ~0.02% of the genome and miss many variants
3. **Rare variant accuracy** - For variants with frequency <0.1%, SNP chip accuracy drops significantly
4. **Confirmation needed** - Clinically significant findings should be confirmed with clinical-grade testing
5. **Genetic counseling recommended** - Especially for pathogenic/likely pathogenic results
