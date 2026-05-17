from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def current_user(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/user/current")


async def list_users(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/user")


async def get_user(client: MetabaseClient, user_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/user/{user_id}")


__all__ = [
    "current_user",
    "get_user",
    "list_users",
]
