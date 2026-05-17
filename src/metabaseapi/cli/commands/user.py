from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.user import CreateUserPasswordResetUrlRequest
from metabaseapi.endpoints.requests.user import CreateUserRequest
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.endpoints.requests.user import DeleteUserRequest
from metabaseapi.endpoints.requests.user import GetUserRecipientsRequest
from metabaseapi.endpoints.requests.user import GetUserRequest
from metabaseapi.endpoints.requests.user import ListUsersRequest
from metabaseapi.endpoints.requests.user import ReactivateUserRequest
from metabaseapi.endpoints.requests.user import UpdateUserModalRequest
from metabaseapi.endpoints.requests.user import UpdateUserPasswordRequest
from metabaseapi.endpoints.requests.user import UpdateUserRequest


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    run_endpoint_command(ctx, ListUsersRequest())


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    run_endpoint_command(ctx, GetUserRequest(user_id=user_id))


@app.command("create-user")
def create_user(ctx: typer.Context, body: str = typer.Argument(..., help="User JSON object")) -> None:
    """Create a user."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateUserRequest(body=payload))


@app.command("list-user-recipients")
def list_user_recipients(ctx: typer.Context) -> None:
    """List active user recipients."""

    run_endpoint_command(ctx, GetUserRecipientsRequest())


@app.command("update-user")
def update_user(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="User update JSON object"),
) -> None:
    """Update a user."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateUserRequest(user_id=user_id, body=payload))


@app.command("delete-user")
def delete_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Disable a user."""

    run_endpoint_command(ctx, DeleteUserRequest(user_id=user_id))


@app.command("update-user-modal")
def update_user_modal(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    modal: str = typer.Argument(...),
) -> None:
    """Mark a modal as seen for a user."""

    run_endpoint_command(ctx, UpdateUserModalRequest(user_id=user_id, modal=modal))


@app.command("update-user-password")
def update_user_password(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Password update JSON object"),
) -> None:
    """Update a user's password."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateUserPasswordRequest(user_id=user_id, body=payload))


@app.command("create-user-password-reset-url")
def create_user_password_reset_url(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Generate a password reset URL for a user."""

    run_endpoint_command(ctx, CreateUserPasswordResetUrlRequest(user_id=user_id))


@app.command("reactivate-user")
def reactivate_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Reactivate a user."""

    run_endpoint_command(ctx, ReactivateUserRequest(user_id=user_id))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    run_endpoint_command(ctx, CurrentUserRequest())
