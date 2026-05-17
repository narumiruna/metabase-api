from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _parse_optional_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("list-actions")
def list_actions(ctx: typer.Context, model_id: str | None = typer.Option(None, "--model-id")) -> None:
    """List actions."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_actions(model_id=model_id)))


@app.command("create-action")
def create_action(ctx: typer.Context, body: str = typer.Argument(..., help="Action JSON object")) -> None:
    """Create an action."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_action(payload)))


@app.command("list-public-actions")
def list_public_actions(ctx: typer.Context) -> None:
    """List public actions."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_public_actions()))


@app.command("get-action")
def get_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Get an action by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_action(action_id)))


@app.command("delete-action")
def delete_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_action(action_id)))


@app.command("get-action-execute")
def get_action_execute(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Fetch execution parameter values for an action."""

    payload = _parse_optional_json_object(parameters, "parameters")
    _run_and_print(_run_client_call(ctx, lambda client: client.get_action_execute(action_id, parameters=payload)))


@app.command("update-action")
def update_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Action JSON object"),
) -> None:
    """Update an action."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_action(action_id, payload)))


@app.command("execute-action")
def execute_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Execute an action."""

    payload = _parse_optional_json_object(parameters, "parameters")
    _run_and_print(_run_client_call(ctx, lambda client: client.execute_action(action_id, parameters=payload)))


@app.command("create-action-public-link")
def create_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Create an action public link."""

    _run_and_print(_run_client_call(ctx, lambda client: client.create_action_public_link(action_id)))


@app.command("delete-action-public-link")
def delete_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action public link."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_action_public_link(action_id)))


@app.command("list-bookmarks")
def list_bookmarks(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_bookmarks()))


@app.command("update-bookmark-ordering")
def update_bookmark_ordering(
    ctx: typer.Context, body: str = typer.Argument(..., help="Bookmark ordering JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_bookmark_ordering(payload)))


@app.command("create-bookmark")
def create_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.create_bookmark(model, item_id)))


@app.command("delete-bookmark")
def delete_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_bookmark(model, item_id)))
