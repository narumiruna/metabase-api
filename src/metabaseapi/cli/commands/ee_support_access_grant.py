from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_support_access_grant import GetEeSupportAccessGrantCurrentRequest
from metabaseapi.endpoints.requests.ee_support_access_grant import GetEeSupportAccessGrantRequest
from metabaseapi.endpoints.requests.ee_support_access_grant import PostEeSupportAccessGrantRequest
from metabaseapi.endpoints.requests.ee_support_access_grant import PutEeSupportAccessGrantIdRevokeRequest
from metabaseapi.wire import QueryParamValue


@app.command("post-api-ee-support-access-grant")
def post_api_ee_support_access_grant(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Support access grant JSON object"),
) -> None:
    """Create a support access grant."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostEeSupportAccessGrantRequest(body=payload))


@app.command("get-api-ee-support-access-grant")
def get_api_ee_support_access_grant(
    ctx: typer.Context,
    ticket_number: str | None = typer.Option(None, "--ticket-number"),
    status: str | None = typer.Option(None, "--status"),
    limit: int | None = typer.Option(None, "--limit"),
    offset: int | None = typer.Option(None, "--offset"),
    params: str | None = typer.Option(None, "--params", help="Additional query params JSON object"),
) -> None:
    """List support access grants."""

    run_endpoint_command(
        ctx,
        GetEeSupportAccessGrantRequest(
            ticket_number=ticket_number,
            status=status,
            limit=limit,
            offset=offset,
            params=cast("dict[str, QueryParamValue]", parse_optional_json_object_or_empty(params, "params")),
        ),
    )


@app.command("get-api-ee-support-access-grant-current")
def get_api_ee_support_access_grant_current(ctx: typer.Context) -> None:
    """Fetch the current support access grant."""

    run_endpoint_command(ctx, GetEeSupportAccessGrantCurrentRequest())


@app.command("put-api-ee-support-access-grant-id-revoke")
def put_api_ee_support_access_grant_id_revoke(
    ctx: typer.Context,
    grant_id: str = typer.Argument(...),
) -> None:
    """Revoke a support access grant."""

    run_endpoint_command(ctx, PutEeSupportAccessGrantIdRevokeRequest(grant_id=grant_id))
