from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase import GetUserKeyValueNamespaceRequest
from metabaseapi.metabase import PutUserKeyValueNamespaceKeyRequest
from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed user helper methods."""

    async def get_user_key_value_namespace_typed(self: MetabaseClient, namespace: str) -> GenericOperationResponse:
        return await self.run(GetUserKeyValueNamespaceRequest(namespace=namespace))

    async def put_user_key_value_namespace_key_typed(
        self: MetabaseClient,
        namespace: str,
        key: str,
        body: JSONValue,
    ) -> GenericOperationResponse:
        return await self.run(PutUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key, body=body))

    async def get_user_key_value_namespace_key_typed(
        self: MetabaseClient, namespace: str, key: str
    ) -> GenericOperationResponse:
        return await self.run(GetUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key))

    async def delete_user_key_value_namespace_key_typed(
        self: MetabaseClient,
        namespace: str,
        key: str,
    ) -> GenericOperationResponse:
        return await self.run(DeleteUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key))


__all__ = ["_MetabaseClientTypedMixin"]
