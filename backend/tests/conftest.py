"""Shared test fixtures."""

from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_23andme_text() -> str:
    """Load sample 23andMe raw data as text."""
    return (FIXTURES_DIR / "sample_23andme.txt").read_text()


@pytest.fixture
def sample_23andme_path() -> Path:
    """Path to sample 23andMe raw data file."""
    return FIXTURES_DIR / "sample_23andme.txt"
