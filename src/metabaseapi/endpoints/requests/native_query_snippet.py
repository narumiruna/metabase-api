from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.native_query_snippet import ListNativeQuerySnippetsResponse
from metabaseapi.endpoints.responses.native_query_snippet import NativeQuerySnippet


class ListNativeQuerySnippetsRequest(EndpointRequest[ListNativeQuerySnippetsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/native-query-snippet"
    response_model = ListNativeQuerySnippetsResponse


class CreateNativeQuerySnippetRequest(EndpointRequest[NativeQuerySnippet]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/native-query-snippet"
    response_model = NativeQuerySnippet


class GetNativeQuerySnippetRequest(EndpointRequest[NativeQuerySnippet]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/native-query-snippet/{id}"
    response_model = NativeQuerySnippet


class UpdateNativeQuerySnippetRequest(EndpointRequest[NativeQuerySnippet]):
    id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/native-query-snippet/{id}"
    response_model = NativeQuerySnippet
