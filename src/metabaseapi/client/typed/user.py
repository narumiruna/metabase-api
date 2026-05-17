from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import CurrentUserResponse
from metabaseapi.endpoints.entities import User
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.endpoints.requests.user import GetUserRequest
from metabaseapi.endpoints.requests.user import ListUsersRequest
from metabaseapi.endpoints.requests.user_key_value import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceRequest
from metabaseapi.endpoints.requests.user_key_value import PutUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListUsersResponse
from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def current_user_typed(client: MetabaseClient) -> CurrentUserResponse:
    return await client.run(CurrentUserRequest())


async def list_users_typed(client: MetabaseClient) -> ListUsersResponse:
    return await client.run(ListUsersRequest())


async def get_user_typed(client: MetabaseClient, user_id: int | str) -> User:
    return await client.run(GetUserRequest(user_id=user_id))


async def get_user_key_value_namespace_typed(client: MetabaseClient, namespace: int | str) -> GenericOperationResponse:
    return await client.run(GetUserKeyValueNamespaceRequest(namespace=str(namespace)))


async def put_user_key_value_namespace_key_typed(
    client: MetabaseClient,
    namespace: int | str,
    key: str,
    body: JSONValue,
) -> GenericOperationResponse:
    return await client.run(PutUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key, body=body))


async def get_user_key_value_namespace_key_typed(
    client: MetabaseClient, namespace: int | str, key: str
) -> GenericOperationResponse:
    return await client.run(GetUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key))


async def delete_user_key_value_namespace_key_typed(
    client: MetabaseClient,
    namespace: int | str,
    key: str,
) -> GenericOperationResponse:
    return await client.run(DeleteUserKeyValueNamespaceKeyRequest(namespace=str(namespace), key=key))


__all__ = [
    "current_user_typed",
    "delete_user_key_value_namespace_key_typed",
    "get_user_key_value_namespace_key_typed",
    "get_user_key_value_namespace_typed",
    "get_user_typed",
    "list_users_typed",
    "put_user_key_value_namespace_key_typed",
]
