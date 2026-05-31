"""Integration tests for the API endpoints."""

import sqlite3
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient

from genesnap.config import settings
from genesnap.db.connection import SCHEMA_SQL, close_db
from genesnap.db.seed import _insert_genotype_interpretations, _insert_variants
from genesnap.main import app

TEST_DB = Path(__file__).parent / "test_api.db"
FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture(autouse=True)
async def setup_test_db(monkeypatch: pytest.MonkeyPatch) -> None:
    """Set up a test database for each test."""
    # Point app at test DB
    monkeypatch.setattr(settings, "db_path", TEST_DB)

    # Create and seed synchronously
    if TEST_DB.exists():
        TEST_DB.unlink()
    conn = sqlite3.connect(TEST_DB)
    conn.executescript(SCHEMA_SQL)
    _insert_variants(conn)
    _insert_genotype_interpretations(conn)
    conn.commit()
    conn.close()

    yield

    # Cleanup
    await close_db()
    TEST_DB.unlink(missing_ok=True)


@pytest.fixture
async def client() -> AsyncClient:
    """Create an async test client for the FastAPI app."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestHealthEndpoint:
    """Tests for GET /api/health."""

    async def test_health_returns_ok(self, client: AsyncClient) -> None:
        """Health endpoint should return status ok."""
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["variant_count"] > 0


class TestUploadEndpoint:
    """Tests for POST /api/upload."""

    async def test_upload_returns_analysis_result(self, client: AsyncClient) -> None:
        """Uploading a valid file should return an AnalysisResult."""
        file_content = (FIXTURES_DIR / "sample_23andme.txt").read_bytes()
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", file_content, "text/plain")},
        )
        assert response.status_code == 200
        data = response.json()
        assert "summary" in data
        assert "health_risks" in data
        assert "pharmacogenomics" in data
        assert "traits" in data

    async def test_upload_finds_known_variants(self, client: AsyncClient) -> None:
        """Should identify known variants from the sample file."""
        file_content = (FIXTURES_DIR / "sample_23andme.txt").read_bytes()
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", file_content, "text/plain")},
        )
        data = response.json()
        summary = data["summary"]

        # Sample file contains rs6025, rs429358, rs1801133, etc.
        assert summary["total_variants_found"] > 0
        assert summary["total_snps_parsed"] == 17  # 19 lines - 1 no-call - 1 internal

    async def test_upload_categorizes_results(self, client: AsyncClient) -> None:
        """Should have results in all three categories from sample data."""
        file_content = (FIXTURES_DIR / "sample_23andme.txt").read_bytes()
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", file_content, "text/plain")},
        )
        data = response.json()
        summary = data["summary"]

        assert summary["health_risk_count"] > 0
        assert summary["pharmacogenomics_count"] > 0
        assert summary["trait_count"] > 0

    async def test_upload_variant_structure(self, client: AsyncClient) -> None:
        """Each variant match should have the expected structure."""
        file_content = (FIXTURES_DIR / "sample_23andme.txt").read_bytes()
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", file_content, "text/plain")},
        )
        data = response.json()
        match = data["health_risks"][0]

        assert "snp" in match
        assert "variant" in match
        assert "interpretation" in match
        assert "risk_level" in match
        assert "publications" in match

        assert "rsid" in match["snp"]
        assert "gene" in match["variant"]
        assert "name" in match["variant"]
        assert "description" in match["variant"]

    async def test_upload_minimal_file(self, client: AsyncClient) -> None:
        """Should handle a minimal file with just one known SNP."""
        content = b"rs6025\t1\t169519049\tAG\n"
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", content, "text/plain")},
        )
        data = response.json()
        assert data["summary"]["total_snps_parsed"] == 1
        assert data["summary"]["total_variants_found"] == 1
        assert data["health_risks"][0]["variant"]["gene"] == "F5"

    async def test_upload_empty_file(self, client: AsyncClient) -> None:
        """Should handle an empty file gracefully."""
        content = b"# Just comments\n# No data\n"
        response = await client.post(
            "/api/upload",
            files={"file": ("genome.txt", content, "text/plain")},
        )
        data = response.json()
        assert data["summary"]["total_snps_parsed"] == 0
        assert data["summary"]["total_variants_found"] == 0
