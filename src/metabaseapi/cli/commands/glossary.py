from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.glossary import CreateGlossaryEntryRequest
from metabaseapi.endpoints.requests.glossary import DeleteGlossaryEntryRequest
from metabaseapi.endpoints.requests.glossary import GetGlossaryRequest
from metabaseapi.endpoints.requests.glossary import UpdateGlossaryEntryRequest


@app.command("get-glossary")
def get_glossary(ctx: typer.Context, search: str | None = typer.Option(None, "--search")) -> None:
    run_endpoint_command(ctx, GetGlossaryRequest(search=search))


@app.command("create-glossary-entry")
def create_glossary_entry(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Glossary entry JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateGlossaryEntryRequest(body=payload))


@app.command("update-glossary-entry")
def update_glossary_entry(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Glossary entry JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateGlossaryEntryRequest(id=id, body=payload))


@app.command("delete-glossary-entry")
def delete_glossary_entry(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DeleteGlossaryEntryRequest(id=id))
