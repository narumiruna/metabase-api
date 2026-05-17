from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.native_query_snippet import CreateNativeQuerySnippetRequest
from metabaseapi.endpoints.requests.native_query_snippet import GetNativeQuerySnippetRequest
from metabaseapi.endpoints.requests.native_query_snippet import ListNativeQuerySnippetsRequest
from metabaseapi.endpoints.requests.native_query_snippet import UpdateNativeQuerySnippetRequest


@app.command("list-native-query-snippets")
def list_native_query_snippets(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListNativeQuerySnippetsRequest())


@app.command("create-native-query-snippet")
def create_native_query_snippet(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Native query snippet JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateNativeQuerySnippetRequest(body=payload))


@app.command("get-native-query-snippet")
def get_native_query_snippet(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetNativeQuerySnippetRequest(id=id))


@app.command("update-native-query-snippet")
def update_native_query_snippet(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Native query snippet JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateNativeQuerySnippetRequest(id=id, body=payload))
