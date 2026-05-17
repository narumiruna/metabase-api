from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_dashboard(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/dashboard", body=dict(body))


async def list_dashboards(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/dashboard")


async def get_dashboard(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/dashboard/{dashboard_id}")


async def get_dashboard_embeddable(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/dashboard/embeddable")


async def get_dashboard_public(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/dashboard/public")


async def save_dashboard(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/dashboard/save", body=dict(body))


async def save_dashboard_to_collection(
    client: MetabaseClient,
    parent_collection_id: int | str,
    body: Mapping[str, object],
) -> JSONValue | None:
    return await client.post(f"/api/dashboard/save/collection/{parent_collection_id}", body=dict(body))


async def create_dashboard_public_link(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.post(f"/api/dashboard/{dashboard_id}/public_link")


async def delete_dashboard_public_link(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/dashboard/{dashboard_id}/public_link")


async def copy_dashboard(
    client: MetabaseClient,
    from_dashboard_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(
        f"/api/dashboard/{from_dashboard_id}/copy",
        body=dict(body) if body is not None else None,
    )


async def delete_dashboard(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/dashboard/{dashboard_id}")


async def update_dashboard(
    client: MetabaseClient, dashboard_id: int | str, body: Mapping[str, object]
) -> JSONValue | None:
    return await client.put(f"/api/dashboard/{dashboard_id}", body=dict(body))


async def update_dashboard_cards(
    client: MetabaseClient, dashboard_id: int | str, body: Mapping[str, object]
) -> JSONValue | None:
    return await client.put(f"/api/dashboard/{dashboard_id}/cards", body=dict(body))


async def get_dashboard_items(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/dashboard/{dashboard_id}/items")


__all__ = [
    "copy_dashboard",
    "create_dashboard",
    "create_dashboard_public_link",
    "delete_dashboard",
    "delete_dashboard_public_link",
    "get_dashboard",
    "get_dashboard_embeddable",
    "get_dashboard_items",
    "get_dashboard_public",
    "list_dashboards",
    "save_dashboard",
    "save_dashboard_to_collection",
    "update_dashboard",
    "update_dashboard_cards",
]
