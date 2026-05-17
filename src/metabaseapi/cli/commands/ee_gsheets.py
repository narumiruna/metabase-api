from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_gsheets import CreateEeGsheetsConnectionRequest
from metabaseapi.endpoints.requests.ee_gsheets import DeleteEeGsheetsConnectionRequest
from metabaseapi.endpoints.requests.ee_gsheets import GetEeGsheetsConnectionRequest
from metabaseapi.endpoints.requests.ee_gsheets import GetEeGsheetsServiceAccountRequest
from metabaseapi.endpoints.requests.ee_gsheets import SyncEeGsheetsConnectionRequest


@app.command("post-api-ee-gsheets-connection")
def post_api_ee_gsheets_connection(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Google Sheets connection JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateEeGsheetsConnectionRequest(body=payload))


@app.command("get-api-ee-gsheets-connection")
def get_api_ee_gsheets_connection(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeGsheetsConnectionRequest())


@app.command("delete-api-ee-gsheets-connection")
def delete_api_ee_gsheets_connection(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, DeleteEeGsheetsConnectionRequest())


@app.command("post-api-ee-gsheets-connection-sync")
def post_api_ee_gsheets_connection_sync(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, SyncEeGsheetsConnectionRequest())


@app.command("get-api-ee-gsheets-service-account")
def get_api_ee_gsheets_service_account(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeGsheetsServiceAccountRequest())
