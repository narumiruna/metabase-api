from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.llm import ExtractLlmTablesResponse
from metabaseapi.endpoints.responses.llm import GenerateLlmSqlResponse
from metabaseapi.endpoints.responses.llm import ListLlmModelsResponse


class ExtractLlmTablesRequest(EndpointRequest[ExtractLlmTablesResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/llm/extract-tables"
    response_model = ExtractLlmTablesResponse


class GenerateLlmSqlRequest(EndpointRequest[GenerateLlmSqlResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/llm/generate-sql"
    response_model = GenerateLlmSqlResponse


class ListLlmModelsRequest(EndpointRequest[ListLlmModelsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/llm/list-models"
    response_model = ListLlmModelsResponse
