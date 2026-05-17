from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Awaitable
from collections.abc import Callable
from collections.abc import Coroutine
from collections.abc import Mapping
from typing import cast

import typer

from metabaseapi import settings
from metabaseapi.client import MetabaseClient
from metabaseapi.errors import MetabaseError
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue

app = typer.Typer(help="Async Metabase API CLI")


def create_client(
    client_settings: settings.Settings,
) -> MetabaseClient:
    return MetabaseClient.from_settings(client_settings)


def _format_json(payload: JSONValue) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True)


def _build_client_settings(
    *,
    base_url: str | None,
    api_key: str | None,
    timeout_seconds: float,
    verify_ssl: bool,
) -> settings.Settings:
    return settings.load_runtime_settings(
        base_url=base_url,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
        verify_ssl=verify_ssl,
    )


def _configure_logging(verbose: bool) -> None:
    if verbose:
        logging.basicConfig(level=logging.INFO)


def _parse_json_body(raw: str | None) -> JSONValue | None:
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter("Invalid JSON body") from exc


def _parse_json_object(raw: str, parameter_name: str) -> dict[str, object]:
    parsed = _parse_json_body(raw)
    if not isinstance(parsed, dict):
        raise typer.BadParameter(f"{parameter_name} must be a JSON object")
    return parsed


def _parse_optional_json_object(raw: str | None, parameter_name: str) -> dict[str, object] | None:
    if raw is None:
        return None
    return _parse_json_object(raw, parameter_name)


def _parse_optional_json_list(raw: str | None, parameter_name: str) -> list[object] | None:
    if raw is None:
        return None
    parsed = _parse_json_body(raw)
    if not isinstance(parsed, list):
        raise typer.BadParameter(f"{parameter_name} must be a JSON array")
    return parsed


def _run_async(coro: Coroutine[object, object, JSONValue | None]) -> JSONValue | None:
    return asyncio.run(coro)


def _run_and_print(coro: Coroutine[object, object, JSONValue | None]) -> None:
    try:
        result = _run_async(coro)
    except (MetabaseError, ValueError) as exc:
        typer.echo(_format_json({"error": str(exc)}), err=True)
        raise typer.Exit(code=1) from exc

    if result is None:
        typer.echo("null")
    else:
        typer.echo(_format_json(result))


def _get_settings(ctx: typer.Context) -> settings.Settings:
    settings_obj = ctx.obj.get("settings")
    if not isinstance(settings_obj, settings.Settings):
        raise TypeError("CLI settings were not initialized")
    return settings_obj


def _run_client_call(
    ctx: typer.Context,
    call: Callable[[MetabaseClient], Awaitable[JSONValue | None]],
) -> Coroutine[object, object, JSONValue | None]:
    async def do_request() -> JSONValue | None:
        async with create_client(_get_settings(ctx)) as client:
            return await call(client)

    return do_request()


@app.callback()
def configure(
    ctx: typer.Context,
    base_url: str | None = typer.Option(None, "--base-url", "-u", envvar="METABASE_URL"),
    api_key: str | None = typer.Option(None, "--api-key", "-k", envvar="METABASE_API_KEY"),
    timeout_seconds: float = typer.Option(30.0, "--timeout", "-t", envvar="METABASE_TIMEOUT_SECONDS"),
    verify_ssl: bool = typer.Option(True, "--verify/--no-verify", envvar="METABASE_VERIFY_SSL"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable basic logging"),
) -> None:
    _configure_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["settings"] = _build_client_settings(
        base_url=base_url,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
        verify_ssl=verify_ssl,
    )


@app.command("list-actions")
def list_actions(ctx: typer.Context, model_id: str | None = typer.Option(None, "--model-id")) -> None:
    """List actions."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_actions(model_id=model_id)))


@app.command("create-action")
def create_action(ctx: typer.Context, body: str = typer.Argument(..., help="Action JSON object")) -> None:
    """Create an action."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_action(payload)))


@app.command("list-public-actions")
def list_public_actions(ctx: typer.Context) -> None:
    """List public actions."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_public_actions()))


@app.command("get-action")
def get_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Get an action by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_action(action_id)))


@app.command("delete-action")
def delete_action(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_action(action_id)))


@app.command("get-action-execute")
def get_action_execute(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Fetch execution parameter values for an action."""

    payload = _parse_optional_json_object(parameters, "parameters")
    _run_and_print(_run_client_call(ctx, lambda client: client.get_action_execute(action_id, parameters=payload)))


@app.command("update-action")
def update_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Action JSON object"),
) -> None:
    """Update an action."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_action(action_id, payload)))


@app.command("execute-action")
def execute_action(
    ctx: typer.Context,
    action_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    """Execute an action."""

    payload = _parse_optional_json_object(parameters, "parameters")
    _run_and_print(_run_client_call(ctx, lambda client: client.execute_action(action_id, parameters=payload)))


@app.command("create-action-public-link")
def create_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Create an action public link."""

    _run_and_print(_run_client_call(ctx, lambda client: client.create_action_public_link(action_id)))


@app.command("delete-action-public-link")
def delete_action_public_link(ctx: typer.Context, action_id: str = typer.Argument(...)) -> None:
    """Delete an action public link."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_action_public_link(action_id)))


@app.command("list-bookmarks")
def list_bookmarks(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_bookmarks()))


@app.command("update-bookmark-ordering")
def update_bookmark_ordering(
    ctx: typer.Context, body: str = typer.Argument(..., help="Bookmark ordering JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_bookmark_ordering(payload)))


@app.command("create-bookmark")
def create_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.create_bookmark(model, item_id)))


@app.command("delete-bookmark")
def delete_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_bookmark(model, item_id)))


@app.command("bug-reporting-connection-pool-details")
def bug_reporting_connection_pool_details(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.bug_reporting_connection_pool_details()))


@app.command("bug-reporting-details")
def bug_reporting_details(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.bug_reporting_details()))


@app.command("get-cache")
def get_cache(
    ctx: typer.Context,
    limit: int | None = typer.Option(None),
    offset: int | None = typer.Option(None),
    sort_column: str | None = typer.Option(None),
    sort_direction: str | None = typer.Option(None),
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_cache(
                limit=limit,
                offset=offset,
                sort_column=sort_column,
                sort_direction=sort_direction,
            ),
        ),
    )


@app.command("put-cache")
def put_cache(ctx: typer.Context, body: str = typer.Argument(..., help="Cache configuration JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.put_cache(payload)))


@app.command("delete-cache")
def delete_cache(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Optional cache delete payload JSON object"),
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.delete_cache(payload or None),
        ),
    )


@app.command("invalidate-cache")
def invalidate_cache(
    ctx: typer.Context, params: str = typer.Argument(..., help="Invalidate cache params JSON object")
) -> None:
    payload = _parse_json_object(params, "params")
    normalized = cast("Mapping[str, QueryParamValue]", payload)
    _run_and_print(_run_client_call(ctx, lambda client: client.invalidate_cache(normalized)))


@app.command("automagic-database-candidates")
def automagic_database_candidates(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_database_candidates(database_id)))


@app.command("automagic-model-index-primary-key")
def automagic_model_index_primary_key(
    ctx: typer.Context,
    model_index_id: str = typer.Argument(...),
    primary_key_id: str = typer.Argument(...),
) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_model_index_primary_key(model_index_id, primary_key_id)),
    )


@app.command("automagic-dashboard-path")
def automagic_dashboard_path(ctx: typer.Context, path: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_dashboard_path(path)))


@app.command("automagic-entity")
def automagic_entity(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_entity(entity, entity_id_or_query)))


@app.command("automagic-entity-cell")
def automagic_entity_cell(ctx: typer.Context, entity: str, entity_id_or_query: str, cell_query: str) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_entity_cell(entity, entity_id_or_query, cell_query))
    )


@app.command("automagic-entity-cell-compare")
def automagic_entity_cell_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_compare(
                entity,
                entity_id_or_query,
                cell_query,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )


@app.command("automagic-entity-cell-rule")
def automagic_entity_cell_rule(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_rule(
                entity, entity_id_or_query, cell_query, prefix, dashboard_template
            ),
        ),
    )


@app.command("automagic-entity-cell-rule-compare")
def automagic_entity_cell_rule_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_rule_compare(
                entity,
                entity_id_or_query,
                cell_query,
                prefix,
                dashboard_template,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )


@app.command("automagic-entity-compare")
def automagic_entity_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_compare(
                entity,
                entity_id_or_query,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )


@app.command("automagic-entity-query-metadata")
def automagic_entity_query_metadata(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_entity_query_metadata(entity, entity_id_or_query))
    )


@app.command("automagic-entity-rule")
def automagic_entity_rule(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_rule(entity, entity_id_or_query, prefix, dashboard_template),
        ),
    )


@app.command("automagic-entity-rule-compare")
def automagic_entity_rule_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_rule_compare(
                entity,
                entity_id_or_query,
                prefix,
                dashboard_template,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )


@app.command("create-api-key")
def create_api_key(ctx: typer.Context, body: str = typer.Argument(..., help="API key JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_api_key(payload)))


@app.command("list-api-keys")
def list_api_keys(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_api_keys()))


@app.command("count-api-keys")
def count_api_keys(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.count_api_keys()))


@app.command("update-api-key")
def update_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...), body: str = typer.Argument(...)) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_api_key(api_key_id, payload)))


@app.command("delete-api-key")
def delete_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_api_key(api_key_id)))


@app.command("regenerate-api-key")
def regenerate_api_key(ctx: typer.Context, api_key_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.regenerate_api_key(api_key_id)))


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.analyze_chart(payload)))


@app.command("list-alerts")
def list_alerts(ctx: typer.Context, user_id: str | None = typer.Option(None, "--user-id")) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_alerts(user_id=user_id)))


@app.command("get-alert")
def get_alert(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_alert(alert_id)))


@app.command("delete-alert-subscription")
def delete_alert_subscription(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_alert_subscription(alert_id)))


@app.command("anonymous-stats")
def anonymous_stats(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.anonymous_stats()))


@app.command("create-analytics-event-batch")
def create_analytics_event_batch(
    ctx: typer.Context, body: str = typer.Argument(..., help="Analytics event batch JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_analytics_event_batch(payload)))


@app.command("agent-execute")
def agent_execute(ctx: typer.Context, body: str = typer.Argument(..., help="Agent execute JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_execute(payload)))


@app.command("get-agent-metric")
def get_agent_metric(ctx: typer.Context, metric_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_metric(metric_id)))


@app.command("get-agent-metric-field-values")
def get_agent_metric_field_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_metric_field_values(metric_id, field_id)))


@app.command("agent-ping")
def agent_ping(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_ping()))


@app.command("agent-search")
def agent_search(ctx: typer.Context, body: str = typer.Argument(..., help="Agent search JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_search(payload)))


@app.command("get-agent-table")
def get_agent_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_table(table_id)))


@app.command("get-agent-table-field-values")
def get_agent_table_field_values(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    field_id: str = typer.Argument(...),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_agent_table_field_values(table_id, field_id)))


@app.command("agent-construct-query")
def agent_construct_query(
    ctx: typer.Context, body: str = typer.Argument(..., help="Agent construct-query JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_construct_query(payload)))


@app.command("agent-query")
def agent_query(ctx: typer.Context, body: str = typer.Argument(..., help="Agent query JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.agent_query(payload)))


@app.command("most-recently-viewed-dashboard")
def most_recently_viewed_dashboard(ctx: typer.Context) -> None:
    """Get the most recently viewed dashboard."""

    _run_and_print(_run_client_call(ctx, lambda client: client.most_recently_viewed_dashboard()))


@app.command("list-popular-items")
def list_popular_items(ctx: typer.Context) -> None:
    """List popular items."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_popular_items()))


@app.command("list-recent-views")
def list_recent_views(ctx: typer.Context) -> None:
    """List recent views."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_recent_views()))


@app.command("list-recents")
def list_recents(ctx: typer.Context, context: str | None = typer.Option(None, "--context")) -> None:
    """List recents."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_recents(context=context)))


@app.command("create-recent")
def create_recent(ctx: typer.Context, body: str = typer.Argument(..., help="Recent item JSON object")) -> None:
    """Add a recently selected item."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_recent(payload)))


@app.command("current-user")
def get_current_user(ctx: typer.Context) -> None:
    """Get current user information."""

    _run_and_print(_run_client_call(ctx, lambda client: client.current_user()))


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_databases()))


@app.command("list-channels")
def list_channels(ctx: typer.Context) -> None:
    """List notification channels."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_channels()))


@app.command("create-channel")
def create_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Create a channel."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_channel(payload)))


@app.command("test-channel")
def test_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Test a channel connection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.test_channel(payload)))


@app.command("get-channel")
def get_channel(ctx: typer.Context, channel_id: str = typer.Argument(..., help="Channel ID")) -> None:
    """Get a channel."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_channel(channel_id)))


@app.command("update-channel")
def update_channel(
    ctx: typer.Context,
    channel_id: str = typer.Argument(..., help="Channel ID"),
    body: str = typer.Argument(..., help="Channel JSON object"),
) -> None:
    """Update a channel."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_channel(channel_id, payload)))


@app.command("create-cloud-migration")
def create_cloud_migration(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Cloud migration JSON object"),
) -> None:
    """Initiate a new cloud migration."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_cloud_migration(payload)))


@app.command("get-cloud-migration")
def get_cloud_migration(ctx: typer.Context) -> None:
    """Get the latest cloud migration, if any."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_cloud_migration()))


@app.command("cancel-cloud-migration")
def cancel_cloud_migration(ctx: typer.Context) -> None:
    """Cancel any ongoing cloud migrations, if any."""

    _run_and_print(_run_client_call(ctx, lambda client: client.cancel_cloud_migration()))


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_cards()))


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_dashboards()))


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_users()))


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_collections()))


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_tables()))


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_database(database_id)))


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


@app.command("get-collection-dashboard-question-candidates")
def get_collection_dashboard_question_candidates(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Find cards in a collection that can be moved into dashboards."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_collection_dashboard_question_candidates(collection_id),
        )
    )


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


if __name__ == "__main__":
    app()
