from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.dataset import DatasetExportRequest
from metabaseapi.endpoints.requests.dataset import DatasetNativeRequest
from metabaseapi.endpoints.requests.dataset import DatasetParameterRemappingRequest
from metabaseapi.endpoints.requests.dataset import DatasetParameterSearchRequest
from metabaseapi.endpoints.requests.dataset import DatasetParameterValuesRequest
from metabaseapi.endpoints.requests.dataset import DatasetPivotRequest
from metabaseapi.endpoints.requests.dataset import DatasetQueryMetadataRequest
from metabaseapi.endpoints.requests.dataset import DatasetQueryRequest


@app.command("post-dataset")
def post_dataset(ctx: typer.Context, body: str = typer.Argument(..., help="Dataset query JSON object")) -> None:
    """Execute an ad-hoc dataset query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetQueryRequest(body=payload))


@app.command("post-dataset-native")
def post_dataset_native(ctx: typer.Context, body: str = typer.Argument(..., help="Dataset query JSON object")) -> None:
    """Fetch the native query for an MBQL dataset query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetNativeRequest(body=payload))


@app.command("post-dataset-parameter-remapping")
def post_dataset_parameter_remapping(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Dataset parameter remapping JSON object"),
) -> None:
    """Return remapped dataset parameter values."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetParameterRemappingRequest(body=payload))


@app.command("post-dataset-parameter-search")
def post_dataset_parameter_search(
    ctx: typer.Context,
    query: str = typer.Argument(..., help="Parameter value search query"),
    body: str = typer.Argument(..., help="Dataset parameter search JSON object"),
) -> None:
    """Return dataset parameter values matching a query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetParameterSearchRequest(query=query, body=payload))


@app.command("post-dataset-parameter-values")
def post_dataset_parameter_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Dataset parameter values JSON object"),
) -> None:
    """Return dataset parameter values."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetParameterValuesRequest(body=payload))


@app.command("post-dataset-pivot")
def post_dataset_pivot(ctx: typer.Context, body: str = typer.Argument(..., help="Dataset pivot JSON object")) -> None:
    """Generate a pivoted dataset for an ad-hoc query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetPivotRequest(body=payload))


@app.command("post-dataset-query-metadata")
def post_dataset_query_metadata(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Dataset query metadata JSON object"),
) -> None:
    """Fetch required query metadata for an ad-hoc dataset query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DatasetQueryMetadataRequest(body=payload))


@app.command("post-dataset-export")
def post_dataset_export(
    ctx: typer.Context,
    export_format: str = typer.Argument(..., help="Export format"),
    body: str = typer.Argument(..., help="Dataset query JSON object"),
) -> None:
    """Execute an ad-hoc dataset query and return exported results."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: DatasetExportRequest(export_format=export_format, body=payload),
    )
