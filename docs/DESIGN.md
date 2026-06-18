# GeneSnap - Design Document

## 1. Project Overview

**GeneSnap** is a web application that parses raw genetic testing data (starting with 23andMe), identifies clinically significant SNP variants, and provides annotated results with links to scientific literature and databases.

**Live at:** [www.genesnap.net](https://www.genesnap.net)

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
Browser
  │
  ├── GET /*           → Vercel CDN → frontend/dist/ (Vite static build)
  └── POST/GET /api/*  → Vercel Serverless Function (Python 3.12)
                              │
                        FastAPI + mangum (ASGI adapter)
                              │
                        /tmp/genesnap.db  ←  copied from bundled api/genesnap.db on cold start
                              │
                        External APIs (ClinVar, PubMed, GWAS, Ensembl)
```

**Local dev — two modes:**
```
# Docker (full stack)
docker compose up
  ├── frontend (nginx :3000) — proxies /api/* to backend:8000
  └── backend  (uvicorn :8000) — reads backend/data/genesnap.db

# Dev server (faster iteration)
cd backend && uv run uvicorn genesnap.main:app --reload   # :8000
cd frontend && npm run dev                                # :5173
  └── Vite proxy: /api/* → localhost:8000
```

### Data Flow

1. User uploads 23andMe raw `.txt` file (or tries the sample file from the landing page)
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
| Language | Python 3.12+ | Strong bioinformatics ecosystem |
| Framework | FastAPI | Async support, auto OpenAPI docs, Pydantic validation |
| ASGI Adapter | mangum | Makes FastAPI work in Vercel serverless / AWS Lambda |
| Package Manager | uv | Fast, modern Python package manager |
| Database | SQLite via aiosqlite | No server needed, portable, sufficient for curated variant DB |
| ORM | None (raw SQL) | SQLite is simple enough; avoids ORM overhead |
| HTTP Client | httpx (timeout=8s) | Async HTTP for API enrichment calls; 8s keeps under Vercel's 10s limit |
| Testing | pytest + pytest-asyncio | Async test support |
| Linting/Format | ruff | Fast, replaces flake8 + black + isort |
| Type Checking | mypy (strict) | Catch bugs early |

### Frontend
| Component | Choice | Rationale |
|-----------|--------|-----------|
| Framework | React 19 + TypeScript | Strong ecosystem |
| Build Tool | Vite | Fast dev server, simple config |
| Styling | Tailwind CSS v4 | Rapid UI development |
| HTTP Client | fetch (native) | Simple enough; enrichment calls have 9s AbortController timeout |
| Linting | ESLint | Standard for React/TS projects |

### Infrastructure
| Component | Choice |
|-----------|--------|
| Hosting | Vercel (Hobby plan) |
| Domain | www.genesnap.net |
| Python runtime | 3.12 (pinned via `.python-version`) |
| Function timeout | 10s (Hobby plan limit) |
| DB in production | Seeded at build time → bundled as `api/genesnap.db` → copied to `/tmp` on cold start |

---

## 4. Backend Design

### 4.1 Project Structure

```
backend/
├── pyproject.toml              # uv project config, dependencies, ruff/mypy config
├── uv.lock
├── src/
│   └── genesnap/
│       ├── main.py             # FastAPI app entry point, CORS, lifespan
│       ├── config.py           # Settings (API keys, DB path via env var)
│       ├── api/
│       │   ├── upload.py       # POST /api/upload - file upload + analysis
│       │   ├── variants.py     # GET /api/variants/{rsid} - variant detail
│       │   └── enrichment.py   # GET /api/enrich/{rsid} - live API enrichment
│       ├── parsers/
│       │   ├── base.py         # Abstract base parser (for future providers)
│       │   └── twentythreeandme.py  # 23andMe raw data parser
│       ├── analysis/
│       │   └── analyzer.py     # Core analysis: match SNPs to curated DB
│       ├── services/
│       │   ├── clinvar.py      # ClinVar E-utilities client
│       │   ├── ensembl.py      # Ensembl VEP REST client
│       │   ├── pharmgkb.py     # PharmGKB API client
│       │   ├── gwas.py         # GWAS Catalog API client
│       │   ├── pubmed.py       # PubMed E-utilities client
│       │   └── cache.py        # API response cache (ephemeral in production)
│       ├── db/
│       │   ├── connection.py   # SQLite connection management, schema, migrations
│       │   ├── queries.py      # SQL query functions
│       │   ├── seed.py         # Seed script to populate curated variants
│       │   └── variants/       # Curated variant data (Python modules)
│       └── models/
│           └── schemas.py      # Pydantic models for API request/response
├── data/
│   └── genesnap.db             # SQLite database (generated, gitignored)
└── tests/
    ├── conftest.py             # Shared fixtures (test DB, sample data, async client)
    ├── fixtures/
    │   └── sample_23andme.txt  # Sample 23andMe raw data for testing + demo
    ├── test_parsers.py
    ├── test_analyzer.py
    ├── test_api.py
    └── test_services.py
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

**Key considerations**:
- Skip comment lines (`#`) and the header line
- Handle `--` (no-call) genotypes — skip in analysis
- Filter out internal IDs (`i` prefix) — only process `rs` prefixed IDs
- Stream-parse the file (don't load all 600K+ lines into memory)
- All coordinates are GRCh37/hg19

### 4.3 Curated Variant Database (SQLite)

**Schema**:

```sql
CREATE TABLE variants (
    rsid TEXT PRIMARY KEY,
    gene TEXT NOT NULL,
    category TEXT NOT NULL,          -- "health_risk" | "pharmacogenomics" | "trait"
    name TEXT NOT NULL,
    significance TEXT NOT NULL,      -- "pathogenic" | "likely_pathogenic" | "risk_factor" | "drug_response" | "association"
    description TEXT NOT NULL,
    risk_allele TEXT,
    normal_allele TEXT,
    chromosome TEXT NOT NULL,
    position INTEGER NOT NULL,
    source TEXT NOT NULL,
    external_ids TEXT,               -- JSON
    publications TEXT,               -- JSON array of PMIDs
    clinvar_stars INTEGER NOT NULL DEFAULT 0,
    odds_ratio REAL,
    last_updated TEXT NOT NULL
);

CREATE TABLE genotype_interpretations (
    rsid TEXT NOT NULL,
    genotype TEXT NOT NULL,
    interpretation TEXT NOT NULL,
    risk_level TEXT NOT NULL,        -- "normal" | "carrier" | "increased_risk" | "high_risk"
    FOREIGN KEY (rsid) REFERENCES variants(rsid),
    PRIMARY KEY (rsid, genotype)
);

CREATE TABLE api_cache (
    cache_key TEXT PRIMARY KEY,
    response_json TEXT NOT NULL,
    fetched_at TEXT NOT NULL,
    expires_at TEXT NOT NULL
);
```

> **Note (production):** The `api_cache` table is stored in `/tmp` on Vercel and is per-function-instance. Cache entries do not persist across cold starts or instances.

### 4.4 Analysis Engine

**Analysis flow**:
1. Parse uploaded file into list of `SNP` objects
2. Extract all rsIDs into a set
3. Query curated DB: `SELECT * FROM variants WHERE rsid IN (?...)`
4. For each match, look up the genotype interpretation
5. Sort by significance/risk level (high risk first)
6. Return categorized results

**Performance target**: < 3 seconds for a full 23andMe file (~600K SNPs)

### 4.5 Enrichment Services

Called **on-demand** when a user clicks a variant for detail. All clients use `timeout=8.0s` (below Vercel's 10s function limit).

| Service | Purpose | Rate Limit |
|---------|---------|------------|
| ClinVar | Clinical significance, review status | 10/sec (with API key) |
| Ensembl VEP | Variant consequences, population freq | 15/sec |
| PharmGKB | Drug interactions, dosing guidelines | 2/sec |
| GWAS Catalog | Trait associations, effect sizes | ~10/sec |
| PubMed | Related papers, abstracts | 10/sec (with API key) |

### 4.6 API Endpoints

```
POST /api/upload
  - Accepts: multipart/form-data (file upload)
  - Returns: AnalysisResult JSON

GET /api/variants/{rsid}
  - Returns: CuratedVariant with genotype interpretations (local DB only)

GET /api/enrich/{rsid}
  - Returns: EnrichmentResult (ClinVar + Ensembl + PubMed)
  - First call may be slow (~2-5s); subsequent calls use instance cache

GET /api/health
  - Returns: {"status": "ok", "variant_count": N}
```

---

## 5. Frontend Design

### 5.1 Project Structure

```
frontend/
├── package.json
├── vite.config.ts              # Dev proxy: /api/* → localhost:8000
├── public/
│   └── sample_23andme.txt     # Sample file served for demo/download
├── src/
│   ├── api/
│   │   └── client.ts          # API client; enrichment has 9s AbortController timeout
│   ├── components/
│   │   ├── FileUpload.tsx      # Drag-and-drop file upload
│   │   ├── AnalysisSummary.tsx # Overview cards
│   │   ├── VariantTable.tsx    # Sortable/filterable variant list
│   │   ├── VariantDetail.tsx   # Expanded view with enrichment data
│   │   ├── RiskBadge.tsx       # Color-coded risk level indicator
│   │   ├── DisclaimerBanner.tsx
│   │   ├── ErrorBoundary.tsx
│   │   ├── GeneticCounselingCard.tsx
│   │   ├── Layout.tsx
│   │   └── Pagination.tsx
│   ├── pages/
│   │   ├── HomePage.tsx        # Upload page + sample file links
│   │   └── ResultsPage.tsx     # Analysis results
│   └── types/
│       └── index.ts            # TypeScript types matching API schemas
```

### 5.2 Pages

**Home / Upload Page**:
- Drag-and-drop zone for .txt file upload
- **"Try sample file →"** button — fetches `sample_23andme.txt`, auto-uploads, shows results immediately
- **"Download sample"** link — lets users inspect the expected file format
- Medical disclaimer banner

**Results Page**:
- **Summary cards**: Total SNPs analyzed, variants found, breakdown by category
- **Three tabs**: Health Risks | Pharmacogenomics | Traits
- **Variant table** per tab: Gene, Variant Name, Genotype, Risk Level, Significance
- **Variant detail panel** (on row click): full description, "Load latest research" button, linked papers, external links

---

## 6. Deployment

### Vercel Configuration (`vercel.json`)

```json
{
  "buildCommand": "PYTHONPATH=./backend/src DB_PATH=./api/genesnap.db uv run --no-project --with aiosqlite --with pydantic-settings python -m genesnap.db.seed && cd frontend && npm ci && npm run build",
  "outputDirectory": "frontend/dist",
  "functions": {
    "api/index.py": { "maxDuration": 10 }
  },
  "rewrites": [
    { "source": "/api/:path*", "destination": "/api/index.py" },
    { "source": "/:path*",     "destination": "/index.html" }
  ]
}
```

### Serverless Entry Point (`api/index.py`)

1. Copies bundled `api/genesnap.db` → `/tmp/genesnap.db` on cold start (fast file copy)
2. Sets `DB_PATH=/tmp/genesnap.db` via `os.environ.setdefault` (writable location)
3. Wraps FastAPI app with `mangum` (ASGI → serverless handler)

### Environment Variables (set in Vercel dashboard)

| Variable | Value |
|----------|-------|
| `DB_PATH` | `/tmp/genesnap.db` |
| `CORS_ORIGINS` | `["https://www.genesnap.net"]` |
| `NCBI_API_KEY` | your key |

### Local Development

| Mode | Command |
|------|---------|
| Full Docker stack | `docker compose up` |
| Backend only | `cd backend && uv run uvicorn genesnap.main:app --reload` |
| Frontend only | `cd frontend && npm run dev` (proxies `/api` to `:8000`) |
| Run tests | `cd backend && uv run pytest` |
| Seed local DB | `cd backend && uv run python -m genesnap.db.seed` |

---

## 7. Key Decisions & Trade-offs

| Decision | Choice | Alternative | Why |
|----------|--------|-------------|-----|
| FastAPI over Flask | FastAPI | Flask | Auto docs, async, Pydantic validation |
| SQLite over PostgreSQL | SQLite | PostgreSQL | No server needed, portable, ~180KB seeded DB |
| No ORM | Raw SQL | SQLAlchemy | Simpler for a small schema |
| On-demand enrichment | Lazy load | Batch on upload | Rate limits; enriching 50+ variants on upload too slow |
| Curated DB + live APIs | Hybrid | API-only or DB-only | Fast initial results + fresh data on drill-down |
| Vercel Hobby | Serverless | VPS/Railway | Free tier; sufficient for demo/personal use |
| mangum adapter | mangum | AWS adapter | Standard ASGI→serverless bridge, works on Vercel |
| DB seeded at build time | Build step | Runtime init | Avoids cold-start seeding latency; bundled DB is ~180KB |
| httpx timeout=8s | 8s | 15s (original) | Keeps enrichment calls under Vercel's 10s function limit |
| 9s client AbortController | 9s | none | Surfaces friendly error before Vercel's hard 10s kill |

---

## 8. Limitations & Disclaimers

The application must clearly communicate:
1. **Not a diagnostic tool** — results are informational only, not medical advice
2. **Genotyping ≠ sequencing** — consumer SNP arrays test ~0.02% of the genome
3. **Rare variant accuracy** — for variants with frequency <0.1%, SNP chip accuracy drops
4. **Confirmation needed** — clinically significant findings should be confirmed with clinical-grade testing
5. **Genetic counseling recommended** — especially for pathogenic/likely pathogenic results
6. **Enrichment cache is ephemeral** — on Vercel, API response cache is per-function-instance and does not persist across cold starts
