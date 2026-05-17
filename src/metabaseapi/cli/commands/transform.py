from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.transform import CancelTransformRequest
from metabaseapi.endpoints.requests.transform import CreateTransformRequest
from metabaseapi.endpoints.requests.transform import DeleteTransformRequest
from metabaseapi.endpoints.requests.transform import DeleteTransformTableRequest
from metabaseapi.endpoints.requests.transform import GetTransformDependenciesRequest
from metabaseapi.endpoints.requests.transform import GetTransformRequest
from metabaseapi.endpoints.requests.transform import GetTransformRunRequest
from metabaseapi.endpoints.requests.transform import ListTransformRunsRequest
from metabaseapi.endpoints.requests.transform import ListTransformsRequest
from metabaseapi.endpoints.requests.transform import ResetTransformCheckpointRequest
from metabaseapi.endpoints.requests.transform import RunTransformRequest
from metabaseapi.endpoints.requests.transform import UpdateTransformRequest
from metabaseapi.wire import QueryParamPrimitive
from metabaseapi.wire import QueryParamValue


def _parse_query_param_value(value: object) -> QueryParamValue | None:
    if isinstance(value, str | int | float | bool) or value is None:
        return value
    if isinstance(value, list):
        parsed_values: list[QueryParamPrimitive] = [
            item for item in value if isinstance(item, str | int | float | bool) or item is None
        ]
        return parsed_values
    return None


def _parse_query_params(raw: str | None) -> dict[str, QueryParamValue]:
    payload = parse_optional_json_object(raw, "params") or {}
    params: dict[str, QueryParamValue] = {}
    for key, value in payload.items():
        parsed_value = _parse_query_param_value(value)
        if parsed_value is not None:
            params[key] = parsed_value
    return params


@app.command("get-api-transform")
def get_api_transform(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Transform query params JSON object"),
) -> None:
    """Get a list of transforms."""

    run_endpoint_command(ctx, ListTransformsRequest(params=_parse_query_params(params)))


@app.command("post-api-transform")
def post_api_transform(ctx: typer.Context, body: str = typer.Argument(..., help="Transform JSON object")) -> None:
    """Create a new transform."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateTransformRequest(body=payload))


@app.command("get-api-transform-run")
def get_api_transform_run(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Transform run filter params JSON object"),
) -> None:
    """Get transform runs based on a set of filter params."""

    run_endpoint_command(ctx, ListTransformRunsRequest(params=_parse_query_params(params)))


@app.command("get-api-transform-run-run-id")
def get_api_transform_run_run_id(ctx: typer.Context, run_id: str = typer.Argument(...)) -> None:
    """Get a transform run by ID."""

    run_endpoint_command(ctx, GetTransformRunRequest(run_id=run_id))


@app.command("get-api-transform-id")
def get_api_transform_id(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Get a specific transform."""

    run_endpoint_command(ctx, GetTransformRequest(id=id))


@app.command("put-api-transform-id")
def put_api_transform_id(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Transform update payload JSON object"),
) -> None:
    """Update a transform."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateTransformRequest(id=id, body=payload))


@app.command("delete-api-transform-id")
def delete_api_transform_id(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Delete a transform."""

    run_endpoint_command(ctx, DeleteTransformRequest(id=id))


@app.command("post-api-transform-id-cancel")
def post_api_transform_id_cancel(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Cancel the current run for a given transform."""

    run_endpoint_command(ctx, CancelTransformRequest(id=id))


@app.command("get-api-transform-id-dependencies")
def get_api_transform_id_dependencies(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Get the dependencies of a specific transform."""

    run_endpoint_command(ctx, GetTransformDependenciesRequest(id=id))


@app.command("post-api-transform-id-reset-checkpoint")
def post_api_transform_id_reset_checkpoint(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Reset the stored checkpoint for an incremental transform."""

    run_endpoint_command(ctx, ResetTransformCheckpointRequest(id=id))


@app.command("post-api-transform-id-run")
def post_api_transform_id_run(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional run payload JSON object"),
) -> None:
    """Run a transform."""

    run_endpoint_command(ctx, RunTransformRequest(id=id, body=parse_optional_json_object_or_empty(body, "body")))


@app.command("delete-api-transform-id-table")
def delete_api_transform_id_table(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Delete a transform's output table."""

    run_endpoint_command(ctx, DeleteTransformTableRequest(id=id))
