from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def anonymous_stats(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/analytics/anonymous-stats")


async def create_analytics_event_batch(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/analytics/internal", body=dict(body))


__all__ = [
    "anonymous_stats",
    "create_analytics_event_batch",
]
