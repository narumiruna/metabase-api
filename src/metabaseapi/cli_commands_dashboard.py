from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_body
from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _parse_optional_json_list
from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app

_FILTERED_OPTION = typer.Option(None, "--filtered", help="Filtered field ID list")
_FILTERING_OPTION = typer.Option(None, "--filtering", help="Filtering field ID list")


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
    ids = [cid if not cid.isdigit() else int(cid) for cid in card_ids.split(",") if cid]
    _run_and_print(_run_client_call(ctx, lambda client: client.card_collections(ids, collection_id=collection_id)))


@app.command("list-embeddable-cards")
def list_embeddable_cards(ctx: typer.Context) -> None:
    """List embeddable cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_embeddable_cards()))


@app.command("pivot-query")
def pivot_query(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query body JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(_run_client_call(ctx, lambda client: client.pivot_query(card_id, body=payload)))


@app.command("list-public-cards")
def list_public_cards(ctx: typer.Context) -> None:
    """List publicly shared cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_public_cards()))


@app.command("get-card-param-search")
def get_card_param_search_values(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_search_values(card_id, param_key, query)))


@app.command("get-card-param-values")
def get_card_param_values(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_values(card_id, param_key)))


@app.command("create-card-public-link")
def create_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Create a public link for a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.create_card_public_link(card_id)))


@app.command("delete-card-public-link")
def delete_card_public_link(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a card."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_card_public_link(card_id)))


@app.command("query-card")
def query_card(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(_run_client_call(ctx, lambda client: client.query_card(card_id, body=payload)))


@app.command("query-card-export")
def query_card_export(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional payload JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_card_export(
                card_id,
                export_format,
                body=payload,
                pivot_results=pivot_results,
                format_rows=format_rows,
            ),
        ),
    )


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


@app.command("cards-dashboards")
def cards_dashboards(ctx: typer.Context, card_ids: str = typer.Argument(..., help="Comma-separated card IDs")) -> None:
    ids: list[int | str]
    ids = [card_id if not card_id.isdigit() else int(card_id) for card_id in card_ids.split(",") if card_id]
    _run_and_print(_run_client_call(ctx, lambda client: client.cards_dashboards(ids)))


@app.command("move-cards")
def move_cards(ctx: typer.Context, body: str = typer.Argument(..., help="Move payload JSON object")) -> None:
    payload = _parse_json_body(body)
    if not isinstance(payload, dict):
        raise typer.BadParameter("body must be a JSON object")
    _run_and_print(_run_client_call(ctx, lambda client: client.move_cards(payload)))


@app.command("get-card-dashboards")
def get_card_dashboards(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_dashboards(card_id)))


@app.command("get-card-param-remapping")
def get_card_param_remapping(
    ctx: typer.Context, card_id: str = typer.Argument(...), param_key: str = typer.Argument(...)
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_param_remapping(card_id, param_key)))


@app.command("get-card-query-metadata")
def get_card_query_metadata(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_query_metadata(card_id)))


@app.command("get-card-series")
def get_card_series(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_card_series(card_id)))


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard(dashboard_id)))


@app.command("get-dashboard-params-valid-filter-fields")
def get_dashboard_params_valid_filter_fields(
    ctx: typer.Context,
    filtered: list[str] | None = _FILTERED_OPTION,
    filtering: list[str] | None = _FILTERING_OPTION,
) -> None:
    """Get valid filter fields for dashboard parameters."""

    filtered_values = [int(item) if item.isdigit() else item for item in (filtered or [])]
    filtering_values = [int(item) if item.isdigit() else item for item in (filtering or [])]
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_params_valid_filter_fields(
                filtered=filtered_values or None,
                filtering=filtering_values or None,
            ),
        )
    )


@app.command("get-dashboard-embeddable")
def get_dashboard_embeddable(ctx: typer.Context) -> None:
    """List embeddable dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_embeddable()))


@app.command("get-dashboard-public")
def get_dashboard_public(ctx: typer.Context) -> None:
    """List public dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_public()))


@app.command("query-dashboard-card")
def query_dashboard_card(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_dashboard_card(
                dashboard_id,
                dashcard_id,
                card_id,
                payload,
            ),
        )
    )


@app.command("create-dashboard")
def create_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard body JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_dashboard(payload)))


@app.command("get-user")
def get_user(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Get a user by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_user(user_id)))


@app.command("create-collection")
def create_collection(ctx: typer.Context, body: str = typer.Argument(..., help="Collection JSON object")) -> None:
    """Create a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_collection(payload)))


@app.command("get-collection")
def get_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Get a collection by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection(collection_id)))


@app.command("update-collection")
def update_collection(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection update payload JSON object"),
) -> None:
    """Update a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_collection(collection_id, payload)))


@app.command("delete-collection")
def delete_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Delete a collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_collection(collection_id)))


@app.command("get-collection-dashboard-question-candidates")
def get_collection_dashboard_question_candidates(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Find cards in a collection that can be moved into dashboards."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_collection_dashboard_question_candidates(collection_id),
        )
    )


@app.command("get-collection-items")
def get_collection_items(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Fetch a collection's items."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_items(collection_id)))


@app.command("get-collection-root")
def get_collection_root(ctx: typer.Context) -> None:
    """Get the root collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root()))


@app.command("get-collection-root-dashboard-question-candidates")
def get_collection_root_dashboard_question_candidates(ctx: typer.Context) -> None:
    """Find cards in root collection that can be moved into dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root_dashboard_question_candidates()))


@app.command("get-collection-root-items")
def get_collection_root_items(ctx: typer.Context) -> None:
    """Fetch objects that the current user should see at root level."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root_items()))


@app.command("post-collection-root-move-dashboard-question-candidates")
def post_collection_root_move_dashboard_question_candidates(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection root move payload JSON object")
) -> None:
    """Move candidate cards to dashboards they appear in."""

    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(ctx, lambda client: client.post_collection_root_move_dashboard_question_candidates(payload))
    )


@app.command("post-collection-move-dashboard-question-candidates")
def post_collection_move_dashboard_question_candidates(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection move payload JSON object"),
) -> None:
    """Move candidate cards to dashboards they appear in for a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.post_collection_move_dashboard_question_candidates(collection_id, payload),
        )
    )


@app.command("get-collection-trash")
def get_collection_trash(ctx: typer.Context) -> None:
    """Fetch the trash collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_trash()))


@app.command("get-collection-tree")
def get_collection_tree(ctx: typer.Context) -> None:
    """Fetch collections in a tree structure."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_tree()))


@app.command("get-collection-graph")
def get_collection_graph(ctx: typer.Context) -> None:
    """Fetch the collection permissions graph."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_graph()))


@app.command("put-collection-graph")
def put_collection_graph(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection graph JSON object")
) -> None:
    """Update collection permissions via graph payload."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.put_collection_graph(payload)))


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_table(table_id)))


@app.command("get-field")
def get_field(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get a field by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_field(field_id)))


@app.command("create-database")
def create_database(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Name of the database to create"),
    engine: str = typer.Argument(..., help="Database engine type"),
    details: str | None = typer.Option(None, "--details", "-d", help="Database details JSON object"),
) -> None:
    """Create a new database."""

    details_payload: dict[str, object] | None
    if details is None:
        details_payload = None
    else:
        parsed = _parse_json_body(details)
        if parsed is not None and not isinstance(parsed, dict):
            raise typer.BadParameter("details must be a JSON object")
        details_payload = parsed

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_database(name=name, engine=engine, details=details_payload),
        ),
    )
