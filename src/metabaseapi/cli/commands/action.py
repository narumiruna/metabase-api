from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.action import CreateActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import CreateActionRequest
from metabaseapi.endpoints.requests.action import DeleteActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import DeleteActionRequest
from metabaseapi.endpoints.requests.action import ExecuteActionRequest
from metabaseapi.endpoints.requests.action import GetActionExecuteRequest
from metabaseapi.endpoints.requests.action import GetActionRequest
from metabaseapi.endpoints.requests.action import ListActionsRequest
from metabaseapi.endpoints.requests.action import ListPublicActionsRequest
from metabaseapi.endpoints.requests.action import UpdateActionRequest


@app.command("list-actions")
def list_actions(ctx: typer.Context, model_id: str | None = typer.Option(None, "--model-id")) -> None:
    """List actions."""

    run_endpoint_command(ctx, ListActionsRequest(model_id=model_id))


@app.command("create-action")
def create_action(ctx: typer.Context, body: str = typer.Argument(..., help="Action JSON object")) -> None:
    """Create an action."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateActionRequest(body=payload))


@app.command("list-public-actions")
def list_public_actions(ctx: typer.Context) -> None:
    """List public actions."""

    run_endpoint_command(ctx, ListPublicActionsRequest())


@app.command("get-action")
def get_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Get an action by ID."""

    run_endpoint_command(ctx, GetActionRequest(action_id=action_id))


@app.command("delete-action")
def delete_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action by ID."""

    run_endpoint_command(ctx, DeleteActionRequest(action_id=action_id))


@app.command("get-action-execute")
def get_action_execute(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Fetch execution parameter values for an action."""

    payload = parse_optional_json_object(parameters, "parameters")
    run_endpoint_command(ctx, GetActionExecuteRequest(action_id=action_id, parameters=payload or {}))


@app.command("update-action")
def update_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Action JSON object"),
) -> None:
    """Update an action."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateActionRequest(action_id=action_id, body=payload))


@app.command("execute-action")
def execute_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Execute an action."""

    payload = parse_optional_json_object(parameters, "parameters")
    run_endpoint_command(ctx, ExecuteActionRequest(action_id=action_id, parameters=payload or {}))


@app.command("create-action-public-link")
def create_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Create an action public link."""

    run_endpoint_command(ctx, CreateActionPublicLinkRequest(action_id=action_id))


@app.command("delete-action-public-link")
def delete_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action public link."""

    run_endpoint_command(ctx, DeleteActionPublicLinkRequest(action_id=action_id))
