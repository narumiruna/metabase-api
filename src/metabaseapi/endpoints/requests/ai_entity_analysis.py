from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class AnalyzeChartRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ai-entity-analysis/analyze-chart"
    response_model = GenericOperationResponse
