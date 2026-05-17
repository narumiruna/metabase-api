from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_user_key_value_namespace(client: MetabaseClient, namespace: int | str) -> JSONValue | None:
    return await client.get(f"/api/user-key-value/namespace/{namespace}")


async def get_user_key_value_namespace_key(client: MetabaseClient, namespace: int | str, key: str) -> JSONValue | None:
    return await client.get(f"/api/user-key-value/namespace/{namespace}/key/{key}")


async def put_user_key_value_namespace_key(
    client: MetabaseClient,
    namespace: int | str,
    key: str,
    body: JSONValue,
) -> JSONValue | None:
    return await client.put(f"/api/user-key-value/namespace/{namespace}/key/{key}", body=body)


async def delete_user_key_value_namespace_key(
    client: MetabaseClient, namespace: int | str, key: str
) -> JSONValue | None:
    return await client.delete(f"/api/user-key-value/namespace/{namespace}/key/{key}")


__all__ = [
    "delete_user_key_value_namespace_key",
    "get_user_key_value_namespace",
    "get_user_key_value_namespace_key",
    "put_user_key_value_namespace_key",
]
