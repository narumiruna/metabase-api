from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.agent import AgentResponse
from metabaseapi.wire import JSONValue


class AgentExecuteRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/execute"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetAgentMetricRequest(EndpointRequest[AgentResponse]):
    metric_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{id}"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/metric/{self.metric_id}"


class GetAgentMetricFieldValuesRequest(EndpointRequest[AgentResponse]):
    metric_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{id}/field/{field-id}/values"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/metric/{self.metric_id}/field/{self.field_id}/values"


class AgentPingRequest(EndpointRequest[AgentResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/ping"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)


class AgentSearchRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/search"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetAgentTableRequest(EndpointRequest[AgentResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{id}"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/table/{self.table_id}"


class GetAgentTableFieldValuesRequest(EndpointRequest[AgentResponse]):
    table_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{id}/field/{field-id}/values"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/table/{self.table_id}/field/{self.field_id}/values"


class AgentConstructQueryRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/construct-query"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class AgentQueryRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/query"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body
