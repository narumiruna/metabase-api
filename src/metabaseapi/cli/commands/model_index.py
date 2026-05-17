from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.model_index import CreateModelIndexRequest
from metabaseapi.endpoints.requests.model_index import DeleteModelIndexRequest
from metabaseapi.endpoints.requests.model_index import GetModelIndexRequest
from metabaseapi.endpoints.requests.model_index import ListModelIndexesRequest


@app.command("create-model-index")
def create_model_index(ctx: typer.Context, body: str = typer.Argument(..., help="Model index JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateModelIndexRequest(body=payload))


@app.command("list-model-indexes")
def list_model_indexes(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListModelIndexesRequest())


@app.command("get-model-index")
def get_model_index(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetModelIndexRequest(id=id))


@app.command("delete-model-index")
def delete_model_index(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DeleteModelIndexRequest(id=id))
