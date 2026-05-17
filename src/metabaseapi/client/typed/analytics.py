from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import AnalyzeChartRequest
from metabaseapi.metabase import CreateAnalyticsEventBatchRequest
from metabaseapi.metabase import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin."""

    async def analyze_chart_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(AnalyzeChartRequest(body=dict(body)))

    async def create_analytics_event_batch_typed(
        self: MetabaseClient, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(CreateAnalyticsEventBatchRequest(body=dict(body)))


__all__ = ["_MetabaseClientTypedMixin"]
