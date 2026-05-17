from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class GetAnonymousStatsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/analytics/anonymous-stats"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class CreateAnalyticsEventBatchRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/analytics/internal"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body
