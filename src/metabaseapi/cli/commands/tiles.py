from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.tiles import GetAdHocQueryTileRequest
from metabaseapi.endpoints.requests.tiles import GetDashboardCardTileRequest
from metabaseapi.endpoints.requests.tiles import GetSavedCardTileRequest


@app.command("get-tiles-card")
def get_tiles_card(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
    lat_field: str = typer.Option(..., "--lat-field"),
    lon_field: str = typer.Option(..., "--lon-field"),
    parameters: str | None = typer.Option(None, "--parameters", help="JSON-encoded parameter array"),
) -> None:
    run_endpoint_command(
        ctx,
        GetSavedCardTileRequest(
            card_id=card_id,
            zoom=zoom,
            x=x,
            y=y,
            lat_field=lat_field,
            lon_field=lon_field,
            parameters=parameters,
        ),
    )


@app.command("get-tiles-dashboard-card")
def get_tiles_dashboard_card(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
    lat_field: str = typer.Option(..., "--lat-field"),
    lon_field: str = typer.Option(..., "--lon-field"),
    parameters: str | None = typer.Option(None, "--parameters", help="JSON-encoded parameter array"),
) -> None:
    run_endpoint_command(
        ctx,
        GetDashboardCardTileRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            card_id=card_id,
            zoom=zoom,
            x=x,
            y=y,
            lat_field=lat_field,
            lon_field=lon_field,
            parameters=parameters,
        ),
    )


@app.command("get-tiles-query")
def get_tiles_query(
    ctx: typer.Context,
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
    query: str = typer.Option(..., "--query", help="JSON-encoded MBQL query"),
    lat_field: str = typer.Option(..., "--lat-field"),
    lon_field: str = typer.Option(..., "--lon-field"),
) -> None:
    run_endpoint_command(
        ctx,
        GetAdHocQueryTileRequest(
            zoom=zoom,
            x=x,
            y=y,
            query=query,
            lat_field=lat_field,
            lon_field=lon_field,
        ),
    )
