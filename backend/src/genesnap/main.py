"""FastAPI application entry point."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from genesnap.api.enrichment import router as enrichment_router
from genesnap.api.upload import router as upload_router
from genesnap.api.variants import router as variants_router
from genesnap.config import settings
from genesnap.db.connection import close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Initialize and clean up application resources."""
    await init_db()
    yield
    await close_db()


app = FastAPI(
    title="Genesnap",
    description="Analyze genetic testing raw data to identify clinically significant SNP variants",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api")
app.include_router(variants_router, prefix="/api")
app.include_router(enrichment_router, prefix="/api")


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """Redirect root to interactive API docs."""
    return RedirectResponse(url="/docs")
