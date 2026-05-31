"""Tests for external API service clients (mocked)."""

from unittest.mock import AsyncMock, patch

import httpx

from genesnap.services.clinvar import ClinVarResult, fetch_clinvar
from genesnap.services.gwas import GWASAssociation, fetch_gwas_associations
from genesnap.services.pubmed import (
    PubMedArticle,
    fetch_pubmed_by_pmids,
    search_pubmed_for_variant,
)


def _mock_response(json_data: dict, status_code: int = 200) -> httpx.Response:
    """Create a mock httpx.Response with a request attached."""
    request = httpx.Request("GET", "https://test.example.com")
    resp = httpx.Response(status_code=status_code, json=json_data, request=request)
    return resp


class TestClinVar:
    """Tests for ClinVar API client."""

    async def test_fetch_clinvar_found(self) -> None:
        """Should return ClinVarResult when variant is found."""
        search_json = {"esearchresult": {"idlist": ["12345"]}}
        summary_json = {
            "result": {
                "12345": {
                    "clinical_significance": {"description": "Pathogenic"},
                    "review_status": "criteria provided, multiple submitters",
                    "trait_set": [{"trait_name": "Hereditary thrombophilia"}],
                    "last_evaluated": "2024-01-15",
                    "title": "NM_000130.5(F5):c.1601G>A (p.Arg534Gln)",
                }
            }
        }

        with patch("genesnap.services.clinvar.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(
                side_effect=[
                    _mock_response(search_json),
                    _mock_response(summary_json),
                ]
            )

            result = await fetch_clinvar("rs6025")

        assert result is not None
        assert result.variant_id == "12345"
        assert result.clinical_significance == "Pathogenic"
        assert "Hereditary thrombophilia" in result.conditions
        assert result.review_status == "criteria provided, multiple submitters"

    async def test_fetch_clinvar_not_found(self) -> None:
        """Should return None when variant is not in ClinVar."""
        search_json = {"esearchresult": {"idlist": []}}

        with patch("genesnap.services.clinvar.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=_mock_response(search_json))

            result = await fetch_clinvar("rs999999999")

        assert result is None

    def test_clinvar_result_to_dict(self) -> None:
        """ClinVarResult.to_dict should include all fields."""
        result = ClinVarResult(
            variant_id="123",
            clinical_significance="Pathogenic",
            conditions=["Disease A"],
        )
        d = result.to_dict()
        assert d["variant_id"] == "123"
        assert d["clinical_significance"] == "Pathogenic"
        assert d["conditions"] == ["Disease A"]


class TestPubMed:
    """Tests for PubMed API client."""

    async def test_fetch_pubmed_by_pmids(self) -> None:
        """Should return articles for given PMIDs."""
        summary_json = {
            "result": {
                "uids": ["7989264"],
                "7989264": {
                    "title": "Factor V Leiden mutation and the risk of DVT.",
                    "authors": [{"name": "Bertina RM"}, {"name": "Koeleman BP"}],
                    "fulljournalname": "Nature",
                    "pubdate": "1994 May 5",
                    "articleids": [{"idtype": "doi", "value": "10.1038/369064a0"}],
                },
            }
        }

        with patch("genesnap.services.pubmed.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=_mock_response(summary_json))

            articles = await fetch_pubmed_by_pmids(["7989264"])

        assert len(articles) == 1
        assert articles[0].pmid == "7989264"
        assert "Factor V" in articles[0].title
        assert articles[0].authors[0] == "Bertina RM"
        assert articles[0].journal == "Nature"
        assert articles[0].doi == "10.1038/369064a0"

    async def test_fetch_pubmed_empty_list(self) -> None:
        """Should return empty list for empty input."""
        articles = await fetch_pubmed_by_pmids([])
        assert articles == []

    async def test_search_pubmed_for_variant(self) -> None:
        """Should search PubMed and return article summaries."""
        search_json = {"esearchresult": {"idlist": ["7989264"]}}
        summary_json = {
            "result": {
                "uids": ["7989264"],
                "7989264": {
                    "title": "Factor V Leiden paper",
                    "authors": [{"name": "Bertina RM"}],
                    "fulljournalname": "Nature",
                    "pubdate": "1994",
                    "articleids": [],
                },
            }
        }

        with patch("genesnap.services.pubmed.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(
                side_effect=[
                    _mock_response(search_json),
                    _mock_response(summary_json),
                ]
            )

            articles = await search_pubmed_for_variant("rs6025")

        assert len(articles) == 1
        assert articles[0].title == "Factor V Leiden paper"

    def test_pubmed_article_to_dict(self) -> None:
        """PubMedArticle.to_dict should include all fields."""
        article = PubMedArticle(
            pmid="123", title="Test", authors=["A"], journal="J", pub_date="2024"
        )
        d = article.to_dict()
        assert d["pmid"] == "123"
        assert d["title"] == "Test"
        assert d["authors"] == ["A"]


class TestGWAS:
    """Tests for GWAS Catalog API client."""

    async def test_fetch_gwas_found(self) -> None:
        """Should return associations when variant has GWAS data."""
        gwas_json = {
            "_embedded": {
                "associations": [
                    {
                        "orPerCopyNum": 1.31,
                        "betaNum": None,
                        "pvalueMantissa": 1.5,
                        "pvalueExponent": -12,
                        "strongestRiskAlleles": [{"riskAlleleName": "rs9939609-A"}],
                        "efoTraits": [{"trait": "body mass index"}],
                        "studyAccession": "GCST000001",
                    }
                ]
            }
        }

        with patch("genesnap.services.gwas.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=_mock_response(gwas_json))

            results = await fetch_gwas_associations("rs9939609")

        assert len(results) == 1
        assert results[0].odds_ratio == 1.31
        assert results[0].risk_allele == "A"
        assert results[0].trait == "body mass index"
        assert results[0].p_value is not None
        assert results[0].p_value < 1e-10

    async def test_fetch_gwas_not_found(self) -> None:
        """Should return empty list for 404 response."""
        with patch("genesnap.services.gwas.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=_mock_response({}, status_code=404))

            results = await fetch_gwas_associations("rs999999999")

        assert results == []

    async def test_fetch_gwas_sorts_by_pvalue(self) -> None:
        """Should sort associations by p-value (most significant first)."""
        gwas_json = {
            "_embedded": {
                "associations": [
                    {
                        "orPerCopyNum": 1.1,
                        "betaNum": None,
                        "pvalueMantissa": 5,
                        "pvalueExponent": -5,
                        "strongestRiskAlleles": [],
                        "efoTraits": [{"trait": "trait A"}],
                    },
                    {
                        "orPerCopyNum": 1.3,
                        "betaNum": None,
                        "pvalueMantissa": 2,
                        "pvalueExponent": -20,
                        "strongestRiskAlleles": [],
                        "efoTraits": [{"trait": "trait B"}],
                    },
                ]
            }
        }

        with patch("genesnap.services.gwas.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=_mock_response(gwas_json))

            results = await fetch_gwas_associations("rs9939609")

        assert len(results) == 2
        # Most significant (smaller p-value) should be first
        assert results[0].trait == "trait B"
        assert results[1].trait == "trait A"

    def test_gwas_association_to_dict(self) -> None:
        """GWASAssociation.to_dict should include all fields."""
        assoc = GWASAssociation(risk_allele="A", odds_ratio=1.31, p_value=1.5e-12, trait="obesity")
        d = assoc.to_dict()
        assert d["risk_allele"] == "A"
        assert d["odds_ratio"] == 1.31
        assert d["trait"] == "obesity"
        assert d["p_value"] == 1.5e-12
