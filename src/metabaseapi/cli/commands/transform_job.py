from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.transform_job import CreateTransformJobRequest
from metabaseapi.endpoints.requests.transform_job import DeleteTransformJobRequest
from metabaseapi.endpoints.requests.transform_job import GetTransformJobRequest
from metabaseapi.endpoints.requests.transform_job import GetTransformJobTransformsRequest
from metabaseapi.endpoints.requests.transform_job import ListTransformJobsRequest
from metabaseapi.endpoints.requests.transform_job import RunTransformJobRequest
from metabaseapi.endpoints.requests.transform_job import UpdateTransformJobRequest
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


@app.command("post-api-transform-job")
def post_api_transform_job(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Transform job JSON object"),
) -> None:
    """Create a new transform job."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateTransformJobRequest(body=payload))


@app.command("get-api-transform-job")
def get_api_transform_job(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Transform job query params JSON object"),
) -> None:
    """Get all transform jobs."""

    run_endpoint_command(ctx, ListTransformJobsRequest(params=_parse_query_params(params)))


@app.command("put-api-transform-job-job-id")
def put_api_transform_job_job_id(
    ctx: typer.Context,
    job_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Transform job update payload JSON object"),
) -> None:
    """Update a transform job."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateTransformJobRequest(job_id=job_id, body=payload))


@app.command("delete-api-transform-job-job-id")
def delete_api_transform_job_job_id(ctx: typer.Context, job_id: str = typer.Argument(...)) -> None:
    """Delete a transform job."""

    run_endpoint_command(ctx, DeleteTransformJobRequest(job_id=job_id))


@app.command("get-api-transform-job-job-id")
def get_api_transform_job_job_id(ctx: typer.Context, job_id: str = typer.Argument(...)) -> None:
    """Get a transform job by ID."""

    run_endpoint_command(ctx, GetTransformJobRequest(job_id=job_id))


@app.command("post-api-transform-job-job-id-run")
def post_api_transform_job_job_id_run(
    ctx: typer.Context,
    job_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional job run payload JSON object"),
) -> None:
    """Run a transform job manually."""

    run_endpoint_command(
        ctx,
        RunTransformJobRequest(job_id=job_id, body=parse_optional_json_object_or_empty(body, "body")),
    )


@app.command("get-api-transform-job-job-id-transforms")
def get_api_transform_job_job_id_transforms(ctx: typer.Context, job_id: str = typer.Argument(...)) -> None:
    """Get the transforms of job specified by the job's ID."""

    run_endpoint_command(ctx, GetTransformJobTransformsRequest(job_id=job_id))
