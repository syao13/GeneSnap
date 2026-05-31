"""API response cache using SQLite."""

import json
from datetime import UTC, datetime, timedelta

import aiosqlite

from genesnap.config import settings


async def get_cached(db: aiosqlite.Connection, cache_key: str) -> dict | None:
    """Get a cached API response if it exists and hasn't expired."""
    cursor = await db.execute(
        "SELECT response_json, expires_at FROM api_cache WHERE cache_key = ?",
        (cache_key,),
    )
    row = await cursor.fetchone()

    if row is None:
        return None

    expires_at = datetime.fromisoformat(row["expires_at"])
    if datetime.now(tz=UTC) > expires_at:
        await db.execute("DELETE FROM api_cache WHERE cache_key = ?", (cache_key,))
        await db.commit()
        return None

    return json.loads(row["response_json"])


async def set_cached(
    db: aiosqlite.Connection,
    cache_key: str,
    data: dict,
    ttl_days: int | None = None,
) -> None:
    """Store an API response in the cache."""
    ttl = ttl_days or settings.api_cache_ttl_days
    now = datetime.now(tz=UTC)
    expires = now + timedelta(days=ttl)

    await db.execute(
        """INSERT OR REPLACE INTO api_cache (cache_key, response_json, fetched_at, expires_at)
        VALUES (?, ?, ?, ?)""",
        (
            cache_key,
            json.dumps(data),
            now.isoformat(),
            expires.isoformat(),
        ),
    )
    await db.commit()
