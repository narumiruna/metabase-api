from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from collections.abc import Coroutine
from typing import cast

import typer
from pydantic import BaseModel

from metabaseapi import settings
from metabaseapi.cli.error_adapter import error_payload
from metabaseapi.cli.output import render_payload
from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.errors import MetabaseError
from metabaseapi.wire import JSONValue

app = typer.Typer(help="Async Metabase API CLI")


def create_client(
    client_settings: settings.Settings,
) -> MetabaseClient:
    return MetabaseClient.from_settings(client_settings)


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


def parse_json_body(raw: str | None) -> JSONValue | None:
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter("Invalid JSON body") from exc


def parse_json_object(raw: str, parameter_name: str) -> dict[str, object]:
    parsed = parse_json_body(raw)
    if not isinstance(parsed, dict):
        raise typer.BadParameter(f"{parameter_name} must be a JSON object")
    return parsed


def parse_optional_json_object(raw: str | None, parameter_name: str) -> dict[str, object] | None:
    if raw is None:
        return None
    return parse_json_object(raw, parameter_name)


def parse_optional_json_list(raw: str | None, parameter_name: str) -> list[object] | None:
    if raw is None:
        return None
    parsed = parse_json_body(raw)
    if not isinstance(parsed, list):
        raise typer.BadParameter(f"{parameter_name} must be a JSON array")
    return parsed


def parse_id_csv(raw: str) -> list[int | str]:
    return [value if not value.isdigit() else int(value) for value in raw.split(",") if value]


def _json_payload(result: object) -> JSONValue | None:
    if isinstance(result, BaseModel):
        return cast("JSONValue", result.model_dump(mode="json", exclude_none=True))
    return cast("JSONValue | None", result)


def _run_async(coro: Coroutine[object, object, object]) -> object:
    return asyncio.run(coro)


def _run_and_print(coro: Coroutine[object, object, object]) -> None:
    try:
        result = _json_payload(_run_async(coro))
    except (MetabaseError, ValueError) as exc:
        typer.echo(render_payload(error_payload(exc)), err=True)
        raise typer.Exit(code=1) from exc

    typer.echo(render_payload(result))


def _get_settings(ctx: typer.Context) -> settings.Settings:
    settings_obj = ctx.obj.get("settings")
    if not isinstance(settings_obj, settings.Settings):
        raise TypeError("CLI settings were not initialized")
    return settings_obj


def run_endpoint_command[ResponseT: BaseModel](ctx: typer.Context, request: EndpointRequest[ResponseT]) -> None:
    async def do_request() -> object:
        async with create_client(_get_settings(ctx)) as client:
            return await client.run(request)

    _run_and_print(do_request())


def run_json_body_endpoint_command[ResponseT: BaseModel](
    ctx: typer.Context,
    raw_body: str,
    build_request: Callable[[dict[str, object]], EndpointRequest[ResponseT]],
) -> None:
    run_endpoint_command(ctx, build_request(parse_json_object(raw_body, "body")))


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
