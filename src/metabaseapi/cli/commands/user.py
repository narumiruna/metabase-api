from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_body
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import user as _raw_user
from metabaseapi.client.raw import user_key_value as _raw_user_key_value


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


@app.command("get-user-key-value-namespace")
def get_user_key_value_namespace(ctx: typer.Context, namespace: str = typer.Argument(...)) -> None:
    """Get all user key-values in a namespace."""

    run_client_command(ctx, lambda client: _raw_user_key_value.get_user_key_value_namespace(client, namespace))


@app.command("put-user-key-value-namespace-key")
def put_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Value JSON"),
) -> None:
    """Upsert a key-value pair for a namespace."""

    payload = parse_json_body(body)
    run_client_command(
        ctx,
        lambda client: _raw_user_key_value.put_user_key_value_namespace_key(client, namespace, key, payload),
    )


@app.command("get-user-key-value-namespace-key")
def get_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Get a namespace key-value pair."""

    run_client_command(ctx, lambda client: _raw_user_key_value.get_user_key_value_namespace_key(client, namespace, key))


@app.command("delete-user-key-value-namespace-key")
def delete_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Delete a namespace key-value pair."""

    run_client_command(
        ctx, lambda client: _raw_user_key_value.delete_user_key_value_namespace_key(client, namespace, key)
    )
