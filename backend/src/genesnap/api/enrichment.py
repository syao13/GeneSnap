"""Enrichment endpoint for live API data on a specific variant."""

import json
import logging

from fastapi import APIRouter

from genesnap.db.connection import get_db
from genesnap.services.cache import get_cached, set_cached
from genesnap.services.clinvar import fetch_clinvar
from genesnap.services.gwas import fetch_gwas_associations
from genesnap.services.pubmed import fetch_pubmed_by_pmids, search_pubmed_for_variant

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/enrich/{rsid}")
async def enrich_variant(rsid: str) -> dict:
    """Fetch live enrichment data for a variant from ClinVar, PubMed, and GWAS Catalog.

    Results are cached for 7 days to avoid redundant API calls.
    """
    db = await get_db()
    cache_key = f"enrich:{rsid}"

    cached = await get_cached(db, cache_key)
    if cached is not None:
        return cached

    result: dict[str, object] = {
        "rsid": rsid,
        "clinvar": None,
        "known_publications": [],
        "search_publications": [],
        "gwas_associations": [],
    }

    # Fetch ClinVar data
    try:
        clinvar_data = await fetch_clinvar(rsid)
        if clinvar_data:
            result["clinvar"] = clinvar_data.to_dict()
    except Exception:
        logger.exception("ClinVar fetch failed for %s", rsid)

    # Fetch known publications (from curated DB PMIDs)
    cursor = await db.execute("SELECT publications FROM variants WHERE rsid = ?", (rsid,))
    row = await cursor.fetchone()
    known_pmids: list[str] = []
    if row and row["publications"]:
        known_pmids = json.loads(row["publications"])

    if known_pmids:
        try:
            articles = await fetch_pubmed_by_pmids(known_pmids)
            result["known_publications"] = [a.to_dict() for a in articles]
        except Exception:
            logger.exception("PubMed fetch failed for known PMIDs of %s", rsid)

    # Search PubMed for additional papers
    try:
        search_articles = await search_pubmed_for_variant(rsid, max_results=5)
        # Filter out articles already in known_publications
        known_set = set(known_pmids)
        result["search_publications"] = [
            a.to_dict() for a in search_articles if a.pmid not in known_set
        ]
    except Exception:
        logger.exception("PubMed search failed for %s", rsid)

    # Fetch GWAS Catalog associations
    try:
        gwas_data = await fetch_gwas_associations(rsid, max_results=5)
        result["gwas_associations"] = [a.to_dict() for a in gwas_data]
    except Exception:
        logger.exception("GWAS Catalog fetch failed for %s", rsid)

    # Cache the result
    await set_cached(db, cache_key, result)

    return result
