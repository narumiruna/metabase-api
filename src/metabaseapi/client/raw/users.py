from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw user helper methods."""

    async def current_user(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/user/current")

    async def list_users(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/user")

    async def get_user(self: MetabaseClient, user_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/user/{user_id}")

    async def get_user_key_value_namespace(self: MetabaseClient, namespace: int | str) -> JSONValue | None:
        return await self.get(f"/api/user-key-value/namespace/{namespace}")

    async def get_user_key_value_namespace_key(
        self: MetabaseClient, namespace: int | str, key: str
    ) -> JSONValue | None:
        return await self.get(f"/api/user-key-value/namespace/{namespace}/key/{key}")

    async def put_user_key_value_namespace_key(
        self: MetabaseClient,
        namespace: int | str,
        key: str,
        body: JSONValue,
    ) -> JSONValue | None:
        return await self.put(f"/api/user-key-value/namespace/{namespace}/key/{key}", body=body)

    async def delete_user_key_value_namespace_key(
        self: MetabaseClient, namespace: int | str, key: str
    ) -> JSONValue | None:
        return await self.delete(f"/api/user-key-value/namespace/{namespace}/key/{key}")


__all__ = ["_MetabaseClientRawMixin"]
