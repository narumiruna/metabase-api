from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.cloud_migration import CancelCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import CreateCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import GetCloudMigrationRequest


@app.command("create-cloud-migration")
def create_cloud_migration(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Cloud migration JSON object"),
) -> None:
    """Initiate a new cloud migration."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, CreateCloudMigrationRequest(body=payload))


@app.command("get-cloud-migration")
def get_cloud_migration(ctx: typer.Context) -> None:
    """Get the latest cloud migration, if any."""

    run_endpoint_command(ctx, GetCloudMigrationRequest())


@app.command("cancel-cloud-migration")
def cancel_cloud_migration(ctx: typer.Context) -> None:
    """Cancel any ongoing cloud migrations, if any."""

    run_endpoint_command(ctx, CancelCloudMigrationRequest())
