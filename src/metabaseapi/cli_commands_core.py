from __future__ import annotations

from collections.abc import Mapping
from typing import cast

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app
from metabaseapi.models import QueryParamValue


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


@app.command("get-comment")
def get_comment(
    ctx: typer.Context,
    model: str | None = typer.Option(None, "--model"),
    model_id: str | None = typer.Option(None, "--model-id"),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_comment(model=model, model_id=model_id)))


@app.command("get-comment-mentions")
def get_comment_mentions(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_comment_mentions()))


@app.command("create-comment")
def create_comment(ctx: typer.Context, body: str = typer.Argument(..., help="Comment body JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_comment(payload)))


@app.command("update-comment")
def update_comment(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Comment body JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_comment(comment_id, payload)))


@app.command("post-comment-reaction")
def post_comment_reaction(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Reaction body JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.post_comment_reaction(comment_id, payload)))


@app.command("delete-comment")
def delete_comment(ctx: typer.Context, comment_id: str = typer.Argument(...)) -> None:
    """Delete a comment."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_comment(comment_id)))


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
