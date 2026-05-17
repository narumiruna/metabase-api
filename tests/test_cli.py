from __future__ import annotations

import pytest
from typer.testing import CliRunner

from metabaseapi import cli
from metabaseapi.errors import MetabaseHTTPStatusError

runner = CliRunner()


class _ClientWithRequestMethods:
    async def __aenter__(self) -> _ClientWithRequestMethods:
        return self

    async def __aexit__(self, *_: object) -> None:
        return None


class _ConvenienceClient(_ClientWithRequestMethods):
    async def list_actions(self, *, model_id: str | None = None) -> dict[str, object]:
        return {"method": "GET", "path": "/api/action", "params": {"model-id": model_id} if model_id else None}

    async def create_action(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/action", "body": body}

    async def list_public_actions(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/action/public"}

    async def get_action(self, action_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/action/{action_id}"}

    async def delete_action(self, action_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/action/{action_id}"}

    async def get_action_execute(
        self,
        action_id: str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/action/{action_id}/execute", "params": parameters}

    async def update_action(self, action_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/action/{action_id}", "body": body}

    async def execute_action(
        self,
        action_id: str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/action/{action_id}/execute", "body": {"parameters": parameters or {}}}

    async def create_action_public_link(self, action_id: str) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/action/{action_id}/public_link"}

    async def delete_action_public_link(self, action_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/action/{action_id}/public_link"}

    async def list_bookmarks(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/bookmark"}

    async def update_bookmark_ordering(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": "/api/bookmark/ordering", "body": body}

    async def create_bookmark(self, model: str, item_id: str) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/bookmark/{model}/{item_id}"}

    async def delete_bookmark(self, model: str, item_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/bookmark/{model}/{item_id}"}

    async def bug_reporting_connection_pool_details(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/bug-reporting/connection-pool-details"}

    async def bug_reporting_details(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/bug-reporting/details"}

    async def get_cache(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sort_column: str | None = None,
        sort_direction: str | None = None,
    ) -> dict[str, object]:
        return {
            "method": "GET",
            "path": "/api/cache",
            "params": {
                k: v
                for k, v in {
                    "limit": limit,
                    "offset": offset,
                    "sort_column": sort_column,
                    "sort_direction": sort_direction,
                }.items()
                if v is not None
            }
            or None,
        }

    async def put_cache(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": "/api/cache", "body": body}

    async def delete_cache(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "DELETE", "path": "/api/cache", "body": body}

    async def invalidate_cache(self, params: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/cache/invalidate", "params": params}

    async def automagic_database_candidates(self, database_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/automagic-dashboards/database/{database_id}/candidates"}

    async def automagic_model_index_primary_key(self, model_index_id: str, primary_key_id: str) -> dict[str, object]:
        return {
            "method": "GET",
            "path": f"/api/automagic-dashboards/model_index/{model_index_id}/primary_key/{primary_key_id}",
        }

    async def automagic_dashboard_path(self, path: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/automagic-dashboards/{path}"}

    async def automagic_entity(self, entity: str, entity_id_or_query: str) -> dict[str, object]:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}")

    async def automagic_entity_cell(self, entity: str, entity_id_or_query: str, cell_query: str) -> dict[str, object]:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/cell/{cell_query}")

    async def automagic_entity_cell_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_cell_rule(
        self, entity: str, entity_id_or_query: str, cell_query: str, prefix: str, dashboard_template: str
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}"
        )

    async def automagic_entity_cell_rule_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_compare(
        self, entity: str, entity_id_or_query: str, comparison_entity: str, comparison_entity_id_or_query: str
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_query_metadata(self, entity: str, entity_id_or_query: str) -> dict[str, object]:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/query_metadata")

    async def automagic_entity_rule(
        self, entity: str, entity_id_or_query: str, prefix: str, dashboard_template: str
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}")

    async def automagic_entity_rule_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> dict[str, object]:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def create_api_key(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/api-key", "body": body}

    async def list_api_keys(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/api-key"}

    async def count_api_keys(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/api-key/count"}

    async def update_api_key(self, api_key_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/api-key/{api_key_id}", "body": body}

    async def delete_api_key(self, api_key_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/api-key/{api_key_id}"}

    async def regenerate_api_key(self, api_key_id: str) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/api-key/{api_key_id}/regenerate"}

    async def analyze_chart(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/ai-entity-analysis/analyze-chart", "body": body}

    async def list_alerts(self, *, user_id: str | None = None) -> dict[str, object]:
        return {"method": "GET", "path": "/api/alert", "params": {"user_id": user_id} if user_id else None}

    async def get_alert(self, alert_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/alert/{alert_id}"}

    async def delete_alert_subscription(self, alert_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/alert/{alert_id}/subscription"}

    async def anonymous_stats(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/analytics/anonymous-stats"}

    async def create_analytics_event_batch(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/analytics/internal", "body": body}

    async def agent_execute(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/agent/v1/execute", "body": body}

    async def get_agent_metric(self, metric_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/agent/v1/metric/{metric_id}"}

    async def get_agent_metric_field_values(self, metric_id: str, field_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/agent/v1/metric/{metric_id}/field/{field_id}/values"}

    async def agent_ping(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/agent/v1/ping"}

    async def agent_search(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/agent/v1/search", "body": body}

    async def get_agent_table(self, table_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/agent/v1/table/{table_id}"}

    async def get_agent_table_field_values(self, table_id: str, field_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/agent/v1/table/{table_id}/field/{field_id}/values"}

    async def agent_construct_query(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/agent/v2/construct-query", "body": body}

    async def agent_query(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/agent/v2/query", "body": body}

    async def most_recently_viewed_dashboard(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/activity/most_recently_viewed_dashboard"}

    async def list_popular_items(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/activity/popular_items"}

    async def list_recent_views(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/activity/recent_views"}

    async def list_recents(self, *, context: str | None = None) -> dict[str, object]:
        return {"method": "GET", "path": "/api/activity/recents", "params": {"context": context} if context else None}

    async def create_recent(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/activity/recents", "body": body}

    async def current_user(self) -> dict[str, str]:
        return {"name": "Alice"}

    async def list_databases(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/database"}

    async def list_channels(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/channel"}

    async def create_channel(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/channel", "body": body}

    async def test_channel(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/channel/test", "body": body}

    async def get_channel(self, channel_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/channel/{channel_id}"}

    async def update_channel(self, channel_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/channel/{channel_id}", "body": body}

    async def create_cloud_migration(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/cloud-migration", "body": body}

    async def get_cloud_migration(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/cloud-migration"}

    async def cancel_cloud_migration(self) -> dict[str, object]:
        return {"method": "PUT", "path": "/api/cloud-migration/cancel"}

    async def create_database(
        self,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> dict[str, object]:
        body: dict[str, object] = {"name": name, "engine": engine}
        if details is not None:
            body["details"] = details
        return {"method": "POST", "path": "/api/database", "body": body}

    async def get_database(self, database_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/database/{database_id}"}

    async def list_cards(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/card"}

    async def create_card(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> dict[str, object]:
        body: dict[str, object] = {
            "name": name,
            "dataset_query": dataset_query,
            "display": display,
            "visualization_settings": visualization_settings or {},
        }
        if card_type is not None:
            body["type"] = card_type
        if collection_id is not None:
            body["collection_id"] = collection_id
        if description is not None:
            body["description"] = description
        if parameters is not None:
            body["parameters"] = parameters
        if result_metadata is not None:
            body["result_metadata"] = result_metadata
        return {"method": "POST", "path": "/api/card", "body": body}

    async def create_question(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        collection_id: str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> dict[str, object]:
        return await self.create_card(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def get_card(self, card_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}"}

    async def card_collections(
        self,
        card_ids: list[int] | list[str],
        collection_id: str | None = None,
    ) -> dict[str, object]:
        return {
            "method": "POST",
            "path": "/api/card/collections",
            "body": {"card_ids": card_ids, **({"collection_id": collection_id} if collection_id else {})},
        }

    async def list_embeddable_cards(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/card/embeddable"}

    async def pivot_query(self, card_id: str, body: dict[str, object] | None = None) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/card/pivot/{card_id}/query", "body": body}

    async def list_public_cards(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/card/public"}

    async def get_card_param_search_values(self, card_id: str, param_key: str, query: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/params/{param_key}/search/{query}"}

    async def get_card_param_values(self, card_id: str, param_key: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/params/{param_key}/values"}

    async def create_card_public_link(self, card_id: str) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/card/{card_id}/public_link"}

    async def delete_card_public_link(self, card_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/card/{card_id}/public_link"}

    async def query_card(self, card_id: str, body: dict[str, object] | None = None) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/card/{card_id}/query", "body": body}

    async def query_card_export(
        self,
        card_id: str,
        export_format: str,
        body: dict[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> dict[str, object]:
        params: dict[str, object] = {}
        if pivot_results is not None:
            params["pivot-results"] = pivot_results
        if format_rows is not None:
            params["format-rows"] = format_rows
        payload: dict[str, object] = {"method": "POST", "path": f"/api/card/{card_id}/query/{export_format}"}
        if params:
            payload["params"] = params
        if body is not None:
            payload["body"] = body
        return payload

    async def update_card(self, card_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/card/{card_id}", "body": body}

    async def delete_card(self, card_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/card/{card_id}"}

    async def copy_card(self, card_id: str) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/card/{card_id}/copy"}

    async def cards_dashboards(self, card_ids: list[int] | list[str]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/cards/dashboards", "body": {"card_ids": card_ids}}

    async def move_cards(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/cards/move", "body": body}

    async def get_card_dashboards(self, card_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/dashboards"}

    async def get_card_param_remapping(self, card_id: str, param_key: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/params/{param_key}/remapping"}

    async def get_card_query_metadata(self, card_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/query_metadata"}

    async def get_card_series(self, card_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/card/{card_id}/series"}

    async def list_dashboards(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/dashboard"}

    async def get_dashboard(self, dashboard_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/dashboard/{dashboard_id}"}

    async def list_users(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/user"}

    async def get_user(self, user_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/user/{user_id}"}

    async def list_collections(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection"}

    async def create_collection(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/collection", "body": body}

    async def get_collection(self, collection_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/collection/{collection_id}"}

    async def update_collection(self, collection_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/collection/{collection_id}", "body": body}

    async def delete_collection(self, collection_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/collection/{collection_id}"}

    async def get_comment(self, model: str | None = None, model_id: str | None = None) -> dict[str, object]:
        del model, model_id
        return {"method": "GET", "path": "/api/comment"}

    async def get_comment_mentions(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/comment/mentions"}

    async def create_comment(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": "/api/comment", "body": body}

    async def update_comment(self, comment_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": f"/api/comment/{comment_id}", "body": body}

    async def post_comment_reaction(self, comment_id: str, body: dict[str, object]) -> dict[str, object]:
        return {"method": "POST", "path": f"/api/comment/{comment_id}/reaction", "body": body}

    async def delete_comment(self, comment_id: str) -> dict[str, object]:
        return {"method": "DELETE", "path": f"/api/comment/{comment_id}"}

    async def get_collection_dashboard_question_candidates(self, collection_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/collection/{collection_id}/dashboard-question-candidates"}

    async def get_collection_items(self, collection_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/collection/{collection_id}/items"}

    async def get_collection_root(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/root"}

    async def get_collection_root_dashboard_question_candidates(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/root/dashboard-question-candidates"}

    async def get_collection_root_items(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/root/items"}

    async def post_collection_root_move_dashboard_question_candidates(
        self, body: dict[str, object]
    ) -> dict[str, object]:
        return {
            "method": "POST",
            "path": "/api/collection/root/move-dashboard-question-candidates",
            "body": body,
        }

    async def post_collection_move_dashboard_question_candidates(
        self, collection_id: str, body: dict[str, object]
    ) -> dict[str, object]:
        return {
            "method": "POST",
            "path": f"/api/collection/{collection_id}/move-dashboard-question-candidates",
            "body": body,
        }

    async def get_collection_trash(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/trash"}

    async def get_collection_tree(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/tree"}

    async def get_collection_graph(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/collection/graph"}

    async def put_collection_graph(self, body: dict[str, object]) -> dict[str, object]:
        return {"method": "PUT", "path": "/api/collection/graph", "body": body}

    async def list_tables(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/table"}

    async def get_table(self, table_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/table/{table_id}"}

    async def get_field(self, field_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/field/{field_id}"}


class _ErrorClient(_ClientWithRequestMethods):
    async def get(self, *_: object, **__: object) -> dict[str, str]:
        raise MetabaseHTTPStatusError(401, {"message": "unauthorized"})

    async def current_user(self) -> dict[str, str]:
        raise MetabaseHTTPStatusError(401, {"message": "unauthorized"})


def test_help_omits_raw_request_commands() -> None:
    result = runner.invoke(cli.app, ["--help"])

    assert result.exit_code == 0
    assert "request" not in result.stdout
    assert "invoke" not in result.stdout


def test_help_lists_every_convenience_command() -> None:
    result = runner.invoke(cli.app, ["--help"])

    assert result.exit_code == 0
    for command in [
        "list-actions",
        "create-action",
        "list-public-actions",
        "get-action",
        "delete-action",
        "get-action-execute",
        "update-action",
        "execute-action",
        "create-action-public-link",
        "delete-action-public-link",
        "list-bookmarks",
        "update-bookmark-ordering",
        "create-bookmark",
        "delete-bookmark",
        "bug-reporting-connection-pool-details",
        "bug-reporting-details",
        "get-cache",
        "put-cache",
        "delete-cache",
        "invalidate-cache",
        "automagic-database-candidates",
        "automagic-model-index-primary-key",
        "automagic-entity",
        "automagic-entity-cell",
        "automagic-entity-cell-compare",
        "automagic-entity-cell-rule",
        "automagic-entity-cell-rule-compare",
        "automagic-entity-compare",
        "automagic-entity-query-metadata",
        "automagic-entity-rule",
        "automagic-entity-rule-compare",
        "create-api-key",
        "list-api-keys",
        "count-api-keys",
        "update-api-key",
        "delete-api-key",
        "regenerate-api-key",
        "analyze-chart",
        "list-alerts",
        "get-alert",
        "delete-alert-subscription",
        "anonymous-stats",
        "create-analytics-event-batch",
        "agent-execute",
        "get-agent-metric",
        "get-agent-metric-field-values",
        "agent-ping",
        "agent-search",
        "get-agent-table",
        "get-agent-table-field-values",
        "agent-construct-query",
        "agent-query",
        "most-recently-viewed-dashboard",
        "list-popular-items",
        "list-recent-views",
        "list-recents",
        "create-recent",
        "current-user",
        "list-databases",
        "list-channels",
        "create-channel",
        "test-channel",
        "get-channel",
        "update-channel",
        "create-cloud-migration",
        "get-cloud-migration",
        "cancel-cloud-migration",
        "create-database",
        "get-database",
        "list-cards",
        "create-card",
        "create-question",
        "get-card",
        "list-embeddable-cards",
        "pivot-query",
        "list-public-cards",
        "get-card-param-search",
        "get-card-param-values",
        "query-card",
        "query-card-export",
        "update-card",
        "delete-card",
        "cards-dashboards",
        "copy-card",
        "get-card-dashboards",
        "move-cards",
        "get-card-param-remapping",
        "get-card-query-metadata",
        "get-card-series",
        "list-dashboards",
        "get-dashboard",
        "list-users",
        "get-user",
        "list-collections",
        "get-collection",
        "update-collection",
        "delete-collection",
        "delete-comment",
        "get-comment",
        "create-comment",
        "get-comment-mentions",
        "update-comment",
        "post-comment-reaction",
        "get-collection-dashboard-question-candidates",
        "get-collection-items",
        "list-tables",
        "get-table",
        "get-field",
        "create-collection",
        "get-collection-root",
        "get-collection-root-dashboard-question-candidates",
        "get-collection-root-items",
        "post-collection-root-move-dashboard-question-candidates",
        "post-collection-move-dashboard-question-candidates",
        "get-collection-trash",
        "get-collection-tree",
        "get-collection-graph",
        "put-collection-graph",
    ]:
        assert command in result.stdout


def test_current_user_command_outputs_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "current-user",
        ],
    )

    assert result.exit_code == 0
    assert result.stdout.strip() == '{\n  "name": "Alice"\n}'


def test_get_database_command_outputs_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "get-database",
            "12",
        ],
    )

    assert result.exit_code == 0
    assert '\n  "path": "/api/database/12"' in result.stdout
    assert '\n  "method": "GET"' in result.stdout


@pytest.mark.parametrize(
    ("command", "expected_path"),
    [
        (["list-actions"], "/api/action"),
        (["list-public-actions"], "/api/action/public"),
        (["get-action", "11"], "/api/action/11"),
        (["get-action-execute", "11"], "/api/action/11/execute"),
        (["list-bookmarks"], "/api/bookmark"),
        (["bug-reporting-connection-pool-details"], "/api/bug-reporting/connection-pool-details"),
        (["bug-reporting-details"], "/api/bug-reporting/details"),
        (["get-cache"], "/api/cache"),
        (["automagic-database-candidates", "1"], "/api/automagic-dashboards/database/1/candidates"),
        (["automagic-model-index-primary-key", "2", "3"], "/api/automagic-dashboards/model_index/2/primary_key/3"),
        (["automagic-entity", "table", "4"], "/api/automagic-dashboards/table/4"),
        (["automagic-entity-cell", "table", "4", "cell"], "/api/automagic-dashboards/table/4/cell/cell"),
        (
            ["automagic-entity-cell-compare", "table", "4", "cell", "table", "5"],
            "/api/automagic-dashboards/table/4/cell/cell/compare/table/5",
        ),
        (
            ["automagic-entity-cell-rule", "table", "4", "cell", "p", "t"],
            "/api/automagic-dashboards/table/4/cell/cell/rule/p/t",
        ),
        (
            ["automagic-entity-cell-rule-compare", "table", "4", "cell", "p", "t", "table", "5"],
            "/api/automagic-dashboards/table/4/cell/cell/rule/p/t/compare/table/5",
        ),
        (["automagic-entity-compare", "table", "4", "table", "5"], "/api/automagic-dashboards/table/4/compare/table/5"),
        (["automagic-entity-query-metadata", "table", "4"], "/api/automagic-dashboards/table/4/query_metadata"),
        (["automagic-entity-rule", "table", "4", "p", "t"], "/api/automagic-dashboards/table/4/rule/p/t"),
        (
            ["automagic-entity-rule-compare", "table", "4", "p", "t", "table", "5"],
            "/api/automagic-dashboards/table/4/rule/p/t/compare/table/5",
        ),
        (["list-api-keys"], "/api/api-key"),
        (["count-api-keys"], "/api/api-key/count"),
        (["list-alerts"], "/api/alert"),
        (["get-alert", "7"], "/api/alert/7"),
        (["anonymous-stats"], "/api/analytics/anonymous-stats"),
        (["get-agent-metric", "1"], "/api/agent/v1/metric/1"),
        (["get-agent-metric-field-values", "1", "2"], "/api/agent/v1/metric/1/field/2/values"),
        (["agent-ping"], "/api/agent/v1/ping"),
        (["get-agent-table", "3"], "/api/agent/v1/table/3"),
        (["get-agent-table-field-values", "3", "4"], "/api/agent/v1/table/3/field/4/values"),
        (["most-recently-viewed-dashboard"], "/api/activity/most_recently_viewed_dashboard"),
        (["list-popular-items"], "/api/activity/popular_items"),
        (["list-recent-views"], "/api/activity/recent_views"),
        (["list-recents"], "/api/activity/recents"),
        (["get-cloud-migration"], "/api/cloud-migration"),
        (["list-databases"], "/api/database"),
        (["list-channels"], "/api/channel"),
        (["get-comment"], "/api/comment"),
        (["list-cards"], "/api/card"),
        (["list-dashboards"], "/api/dashboard"),
        (["list-users"], "/api/user"),
        (["list-collections"], "/api/collection"),
        (["list-tables"], "/api/table"),
        (["get-database", "12"], "/api/database/12"),
        (["get-card", "13"], "/api/card/13"),
        (["list-embeddable-cards"], "/api/card/embeddable"),
        (["list-public-cards"], "/api/card/public"),
        (["get-card-param-search", "13", "abc", "Orange"], "/api/card/13/params/abc/search/Orange"),
        (["get-card-param-values", "13", "abc"], "/api/card/13/params/abc/values"),
        (["get-card-dashboards", "13"], "/api/card/13/dashboards"),
        (["get-card-param-remapping", "13", "abc"], "/api/card/13/params/abc/remapping"),
        (["get-card-query-metadata", "13"], "/api/card/13/query_metadata"),
        (["get-card-series", "13"], "/api/card/13/series"),
        (["get-dashboard", "14"], "/api/dashboard/14"),
        (["get-user", "15"], "/api/user/15"),
        (["get-collection", "7"], "/api/collection/7"),
        (["get-collection", "root"], "/api/collection/root"),
        (["get-collection-dashboard-question-candidates", "7"], "/api/collection/7/dashboard-question-candidates"),
        (["get-collection-items", "7"], "/api/collection/7/items"),
        (["get-collection-root"], "/api/collection/root"),
        (["get-collection-root-dashboard-question-candidates"], "/api/collection/root/dashboard-question-candidates"),
        (["get-collection-root-items"], "/api/collection/root/items"),
        (["get-collection-trash"], "/api/collection/trash"),
        (["get-collection-tree"], "/api/collection/tree"),
        (["get-collection-graph"], "/api/collection/graph"),
        (["get-table", "16"], "/api/table/16"),
        (["get-field", "17"], "/api/field/17"),
    ],
)
def test_read_endpoint_commands_cover_handwritten_surface(
    monkeypatch: pytest.MonkeyPatch,
    command: list[str],
    expected_path: str,
) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        ["--base-url", "http://localhost:3000", "--api-key", "abc", *command],
    )

    assert result.exit_code == 0
    assert '\n  "method": "GET"' in result.stdout
    assert f'\n  "path": "{expected_path}"' in result.stdout


@pytest.mark.parametrize(
    ("command", "expected_method", "expected_path"),
    [
        (["create-action", '{"name":"action"}'], "POST", "/api/action"),
        (["create-channel", '{"name":"Slack"}'], "POST", "/api/channel"),
        (["test-channel", '{"name":"Slack"}'], "POST", "/api/channel/test"),
        (["create-comment", '{"text":"Hi","model":"card","model_id":13}'], "POST", "/api/comment"),
        (["get-comment-mentions"], "GET", "/api/comment/mentions"),
        (["update-comment", "11", '{"text":"updated"}'], "PUT", "/api/comment/11"),
        (["post-comment-reaction", "11", '{"emoji":"👍"}'], "POST", "/api/comment/11/reaction"),
        (["get-channel", "11"], "GET", "/api/channel/11"),
        (["update-channel", "11", '{"name":"Slack"}'], "PUT", "/api/channel/11"),
        (["create-cloud-migration", '{"environment":"prod"}'], "POST", "/api/cloud-migration"),
        (["cancel-cloud-migration"], "PUT", "/api/cloud-migration/cancel"),
        (["create-collection", '{"name":"New"}'], "POST", "/api/collection"),
        (["get-collection-graph"], "GET", "/api/collection/graph"),
        (["put-collection-graph", '{"groups":["admin"]}'], "PUT", "/api/collection/graph"),
        (
            ["post-collection-root-move-dashboard-question-candidates", '{"card_ids":[1]}'],
            "POST",
            "/api/collection/root/move-dashboard-question-candidates",
        ),
        (
            ["post-collection-move-dashboard-question-candidates", "7", '{"card_ids":[1]}'],
            "POST",
            "/api/collection/7/move-dashboard-question-candidates",
        ),
        (["update-collection", "7", '{"name":"New"}'], "PUT", "/api/collection/7"),
        (["get-comment"], "GET", "/api/comment"),
        (["delete-comment", "7"], "DELETE", "/api/comment/7"),
        (["delete-collection", "7"], "DELETE", "/api/collection/7"),
        (["delete-action", "11"], "DELETE", "/api/action/11"),
        (["card-collections", "1,2", "--collection-id", "root"], "POST", "/api/card/collections"),
        (["cards-dashboards", "1,2"], "POST", "/api/cards/dashboards"),
        (["list-embeddable-cards"], "GET", "/api/card/embeddable"),
        (["pivot-query", "13", '{"x":1}'], "POST", "/api/card/pivot/13/query"),
        (["list-public-cards"], "GET", "/api/card/public"),
        (["create-card-public-link", "13"], "POST", "/api/card/13/public_link"),
        (["delete-card-public-link", "13"], "DELETE", "/api/card/13/public_link"),
        (["query-card", "13", '{"x":1}'], "POST", "/api/card/13/query"),
        (["query-card-export", "13", "csv", '{"x":1}'], "POST", "/api/card/13/query/csv"),
        (["move-cards", '{"card_ids":[1],"collection_id":"root"}'], "POST", "/api/cards/move"),
        (["update-card", "13", '{"name":"copy"}'], "PUT", "/api/card/13"),
        (["delete-card", "13"], "DELETE", "/api/card/13"),
        (["copy-card", "13"], "POST", "/api/card/13/copy"),
        (["get-card-dashboards", "13"], "GET", "/api/card/13/dashboards"),
        (["get-card-param-remapping", "13", "abc"], "GET", "/api/card/13/params/abc/remapping"),
        (["get-card-query-metadata", "13"], "GET", "/api/card/13/query_metadata"),
        (["get-card-series", "13"], "GET", "/api/card/13/series"),
        (["update-action", "11", '{"name":"action"}'], "PUT", "/api/action/11"),
        (["execute-action", "11", "--parameters", '{"id":1}'], "POST", "/api/action/11/execute"),
        (["create-action-public-link", "11"], "POST", "/api/action/11/public_link"),
        (["delete-action-public-link", "11"], "DELETE", "/api/action/11/public_link"),
        (["update-bookmark-ordering", '{"ids":[1]}'], "PUT", "/api/bookmark/ordering"),
        (
            ["get-cache", "--limit", "10", "--offset", "20", "--sort-column", "name", "--sort-direction", "asc"],
            "GET",
            "/api/cache",
        ),
        (["put-cache", '{"type":"lru"}'], "PUT", "/api/cache"),
        (["delete-cache"], "DELETE", "/api/cache"),
        (["invalidate-cache", '{"dashboard":[15],"include":["question"]}'], "POST", "/api/cache/invalidate"),
        (["create-bookmark", "card", "1"], "POST", "/api/bookmark/card/1"),
        (["delete-bookmark", "card", "1"], "DELETE", "/api/bookmark/card/1"),
        (["create-api-key", '{"name":"key","group_id":1}'], "POST", "/api/api-key"),
        (["update-api-key", "7", '{"name":"key"}'], "PUT", "/api/api-key/7"),
        (["delete-api-key", "7"], "DELETE", "/api/api-key/7"),
        (["regenerate-api-key", "7"], "PUT", "/api/api-key/7/regenerate"),
        (["analyze-chart", '{"image":"base64"}'], "POST", "/api/ai-entity-analysis/analyze-chart"),
        (["delete-alert-subscription", "7"], "DELETE", "/api/alert/7/subscription"),
        (["create-analytics-event-batch", '{"events":[]}'], "POST", "/api/analytics/internal"),
        (["agent-execute", '{"query":"abc"}'], "POST", "/api/agent/v1/execute"),
        (["agent-search", '{"query":"orders"}'], "POST", "/api/agent/v1/search"),
        (["agent-construct-query", '{"source":"x"}'], "POST", "/api/agent/v2/construct-query"),
        (["agent-query", '{"source":"x"}'], "POST", "/api/agent/v2/query"),
        (["create-recent", '{"model":"card","model_id":1}'], "POST", "/api/activity/recents"),
    ],
)
def test_action_mutation_commands_cover_handwritten_surface(
    monkeypatch: pytest.MonkeyPatch,
    command: list[str],
    expected_method: str,
    expected_path: str,
) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(cli.app, ["--base-url", "http://localhost:3000", "--api-key", "abc", *command])

    assert result.exit_code == 0
    assert f'\n  "method": "{expected_method}"' in result.stdout
    assert f'\n  "path": "{expected_path}"' in result.stdout


def test_create_question_command_posts_card_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "create-question",
            "Orders",
            '{"database": 1, "type": "query", "query": {"source-table": 2}}',
            "--display",
            "table",
            "--visualization-settings",
            '{"table.pivot": false}',
            "--collection-id",
            "root",
            "--description",
            "Orders question",
        ],
    )

    assert result.exit_code == 0
    assert '\n  "method": "POST"' in result.stdout
    assert '\n  "path": "/api/card"' in result.stdout
    assert '\n    "type": "question"' in result.stdout
    assert '\n    "collection_id": "root"' in result.stdout


def test_create_card_command_rejects_non_object_dataset_query(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "create-card",
            "Orders",
            "[]",
        ],
    )

    assert result.exit_code != 0


def test_create_database_command_posts_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "create-database",
            "analytics",
            "postgres",
            "--details",
            '{"host": "db.local", "port": 5432}',
        ],
    )

    assert result.exit_code == 0
    assert '\n  "method": "POST"' in result.stdout
    assert '\n  "path": "/api/database"' in result.stdout
    assert '\n  "body"' in result.stdout


def test_create_database_command_invalid_details_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ConvenienceClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "create-database",
            "analytics",
            "postgres",
            "--details",
            "{bad-json}",
        ],
    )

    assert result.exit_code != 0


def test_error_response_is_reported_as_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _ErrorClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "current-user",
        ],
    )

    assert result.exit_code == 1
    assert '"error": ' in result.stdout + result.stderr


def test_missing_api_key_fails_fast(monkeypatch: pytest.MonkeyPatch) -> None:
    def should_not_be_called(_settings: object) -> None:
        raise AssertionError("create_client should not be used when API key is missing")

    monkeypatch.setattr(cli, "create_client", should_not_be_called)

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "current-user",
        ],
    )

    assert result.exit_code != 0
