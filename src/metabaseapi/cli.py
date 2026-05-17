from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Awaitable
from collections.abc import Callable
from collections.abc import Coroutine

import typer

from metabaseapi import settings
from metabaseapi.client import MetabaseClient
from metabaseapi.errors import MetabaseError
from metabaseapi.models import JSONValue

app = typer.Typer(help="Async Metabase API CLI")


def create_client(
    client_settings: settings.Settings,
) -> MetabaseClient:
    return MetabaseClient.from_settings(client_settings)


def _format_json(payload: JSONValue) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True)


def _build_client_settings(
    *,
    base_url: str | None,
    api_key: str | None,
    timeout_seconds: float,
    verify_ssl: bool,
) -> settings.Settings:
    return settings.load_runtime_settings(
        base_url=base_url,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
        verify_ssl=verify_ssl,
    )


def _configure_logging(verbose: bool) -> None:
    if verbose:
        logging.basicConfig(level=logging.INFO)


def _parse_json_body(raw: str | None) -> JSONValue | None:
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter("Invalid JSON body") from exc


def _parse_json_object(raw: str, parameter_name: str) -> dict[str, object]:
    parsed = _parse_json_body(raw)
    if not isinstance(parsed, dict):
        raise typer.BadParameter(f"{parameter_name} must be a JSON object")
    return parsed


def _parse_optional_json_object(raw: str | None, parameter_name: str) -> dict[str, object] | None:
    if raw is None:
        return None
    return _parse_json_object(raw, parameter_name)


def _parse_optional_json_list(raw: str | None, parameter_name: str) -> list[object] | None:
    if raw is None:
        return None
    parsed = _parse_json_body(raw)
    if not isinstance(parsed, list):
        raise typer.BadParameter(f"{parameter_name} must be a JSON array")
    return parsed


def _run_async(coro: Coroutine[object, object, JSONValue | None]) -> JSONValue | None:
    return asyncio.run(coro)


def _run_and_print(coro: Coroutine[object, object, JSONValue | None]) -> None:
    try:
        result = _run_async(coro)
    except (MetabaseError, ValueError) as exc:
        typer.echo(_format_json({"error": str(exc)}), err=True)
        raise typer.Exit(code=1) from exc

    if result is None:
        typer.echo("null")
    else:
        typer.echo(_format_json(result))


def _get_settings(ctx: typer.Context) -> settings.Settings:
    settings_obj = ctx.obj.get("settings")
    if not isinstance(settings_obj, settings.Settings):
        raise TypeError("CLI settings were not initialized")
    return settings_obj


def _run_client_call(
    ctx: typer.Context,
    call: Callable[[MetabaseClient], Awaitable[JSONValue | None]],
) -> Coroutine[object, object, JSONValue | None]:
    async def do_request() -> JSONValue | None:
        async with create_client(_get_settings(ctx)) as client:
            return await call(client)

    return do_request()


@app.callback()
def configure(
    ctx: typer.Context,
    base_url: str | None = typer.Option(None, "--base-url", "-u", envvar="METABASE_URL"),
    api_key: str | None = typer.Option(None, "--api-key", "-k", envvar="METABASE_API_KEY"),
    timeout_seconds: float = typer.Option(30.0, "--timeout", "-t", envvar="METABASE_TIMEOUT_SECONDS"),
    verify_ssl: bool = typer.Option(True, "--verify/--no-verify", envvar="METABASE_VERIFY_SSL"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable basic logging"),
) -> None:
    _configure_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["settings"] = _build_client_settings(
        base_url=base_url,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
        verify_ssl=verify_ssl,
    )


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


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    _run_and_print(_run_client_call(ctx, lambda client: client.current_user()))


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_databases()))


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_cards()))


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_dashboards()))


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_users()))


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_collections()))


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_tables()))


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_database(database_id)))


@app.command("create-card")
def create_card(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Card name"),
    dataset_query: str = typer.Argument(..., help="Dataset query JSON object"),
    display: str = typer.Option("table", "--display", help="Visualization display type"),
    visualization_settings: str | None = typer.Option(
        None,
        "--visualization-settings",
        help="Visualization settings JSON object",
    ),
    card_type: str | None = typer.Option("question", "--type", help="Card type: question, metric, or model"),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Collection ID"),
    description: str | None = typer.Option(None, "--description", help="Card description"),
    parameters: str | None = typer.Option(None, "--parameters", help="Parameters JSON array"),
    result_metadata: str | None = typer.Option(None, "--result-metadata", help="Result metadata JSON array"),
) -> None:
    """Create a card/question/model."""

    dataset_query_payload = _parse_json_object(dataset_query, "dataset-query")
    visualization_settings_payload = _parse_optional_json_object(
        visualization_settings,
        "visualization-settings",
    )
    parameters_payload = _parse_optional_json_list(parameters, "parameters")
    result_metadata_payload = _parse_optional_json_list(result_metadata, "result-metadata")

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_card(
                name=name,
                dataset_query=dataset_query_payload,
                display=display,
                visualization_settings=visualization_settings_payload,
                card_type=card_type,
                collection_id=collection_id,
                description=description,
                parameters=parameters_payload,
                result_metadata=result_metadata_payload,
            ),
        ),
    )


@app.command("create-question")
def create_question(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Question name"),
    dataset_query: str = typer.Argument(..., help="Dataset query JSON object"),
    display: str = typer.Option("table", "--display", help="Visualization display type"),
    visualization_settings: str | None = typer.Option(
        None,
        "--visualization-settings",
        help="Visualization settings JSON object",
    ),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Collection ID"),
    description: str | None = typer.Option(None, "--description", help="Question description"),
    parameters: str | None = typer.Option(None, "--parameters", help="Parameters JSON array"),
    result_metadata: str | None = typer.Option(None, "--result-metadata", help="Result metadata JSON array"),
) -> None:
    """Create a question."""

    dataset_query_payload = _parse_json_object(dataset_query, "dataset-query")
    visualization_settings_payload = _parse_optional_json_object(
        visualization_settings,
        "visualization-settings",
    )
    parameters_payload = _parse_optional_json_list(parameters, "parameters")
    result_metadata_payload = _parse_optional_json_list(result_metadata, "result-metadata")

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_question(
                name=name,
                dataset_query=dataset_query_payload,
                display=display,
                visualization_settings=visualization_settings_payload,
                collection_id=collection_id,
                description=description,
                parameters=parameters_payload,
                result_metadata=result_metadata_payload,
            ),
        ),
    )


@app.command("get-card")
def get_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Get a card by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_card(card_id)))


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard(dashboard_id)))


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_user(user_id)))


@app.command("get-collection")
def get_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Get a collection by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection(collection_id)))


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_table(table_id)))


@app.command("get-field")
def get_field(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get a field by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_field(field_id)))


@app.command("create-database")
def create_database(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Name of the database to create"),
    engine: str = typer.Argument(..., help="Database engine type"),
    details: str | None = typer.Option(None, "--details", "-d", help="Database details JSON object"),
) -> None:
    """Create a new database."""

    details_payload: dict[str, object] | None
    if details is None:
        details_payload = None
    else:
        parsed = _parse_json_body(details)
        if parsed is not None and not isinstance(parsed, dict):
            raise typer.BadParameter("details must be a JSON object")
        details_payload = parsed

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_database(name=name, engine=engine, details=details_payload),
        ),
    )


if __name__ == "__main__":
    app()
