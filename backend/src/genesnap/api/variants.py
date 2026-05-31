"""Variant detail and health check endpoints."""

from fastapi import APIRouter

from genesnap.db.connection import get_db
from genesnap.db.queries import get_variant_count
from genesnap.models.schemas import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    db = await get_db()
    count = await get_variant_count(db)
    return HealthResponse(status="ok", variant_count=count)
