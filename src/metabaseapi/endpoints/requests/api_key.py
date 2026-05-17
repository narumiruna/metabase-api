from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.api_key import ApiKeyCountResponse
from metabaseapi.endpoints.responses.api_key import DeleteApiKeyResponse
from metabaseapi.endpoints.responses.api_key import ListApiKeysResponse


class CreateApiKeyRequest(EndpointRequest[ApiKey]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/api-key"
    response_model = ApiKey


class ListApiKeysRequest(EndpointRequest[ListApiKeysResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key"
    response_model = ListApiKeysResponse


class CountApiKeysRequest(EndpointRequest[ApiKeyCountResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key/count"
    response_model = ApiKeyCountResponse


class UpdateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{api_key_id}"
    response_model = ApiKey


class DeleteApiKeyRequest(EndpointRequest[DeleteApiKeyResponse]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/api-key/{api_key_id}"
    response_model = DeleteApiKeyResponse


class RegenerateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{api_key_id}/regenerate"
    response_model = ApiKey
