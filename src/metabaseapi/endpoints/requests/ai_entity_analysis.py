from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.execution import _BaseMetabaseRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.wire import JSONValue


class AnalyzeChartRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ai-entity-analysis/analyze-chart"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body
