from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def pivot_query(
    client: MetabaseClient,
    card_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(f"/api/card/pivot/{card_id}/query", body=dict(body) if body is not None else None)


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


async def cards_dashboards(client: MetabaseClient, card_ids: list[int | str]) -> JSONValue | None:
    return await client.post("/api/cards/dashboards", body={"card_ids": card_ids})


async def get_card_dashboards(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/dashboards")


async def get_card_param_search_values(
    client: MetabaseClient,
    card_id: int | str,
    param_key: str,
    query: str,
) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/search/{query}")


async def get_card_param_values(client: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/values")


async def get_card_param_remapping(client: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/params/{param_key}/remapping")


async def get_card_query_metadata(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/query_metadata")


async def get_card_series(client: MetabaseClient, card_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/card/{card_id}/series")


__all__ = [
    "cards_dashboards",
    "get_card_dashboards",
    "get_card_param_remapping",
    "get_card_param_search_values",
    "get_card_param_values",
    "get_card_query_metadata",
    "get_card_series",
    "pivot_query",
    "query_card",
    "query_card_export",
]
