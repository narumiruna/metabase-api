from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.mt_gtap import DeleteMtGtapIdRequest
from metabaseapi.endpoints.requests.mt_gtap import GetMtGtapIdRequest
from metabaseapi.endpoints.requests.mt_gtap import GetMtGtapRequest
from metabaseapi.endpoints.requests.mt_gtap import PostMtGtapRequest
from metabaseapi.endpoints.requests.mt_gtap import PostMtGtapValidateRequest
from metabaseapi.endpoints.requests.mt_gtap import PutMtGtapIdRequest


@app.command("get-api-mt-gtap")
def get_api_mt_gtap(
    ctx: typer.Context,
    group_id: str | None = typer.Option(None, "--group-id"),
    table_id: str | None = typer.Option(None, "--table-id"),
) -> None:
    """List GTAPs or fetch one by group and table IDs."""

    run_endpoint_command(ctx, GetMtGtapRequest(group_id=group_id, table_id=table_id))


@app.command("post-api-mt-gtap")
def post_api_mt_gtap(ctx: typer.Context, body: str = typer.Argument(..., help="GTAP JSON object")) -> None:
    """Create a GTAP."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostMtGtapRequest(body=payload))


@app.command("post-api-mt-gtap-validate")
def post_api_mt_gtap_validate(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="GTAP validation JSON object"),
) -> None:
    """Validate a GTAP sandbox."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostMtGtapValidateRequest(body=payload))


@app.command("get-api-mt-gtap-id")
def get_api_mt_gtap_id(ctx: typer.Context, gtap_id: str = typer.Argument(...)) -> None:
    """Fetch a GTAP."""

    run_endpoint_command(ctx, GetMtGtapIdRequest(gtap_id=gtap_id))


@app.command("put-api-mt-gtap-id")
def put_api_mt_gtap_id(
    ctx: typer.Context,
    gtap_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="GTAP update JSON object"),
) -> None:
    """Update a GTAP."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutMtGtapIdRequest(gtap_id=gtap_id, body=payload))


@app.command("delete-api-mt-gtap-id")
def delete_api_mt_gtap_id(ctx: typer.Context, gtap_id: str = typer.Argument(...)) -> None:
    """Delete a GTAP."""

    run_endpoint_command(ctx, DeleteMtGtapIdRequest(gtap_id=gtap_id))
