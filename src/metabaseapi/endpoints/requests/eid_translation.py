from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.eid_translation import EidTranslationResponse


class TranslateEntityIdsRequest(EndpointRequest[EidTranslationResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/eid-translation/translate"
    response_model = EidTranslationResponse
