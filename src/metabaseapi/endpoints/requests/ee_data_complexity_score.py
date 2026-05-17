from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_data_complexity_score import EeDataComplexityScoreResponse


class GetEeDataComplexityScoreComplexityRequest(EndpointRequest[EeDataComplexityScoreResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/data-complexity-score/complexity"
    response_model = EeDataComplexityScoreResponse
