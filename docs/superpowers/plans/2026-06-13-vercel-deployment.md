# Vercel Deployment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deploy GeneSnap to Vercel (frontend as static site, backend as a single Python serverless function) with a custom domain, while keeping `docker compose up` and `npm run dev` working on master.

**Architecture:** A `vercel.json` at the repo root routes `/api/*` to a single Python serverless function (`api/index.py`) that wraps the existing FastAPI app via `mangum`. Everything else is served from the Vite static build. The SQLite DB is seeded into `/tmp` on cold start. Local dev is untouched.

**Tech Stack:** Vercel (Hobby), mangum 0.17+, FastAPI (existing), Vite (existing)

---

## File Map

| Action | Path | Purpose |
|--------|------|---------|
| Create | `vercel.json` | Vercel routing + build config |
| Create | `api/index.py` | ASGI entry point for Vercel |
| Create | `api/requirements.txt` | Python deps for Vercel to install |
| Modify | `frontend/src/api/client.ts` | 9-second timeout on enrichment calls |
| Modify | `.env.example` | Document production env vars |

---

## Task 1: Add `vercel.json`

**Files:**
- Create: `vercel.json`

- [ ] **Step 1: Create `vercel.json` at the repo root**

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

- [ ] **Step 2: Verify it's valid JSON**

```bash
python3 -c "import json; json.load(open('vercel.json')); print('valid')"
```

Expected output: `valid`

- [ ] **Step 3: Commit**

```bash
git add vercel.json
git commit -m "feat: add vercel routing config"
```

---

## Task 2: Add Vercel Python entry point

**Files:**
- Create: `api/index.py`
- Create: `api/requirements.txt`

- [ ] **Step 1: Create `api/index.py`**

```python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend", "src"))

from genesnap.main import app  # noqa: E402
from mangum import Mangum  # noqa: E402

handler = Mangum(app, lifespan="auto")
```

`sys.path.insert` makes `genesnap` importable from `backend/src/`. `lifespan="auto"` lets FastAPI's `init_db()` run on cold start, seeding `/tmp/genesnap.db`.

- [ ] **Step 2: Create `api/requirements.txt`**

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

- [ ] **Step 3: Verify the import resolves locally**

Run from the repo root (uses the backend's uv virtualenv which has all deps installed):

```bash
cd backend && uv run python3 -c "
import os, sys
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
from genesnap.main import app
print('import OK:', app.title)
"
```

Expected output: `import OK: Genesnap`

If you get `ModuleNotFoundError: No module named 'genesnap'`, make sure you're running from the `backend/` directory and that `uv sync` has been run at least once (`cd backend && uv sync`).

- [ ] **Step 4: Commit**

```bash
git add api/index.py api/requirements.txt
git commit -m "feat: add vercel serverless entry point"
```

---

## Task 3: Add enrichment timeout guard

**Files:**
- Modify: `frontend/src/api/client.ts`

The Vercel Hobby plan hard-kills functions at 10 seconds. Without a client-side timeout, a slow enrichment call produces a silent 504. This wraps the enrichment fetch in a 9-second `AbortController` so the user gets a readable error instead.

- [ ] **Step 1: Replace `enrichVariant` in `frontend/src/api/client.ts`**

Current file (`frontend/src/api/client.ts`):

```typescript
import type { AnalysisResult, EnrichmentResult } from '../types'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

export async function uploadFile(file: File): Promise<AnalysisResult> {
  const formData = new FormData()
  formData.append('file', file)

  const response = await fetch(`${BASE_URL}/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    const text = await response.text()
    throw new Error(`Upload failed (${response.status}): ${text}`)
  }

  return response.json()
}

export async function enrichVariant(rsid: string): Promise<EnrichmentResult> {
  const response = await fetch(`${BASE_URL}/enrich/${rsid}`)

  if (!response.ok) {
    const text = await response.text()
    throw new Error(`Enrichment failed (${response.status}): ${text}`)
  }

  return response.json()
}
```

Replace `enrichVariant` with:

```typescript
export async function enrichVariant(rsid: string): Promise<EnrichmentResult> {
  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 9000)

  try {
    const response = await fetch(`${BASE_URL}/enrich/${rsid}`, {
      signal: controller.signal,
    })

    if (!response.ok) {
      const text = await response.text()
      throw new Error(`Enrichment failed (${response.status}): ${text}`)
    }

    return response.json()
  } catch (err) {
    if (err instanceof Error && err.name === 'AbortError') {
      throw new Error('Enrichment is taking too long — please try again')
    }
    throw err
  } finally {
    clearTimeout(timeoutId)
  }
}
```

- [ ] **Step 2: Verify the frontend builds without errors**

```bash
cd frontend && npm run build
```

Expected: build completes with no TypeScript errors.

- [ ] **Step 3: Commit**

```bash
git add frontend/src/api/client.ts
git commit -m "feat: add 9s timeout guard on enrichment fetch"
```

---

## Task 4: Update `.env.example`

**Files:**
- Modify: `.env.example`

- [ ] **Step 1: Replace `.env.example` with the following**

```bash
# NCBI API key (free) - get one at https://www.ncbi.nlm.nih.gov/account/settings/
# Provides higher rate limits for ClinVar and PubMed API calls
NCBI_API_KEY=

# CORS origins - must include your production domain when deploying
# Local Docker:  CORS_ORIGINS=["http://localhost:3000"]
# Local dev:     CORS_ORIGINS=["http://localhost:5173"]
# Production:    CORS_ORIGINS=["https://yourdomain.com"]
CORS_ORIGINS=["http://localhost:5173"]

# Database path
# Local (default): computed relative to config.py — no need to set
# Vercel:          DB_PATH=/tmp/genesnap.db
DB_PATH=
```

- [ ] **Step 2: Commit**

```bash
git add .env.example
git commit -m "docs: update env.example with production vars"
```

---

## Task 5: Deploy to Vercel

These are dashboard steps — no code changes. Do these after pushing all commits to `master`.

- [ ] **Step 1: Push master to GitHub (if not already)**

```bash
git push origin master
```

- [ ] **Step 2: Create Vercel project**

1. Go to [vercel.com](https://vercel.com) → **Add New Project**
2. Import your GitHub repo
3. Vercel will detect `vercel.json` automatically — no framework preset needed
4. Leave **Root Directory** as `/` (the repo root)
5. Click **Deploy** — let the first build run (it will fail on CORS, that's expected)

- [ ] **Step 3: Set environment variables**

In Vercel dashboard → Project → **Settings** → **Environment Variables**, add:

| Name | Value | Environments |
|------|-------|-------------|
| `DB_PATH` | `/tmp/genesnap.db` | Production, Preview |
| `CORS_ORIGINS` | `["https://your-vercel-app.vercel.app"]` | Production, Preview |
| `NCBI_API_KEY` | your key | Production, Preview |

For `CORS_ORIGINS`, use the `.vercel.app` URL Vercel assigned (visible on the project dashboard) until you have a custom domain.

- [ ] **Step 4: Redeploy**

In Vercel dashboard → **Deployments** → click the latest deployment → **Redeploy**.

- [ ] **Step 5: Verify the health endpoint**

```bash
curl https://your-app.vercel.app/api/health
```

Expected response:
```json
{"status": "ok", "variant_count": <number>}
```

If `variant_count` is 0, the DB seed didn't run — check the function logs in Vercel dashboard → Functions tab.

- [ ] **Step 6: Verify the frontend loads**

Open `https://your-app.vercel.app` in a browser. The upload page should load and the file upload flow should work end-to-end.

---

## Task 6: Connect custom domain

- [ ] **Step 1: Buy a domain**

Recommended: [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) (~$10/yr for `.com`, at-cost pricing).

Alternative: Buy directly in Vercel dashboard → Project → **Settings** → **Domains** → **Buy** (slightly pricier, zero DNS config).

- [ ] **Step 2: Add domain to Vercel**

In Vercel dashboard → Project → **Settings** → **Domains** → **Add**.

Enter your domain (e.g. `genesnap.app`). Vercel will show you the DNS records to add.

- [ ] **Step 3: Configure DNS (if bought outside Vercel)**

In your registrar's DNS panel, add the records Vercel shows you — typically an `A` record or `CNAME`. Vercel auto-provisions SSL/TLS via Let's Encrypt once DNS propagates (5–30 minutes).

- [ ] **Step 4: Update `CORS_ORIGINS` env var**

In Vercel dashboard → **Settings** → **Environment Variables**, update `CORS_ORIGINS` to your real domain:

```
["https://yourdomain.com"]
```

- [ ] **Step 5: Redeploy and verify**

Trigger a redeploy (push an empty commit or click Redeploy in dashboard):

```bash
git commit --allow-empty -m "chore: trigger redeploy for domain update"
git push origin master
```

Open `https://yourdomain.com` — the app should load over HTTPS with a valid cert.
