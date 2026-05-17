from __future__ import annotations

from collections.abc import Mapping
from typing import cast

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app
from metabaseapi.models import QueryParamValue


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
            lambda client: client.get_cache(
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
    _run_and_print(_run_client_call(ctx, lambda client: client.put_cache(payload)))


@app.command("delete-cache")
def delete_cache(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Optional cache delete payload JSON object"),
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.delete_cache(payload or None),
        ),
    )


@app.command("invalidate-cache")
def invalidate_cache(
    ctx: typer.Context, params: str = typer.Argument(..., help="Invalidate cache params JSON object")
) -> None:
    payload = _parse_json_object(params, "params")
    normalized = cast("Mapping[str, QueryParamValue]", payload)
    _run_and_print(_run_client_call(ctx, lambda client: client.invalidate_cache(normalized)))
