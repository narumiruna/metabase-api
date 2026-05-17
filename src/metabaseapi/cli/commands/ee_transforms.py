from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_transforms import GetEeTransformsIdInspectLensIdRequest
from metabaseapi.endpoints.requests.ee_transforms import GetEeTransformsIdInspectRequest
from metabaseapi.endpoints.requests.ee_transforms import PostEeTransformsIdInspectLensIdQueryRequest
from metabaseapi.wire import QueryParamValue


@app.command("get-api-ee-transforms-id-inspect")
def get_api_ee_transforms_id_inspect(ctx: typer.Context, transform_id: str = typer.Argument(...)) -> None:
    """Discover inspector lenses for a transform."""

    run_endpoint_command(ctx, GetEeTransformsIdInspectRequest(transform_id=transform_id))


@app.command("get-api-ee-transforms-id-inspect-lens-id")
def get_api_ee_transforms_id_inspect_lens_id(
    ctx: typer.Context,
    transform_id: str = typer.Argument(...),
    lens_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Lens query params JSON object"),
) -> None:
    """Fetch transform inspector lens contents."""

    run_endpoint_command(
        ctx,
        GetEeTransformsIdInspectLensIdRequest(
            transform_id=transform_id,
            lens_id=lens_id,
            params=cast("dict[str, QueryParamValue]", parse_optional_json_object_or_empty(params, "params")),
        ),
    )


@app.command("post-api-ee-transforms-id-inspect-lens-id-query")
def post_api_ee_transforms_id_inspect_lens_id_query(
    ctx: typer.Context,
    transform_id: str = typer.Argument(...),
    lens_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Inspector query JSON object"),
) -> None:
    """Execute a transform inspector query."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeTransformsIdInspectLensIdQueryRequest(
            transform_id=transform_id,
            lens_id=lens_id,
            body=payload,
        ),
    )
