from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class PostDashboardPivotQueryRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/pivot/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/pivot/{self.dashboard_id}/dashcard/{self.dashcard_id}/card/{self.card_id}/query"

    def request_body(self) -> JSONValue | None:
        return self.body


class GetDashboardDashcardExecuteRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class ExecuteDashboardDashcardRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class DashboardParamRemappingRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/remapping"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/remapping"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamSearchRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    query: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/search/{query}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/search/{self.query}"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamValuesRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/values"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/values"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class GetDashboardQueryMetadataRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/query_metadata"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/query_metadata"


class GetDashboardRelatedRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/related"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/related"
