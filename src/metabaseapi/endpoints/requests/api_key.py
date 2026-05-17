from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.api_key import ListApiKeysResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class CreateApiKeyRequest(EndpointRequest[ApiKey]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/api-key"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def request_body(self) -> JSONValue:
        return self.body


class ListApiKeysRequest(EndpointRequest[ListApiKeysResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key"

    async def do(self, client: MetabaseRequestClient) -> ListApiKeysResponse:
        return await self.execute(client, ListApiKeysResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListApiKeysResponse:
        return self.execute_sync(client, ListApiKeysResponse)


class CountApiKeysRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key/count"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class UpdateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteApiKeyRequest(EndpointRequest[GenericOperationResponse]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"


class RegenerateApiKeyRequest(EndpointRequest[ApiKey]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}/regenerate"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}/regenerate"
