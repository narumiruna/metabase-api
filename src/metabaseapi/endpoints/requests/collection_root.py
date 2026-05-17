from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class GetCollectionRootRequest(EndpointRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)


class GetCollectionRootDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetCollectionRootItemsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/items"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class PostCollectionRootMoveDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/root/move-dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body
