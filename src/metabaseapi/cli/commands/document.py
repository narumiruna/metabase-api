from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.document import CopyDocumentRequest
from metabaseapi.endpoints.requests.document import CreateDocumentPublicLinkRequest
from metabaseapi.endpoints.requests.document import CreateDocumentRequest
from metabaseapi.endpoints.requests.document import DeleteDocumentPublicLinkRequest
from metabaseapi.endpoints.requests.document import DeleteDocumentRequest
from metabaseapi.endpoints.requests.document import DocumentCardQueryExportRequest
from metabaseapi.endpoints.requests.document import GetDocumentRequest
from metabaseapi.endpoints.requests.document import ListDocumentsRequest
from metabaseapi.endpoints.requests.document import ListPublicDocumentsRequest
from metabaseapi.endpoints.requests.document import UpdateDocumentRequest


@app.command("list-documents")
def list_documents(ctx: typer.Context) -> None:
    """List documents."""

    run_endpoint_command(ctx, ListDocumentsRequest())


@app.command("create-document")
def create_document(ctx: typer.Context, body: str = typer.Argument(..., help="Document body JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateDocumentRequest(body=payload))


@app.command("list-public-documents")
def list_public_documents(ctx: typer.Context) -> None:
    """List publicly shared documents."""

    run_endpoint_command(ctx, ListPublicDocumentsRequest())


@app.command("get-document")
def get_document(ctx: typer.Context, document_id: str = typer.Argument(...)) -> None:
    """Get a document by ID."""

    run_endpoint_command(ctx, GetDocumentRequest(document_id=document_id))


@app.command("update-document")
def update_document(
    ctx: typer.Context,
    document_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Document body JSON object"),
) -> None:
    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateDocumentRequest(document_id=document_id, body=payload),
    )


@app.command("delete-document")
def delete_document(ctx: typer.Context, document_id: str = typer.Argument(...)) -> None:
    """Delete an archived document."""

    run_endpoint_command(ctx, DeleteDocumentRequest(document_id=document_id))


@app.command("export-document-card-query")
def export_document_card_query(
    ctx: typer.Context,
    document_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body") or {}
    run_endpoint_command(
        ctx,
        DocumentCardQueryExportRequest(
            document_id=document_id,
            card_id=card_id,
            export_format=export_format,
            body=payload,
        ),
    )


@app.command("create-document-public-link")
def create_document_public_link(ctx: typer.Context, document_id: str = typer.Argument(...)) -> None:
    """Create a public link for a document."""

    run_endpoint_command(ctx, CreateDocumentPublicLinkRequest(document_id=document_id))


@app.command("delete-document-public-link")
def delete_document_public_link(ctx: typer.Context, document_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a document."""

    run_endpoint_command(ctx, DeleteDocumentPublicLinkRequest(document_id=document_id))


@app.command("copy-document")
def copy_document(
    ctx: typer.Context,
    from_document_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional copy payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body")
    run_endpoint_command(ctx, CopyDocumentRequest(from_document_id=from_document_id, body=payload))
