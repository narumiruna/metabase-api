from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.eid_translation import TranslateEntityIdsRequest


@app.command("post-api-eid-translation-translate")
def post_api_eid_translation_translate(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Entity ID translation JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: TranslateEntityIdsRequest(body=payload))
