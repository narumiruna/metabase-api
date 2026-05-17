from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_stale import GetEeStaleIdRequest
from metabaseapi.wire import QueryParamValue


@app.command("get-api-ee-stale-id")
def get_api_ee_stale_id(
    ctx: typer.Context,
    stale_id: str = typer.Argument(...),
    before_date: str | None = typer.Option(None, "--before-date"),
    limit: int | None = typer.Option(None, "--limit"),
    offset: int | None = typer.Option(None, "--offset"),
    params: str | None = typer.Option(None, "--params", help="Additional query params JSON object"),
) -> None:
    """Fetch stale entities for a collection-like scope."""

    run_endpoint_command(
        ctx,
        GetEeStaleIdRequest(
            stale_id=stale_id,
            before_date=before_date,
            limit=limit,
            offset=offset,
            params=cast("dict[str, QueryParamValue]", parse_optional_json_object_or_empty(params, "params")),
        ),
    )
