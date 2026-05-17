from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_dashboard_params_valid_filter_fields(
    client: MetabaseClient,
    *,
    filtered: list[int | str] | None = None,
    filtering: list[int | str] | None = None,
) -> JSONValue | None:
    params: dict[str, QueryParamValue] = {}
    if filtered is not None:
        params["filtered"] = list(filtered)
    if filtering is not None:
        params["filtering"] = list(filtering)
    return await client.get("/api/dashboard/params/valid-filter-fields", params=params or None)


async def query_dashboard_card(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    card_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(
        f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query",
        body=dict(body) if body is not None else None,
    )


async def query_dashboard_card_export(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
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
        f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query/{export_format}",
        body=dict(body) if body is not None else None,
        params=params or None,
    )


async def query_dashboard_card_pivot(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    card_id: int | str,
    body: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(
        f"/api/dashboard/pivot/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query",
        body=dict(body) if body is not None else None,
    )


async def get_dashboard_dashcard_execute(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    *,
    parameters: Mapping[str, QueryParamValue] | None = None,
) -> JSONValue | None:
    return await client.get(
        f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/execute",
        params=parameters,
    )


async def execute_dashboard_dashcard(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    *,
    parameters: Mapping[str, object] | None = None,
) -> JSONValue | None:
    return await client.post(
        f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/execute",
        body={"parameters": dict(parameters or {})},
    )


async def get_dashboard_param_remapping(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    *,
    parameters: Mapping[str, QueryParamValue] | None = None,
) -> JSONValue | None:
    return await client.get(
        f"/api/dashboard/{dashboard_id}/params/{param_key}/remapping",
        params=parameters,
    )


async def get_dashboard_param_search_values(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    query: str,
    *,
    parameters: Mapping[str, QueryParamValue] | None = None,
) -> JSONValue | None:
    return await client.get(
        f"/api/dashboard/{dashboard_id}/params/{param_key}/search/{query}",
        params=parameters,
    )


async def get_dashboard_param_values(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    *,
    parameters: Mapping[str, QueryParamValue] | None = None,
) -> JSONValue | None:
    return await client.get(
        f"/api/dashboard/{dashboard_id}/params/{param_key}/values",
        params=parameters,
    )


async def get_dashboard_query_metadata(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/dashboard/{dashboard_id}/query_metadata")


async def get_dashboard_related(client: MetabaseClient, dashboard_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/dashboard/{dashboard_id}/related")


__all__ = [
    "execute_dashboard_dashcard",
    "get_dashboard_dashcard_execute",
    "get_dashboard_param_remapping",
    "get_dashboard_param_search_values",
    "get_dashboard_param_values",
    "get_dashboard_params_valid_filter_fields",
    "get_dashboard_query_metadata",
    "get_dashboard_related",
    "query_dashboard_card",
    "query_dashboard_card_export",
    "query_dashboard_card_pivot",
]
