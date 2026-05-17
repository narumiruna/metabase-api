from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_serialization import PostEeSerializationExportRequest
from metabaseapi.endpoints.requests.ee_serialization import PostEeSerializationImportRequest


@app.command("post-api-ee-serialization-export")
def post_api_ee_serialization_export(
    ctx: typer.Context,
    body: str | None = typer.Option(None, "--body", help="Serialization export JSON object"),
) -> None:
    """Export serialized Metabase instance data."""

    run_endpoint_command(ctx, PostEeSerializationExportRequest(body=parse_optional_json_object_or_empty(body, "body")))


@app.command("post-api-ee-serialization-import")
def post_api_ee_serialization_import(
    ctx: typer.Context,
    file_path: str = typer.Option(..., "--file", help="Path to serialization archive"),
    body: str | None = typer.Option(None, "--body", help="Additional import JSON object"),
) -> None:
    """Import serialized Metabase instance data from an archive path."""

    run_endpoint_command(
        ctx,
        PostEeSerializationImportRequest(
            file_path=file_path,
            body=parse_optional_json_object_or_empty(body, "body"),
        ),
    )
