from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.endpoints.requests.user import GetUserRequest
from metabaseapi.endpoints.requests.user import ListUsersRequest


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    run_endpoint_command(ctx, ListUsersRequest())


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    run_endpoint_command(ctx, GetUserRequest(user_id=user_id))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    run_endpoint_command(ctx, CurrentUserRequest())
