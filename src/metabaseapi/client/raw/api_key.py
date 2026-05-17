from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_api_key(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/api-key", body=dict(body))


async def list_api_keys(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/api-key")


async def count_api_keys(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/api-key/count")


async def update_api_key(client: MetabaseClient, api_key_id: int | str, body: dict[str, object]) -> JSONValue | None:
    return await client.put(f"/api/api-key/{api_key_id}", body=dict(body))


async def delete_api_key(client: MetabaseClient, api_key_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/api-key/{api_key_id}")


async def regenerate_api_key(client: MetabaseClient, api_key_id: int | str) -> JSONValue | None:
    return await client.put(f"/api/api-key/{api_key_id}/regenerate")


__all__ = [
    "count_api_keys",
    "create_api_key",
    "delete_api_key",
    "list_api_keys",
    "regenerate_api_key",
    "update_api_key",
]
