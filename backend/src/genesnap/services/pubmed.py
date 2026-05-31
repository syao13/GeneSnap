"""PubMed API client using NCBI E-utilities."""

import httpx

from genesnap.config import settings

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


class PubMedArticle:
    """A PubMed article summary."""

    def __init__(
        self,
        *,
        pmid: str = "",
        title: str = "",
        authors: list[str] | None = None,
        journal: str = "",
        pub_date: str = "",
        doi: str = "",
    ) -> None:
        self.pmid = pmid
        self.title = title
        self.authors = authors or []
        self.journal = journal
        self.pub_date = pub_date
        self.doi = doi

    def to_dict(self) -> dict[str, object]:
        return {
            "pmid": self.pmid,
            "title": self.title,
            "authors": self.authors,
            "journal": self.journal,
            "pub_date": self.pub_date,
            "doi": self.doi,
        }


async def fetch_pubmed_by_pmids(pmids: list[str]) -> list[PubMedArticle]:
    """Fetch PubMed article summaries by a list of PMIDs."""
    if not pmids:
        return []

    params: dict[str, str] = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
    }
    if settings.ncbi_api_key:
        params["api_key"] = settings.ncbi_api_key

    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.get(ESUMMARY_URL, params=params)
        resp.raise_for_status()
        data = resp.json()

    result_data = data.get("result", {})
    articles: list[PubMedArticle] = []

    for pmid in pmids:
        entry = result_data.get(pmid, {})
        if not entry or "error" in entry:
            continue

        # Parse authors
        authors: list[str] = []
        author_list = entry.get("authors", [])
        if isinstance(author_list, list):
            authors = [a.get("name", "") for a in author_list if a.get("name")]

        # Parse DOI from article IDs
        doi = ""
        for id_entry in entry.get("articleids", []):
            if id_entry.get("idtype") == "doi":
                doi = id_entry.get("value", "")
                break

        articles.append(
            PubMedArticle(
                pmid=pmid,
                title=entry.get("title", ""),
                authors=authors,
                journal=entry.get("fulljournalname", entry.get("source", "")),
                pub_date=entry.get("pubdate", ""),
                doi=doi,
            )
        )

    return articles


async def search_pubmed_for_variant(rsid: str, max_results: int = 5) -> list[PubMedArticle]:
    """Search PubMed for articles mentioning a specific rsID."""
    search_params: dict[str, str] = {
        "db": "pubmed",
        "term": rsid,
        "retmode": "json",
        "retmax": str(max_results),
        "sort": "relevance",
    }
    if settings.ncbi_api_key:
        search_params["api_key"] = settings.ncbi_api_key

    async with httpx.AsyncClient(timeout=15.0) as client:
        search_resp = await client.get(ESEARCH_URL, params=search_params)
        search_resp.raise_for_status()
        search_data = search_resp.json()

    id_list = search_data.get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return []

    return await fetch_pubmed_by_pmids(id_list)
