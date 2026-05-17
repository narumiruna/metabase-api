from __future__ import annotations

from collections.abc import Mapping
from typing import cast

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import cache as _raw_cache
from metabaseapi.wire import QueryParamValue


@app.command("get-cache")
def get_cache(
    ctx: typer.Context,
    limit: int | None = typer.Option(None),
    offset: int | None = typer.Option(None),
    sort_column: str | None = typer.Option(None),
    sort_direction: str | None = typer.Option(None),
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_cache.get_cache(
                client,
                limit=limit,
                offset=offset,
                sort_column=sort_column,
                sort_direction=sort_direction,
            ),
        ),
    )


@app.command("put-cache")
def put_cache(ctx: typer.Context, body: str = typer.Argument(..., help="Cache configuration JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: _raw_cache.put_cache(client, payload)))


@app.command("delete-cache")
def delete_cache(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Optional cache delete payload JSON object"),
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_cache.delete_cache(client, payload or None),
        ),
    )


@app.command("invalidate-cache")
def invalidate_cache(
    ctx: typer.Context, params: str = typer.Argument(..., help="Invalidate cache params JSON object")
) -> None:
    payload = _parse_json_object(params, "params")
    normalized = cast("Mapping[str, QueryParamValue]", payload)
    _run_and_print(_run_client_call(ctx, lambda client: _raw_cache.invalidate_cache(client, normalized)))
