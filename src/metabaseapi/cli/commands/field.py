from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import field as _raw_field


@app.command("get-field")
def get_field(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get a field by ID."""

    run_client_command(ctx, lambda client: _raw_field.get_field(client, field_id))
