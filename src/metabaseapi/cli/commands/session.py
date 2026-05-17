from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.session import CreateSessionRequest
from metabaseapi.endpoints.requests.session import DeleteSessionRequest
from metabaseapi.endpoints.requests.session import ForgotPasswordRequest
from metabaseapi.endpoints.requests.session import GetSessionPropertiesRequest
from metabaseapi.endpoints.requests.session import GoogleAuthRequest
from metabaseapi.endpoints.requests.session import PasswordCheckRequest
from metabaseapi.endpoints.requests.session import PasswordResetTokenValidRequest
from metabaseapi.endpoints.requests.session import ResetPasswordRequest


@app.command("login")
def login(ctx: typer.Context, body: str = typer.Argument(..., help="Session login JSON object")) -> None:
    """Login."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateSessionRequest(body=payload))


@app.command("logout")
def logout(ctx: typer.Context) -> None:
    """Logout."""

    run_endpoint_command(ctx, DeleteSessionRequest())


@app.command("forgot-password")
def forgot_password(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Forgot password JSON object"),
) -> None:
    """Send a password reset email."""

    run_json_body_endpoint_command(ctx, body, lambda payload: ForgotPasswordRequest(body=payload))


@app.command("google-auth")
def google_auth(ctx: typer.Context, body: str = typer.Argument(..., help="Google auth JSON object")) -> None:
    """Login with Google Auth."""

    run_json_body_endpoint_command(ctx, body, lambda payload: GoogleAuthRequest(body=payload))


@app.command("check-password")
def check_password(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Password check JSON object"),
) -> None:
    """Check password complexity."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PasswordCheckRequest(body=payload))


@app.command("validate-password-reset-token")
def validate_password_reset_token(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    """Check whether a password reset token is valid."""

    run_endpoint_command(ctx, PasswordResetTokenValidRequest(token=token))


@app.command("get-session-properties")
def get_session_properties(ctx: typer.Context) -> None:
    """Get session-readable properties."""

    run_endpoint_command(ctx, GetSessionPropertiesRequest())


@app.command("reset-password")
def reset_password(ctx: typer.Context, body: str = typer.Argument(..., help="Password reset JSON object")) -> None:
    """Reset password with a reset token."""

    run_json_body_endpoint_command(ctx, body, lambda payload: ResetPasswordRequest(body=payload))
