from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_semantic_search import EeSemanticSearchStatusResponse


class GetEeSemanticSearchStatusRequest(EndpointRequest[EeSemanticSearchStatusResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/semantic-search/status"
    response_model = EeSemanticSearchStatusResponse
