from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin façade."""

    async def analyze_chart(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/ai-entity-analysis/analyze-chart", body=dict(body))

    async def anonymous_stats(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/analytics/anonymous-stats")

    async def create_analytics_event_batch(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/analytics/internal", body=dict(body))


__all__ = ["_MetabaseClientRawMixin"]
