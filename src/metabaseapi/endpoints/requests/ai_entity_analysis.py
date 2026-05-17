from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ai_entity_analysis import AnalyzeChartResponse


class AnalyzeChartRequest(EndpointRequest[AnalyzeChartResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ai-entity-analysis/analyze-chart"
    response_model = AnalyzeChartResponse
