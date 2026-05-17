from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_upload_management import DeleteEeUploadManagementTablesIdRequest
from metabaseapi.endpoints.requests.ee_upload_management import GetEeUploadManagementTablesRequest
from metabaseapi.wire import QueryParamValue


@app.command("get-api-ee-upload-management-tables")
def get_api_ee_upload_management_tables(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Query params JSON object"),
) -> None:
    """List uploaded tables visible to the current user."""

    run_endpoint_command(
        ctx,
        GetEeUploadManagementTablesRequest(
            params=cast("dict[str, QueryParamValue]", parse_optional_json_object_or_empty(params, "params")),
        ),
    )


@app.command("delete-api-ee-upload-management-tables-id")
def delete_api_ee_upload_management_tables_id(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    archive_cards: bool | None = typer.Option(None, "--archive-cards/--keep-cards"),
) -> None:
    """Delete an uploaded table."""

    run_endpoint_command(
        ctx,
        DeleteEeUploadManagementTablesIdRequest(table_id=table_id, archive_cards=archive_cards),
    )
