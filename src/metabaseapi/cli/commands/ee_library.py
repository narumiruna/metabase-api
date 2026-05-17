from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_library import CreateEeLibraryRequest
from metabaseapi.endpoints.requests.ee_library import GetEeLibraryRequest
from metabaseapi.endpoints.requests.ee_library import GetEeLibraryTreeRequest


@app.command("post-api-ee-library")
def post_api_ee_library(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, CreateEeLibraryRequest())


@app.command("get-api-ee-library")
def get_api_ee_library(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeLibraryRequest())


@app.command("get-api-ee-library-tree")
def get_api_ee_library_tree(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeLibraryTreeRequest())
