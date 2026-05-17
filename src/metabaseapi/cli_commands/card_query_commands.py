from __future__ import annotations

import typer

from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("pivot-query")
def pivot_query(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query body JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(_run_client_call(ctx, lambda client: client.pivot_query(card_id, body=payload)))


@app.command("query-card")
def query_card(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(_run_client_call(ctx, lambda client: client.query_card(card_id, body=payload)))


@app.command("query-card-export")
def query_card_export(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional payload JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_card_export(
                card_id,
                export_format,
                body=payload,
                pivot_results=pivot_results,
                format_rows=format_rows,
            ),
        ),
    )


@app.command("cards-dashboards")
def cards_dashboards(ctx: typer.Context, card_ids: str = typer.Argument(..., help="Comma-separated card IDs")) -> None:
    ids: list[int | str]
    ids = [card_id if not card_id.isdigit() else int(card_id) for card_id in card_ids.split(",") if card_id]
    _run_and_print(_run_client_call(ctx, lambda client: client.cards_dashboards(ids)))


@app.command("get-card-dashboards")
def get_card_dashboards(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_dashboards(card_id)))


@app.command("get-card-param-search")
def get_card_param_search_values(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_search_values(card_id, param_key, query)))


@app.command("get-card-param-values")
def get_card_param_values(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_values(card_id, param_key)))


@app.command("get-card-param-remapping")
def get_card_param_remapping(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_remapping(card_id, param_key)))


@app.command("get-card-query-metadata")
def get_card_query_metadata(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_query_metadata(card_id)))


@app.command("get-card-series")
def get_card_series(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_series(card_id)))
