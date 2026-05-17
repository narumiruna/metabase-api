from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.api_key import ListApiKeysResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class CreateApiKeyRequest(EndpointRequest[ApiKey]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/api-key"
    response_model: ClassVar[object] = ApiKey

    def request_body(self) -> JSONValue:
        return self.body


class ListApiKeysRequest(EndpointRequest[ListApiKeysResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key"
    response_model: ClassVar[object] = ListApiKeysResponse


class CountApiKeysRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key/count"
    response_model: ClassVar[object] = GenericOperationResponse


class UpdateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"
    response_model: ClassVar[object] = ApiKey

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteApiKeyRequest(EndpointRequest[GenericOperationResponse]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"


class RegenerateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}/regenerate"
    response_model: ClassVar[object] = ApiKey

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}/regenerate"
