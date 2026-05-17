from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.endpoints.requests.api_key import CountApiKeysRequest
from metabaseapi.endpoints.requests.api_key import CreateApiKeyRequest
from metabaseapi.endpoints.requests.api_key import DeleteApiKeyRequest
from metabaseapi.endpoints.requests.api_key import ListApiKeysRequest
from metabaseapi.endpoints.requests.api_key import RegenerateApiKeyRequest
from metabaseapi.endpoints.requests.api_key import UpdateApiKeyRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListApiKeysResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_api_key_typed(client: MetabaseClient, body: dict[str, object]) -> ApiKey:
    return await client.run(CreateApiKeyRequest(body=body))


async def list_api_keys_typed(client: MetabaseClient) -> ListApiKeysResponse:
    return await client.run(ListApiKeysRequest())


async def count_api_keys_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(CountApiKeysRequest())


async def update_api_key_typed(client: MetabaseClient, api_key_id: int | str, body: dict[str, object]) -> ApiKey:
    return await client.run(UpdateApiKeyRequest(api_key_id=api_key_id, body=body))


async def delete_api_key_typed(client: MetabaseClient, api_key_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteApiKeyRequest(api_key_id=api_key_id))


async def regenerate_api_key_typed(client: MetabaseClient, api_key_id: int | str) -> ApiKey:
    return await client.run(RegenerateApiKeyRequest(api_key_id=api_key_id))


__all__ = [
    "count_api_keys_typed",
    "create_api_key_typed",
    "delete_api_key_typed",
    "list_api_keys_typed",
    "regenerate_api_key_typed",
    "update_api_key_typed",
]
