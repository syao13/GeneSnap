# Vercel Deployment Design

**Date:** 2026-06-13  
**Status:** Approved

## Overview

Deploy GeneSnap (React + FastAPI + SQLite) entirely on Vercel, keeping the `master` branch runnable locally via Docker Compose without any changes to existing code.

## Constraints

- Vercel Hobby plan (10-second function timeout)
- All infrastructure on Vercel — no separate backend host
- `docker compose up` must continue to work after all changes
- Enrichment (ClinVar, PubMed, etc.) works on-the-fly; no persistent cache needed in production

## Architecture

```
Browser
  │
  ├── GET /*           → Vercel CDN → frontend/dist/ (Vite static build)
  └── POST/GET /api/*  → Vercel Serverless Function → api/index.py
                                                          │
                                                    FastAPI app
                                                    (mangum ASGI adapter)
                                                          │
                                                    /tmp/genesnap.db
                                                    (seeded on cold start)
```

Local dev — two modes, both unchanged:
```
# Docker (full stack)
docker compose up
  ├── frontend (nginx :3000) — proxies /api/* to backend:8000
  └── backend  (uvicorn :8000) — reads /app/data/genesnap.db

# Dev server (faster iteration)
cd backend && uv run uvicorn genesnap.main:app --reload   # :8000
cd frontend && npm run dev                                # :5173
  └── Vite proxy: /api/* → localhost:8000 (vite.config.ts)
  └── CORS: config.py default includes http://localhost:5173 ✓
```

## File Changes

### New files

**`vercel.json`** — routing and build config:
```json
{
  "buildCommand": "cd frontend && npm ci && npm run build",
  "outputDirectory": "frontend/dist",
  "rewrites": [
    { "source": "/api/:path*", "destination": "/api/index.py" },
    { "source": "/:path*",     "destination": "/index.html" }
  ]
}
```

**`api/index.py`** — thin ASGI entry point:
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend', 'src'))

from genesnap.main import app
from mangum import Mangum

handler = Mangum(app, lifespan="auto")
```

`lifespan="auto"` ensures `init_db()` runs on cold start, seeding `/tmp/genesnap.db`. Warm invocations reuse the existing file. Cold start overhead: ~1–2 seconds extra on first request to a new function instance.

**`api/requirements.txt`** — Python deps for Vercel to install:
```
fastapi>=0.115.0
uvicorn[standard]>=0.34.0
aiosqlite>=0.21.0
httpx>=0.28.0
python-multipart>=0.0.20
pydantic>=2.10.0
pydantic-settings>=2.7.0
mangum>=0.17.0
```

### Modified files

**`frontend/src/api/client.ts`** — add a 9-second `AbortController` timeout on enrichment calls. Surfaces a clean error to the user if Vercel's 10s hard limit is about to be hit.

**`.env.example`** — document the production env vars (see Environment Variables below).

### Unchanged

- `docker-compose.yml`
- `backend/src/` (all FastAPI source)
- `backend/src/genesnap/config.py` (pydantic-settings already reads from env vars)
- All frontend components except the enrichment timeout addition

## Environment Variables

Set these in the Vercel dashboard under Project → Settings → Environment Variables:

| Variable | Vercel value | Local (docker-compose) | Purpose |
|---|---|---|---|
| `DB_PATH` | `/tmp/genesnap.db` | `/app/data/genesnap.db` | Only `/tmp` is writable in serverless |
| `CORS_ORIGINS` | `["https://yourdomain.com"]` | `["http://localhost:3000"]` | Allow production domain |
| `NCBI_API_KEY` | your key | optional | Higher rate limits on ClinVar/PubMed |

`DB_PATH=/tmp/genesnap.db` is the critical one — the default in `config.py` points to `backend/data/genesnap.db`, which is read-only in the Vercel bundle.

## Enrichment Timeout Behaviour

On Hobby plan, Vercel hard-kills functions at 10 seconds. External API calls (ClinVar, PubMed, Ensembl) can take 2–5 seconds each. The guard:

- Frontend wraps enrichment fetch in `AbortController` with 9-second timeout
- On abort, displays "Enrichment is taking too long — try again"
- Prevents silent 504 errors from reaching the user

No server-side caching is needed for the initial deployment. At higher traffic, Vercel KV or Upstash Redis can be added as a cache layer without touching the existing backend structure.

## Domain Setup (Operational Steps)

1. **Buy domain** — Cloudflare Registrar (at-cost, ~$10/yr for .com) is recommended for best pricing and DNS management. Alternatively, buy directly in the Vercel dashboard for zero DNS config.
2. **Connect to Vercel** — Project Settings → Domains → add domain. Vercel auto-provisions SSL/TLS via Let's Encrypt.
3. **Update `CORS_ORIGINS`** — once domain is confirmed, set it in Vercel env vars.
4. DNS propagation takes 5–30 minutes.

## Deployment Steps (Summary)

1. Add `vercel.json`, `api/index.py`, `api/requirements.txt`
2. Add enrichment timeout guard in frontend
3. Update `.env.example`
4. Push to `master`
5. Connect repo to Vercel (vercel.com → Add New Project → import from GitHub, set production branch to `master`)
6. Set env vars in Vercel dashboard
7. Trigger first deploy (or let Vercel auto-deploy on push)
8. Buy and connect domain
9. Update `CORS_ORIGINS` to production domain, redeploy

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Enrichment timeout on Hobby | Medium | 9s client-side abort guard |
| Cold start latency (DB seeding) | Low | ~1–2s extra on cold start; acceptable |
| Vercel Python bundle size | Low | Source + deps well under 250MB limit |
| SQLite write failure (wrong path) | Low | `DB_PATH=/tmp/genesnap.db` env var |
