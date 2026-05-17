from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import AgentConstructQueryRequest
from metabaseapi.metabase import AgentExecuteRequest
from metabaseapi.metabase import AgentPingRequest
from metabaseapi.metabase import AgentQueryRequest
from metabaseapi.metabase import AgentResponse
from metabaseapi.metabase import AgentSearchRequest
from metabaseapi.metabase import GetAgentMetricFieldValuesRequest
from metabaseapi.metabase import GetAgentMetricRequest
from metabaseapi.metabase import GetAgentTableFieldValuesRequest
from metabaseapi.metabase import GetAgentTableRequest

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for agent endpoints."""

    async def agent_execute_typed(self: MetabaseClient, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentExecuteRequest(body=body))

    async def get_agent_metric_typed(self: MetabaseClient, metric_id: int | str) -> AgentResponse:
        return await self.run(GetAgentMetricRequest(metric_id=metric_id))

    async def get_agent_metric_field_values_typed(
        self: MetabaseClient, metric_id: int | str, field_id: int | str
    ) -> AgentResponse:
        return await self.run(GetAgentMetricFieldValuesRequest(metric_id=metric_id, field_id=field_id))

    async def agent_ping_typed(self: MetabaseClient) -> AgentResponse:
        return await self.run(AgentPingRequest())

    async def agent_search_typed(self: MetabaseClient, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentSearchRequest(body=body))

    async def get_agent_table_typed(self: MetabaseClient, table_id: int | str) -> AgentResponse:
        return await self.run(GetAgentTableRequest(table_id=table_id))

    async def get_agent_table_field_values_typed(
        self: MetabaseClient,
        table_id: int | str,
        field_id: int | str,
    ) -> AgentResponse:
        return await self.run(GetAgentTableFieldValuesRequest(table_id=table_id, field_id=field_id))

    async def agent_construct_query_typed(self: MetabaseClient, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentConstructQueryRequest(body=body))

    async def agent_query_typed(self: MetabaseClient, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentQueryRequest(body=body))


__all__ = ["_MetabaseClientTypedMixin"]
