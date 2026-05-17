from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class GetBugReportingConnectionPoolDetailsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/connection-pool-details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetBugReportingDetailsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)
