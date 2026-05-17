from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.embed_theme import CopyEmbedThemeRequest
from metabaseapi.endpoints.requests.embed_theme import CreateEmbedThemeRequest
from metabaseapi.endpoints.requests.embed_theme import DeleteEmbedThemeRequest
from metabaseapi.endpoints.requests.embed_theme import GetEmbedThemeRequest
from metabaseapi.endpoints.requests.embed_theme import ListEmbedThemesRequest
from metabaseapi.endpoints.requests.embed_theme import SeedDefaultEmbedThemesRequest
from metabaseapi.endpoints.requests.embed_theme import UpdateEmbedThemeRequest


@app.command("list-embed-themes")
def list_embed_themes(ctx: typer.Context) -> None:
    """List embedding themes."""

    run_endpoint_command(ctx, ListEmbedThemesRequest())


@app.command("create-embed-theme")
def create_embed_theme(ctx: typer.Context, body: str = typer.Argument(..., help="Embed theme JSON object")) -> None:
    """Create an embedding theme."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateEmbedThemeRequest(body=payload))


@app.command("seed-default-embed-themes")
def seed_default_embed_themes(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Default embed themes JSON object"),
) -> None:
    """Seed default embedding themes."""

    run_json_body_endpoint_command(ctx, body, lambda payload: SeedDefaultEmbedThemesRequest(body=payload))


@app.command("get-embed-theme")
def get_embed_theme(ctx: typer.Context, embed_theme_id: str = typer.Argument(...)) -> None:
    """Get an embedding theme by ID."""

    run_endpoint_command(ctx, GetEmbedThemeRequest(embed_theme_id=embed_theme_id))


@app.command("update-embed-theme")
def update_embed_theme(
    ctx: typer.Context,
    embed_theme_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Embed theme update JSON object"),
) -> None:
    """Update an embedding theme."""

    run_json_body_endpoint_command(
        ctx, body, lambda payload: UpdateEmbedThemeRequest(embed_theme_id=embed_theme_id, body=payload)
    )


@app.command("delete-embed-theme")
def delete_embed_theme(ctx: typer.Context, embed_theme_id: str = typer.Argument(...)) -> None:
    """Delete an embedding theme."""

    run_endpoint_command(ctx, DeleteEmbedThemeRequest(embed_theme_id=embed_theme_id))


@app.command("copy-embed-theme")
def copy_embed_theme(ctx: typer.Context, embed_theme_id: str = typer.Argument(...)) -> None:
    """Copy an embedding theme."""

    run_endpoint_command(ctx, CopyEmbedThemeRequest(embed_theme_id=embed_theme_id))
