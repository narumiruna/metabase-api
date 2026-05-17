from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_embedding_hub import EeEmbeddingHubChecklistResponse


class GetEeEmbeddingHubChecklistRequest(EndpointRequest[EeEmbeddingHubChecklistResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/embedding-hub/checklist"
    response_model = EeEmbeddingHubChecklistResponse
