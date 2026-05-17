from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_data_studio import PostEeDataStudioTablePublishTablesRequest
from metabaseapi.endpoints.requests.ee_data_studio import PostEeDataStudioTableUnpublishTablesRequest


@app.command("post-ee-data-studio-table-publish-tables")
def post_ee_data_studio_table_publish_tables(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="EE Data Studio table publish JSON object"),
) -> None:
    """Publish selected tables and upstream dependencies."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeDataStudioTablePublishTablesRequest(body=payload),
    )


@app.command("post-ee-data-studio-table-unpublish-tables")
def post_ee_data_studio_table_unpublish_tables(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="EE Data Studio table unpublish JSON object"),
) -> None:
    """Unpublish selected tables and downstream dependents."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeDataStudioTableUnpublishTablesRequest(body=payload),
    )
