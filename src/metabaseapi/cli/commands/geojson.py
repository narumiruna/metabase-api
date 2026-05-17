from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.geojson import GetGeojsonByKeyRequest
from metabaseapi.endpoints.requests.geojson import GetGeojsonRequest


@app.command("get-geojson")
def get_geojson(ctx: typer.Context, url: str = typer.Option(..., "--url")) -> None:
    run_endpoint_command(ctx, GetGeojsonRequest(url=url))


@app.command("get-geojson-key")
def get_geojson_key(ctx: typer.Context, key: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetGeojsonByKeyRequest(key=key))
