from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.ai_entity_analysis import AnalyzeChartRequest
from metabaseapi.endpoints.requests.analytics import CreateAnalyticsEventBatchRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def analyze_chart_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(AnalyzeChartRequest(body=dict(body)))


async def create_analytics_event_batch_typed(
    client: MetabaseClient, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(CreateAnalyticsEventBatchRequest(body=dict(body)))


__all__ = [
    "analyze_chart_typed",
    "create_analytics_event_batch_typed",
]
