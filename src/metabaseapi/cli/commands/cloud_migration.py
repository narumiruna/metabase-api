from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import cloud_migration as _raw_cloud_migration


@app.command("create-cloud-migration")
def create_cloud_migration(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Cloud migration JSON object"),
) -> None:
    """Initiate a new cloud migration."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: _raw_cloud_migration.create_cloud_migration(client, payload)))


@app.command("get-cloud-migration")
def get_cloud_migration(ctx: typer.Context) -> None:
    """Get the latest cloud migration, if any."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_cloud_migration.get_cloud_migration(
                client,
            ),
        )
    )


@app.command("cancel-cloud-migration")
def cancel_cloud_migration(ctx: typer.Context) -> None:
    """Cancel any ongoing cloud migrations, if any."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_cloud_migration.cancel_cloud_migration(
                client,
            ),
        )
    )
