from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_body
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.user_key_value import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceRequest
from metabaseapi.endpoints.requests.user_key_value import PutUserKeyValueNamespaceKeyRequest


@app.command("get-user-key-value-namespace")
def get_user_key_value_namespace(ctx: typer.Context, namespace: str = typer.Argument(...)) -> None:
    """Get all user key-values in a namespace."""

    run_endpoint_command(ctx, GetUserKeyValueNamespaceRequest(namespace=namespace))


@app.command("put-user-key-value-namespace-key")
def put_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Value JSON"),
) -> None:
    """Upsert a key-value pair for a namespace."""

    payload = parse_json_body(body)
    run_endpoint_command(ctx, PutUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key, body=payload))


@app.command("get-user-key-value-namespace-key")
def get_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Get a namespace key-value pair."""

    run_endpoint_command(ctx, GetUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key))


@app.command("delete-user-key-value-namespace-key")
def delete_user_key_value_namespace_key(
    ctx: typer.Context,
    namespace: str = typer.Argument(...),
    key: str = typer.Argument(...),
) -> None:
    """Delete a namespace key-value pair."""

    run_endpoint_command(ctx, DeleteUserKeyValueNamespaceKeyRequest(namespace=namespace, key=key))
