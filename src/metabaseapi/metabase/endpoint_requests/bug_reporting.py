from __future__ import annotations

from typing import ClassVar

from metabaseapi.metabase.request_base import MetabaseRequestClient
from metabaseapi.metabase.request_base import _BaseMetabaseRequest
from metabaseapi.metabase.responses import GenericOperationResponse


class GetBugReportingConnectionPoolDetailsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/connection-pool-details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetBugReportingDetailsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)
