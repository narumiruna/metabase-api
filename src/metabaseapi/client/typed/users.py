from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import CurrentUserRequest
from metabaseapi.metabase import CurrentUserResponse
from metabaseapi.metabase import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase import GetUserKeyValueNamespaceRequest
from metabaseapi.metabase import GetUserRequest
from metabaseapi.metabase import ListUsersRequest
from metabaseapi.metabase import ListUsersResponse
from metabaseapi.metabase import PutUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase import User
from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed user helper methods."""

    async def current_user_typed(self: MetabaseClient) -> CurrentUserResponse:
        return await self.run(CurrentUserRequest())

    async def list_users_typed(self: MetabaseClient) -> ListUsersResponse:
        return await self.run(ListUsersRequest())

    async def get_user_typed(self: MetabaseClient, user_id: int | str) -> User:
        return await self.run(GetUserRequest(user_id=user_id))

    async def get_user_key_value_namespace_typed(
        self: MetabaseClient, namespace: int | str
    ) -> GenericOperationResponse:
        return await self.run(GetUserKeyValueNamespaceRequest(namespace=str(namespace)))

    async def put_user_key_value_namespace_key_typed(
        self: MetabaseClient,
        namespace: int | str,
        key: str,
        body: JSONValue,
    ) -> GenericOperationResponse:
        return await self.run(PutUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key, body=body))

    async def get_user_key_value_namespace_key_typed(
        self: MetabaseClient, namespace: int | str, key: str
    ) -> GenericOperationResponse:
        return await self.run(GetUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key))

    async def delete_user_key_value_namespace_key_typed(
        self: MetabaseClient,
        namespace: int | str,
        key: str,
    ) -> GenericOperationResponse:
        return await self.run(DeleteUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key))


__all__ = ["_MetabaseClientTypedMixin"]
