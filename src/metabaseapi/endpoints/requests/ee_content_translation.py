from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_content_translation import EeContentTranslationCsvResponse
from metabaseapi.endpoints.responses.ee_content_translation import EeContentTranslationDictionaryResponse
from metabaseapi.endpoints.responses.ee_content_translation import EeContentTranslationUploadResponse


class GetEeContentTranslationCsvRequest(EndpointRequest[EeContentTranslationCsvResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/content-translation/csv"
    response_model = EeContentTranslationCsvResponse


class GetEeContentTranslationDictionaryRequest(EndpointRequest[EeContentTranslationDictionaryResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/content-translation/dictionary"
    response_model = EeContentTranslationDictionaryResponse


class GetEeContentTranslationDictionaryTokenRequest(EndpointRequest[EeContentTranslationDictionaryResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/content-translation/dictionary/{token}"
    response_model = EeContentTranslationDictionaryResponse


class PostEeContentTranslationUploadDictionaryRequest(EndpointRequest[EeContentTranslationUploadResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/content-translation/upload-dictionary"
    response_model = EeContentTranslationUploadResponse
