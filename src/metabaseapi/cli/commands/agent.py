from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import agent as _raw_agent


@app.command("agent-execute")
def agent_execute(ctx: typer.Context, body: str = typer.Argument(..., help="Agent execute JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_agent.agent_execute(client, payload))


@app.command("get-agent-metric")
def get_agent_metric(ctx: typer.Context, metric_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_agent.get_agent_metric(client, metric_id))


@app.command("get-agent-metric-field-values")
def get_agent_metric_field_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    run_client_command(ctx, lambda client: _raw_agent.get_agent_metric_field_values(client, metric_id, field_id))


@app.command("agent-ping")
def agent_ping(ctx: typer.Context) -> None:
    run_client_command(
        ctx,
        lambda client: _raw_agent.agent_ping(
            client,
        ),
    )


@app.command("agent-search")
def agent_search(ctx: typer.Context, body: str = typer.Argument(..., help="Agent search JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_agent.agent_search(client, payload))


@app.command("get-agent-table")
def get_agent_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_agent.get_agent_table(client, table_id))


@app.command("get-agent-table-field-values")
def get_agent_table_field_values(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    run_client_command(ctx, lambda client: _raw_agent.get_agent_table_field_values(client, table_id, field_id))


@app.command("agent-construct-query")
def agent_construct_query(
    ctx: typer.Context, body: str = typer.Argument(..., help="Agent construct-query JSON object")
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_agent.agent_construct_query(client, payload))


@app.command("agent-query")
def agent_query(ctx: typer.Context, body: str = typer.Argument(..., help="Agent query JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_agent.agent_query(client, payload))
