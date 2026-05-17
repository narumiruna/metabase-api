from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import ApiKey
from metabaseapi.metabase import CountApiKeysRequest
from metabaseapi.metabase import CreateApiKeyRequest
from metabaseapi.metabase import DeleteApiKeyRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import ListApiKeysRequest
from metabaseapi.metabase import ListApiKeysResponse
from metabaseapi.metabase import RegenerateApiKeyRequest
from metabaseapi.metabase import UpdateApiKeyRequest

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for API key endpoints."""

    async def create_api_key_typed(self: MetabaseClient, body: dict[str, object]) -> ApiKey:
        return await self.run(CreateApiKeyRequest(body=body))

    async def list_api_keys_typed(self: MetabaseClient) -> ListApiKeysResponse:
        return await self.run(ListApiKeysRequest())

    async def count_api_keys_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(CountApiKeysRequest())

    async def update_api_key_typed(self: MetabaseClient, api_key_id: int | str, body: dict[str, object]) -> ApiKey:
        return await self.run(UpdateApiKeyRequest(api_key_id=api_key_id, body=body))

    async def delete_api_key_typed(self: MetabaseClient, api_key_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteApiKeyRequest(api_key_id=api_key_id))

    async def regenerate_api_key_typed(self: MetabaseClient, api_key_id: int | str) -> ApiKey:
        return await self.run(RegenerateApiKeyRequest(api_key_id=api_key_id))


__all__ = ["_MetabaseClientTypedMixin"]
