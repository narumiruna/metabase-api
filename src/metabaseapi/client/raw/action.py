from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import cast

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_actions(client: MetabaseClient, *, model_id: int | str | None = None) -> JSONValue | None:
    params = {"model-id": model_id} if model_id is not None else None
    return await client.get("/api/action", params=params)


async def create_action(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/action", body=dict(body))


async def list_public_actions(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/action/public")


async def get_action(client: MetabaseClient, action_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/action/{action_id}")


async def delete_action(client: MetabaseClient, action_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/action/{action_id}")


async def get_action_execute(
    client: MetabaseClient,
    action_id: int | str,
    *,
    parameters: Mapping[str, object] | None = None,
) -> JSONValue | None:
    query_params = cast(Mapping[str, QueryParamValue] | None, parameters)
    return await client.get(f"/api/action/{action_id}/execute", params=query_params)


async def update_action(client: MetabaseClient, action_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
    return await client.put(f"/api/action/{action_id}", body=dict(body))


async def execute_action(
    client: MetabaseClient,
    action_id: int | str,
    *,
    parameters: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(
        f"/api/action/{action_id}/execute",
        body={"parameters": dict(parameters or {})},
    )


async def create_action_public_link(client: MetabaseClient, action_id: int | str) -> JSONValue | None:
    return await client.post(f"/api/action/{action_id}/public_link")


async def delete_action_public_link(client: MetabaseClient, action_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/action/{action_id}/public_link")


__all__ = [
    "create_action",
    "create_action_public_link",
    "delete_action",
    "delete_action_public_link",
    "execute_action",
    "get_action",
    "get_action_execute",
    "list_actions",
    "list_public_actions",
    "update_action",
]
