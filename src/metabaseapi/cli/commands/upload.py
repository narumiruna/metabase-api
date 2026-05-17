from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.upload import UploadCsvRequest


def _build_upload_csv_body(raw_body: str | None, file_path: Path | None) -> dict[str, object]:
    if raw_body is None and file_path is None:
        raise typer.BadParameter("Provide --body or --file")

    payload = parse_optional_json_object_or_empty(raw_body, "body")
    if file_path is not None:
        payload["file_name"] = file_path.name
        payload["csv"] = file_path.read_text(encoding="utf-8")
    return payload


@app.command("post-api-upload-csv")
def post_api_upload_csv(
    ctx: typer.Context,
    body: str | None = typer.Option(None, "--body", help="Upload CSV JSON object"),
    file_path: Annotated[
        Path | None,
        typer.Option("--file", exists=True, dir_okay=False, readable=True),
    ] = None,
) -> None:
    run_endpoint_command(ctx, UploadCsvRequest(body=_build_upload_csv_body(body, file_path)))
