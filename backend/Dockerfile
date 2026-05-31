FROM python:3.12-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies first (cached layer)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Copy source code
COPY src/ src/

# Install the project itself
RUN uv sync --frozen --no-dev

# ---------------------------------------------------------------------------
# Runtime stage
# ---------------------------------------------------------------------------
FROM python:3.12-slim

WORKDIR /app

# Copy virtual environment and source from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src

# Ensure venv is on PATH
ENV PATH="/app/.venv/bin:$PATH"

# Create data directory
RUN mkdir -p /app/data

# Seed the database at build time
ENV DB_PATH=/app/data/genesnap.db
RUN python -m genesnap.db.seed

EXPOSE 8000

CMD ["uvicorn", "genesnap.main:app", "--host", "0.0.0.0", "--port", "8000"]
