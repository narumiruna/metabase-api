from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def agent_execute(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/agent/v1/execute", body=dict(body))


async def get_agent_metric(client: MetabaseClient, metric_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/agent/v1/metric/{metric_id}")


async def get_agent_metric_field_values(
    client: MetabaseClient, metric_id: int | str, field_id: int | str
) -> JSONValue | None:
    return await client.get(f"/api/agent/v1/metric/{metric_id}/field/{field_id}/values")


async def agent_ping(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/agent/v1/ping")


async def agent_search(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/agent/v1/search", body=dict(body))


async def get_agent_table(client: MetabaseClient, table_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/agent/v1/table/{table_id}")


async def get_agent_table_field_values(
    client: MetabaseClient,
    table_id: int | str,
    field_id: int | str,
) -> JSONValue | None:
    return await client.get(f"/api/agent/v1/table/{table_id}/field/{field_id}/values")


async def agent_construct_query(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/agent/v2/construct-query", body=dict(body))


async def agent_query(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/agent/v2/query", body=dict(body))


__all__ = [
    "agent_construct_query",
    "agent_execute",
    "agent_ping",
    "agent_query",
    "agent_search",
    "get_agent_metric",
    "get_agent_metric_field_values",
    "get_agent_table",
    "get_agent_table_field_values",
]
