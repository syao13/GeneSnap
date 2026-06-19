"""Upload endpoint for genetic testing raw data."""

import gzip

from fastapi import APIRouter, UploadFile

from genesnap.analysis.analyzer import analyze_snps
from genesnap.db.connection import get_db
from genesnap.models.schemas import AnalysisResult
from genesnap.parsers.twentythreeandme import parse_23andme

router = APIRouter()


@router.post("/upload", response_model=AnalysisResult)
async def upload_file(file: UploadFile) -> AnalysisResult:
    """Upload a 23andMe raw data file and analyze it."""
    content = await file.read()
    try:
        content = gzip.decompress(content)
    except (gzip.BadGzipFile, OSError):
        pass  # not gzip-compressed, use as-is
    text = content.decode("utf-8")

    snps = parse_23andme(text)
    db = await get_db()
    result = await analyze_snps(db, snps)

    return result
