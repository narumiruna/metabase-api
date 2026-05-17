from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import action as _raw_action


@app.command("list-actions")
def list_actions(ctx: typer.Context, model_id: str | None = typer.Option(None, "--model-id")) -> None:
    """List actions."""

    run_client_command(ctx, lambda client: _raw_action.list_actions(client, model_id=model_id))


@app.command("create-action")
def create_action(ctx: typer.Context, body: str = typer.Argument(..., help="Action JSON object")) -> None:
    """Create an action."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_action.create_action(client, payload))


@app.command("list-public-actions")
def list_public_actions(ctx: typer.Context) -> None:
    """List public actions."""

    run_client_command(
        ctx,
        lambda client: _raw_action.list_public_actions(
            client,
        ),
    )


@app.command("get-action")
def get_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Get an action by ID."""

    run_client_command(ctx, lambda client: _raw_action.get_action(client, action_id))


@app.command("delete-action")
def delete_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action by ID."""

    run_client_command(ctx, lambda client: _raw_action.delete_action(client, action_id))


@app.command("get-action-execute")
def get_action_execute(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Fetch execution parameter values for an action."""

    payload = parse_optional_json_object(parameters, "parameters")
    run_client_command(ctx, lambda client: _raw_action.get_action_execute(client, action_id, parameters=payload))


@app.command("update-action")
def update_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Action JSON object"),
) -> None:
    """Update an action."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_action.update_action(client, action_id, payload))


@app.command("execute-action")
def execute_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Execute an action."""

    payload = parse_optional_json_object(parameters, "parameters")
    run_client_command(ctx, lambda client: _raw_action.execute_action(client, action_id, parameters=payload))


@app.command("create-action-public-link")
def create_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Create an action public link."""

    run_client_command(ctx, lambda client: _raw_action.create_action_public_link(client, action_id))


@app.command("delete-action-public-link")
def delete_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action public link."""

    run_client_command(ctx, lambda client: _raw_action.delete_action_public_link(client, action_id))
