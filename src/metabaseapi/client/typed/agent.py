from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.agent import AgentConstructQueryRequest
from metabaseapi.endpoints.requests.agent import AgentExecuteRequest
from metabaseapi.endpoints.requests.agent import AgentPingRequest
from metabaseapi.endpoints.requests.agent import AgentQueryRequest
from metabaseapi.endpoints.requests.agent import AgentSearchRequest
from metabaseapi.endpoints.requests.agent import GetAgentMetricFieldValuesRequest
from metabaseapi.endpoints.requests.agent import GetAgentMetricRequest
from metabaseapi.endpoints.requests.agent import GetAgentTableFieldValuesRequest
from metabaseapi.endpoints.requests.agent import GetAgentTableRequest
from metabaseapi.endpoints.responses import AgentResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def agent_execute_typed(client: MetabaseClient, body: dict[str, object]) -> AgentResponse:
    return await client.run(AgentExecuteRequest(body=body))


async def get_agent_metric_typed(client: MetabaseClient, metric_id: int | str) -> AgentResponse:
    return await client.run(GetAgentMetricRequest(metric_id=metric_id))


async def get_agent_metric_field_values_typed(
    client: MetabaseClient, metric_id: int | str, field_id: int | str
) -> AgentResponse:
    return await client.run(GetAgentMetricFieldValuesRequest(metric_id=metric_id, field_id=field_id))


async def agent_ping_typed(client: MetabaseClient) -> AgentResponse:
    return await client.run(AgentPingRequest())


async def agent_search_typed(client: MetabaseClient, body: dict[str, object]) -> AgentResponse:
    return await client.run(AgentSearchRequest(body=body))


async def get_agent_table_typed(client: MetabaseClient, table_id: int | str) -> AgentResponse:
    return await client.run(GetAgentTableRequest(table_id=table_id))


async def get_agent_table_field_values_typed(
    client: MetabaseClient,
    table_id: int | str,
    field_id: int | str,
) -> AgentResponse:
    return await client.run(GetAgentTableFieldValuesRequest(table_id=table_id, field_id=field_id))


async def agent_construct_query_typed(client: MetabaseClient, body: dict[str, object]) -> AgentResponse:
    return await client.run(AgentConstructQueryRequest(body=body))


async def agent_query_typed(client: MetabaseClient, body: dict[str, object]) -> AgentResponse:
    return await client.run(AgentQueryRequest(body=body))


__all__ = [
    "agent_construct_query_typed",
    "agent_execute_typed",
    "agent_ping_typed",
    "agent_query_typed",
    "agent_search_typed",
    "get_agent_metric_field_values_typed",
    "get_agent_metric_typed",
    "get_agent_table_field_values_typed",
    "get_agent_table_typed",
]
