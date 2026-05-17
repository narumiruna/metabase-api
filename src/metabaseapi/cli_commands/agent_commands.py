from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("agent-execute")
def agent_execute(ctx: typer.Context, body: str = typer.Argument(..., help="Agent execute JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_execute(payload)))


@app.command("get-agent-metric")
def get_agent_metric(ctx: typer.Context, metric_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_metric(metric_id)))


@app.command("get-agent-metric-field-values")
def get_agent_metric_field_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_metric_field_values(metric_id, field_id)))


@app.command("agent-ping")
def agent_ping(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_ping()))


@app.command("agent-search")
def agent_search(ctx: typer.Context, body: str = typer.Argument(..., help="Agent search JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_search(payload)))


@app.command("get-agent-table")
def get_agent_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_table(table_id)))


@app.command("get-agent-table-field-values")
def get_agent_table_field_values(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_table_field_values(table_id, field_id)))


@app.command("agent-construct-query")
def agent_construct_query(
    ctx: typer.Context, body: str = typer.Argument(..., help="Agent construct-query JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_construct_query(payload)))


@app.command("agent-query")
def agent_query(ctx: typer.Context, body: str = typer.Argument(..., help="Agent query JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_query(payload)))
