from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import user as _raw_user


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    run_client_command(
        ctx,
        lambda client: _raw_user.list_users(
            client,
        ),
    )


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    run_client_command(ctx, lambda client: _raw_user.get_user(client, user_id))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    run_client_command(
        ctx,
        lambda client: _raw_user.current_user(
            client,
        ),
    )

