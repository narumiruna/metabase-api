from __future__ import annotations

from collections.abc import Mapping
from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.cache import DeleteCacheRequest
from metabaseapi.endpoints.requests.cache import GetCacheRequest
from metabaseapi.endpoints.requests.cache import InvalidateCacheRequest
from metabaseapi.endpoints.requests.cache import PutCacheRequest
from metabaseapi.wire import QueryParamValue


@app.command("get-cache")
def get_cache(
    ctx: typer.Context,
    limit: int | None = typer.Option(None),
    offset: int | None = typer.Option(None),
    sort_column: str | None = typer.Option(None),
    sort_direction: str | None = typer.Option(None),
) -> None:
    run_endpoint_command(
        ctx,
        GetCacheRequest(
            limit=limit,
            offset=offset,
            sort_column=sort_column,
            sort_direction=sort_direction,
        ),
    )


@app.command("put-cache")
def put_cache(ctx: typer.Context, body: str = typer.Argument(..., help="Cache configuration JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: PutCacheRequest(body=payload))


@app.command("delete-cache")
def delete_cache(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Optional cache delete payload JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: DeleteCacheRequest(body=payload))


@app.command("invalidate-cache")
def invalidate_cache(
    ctx: typer.Context, params: str = typer.Argument(..., help="Invalidate cache params JSON object")
) -> None:
    payload = parse_json_object(params, "params")
    normalized = dict(cast("Mapping[str, QueryParamValue]", payload))
    run_endpoint_command(ctx, InvalidateCacheRequest(params=normalized))
