"""GWAS Catalog API client for fetching odds ratios and association data."""

import logging

import httpx

logger = logging.getLogger(__name__)

GWAS_API_BASE = "https://www.ebi.ac.uk/gwas/rest/api"


class GWASAssociation:
    """A single GWAS association for a variant."""

    def __init__(
        self,
        *,
        risk_allele: str = "",
        odds_ratio: float | None = None,
        beta: float | None = None,
        p_value: float | None = None,
        trait: str = "",
        study_accession: str = "",
    ) -> None:
        self.risk_allele = risk_allele
        self.odds_ratio = odds_ratio
        self.beta = beta
        self.p_value = p_value
        self.trait = trait
        self.study_accession = study_accession

    def to_dict(self) -> dict[str, object]:
        return {
            "risk_allele": self.risk_allele,
            "odds_ratio": self.odds_ratio,
            "beta": self.beta,
            "p_value": self.p_value,
            "trait": self.trait,
            "study_accession": self.study_accession,
        }


async def fetch_gwas_associations(rsid: str, max_results: int = 5) -> list[GWASAssociation]:
    """Fetch GWAS associations for a given rsID from the EBI GWAS Catalog.

    Returns a list of associations sorted by p-value (most significant first).
    Returns an empty list if no associations are found.
    """
    url = f"{GWAS_API_BASE}/singleNucleotidePolymorphisms/{rsid}/associations"

    async with httpx.AsyncClient(timeout=8.0) as client:
        resp = await client.get(url, headers={"Accept": "application/json"})
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        data = resp.json()

    raw_associations = data.get("_embedded", {}).get("associations", [])
    if not raw_associations:
        return []

    results: list[GWASAssociation] = []
    for assoc in raw_associations:
        # Parse odds ratio
        or_value = assoc.get("orPerCopyNum")
        odds_ratio = float(or_value) if or_value is not None else None

        # Parse beta
        beta_value = assoc.get("betaNum")
        beta = float(beta_value) if beta_value is not None else None

        # Parse p-value from mantissa + exponent
        p_mantissa = assoc.get("pvalueMantissa")
        p_exponent = assoc.get("pvalueExponent")
        p_value: float | None = None
        if p_mantissa is not None and p_exponent is not None:
            p_value = float(p_mantissa) * (10 ** int(p_exponent))

        # Parse risk allele from strongestRiskAlleles
        risk_allele = ""
        risk_alleles = assoc.get("strongestRiskAlleles", [])
        if risk_alleles:
            allele_name = risk_alleles[0].get("riskAlleleName", "")
            # Format is typically "rs12345-A", extract the allele letter
            if "-" in allele_name:
                risk_allele = allele_name.split("-", 1)[1]

        # Parse trait from efoTraits
        trait = ""
        efo_traits = assoc.get("efoTraits", [])
        if efo_traits:
            trait = efo_traits[0].get("trait", "")

        # Parse study accession
        study_accession = assoc.get("studyAccession", "") or ""

        results.append(
            GWASAssociation(
                risk_allele=risk_allele,
                odds_ratio=odds_ratio,
                beta=beta,
                p_value=p_value,
                trait=trait,
                study_accession=study_accession,
            )
        )

    # Sort by p-value (most significant first), None values last
    results.sort(key=lambda a: a.p_value if a.p_value is not None else 1.0)
    return results[:max_results]
