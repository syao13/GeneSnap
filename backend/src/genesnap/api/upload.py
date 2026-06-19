"""Upload endpoint for genetic testing raw data."""

import gzip

from fastapi import APIRouter, UploadFile

from genesnap.analysis.analyzer import analyze_snps
from genesnap.db.connection import get_db
from genesnap.models.schemas import AnalysisResult, SNP
from genesnap.parsers.twentythreeandme import parse_23andme

router = APIRouter()


def _parse_compact(text: str) -> list[SNP]:
    """Parse the compact rsid\tgenotype format sent by the frontend."""
    snps = []
    for line in text.splitlines():
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            rsid, genotype = parts[0], parts[1]
            if rsid.startswith('rs') and genotype not in ('--', ''):
                snps.append(SNP(rsid=rsid, chromosome='', position=0, genotype=genotype))
    return snps


@router.post("/upload", response_model=AnalysisResult)
async def upload_file(file: UploadFile) -> AnalysisResult:
    """Upload a 23andMe raw data file and analyze it."""
    content = await file.read()
    try:
        content = gzip.decompress(content)
    except (gzip.BadGzipFile, OSError):
        pass  # not gzip-compressed, use as-is
    text = content.decode("utf-8")

    first_data = next((l for l in text.splitlines() if l and not l.startswith('#')), '')
    if first_data.count('\t') == 1:
        snps = _parse_compact(text)
    else:
        snps = parse_23andme(text)

    db = await get_db()
    return await analyze_snps(db, snps)
