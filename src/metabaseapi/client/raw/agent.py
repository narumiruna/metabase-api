from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for agent endpoints."""

    async def agent_execute(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v1/execute", body=dict(body))

    async def get_agent_metric(self: MetabaseClient, metric_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/metric/{metric_id}")

    async def get_agent_metric_field_values(
        self: MetabaseClient, metric_id: int | str, field_id: int | str
    ) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/metric/{metric_id}/field/{field_id}/values")

    async def agent_ping(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/agent/v1/ping")

    async def agent_search(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v1/search", body=dict(body))

    async def get_agent_table(self: MetabaseClient, table_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/table/{table_id}")

    async def get_agent_table_field_values(
        self: MetabaseClient,
        table_id: int | str,
        field_id: int | str,
    ) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/table/{table_id}/field/{field_id}/values")

    async def agent_construct_query(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v2/construct-query", body=dict(body))

    async def agent_query(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v2/query", body=dict(body))


__all__ = ["_MetabaseClientRawMixin"]
