from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_advanced_permissions import DeleteEeImpersonationRequest
from metabaseapi.endpoints.requests.ee_advanced_permissions import GetEeApplicationPermissionsGraphRequest
from metabaseapi.endpoints.requests.ee_advanced_permissions import GetEeImpersonationRequest
from metabaseapi.endpoints.requests.ee_advanced_permissions import PutEeApplicationPermissionsGraphRequest


@app.command("get-ee-advanced-permissions-application-graph")
def get_ee_advanced_permissions_application_graph(ctx: typer.Context) -> None:
    """Fetch the EE application permissions graph."""

    run_endpoint_command(ctx, GetEeApplicationPermissionsGraphRequest())


@app.command("put-ee-advanced-permissions-application-graph")
def put_ee_advanced_permissions_application_graph(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Application permissions graph JSON object"),
    skip_graph: bool | None = typer.Option(None, "--skip-graph/--no-skip-graph"),
    force: bool | None = typer.Option(None, "--force/--no-force"),
) -> None:
    """Update the EE application permissions graph."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutEeApplicationPermissionsGraphRequest(body=payload, skip_graph=skip_graph, force=force),
    )


@app.command("get-ee-advanced-permissions-impersonation")
def get_ee_advanced_permissions_impersonation(
    ctx: typer.Context,
    group_id: str | None = typer.Option(None, "--group-id"),
    db_id: str | None = typer.Option(None, "--db-id"),
) -> None:
    """Fetch EE connection impersonation policies."""

    run_endpoint_command(ctx, GetEeImpersonationRequest(group_id=group_id, db_id=db_id))


@app.command("delete-ee-advanced-permissions-impersonation")
def delete_ee_advanced_permissions_impersonation(
    ctx: typer.Context,
    impersonation_id: str = typer.Argument(...),
) -> None:
    """Delete an EE connection impersonation policy."""

    run_endpoint_command(ctx, DeleteEeImpersonationRequest(impersonation_id=impersonation_id))
