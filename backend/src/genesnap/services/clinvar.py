"""ClinVar API client using NCBI E-utilities."""

import httpx

from genesnap.config import settings

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


class ClinVarResult:
    """Parsed ClinVar data for a variant."""

    def __init__(
        self,
        *,
        variant_id: str = "",
        clinical_significance: str = "",
        review_status: str = "",
        conditions: list[str] | None = None,
        last_evaluated: str = "",
        title: str = "",
    ) -> None:
        self.variant_id = variant_id
        self.clinical_significance = clinical_significance
        self.review_status = review_status
        self.conditions = conditions or []
        self.last_evaluated = last_evaluated
        self.title = title

    def to_dict(self) -> dict[str, object]:
        return {
            "variant_id": self.variant_id,
            "clinical_significance": self.clinical_significance,
            "review_status": self.review_status,
            "conditions": self.conditions,
            "last_evaluated": self.last_evaluated,
            "title": self.title,
        }


async def fetch_clinvar(rsid: str) -> ClinVarResult | None:
    """Fetch ClinVar data for a given rsID.

    Returns None if no ClinVar entry is found.
    """
    params: dict[str, str] = {
        "db": "clinvar",
        "term": f"{rsid}[variant name]",
        "retmode": "json",
        "retmax": "5",
    }
    if settings.ncbi_api_key:
        params["api_key"] = settings.ncbi_api_key

    async with httpx.AsyncClient(timeout=8.0) as client:
        # Step 1: Search for the variant
        search_resp = await client.get(ESEARCH_URL, params=params)
        search_resp.raise_for_status()
        search_data = search_resp.json()

        id_list = search_data.get("esearchresult", {}).get("idlist", [])
        if not id_list:
            return None

        # Step 2: Get summary for the first match
        summary_params: dict[str, str] = {
            "db": "clinvar",
            "id": id_list[0],
            "retmode": "json",
        }
        if settings.ncbi_api_key:
            summary_params["api_key"] = settings.ncbi_api_key

        summary_resp = await client.get(ESUMMARY_URL, params=summary_params)
        summary_resp.raise_for_status()
        summary_data = summary_resp.json()

        result_data = summary_data.get("result", {})
        uid = id_list[0]
        entry = result_data.get(uid, {})

        if not entry:
            return None

        # Parse clinical significance
        clinical_sig = entry.get("clinical_significance", {})
        sig_description = ""
        if isinstance(clinical_sig, dict):
            sig_description = clinical_sig.get("description", "")
        elif isinstance(clinical_sig, str):
            sig_description = clinical_sig

        # Parse conditions/traits
        conditions: list[str] = []
        trait_set = entry.get("trait_set", [])
        if isinstance(trait_set, list):
            for trait in trait_set:
                trait_name = trait.get("trait_name", "")
                if trait_name:
                    conditions.append(trait_name)

        return ClinVarResult(
            variant_id=uid,
            clinical_significance=sig_description,
            review_status=entry.get("review_status", ""),
            conditions=conditions,
            last_evaluated=entry.get("last_evaluated", ""),
            title=entry.get("title", ""),
        )
