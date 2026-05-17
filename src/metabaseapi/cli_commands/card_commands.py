from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_body
from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _parse_optional_json_list
from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_cards()))


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

    dataset_query_payload = _parse_json_object(dataset_query, "dataset-query")
    visualization_settings_payload = _parse_optional_json_object(
        visualization_settings,
        "visualization-settings",
    )
    parameters_payload = _parse_optional_json_list(parameters, "parameters")
    result_metadata_payload = _parse_optional_json_list(result_metadata, "result-metadata")

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_card(
                name=name,
                dataset_query=dataset_query_payload,
                display=display,
                visualization_settings=visualization_settings_payload,
                card_type=card_type,
                collection_id=collection_id,
                description=description,
                parameters=parameters_payload,
                result_metadata=result_metadata_payload,
            ),
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

    dataset_query_payload = _parse_json_object(dataset_query, "dataset-query")
    visualization_settings_payload = _parse_optional_json_object(
        visualization_settings,
        "visualization-settings",
    )
    parameters_payload = _parse_optional_json_list(parameters, "parameters")
    result_metadata_payload = _parse_optional_json_list(result_metadata, "result-metadata")

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_question(
                name=name,
                dataset_query=dataset_query_payload,
                display=display,
                visualization_settings=visualization_settings_payload,
                collection_id=collection_id,
                description=description,
                parameters=parameters_payload,
                result_metadata=result_metadata_payload,
            ),
        ),
    )


@app.command("get-card")
def get_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Get a card by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_card(card_id)))


@app.command("card-collections")
def card_collections(
    ctx: typer.Context,
    card_ids: str = typer.Argument(..., help="Comma-separated card IDs"),
    collection_id: str | None = typer.Option(None, "--collection-id", help="Target collection ID"),
) -> None:
    ids: list[int | str]
    ids = [card_id if not card_id.isdigit() else int(card_id) for card_id in card_ids.split(",") if card_id]
    _run_and_print(_run_client_call(ctx, lambda client: client.card_collections(ids, collection_id=collection_id)))


@app.command("list-embeddable-cards")
def list_embeddable_cards(ctx: typer.Context) -> None:
    """List embeddable cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_embeddable_cards()))


@app.command("list-public-cards")
def list_public_cards(ctx: typer.Context) -> None:
    """List publicly shared cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_public_cards()))


@app.command("create-card-public-link")
def create_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Create a public link for a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.create_card_public_link(card_id)))


@app.command("delete-card-public-link")
def delete_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_card_public_link(card_id)))


@app.command("update-card")
def update_card(ctx: typer.Context, card_id: str = typer.Argument(...), body: str = typer.Argument(...)) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_card(card_id, payload)))


@app.command("delete-card")
def delete_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Delete a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_card(card_id)))


@app.command("copy-card")
def copy_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Copy a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.copy_card(card_id)))


@app.command("move-cards")
def move_cards(ctx: typer.Context, body: str = typer.Argument(..., help="Move payload JSON object")) -> None:
    payload = _parse_json_body(body)
    if not isinstance(payload, dict):
        raise typer.BadParameter("body must be a JSON object")
    _run_and_print(_run_client_call(ctx, lambda client: client.move_cards(payload)))
