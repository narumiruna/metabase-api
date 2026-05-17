from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.transform_tag import CreateTransformTagRequest
from metabaseapi.endpoints.requests.transform_tag import DeleteTransformTagRequest
from metabaseapi.endpoints.requests.transform_tag import ListTransformTagsRequest
from metabaseapi.endpoints.requests.transform_tag import UpdateTransformTagRequest
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


@app.command("post-api-transform-tag")
def post_api_transform_tag(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Transform tag JSON object"),
) -> None:
    """Create a new transform tag."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateTransformTagRequest(body=payload))


@app.command("get-api-transform-tag")
def get_api_transform_tag(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Transform tag query params JSON object"),
) -> None:
    """Get a list of all transform tags."""

    run_endpoint_command(ctx, ListTransformTagsRequest(params=_parse_query_params(params)))


@app.command("put-api-transform-tag-tag-id")
def put_api_transform_tag_tag_id(
    ctx: typer.Context,
    tag_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Transform tag update payload JSON object"),
) -> None:
    """Update a transform tag."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateTransformTagRequest(tag_id=tag_id, body=payload))


@app.command("delete-api-transform-tag-tag-id")
def delete_api_transform_tag_tag_id(ctx: typer.Context, tag_id: str = typer.Argument(...)) -> None:
    """Delete a transform tag. Removes it from all transforms and jobs."""

    run_endpoint_command(ctx, DeleteTransformTagRequest(tag_id=tag_id))
