from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import card as _raw_card


@app.command("pivot-query")
def pivot_query(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query body JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(ctx, lambda client: _raw_card.pivot_query(client, card_id, body=payload))


@app.command("query-card")
def query_card(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(ctx, lambda client: _raw_card.query_card(client, card_id, body=payload))


@app.command("query-card-export")
def query_card_export(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional payload JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(
        ctx,
        lambda client: _raw_card.query_card_export(
            client,
            card_id,
            export_format,
            body=payload,
            pivot_results=pivot_results,
            format_rows=format_rows,
        ),
    )


@app.command("cards-dashboards")
def cards_dashboards(ctx: typer.Context, card_ids: str = typer.Argument(..., help="Comma-separated card IDs")) -> None:
    ids: list[int | str]
    ids = [card_id if not card_id.isdigit() else int(card_id) for card_id in card_ids.split(",") if card_id]
    run_client_command(ctx, lambda client: _raw_card.cards_dashboards(client, ids))


@app.command("get-card-dashboards")
def get_card_dashboards(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_dashboards(client, card_id))


@app.command("get-card-param-search")
def get_card_param_search_values(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_param_search_values(client, card_id, param_key, query))


@app.command("get-card-param-values")
def get_card_param_values(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_param_values(client, card_id, param_key))


@app.command("get-card-param-remapping")
def get_card_param_remapping(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_param_remapping(client, card_id, param_key))


@app.command("get-card-query-metadata")
def get_card_query_metadata(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_query_metadata(client, card_id))


@app.command("get-card-series")
def get_card_series(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_card.get_card_series(client, card_id))
