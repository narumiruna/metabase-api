from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.api_key import CountApiKeysRequest
from metabaseapi.endpoints.requests.api_key import CreateApiKeyRequest
from metabaseapi.endpoints.requests.api_key import DeleteApiKeyRequest
from metabaseapi.endpoints.requests.api_key import ListApiKeysRequest
from metabaseapi.endpoints.requests.api_key import RegenerateApiKeyRequest
from metabaseapi.endpoints.requests.api_key import UpdateApiKeyRequest


@app.command("create-api-key")
def create_api_key(ctx: typer.Context, body: str = typer.Argument(..., help="API key JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, CreateApiKeyRequest(body=payload))


@app.command("list-api-keys")
def list_api_keys(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListApiKeysRequest())


@app.command("count-api-keys")
def count_api_keys(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, CountApiKeysRequest())


@app.command("update-api-key")
def update_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...), body: str = typer.Argument(...)) -> None:
    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, UpdateApiKeyRequest(api_key_id=api_key_id, body=payload))


@app.command("delete-api-key")
def delete_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DeleteApiKeyRequest(api_key_id=api_key_id))


@app.command("regenerate-api-key")
def regenerate_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, RegenerateApiKeyRequest(api_key_id=api_key_id))
