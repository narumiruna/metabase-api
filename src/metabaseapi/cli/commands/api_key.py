from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("create-api-key")
def create_api_key(ctx: typer.Context, body: str = typer.Argument(..., help="API key JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_api_key(payload)))


@app.command("list-api-keys")
def list_api_keys(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_api_keys()))


@app.command("count-api-keys")
def count_api_keys(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.count_api_keys()))


@app.command("update-api-key")
def update_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...), body: str = typer.Argument(...)) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_api_key(api_key_id, payload)))


@app.command("delete-api-key")
def delete_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_api_key(api_key_id)))


@app.command("regenerate-api-key")
def regenerate_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.regenerate_api_key(api_key_id)))
