from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Coroutine
from typing import Annotated

import typer

from . import settings
from .client import MetabaseClient
from .errors import MetabaseError
from .models import JSONValue
from .models import get_request_model

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


def _parse_key_value_pairs(values: list[str] | None) -> dict[str, str | int | bool | float | None]:
    pairs: dict[str, str | int | bool | float | None] = {}
    if values is None:
        return pairs
    for item in values:
        if "=" not in item:
            raise typer.BadParameter(f"Invalid parameter format: {item}, expected key=value")
        key, value = item.split("=", 1)
        pairs[key] = value
    return pairs


def _parse_json_body(raw: str | None) -> JSONValue | None:
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter("Invalid JSON body") from exc


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


def _run_raw_request(
    client_settings: settings.Settings,
    method: str,
    path: str,
    query: list[str] | None,
    body: str | None,
) -> Coroutine[object, object, JSONValue | None]:
    params = _parse_key_value_pairs(query)
    payload = _parse_json_body(body)

    request_model = get_request_model(method, path)
    api_request = request_model(method=method, path=path, params=params, body=payload)
    if api_request.method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        raise typer.BadParameter("method must be GET, POST, PUT, PATCH, or DELETE")

    async def do_request() -> JSONValue | None:
        async with create_client(client_settings) as client:
            return await client.request(
                api_request.method,
                api_request.path,
                params=api_request.params,
                json_data=api_request.body,
            )

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


@app.command()
def request(
    ctx: typer.Context,
    method: str = typer.Argument(..., help="HTTP method (GET, POST, PUT, PATCH, DELETE)"),
    path: str = typer.Argument(..., help="API path or absolute URL"),
    query: Annotated[
        list[str] | None, typer.Option("--query", "-q", help="Repeatable key=value query parameters")
    ] = None,
    body: Annotated[str | None, typer.Option("--body", "-b", help="Raw JSON body for POST/PUT requests")] = None,
) -> None:
    """Send a raw Metabase HTTP request."""

    client_settings = _get_settings(ctx)
    _run_and_print(_run_raw_request(client_settings, method, path, query, body))


@app.command("invoke")
def invoke(
    ctx: typer.Context,
    method: str = typer.Argument(..., help="HTTP method (GET, POST, PUT, PATCH, DELETE)"),
    path: str = typer.Argument(..., help="API path or absolute URL"),
    query: Annotated[
        list[str] | None, typer.Option("--query", "-q", help="Repeatable key=value query parameters")
    ] = None,
    body: Annotated[str | None, typer.Option("--body", "-b", help="Raw JSON body for POST/PUT requests")] = None,
) -> None:
    """Generic API invoke command for structured endpoint calls."""

    client_settings = _get_settings(ctx)
    _run_and_print(_run_raw_request(client_settings, method, path, query, body))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    async def do_request() -> JSONValue:
        async with create_client(_get_settings(ctx)) as client:
            return await client.current_user()

    _run_and_print(do_request())


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", "/api/database", None, None))


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", "/api/card", None, None))


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", "/api/user", None, None))


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", "/api/collection", None, None))


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: int = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    async def do_request() -> JSONValue:
        async with create_client(_get_settings(ctx)) as client:
            return await client.get_dashboard(dashboard_id)

    _run_and_print(do_request())


@app.command("get-card")
def get_card(ctx: typer.Context, card_id: int = typer.Argument(...)) -> None:
    """Get a card by ID."""

    async def do_request() -> JSONValue:
        async with create_client(_get_settings(ctx)) as client:
            return await client.get_card(card_id)

    _run_and_print(do_request())


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: int = typer.Argument(...)) -> None:
    """Get a user by ID."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", f"/api/user/{user_id}", None, None))


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: int = typer.Argument(...)) -> None:
    """Get a table by ID."""

    _run_and_print(_run_raw_request(_get_settings(ctx), "GET", f"/api/table/{table_id}", None, None))


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: int = typer.Argument(...)) -> None:
    """Get a database by ID."""

    async def do_request() -> JSONValue:
        async with create_client(_get_settings(ctx)) as client:
            return await client.get(f"/api/database/{database_id}")

    _run_and_print(do_request())


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

    body: dict[str, object] = {"name": name, "engine": engine}
    if details_payload is not None:
        body["details"] = details_payload

    async def do_request() -> JSONValue:
        async with create_client(_get_settings(ctx)) as client:
            return await client.post("/api/database", body=body)

    _run_and_print(do_request())


if __name__ == "__main__":
    app()
