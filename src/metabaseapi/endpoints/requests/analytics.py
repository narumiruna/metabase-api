from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.analytics import AnalyticsEventBatchResponse
from metabaseapi.endpoints.responses.analytics import AnonymousStatsResponse


class GetAnonymousStatsRequest(EndpointRequest[AnonymousStatsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/analytics/anonymous-stats"
    response_model = AnonymousStatsResponse


class CreateAnalyticsEventBatchRequest(EndpointRequest[AnalyticsEventBatchResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/analytics/internal"
    response_model = AnalyticsEventBatchResponse
