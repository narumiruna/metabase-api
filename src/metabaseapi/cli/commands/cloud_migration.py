from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import cloud_migration as _raw_cloud_migration


@app.command("create-cloud-migration")
def create_cloud_migration(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Cloud migration JSON object"),
) -> None:
    """Initiate a new cloud migration."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_cloud_migration.create_cloud_migration(client, payload))


@app.command("get-cloud-migration")
def get_cloud_migration(ctx: typer.Context) -> None:
    """Get the latest cloud migration, if any."""

    run_client_command(
        ctx,
        lambda client: _raw_cloud_migration.get_cloud_migration(
            client,
        ),
    )


@app.command("cancel-cloud-migration")
def cancel_cloud_migration(ctx: typer.Context) -> None:
    """Cancel any ongoing cloud migrations, if any."""

    run_client_command(
        ctx,
        lambda client: _raw_cloud_migration.cancel_cloud_migration(
            client,
        ),
    )
