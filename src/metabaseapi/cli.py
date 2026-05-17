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


def _register_commands() -> None:
    import metabaseapi.cli_commands_core
    import metabaseapi.cli_commands_dashboard  # noqa: F401


_register_commands()

if __name__ == "__main__":
    app()
