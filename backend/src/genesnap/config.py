"""Application configuration via environment variables."""

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    ncbi_api_key: str = ""
    db_path: Path = Path(__file__).parent.parent.parent / "data" / "genesnap.db"
    api_cache_ttl_days: int = 7
    debug: bool = False
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
