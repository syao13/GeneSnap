# Genesnap

A web application that parses raw 23andMe genetic data, identifies clinically significant SNP variants, and provides annotated results linked to scientific literature and databases.

> **Disclaimer:** This tool is for informational purposes only and is not medical advice. Clinically significant findings should be confirmed with clinical-grade testing and reviewed with a genetic counselor.

## Tech Stack

- **Backend:** Python 3.12+, FastAPI, SQLite (aiosqlite), uv
- **Frontend:** React 19, TypeScript, Vite, Tailwind CSS

---

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- [Node.js](https://nodejs.org/) 18+
- [Docker](https://www.docker.com/) (optional, for containerized setup)

---

## Running Locally (Development)

### 1. Backend

```bash
cd backend

# Install dependencies
uv sync

# Copy and configure environment variables
cp ../.env.example .env
# Edit .env and set NCBI_API_KEY (optional but recommended for higher API rate limits)

# Start the dev server
uv run uvicorn genesnap.main:app --reload --port 8000
```

The API will be available at http://localhost:8000.
Interactive API docs (Swagger UI) are at http://localhost:8000/docs.

### 2. Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The frontend will be available at http://localhost:5173.

---

## Running with Docker

```bash
# Copy and configure environment variables
cp .env.example .env
# Edit .env and set NCBI_API_KEY if desired

# Build and start both services
docker compose up --build
```

The app will be available at http://localhost:3000.

---

## Environment Variables

Copy `.env.example` to `.env` in the project root:

| Variable | Required | Description |
|----------|----------|-------------|
| `NCBI_API_KEY` | Optional | Free NCBI API key for higher rate limits on ClinVar/PubMed. Get one at https://www.ncbi.nlm.nih.gov/account/settings/ |

---

## Development

### Backend

```bash
cd backend

# Run tests
uv run pytest

# Lint and format
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy src/
```

### Frontend

```bash
cd frontend

# Lint
npm run lint

# Build for production
npm run build
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/upload` | Upload a 23andMe `.txt` file and get analysis results |
| `GET` | `/api/variants/{rsid}` | Get curated variant details for an rsID |
| `GET` | `/api/enrich/{rsid}` | Fetch live enrichment data from ClinVar, PubMed, Ensembl |
| `GET` | `/api/health` | Health check |
