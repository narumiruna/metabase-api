from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_content_translation import GetEeContentTranslationCsvRequest
from metabaseapi.endpoints.requests.ee_content_translation import GetEeContentTranslationDictionaryRequest
from metabaseapi.endpoints.requests.ee_content_translation import GetEeContentTranslationDictionaryTokenRequest
from metabaseapi.endpoints.requests.ee_content_translation import PostEeContentTranslationUploadDictionaryRequest


@app.command("get-ee-content-translation-csv")
def get_ee_content_translation_csv(ctx: typer.Context) -> None:
    """Fetch the content translation dictionary as CSV."""

    run_endpoint_command(ctx, GetEeContentTranslationCsvRequest())


@app.command("get-ee-content-translation-dictionary")
def get_ee_content_translation_dictionary(ctx: typer.Context) -> None:
    """Fetch the authenticated content translation dictionary."""

    run_endpoint_command(ctx, GetEeContentTranslationDictionaryRequest())


@app.command("get-ee-content-translation-dictionary-token")
def get_ee_content_translation_dictionary_token(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    """Fetch the token-authenticated content translation dictionary."""

    run_endpoint_command(ctx, GetEeContentTranslationDictionaryTokenRequest(token=token))


@app.command("post-ee-content-translation-upload-dictionary")
def post_ee_content_translation_upload_dictionary(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Content translation upload JSON object"),
) -> None:
    """Upload content translation dictionary data."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeContentTranslationUploadDictionaryRequest(body=payload),
    )
