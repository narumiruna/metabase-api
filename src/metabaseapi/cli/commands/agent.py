from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.agent import AgentConstructQueryRequest
from metabaseapi.endpoints.requests.agent import AgentExecuteRequest
from metabaseapi.endpoints.requests.agent import AgentPingRequest
from metabaseapi.endpoints.requests.agent import AgentQueryRequest
from metabaseapi.endpoints.requests.agent import AgentSearchRequest
from metabaseapi.endpoints.requests.agent import GetAgentMetricFieldValuesRequest
from metabaseapi.endpoints.requests.agent import GetAgentMetricRequest
from metabaseapi.endpoints.requests.agent import GetAgentTableFieldValuesRequest
from metabaseapi.endpoints.requests.agent import GetAgentTableRequest


@app.command("agent-execute")
def agent_execute(ctx: typer.Context, body: str = typer.Argument(..., help="Agent execute JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: AgentExecuteRequest(body=payload))


@app.command("get-agent-metric")
def get_agent_metric(ctx: typer.Context, metric_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetAgentMetricRequest(metric_id=metric_id))


@app.command("get-agent-metric-field-values")
def get_agent_metric_field_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    run_endpoint_command(ctx, GetAgentMetricFieldValuesRequest(metric_id=metric_id, field_id=field_id))


@app.command("agent-ping")
def agent_ping(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, AgentPingRequest())


@app.command("agent-search")
def agent_search(ctx: typer.Context, body: str = typer.Argument(..., help="Agent search JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: AgentSearchRequest(body=payload))


@app.command("get-agent-table")
def get_agent_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetAgentTableRequest(table_id=table_id))


@app.command("get-agent-table-field-values")
def get_agent_table_field_values(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    run_endpoint_command(ctx, GetAgentTableFieldValuesRequest(table_id=table_id, field_id=field_id))


@app.command("agent-construct-query")
def agent_construct_query(
    ctx: typer.Context, body: str = typer.Argument(..., help="Agent construct-query JSON object")
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: AgentConstructQueryRequest(body=payload))


@app.command("agent-query")
def agent_query(ctx: typer.Context, body: str = typer.Argument(..., help="Agent query JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: AgentQueryRequest(body=payload))
