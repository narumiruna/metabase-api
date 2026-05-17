from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_body
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_users()))


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_user(user_id)))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    _run_and_print(_run_client_call(ctx, lambda client: client.current_user()))


@app.command("get-user-key-value-namespace")
def get_user_key_value_namespace(ctx: typer.Context, namespace: str = typer.Argument(...)) -> None:
    """Get all user key-values in a namespace."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_user_key_value_namespace(namespace)))


@app.command("put-user-key-value-namespace-key")
def put_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Value JSON"),
) -> None:
    """Upsert a key-value pair for a namespace."""

    payload = _parse_json_body(body)
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.put_user_key_value_namespace_key(namespace, key, payload),
        )
    )


@app.command("get-user-key-value-namespace-key")
def get_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Get a namespace key-value pair."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_user_key_value_namespace_key(namespace, key)))


@app.command("delete-user-key-value-namespace-key")
def delete_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Delete a namespace key-value pair."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_user_key_value_namespace_key(namespace, key)))
