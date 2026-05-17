from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_cards(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/card")


async def create_card(
    client: MetabaseClient,
    *,
    name: str,
    dataset_query: Mapping[str, object],
    display: str,
    visualization_settings: Mapping[str, object] | None = None,
    card_type: str | None = "question",
    collection_id: int | str | None = None,
    description: str | None = None,
    parameters: list[object] | None = None,
    result_metadata: list[object] | None = None,
) -> JSONValue | None:
    body: dict[str, object] = {
        "name": name,
        "dataset_query": dict(dataset_query),
        "display": display,
        "visualization_settings": dict(visualization_settings or {}),
    }
    if card_type is not None:
        body["type"] = card_type
    if collection_id is not None:
        body["collection_id"] = collection_id
    if description is not None:
        body["description"] = description
    if parameters is not None:
        body["parameters"] = parameters
    if result_metadata is not None:
        body["result_metadata"] = result_metadata
    return await client.post("/api/card", body=body)


async def create_question(
    client: MetabaseClient,
    *,
    name: str,
    dataset_query: Mapping[str, object],
    display: str,
    visualization_settings: Mapping[str, object] | None = None,
    collection_id: int | str | None = None,
    description: str | None = None,
    parameters: list[object] | None = None,
    result_metadata: list[object] | None = None,
) -> JSONValue | None:
    return await create_card(
        client,
        name=name,
        dataset_query=dataset_query,
        display=display,
        visualization_settings=visualization_settings,
        card_type="question",
        collection_id=collection_id,
        description=description,
        parameters=parameters,
        result_metadata=result_metadata,
    )


async def card_collections(
    client: MetabaseClient,
    card_ids: list[int | str],
    collection_id: int | str | None = None,
) -> JSONValue | None:
    body: dict[str, object] = {"card_ids": card_ids}
    if collection_id is not None:
        body["collection_id"] = collection_id
    return await client.post("/api/card/collections", body=body)


async def list_embeddable_cards(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/card/embeddable")


async def pivot_query(
    client: MetabaseClient,
    card_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(f"/api/card/pivot/{card_id}/query", body=dict(body) if body is not None else None)


async def list_public_cards(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/card/public")


async def get_card_param_search_values(
    client: MetabaseClient,
    card_id: int | str,
    param_key: str,
    query: str,
) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/search/{query}")


async def get_card_param_values(client: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/values")


async def create_card_public_link(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.post(f"/api/card/{card_id}/public_link")


async def delete_card_public_link(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/card/{card_id}/public_link")


async def query_card(
    client: MetabaseClient,
    card_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(f"/api/card/{card_id}/query", body=dict(body) if body is not None else None)


async def query_card_export(
    client: MetabaseClient,
    card_id: int | str,
    export_format: str,
    body: Mapping[str, object] | None = None,
    *,
    pivot_results: bool | None = None,
    format_rows: bool | None = None,
) -> JSONValue | None:
    params: dict[str, QueryParamValue] = {}
    if pivot_results is not None:
        params["pivot-results"] = pivot_results
    if format_rows is not None:
        params["format-rows"] = format_rows
    return await client.post(
        f"/api/card/{card_id}/query/{export_format}",
        body=dict(body) if body is not None else None,
        params=params or None,
    )


async def update_card(client: MetabaseClient, card_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
    return await client.put(f"/api/card/{card_id}", body=dict(body))


async def delete_card(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/card/{card_id}")


async def copy_card(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.post(f"/api/card/{card_id}/copy")


async def cards_dashboards(client: MetabaseClient, card_ids: list[int | str]) -> JSONValue | None:
    return await client.post("/api/cards/dashboards", body={"card_ids": card_ids})


async def move_cards(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/cards/move", body=dict(body))


async def get_card_dashboards(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/dashboards")


async def get_card_param_remapping(client: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/remapping")


async def get_card_query_metadata(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/query_metadata")


async def get_card_series(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/series")


async def get_card(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}")


__all__ = [
    "card_collections",
    "cards_dashboards",
    "copy_card",
    "create_card",
    "create_card_public_link",
    "create_question",
    "delete_card",
    "delete_card_public_link",
    "get_card",
    "get_card_dashboards",
    "get_card_param_remapping",
    "get_card_param_search_values",
    "get_card_param_values",
    "get_card_query_metadata",
    "get_card_series",
    "list_cards",
    "list_embeddable_cards",
    "list_public_cards",
    "move_cards",
    "pivot_query",
    "query_card",
    "query_card_export",
    "update_card",
]
