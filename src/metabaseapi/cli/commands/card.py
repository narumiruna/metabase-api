from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_id_csv
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import parse_optional_json_list
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.card import CopyCardRequest
from metabaseapi.endpoints.requests.card import CreateCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import CreateCardRequest
from metabaseapi.endpoints.requests.card import DeleteCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import DeleteCardRequest
from metabaseapi.endpoints.requests.card import GetCardCollectionsRequest
from metabaseapi.endpoints.requests.card import GetCardEmbeddableRequest
from metabaseapi.endpoints.requests.card import GetCardPublicRequest
from metabaseapi.endpoints.requests.card import GetCardRequest
from metabaseapi.endpoints.requests.card import ListCardsRequest
from metabaseapi.endpoints.requests.card import MoveCardsRequest
from metabaseapi.endpoints.requests.card import UpdateCardRequest


def _build_create_card_request(
    *,
    name: str,
    dataset_query: str,
    display: str,
    visualization_settings: str | None,
    card_type: str | None,
    collection_id: str | None,
    description: str | None,
    parameters: str | None,
    result_metadata: str | None,
) -> CreateCardRequest:
    visualization_settings_payload = parse_optional_json_object(
        visualization_settings,
        "visualization-settings",
    )
    return CreateCardRequest(
        name=name,
        dataset_query=parse_json_object(dataset_query, "dataset-query"),
        display=display,
        visualization_settings=visualization_settings_payload or {},
        type=card_type,
        collection_id=collection_id,
        description=description,
        parameters=parse_optional_json_list(parameters, "parameters"),
        result_metadata=parse_optional_json_list(result_metadata, "result-metadata"),
    )


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    run_endpoint_command(ctx, ListCardsRequest())


@app.command("create-card")
def create_card(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Card name"),
    dataset_query: str = typer.Argument(..., help="Dataset query JSON object"),
    display: str = typer.Option("table", "--display", help="Visualization display type"),
    visualization_settings: str | None = typer.Option(
        None,
        "--visualization-settings",
        help="Visualization settings JSON object",
    ),
    card_type: str | None = typer.Option("question", "--type", help="Card type: question, metric, or model"),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Collection ID"),
    description: str | None = typer.Option(None, "--description", help="Card description"),
    parameters: str | None = typer.Option(None, "--parameters", help="Parameters JSON array"),
    result_metadata: str | None = typer.Option(None, "--result-metadata", help="Result metadata JSON array"),
) -> None:
    """Create a card/question/model."""

    run_endpoint_command(
        ctx,
        _build_create_card_request(
            name=name,
            display=display,
            dataset_query=dataset_query,
            visualization_settings=visualization_settings,
            card_type=card_type,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        ),
    )


@app.command("create-question")
def create_question(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Question name"),
    dataset_query: str = typer.Argument(..., help="Dataset query JSON object"),
    display: str = typer.Option("table", "--display", help="Visualization display type"),
    visualization_settings: str | None = typer.Option(
        None,
        "--visualization-settings",
        help="Visualization settings JSON object",
    ),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Collection ID"),
    description: str | None = typer.Option(None, "--description", help="Question description"),
    parameters: str | None = typer.Option(None, "--parameters", help="Parameters JSON array"),
    result_metadata: str | None = typer.Option(None, "--result-metadata", help="Result metadata JSON array"),
) -> None:
    """Create a question."""

    run_endpoint_command(
        ctx,
        _build_create_card_request(
            name=name,
            display=display,
            dataset_query=dataset_query,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        ),
    )


@app.command("get-card")
def get_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Get a card by ID."""

    run_endpoint_command(ctx, GetCardRequest(card_id=card_id))


@app.command("card-collections")
def card_collections(
    ctx: typer.Context,
    card_ids: str = typer.Argument(..., help="Comma-separated card IDs"),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Target collection ID"),
) -> None:
    run_endpoint_command(ctx, GetCardCollectionsRequest(card_ids=parse_id_csv(card_ids), collection_id=collection_id))


@app.command("list-embeddable-cards")
def list_embeddable_cards(ctx: typer.Context) -> None:
    """List embeddable cards."""

    run_endpoint_command(ctx, GetCardEmbeddableRequest())


@app.command("list-public-cards")
def list_public_cards(ctx: typer.Context) -> None:
    """List publicly shared cards."""

    run_endpoint_command(ctx, GetCardPublicRequest())


@app.command("create-card-public-link")
def create_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Create a public link for a card."""

    run_endpoint_command(ctx, CreateCardPublicLinkRequest(card_id=card_id))


@app.command("delete-card-public-link")
def delete_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a card."""

    run_endpoint_command(ctx, DeleteCardPublicLinkRequest(card_id=card_id))


@app.command("update-card")
def update_card(ctx: typer.Context, card_id: str = typer.Argument(...), body: str = typer.Argument(...)) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateCardRequest(card_id=card_id, body=payload))


@app.command("delete-card")
def delete_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Delete a card."""

    run_endpoint_command(ctx, DeleteCardRequest(card_id=card_id))


@app.command("copy-card")
def copy_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Copy a card."""

    run_endpoint_command(ctx, CopyCardRequest(card_id=card_id))


@app.command("move-cards")
def move_cards(ctx: typer.Context, body: str = typer.Argument(..., help="Move payload JSON object")) -> None:
    run_endpoint_command(ctx, MoveCardsRequest(body=parse_json_object(body, "body")))
