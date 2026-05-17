from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_replacement import GetEeReplacementRunsIdRequest
from metabaseapi.endpoints.requests.ee_replacement import GetEeReplacementRunsRequest
from metabaseapi.endpoints.requests.ee_replacement import PostEeReplacementCheckReplaceSourceRequest
from metabaseapi.endpoints.requests.ee_replacement import PostEeReplacementReplaceModelWithTransformRequest
from metabaseapi.endpoints.requests.ee_replacement import PostEeReplacementReplaceSourceRequest
from metabaseapi.endpoints.requests.ee_replacement import PostEeReplacementRunsIdCancelRequest


@app.command("post-api-ee-replacement-check-replace-source")
def post_api_ee_replacement_check_replace_source(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Replacement compatibility check JSON object"),
) -> None:
    """Check whether a source entity can be replaced by a target entity."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostEeReplacementCheckReplaceSourceRequest(body=payload))


@app.command("post-api-ee-replacement-replace-model-with-transform")
def post_api_ee_replacement_replace_model_with_transform(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Model replacement transform JSON object"),
) -> None:
    """Replace a model with the output table from a generated transform."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeReplacementReplaceModelWithTransformRequest(body=payload),
    )


@app.command("post-api-ee-replacement-replace-source")
def post_api_ee_replacement_replace_source(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Source replacement JSON object"),
) -> None:
    """Replace all usages of a source entity with a target entity."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostEeReplacementReplaceSourceRequest(body=payload))


@app.command("get-api-ee-replacement-runs")
def get_api_ee_replacement_runs(
    ctx: typer.Context,
    is_active: bool | None = typer.Option(None, "--is-active/--not-active"),
) -> None:
    """List replacement runs."""

    run_endpoint_command(ctx, GetEeReplacementRunsRequest(is_active=is_active))


@app.command("get-api-ee-replacement-runs-id")
def get_api_ee_replacement_runs_id(
    ctx: typer.Context,
    id: str = typer.Argument(...),
) -> None:
    """Get the status of a source replacement run."""

    run_endpoint_command(ctx, GetEeReplacementRunsIdRequest(id=id))


@app.command("post-api-ee-replacement-runs-id-cancel")
def post_api_ee_replacement_runs_id_cancel(
    ctx: typer.Context,
    id: str = typer.Argument(...),
) -> None:
    """Cancel a running source replacement."""

    run_endpoint_command(ctx, PostEeReplacementRunsIdCancelRequest(id=id))
