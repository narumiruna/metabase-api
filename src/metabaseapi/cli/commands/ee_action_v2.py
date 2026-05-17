from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_action_v2 import EeActionV2ExecuteBulkRequest
from metabaseapi.endpoints.requests.ee_action_v2 import EeActionV2ExecuteFormRequest
from metabaseapi.endpoints.requests.ee_action_v2 import EeActionV2ExecuteRequest


@app.command("ee-action-v2-execute")
def ee_action_v2_execute(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Action v2 execution JSON object"),
) -> None:
    """Execute an EE action v2 with a single input."""

    run_json_body_endpoint_command(ctx, body, lambda payload: EeActionV2ExecuteRequest(body=payload))


@app.command("ee-action-v2-execute-bulk")
def ee_action_v2_execute_bulk(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Action v2 bulk execution JSON object"),
) -> None:
    """Execute an EE action v2 with multiple inputs."""

    run_json_body_endpoint_command(ctx, body, lambda payload: EeActionV2ExecuteBulkRequest(body=payload))


@app.command("ee-action-v2-execute-form")
def ee_action_v2_execute_form(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Action v2 execute-form JSON object"),
) -> None:
    """Describe an EE action v2 execution form."""

    run_json_body_endpoint_command(ctx, body, lambda payload: EeActionV2ExecuteFormRequest(body=payload))
