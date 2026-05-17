from __future__ import annotations

import asyncio
import json
from collections.abc import Coroutine

import httpx
import pytest

from metabaseapi.client import MetabaseClient
from metabaseapi.client.raw import action as raw_action
from metabaseapi.client.raw import activity as raw_activity
from metabaseapi.client.raw import agent as raw_agent
from metabaseapi.client.raw import alert as raw_alert
from metabaseapi.client.raw import analytics as raw_analytics
from metabaseapi.client.raw import api_key as raw_api_key
from metabaseapi.client.raw import automagic as raw_automagic
from metabaseapi.client.raw import bookmark as raw_bookmark
from metabaseapi.client.raw import bug_reporting as raw_bug_reporting
from metabaseapi.client.raw import cache as raw_cache
from metabaseapi.client.raw import card as raw_card
from metabaseapi.client.raw import channel as raw_channel
from metabaseapi.client.raw import cloud_migration as raw_cloud_migration
from metabaseapi.client.raw import collection as raw_collection
from metabaseapi.client.raw import comment as raw_comment
from metabaseapi.client.raw import dashboard as raw_dashboard
from metabaseapi.client.raw import data_studio as raw_data_studio
from metabaseapi.client.raw import database as raw_database
from metabaseapi.client.raw import schema as raw_schema
from metabaseapi.client.raw import user as raw_user
from metabaseapi.client.raw import user_key_value as raw_user_key_value
from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError


def _run(coro: Coroutine[object, object, object]) -> object:
    return asyncio.run(coro)


def test_request_includes_api_key_and_query_parameters() -> None:
    captured: dict[str, str | dict[str, str] | None] = {}

    async def handler(_request: httpx.Request) -> httpx.Response:
        captured["url"] = str(_request.url)
        captured["method"] = _request.method
        captured["params"] = dict(_request.url.params)
        captured["x-api-key"] = _request.headers.get("X-API-Key")
        captured["accept"] = _request.headers.get("Accept")
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000/",
        api_key="abc",
        timeout_seconds=3.0,
        verify_ssl=False,
        client=httpx.AsyncClient(transport=transport, timeout=3.0, verify=False),
    )

    result = _run(client.get("/api/user/current", params={"a": "1"}))

    request_url = captured["url"]
    assert isinstance(request_url, str)
    assert request_url.startswith("http://localhost:3000/api/user/current")
    assert captured["method"] == "GET"
    assert captured["params"] == {"a": "1"}
    assert captured["x-api-key"] == "abc"
    assert captured["accept"] == "application/json"
    assert result == {"ok": True}


def test_repeated_query_parameters_are_preserved() -> None:
    captured: list[tuple[str, str]] = []

    async def handler(_request: httpx.Request) -> httpx.Response:
        captured.extend(_request.url.params.multi_items())
        return httpx.Response(200, json={"ok": True})

    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )

    result = _run(client.get("/api/search", params={"models": ["card", "dashboard"]}))

    assert result == {"ok": True}
    assert captured == [("models", "card"), ("models", "dashboard")]


def test_post_sends_json_body() -> None:
    async def handler(_request: httpx.Request) -> httpx.Response:
        assert _request.method == "POST"
        payload = json.loads(_request.content.decode())
        assert payload == {"foo": "bar"}
        return httpx.Response(200, json={"received": payload})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result = _run(client.post("/api/session", body={"foo": "bar"}))
    assert result == {"received": {"foo": "bar"}}


def test_raw_paths_cover_handwritten_endpoint_surface() -> None:
    captured: list[tuple[str, str, object | None]] = []

    async def handler(_request: httpx.Request) -> httpx.Response:
        body: object | None = None
        if _request.content:
            body = json.loads(_request.content.decode())
        captured.append((_request.method, _request.url.path, body))
        return httpx.Response(200, json={"method": _request.method, "path": _request.url.path})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="https://metabase.local",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    calls = [
        (raw_action.list_actions(client), ("GET", "/api/action", None)),
        (raw_action.create_action(client, {"name": "notify"}), ("POST", "/api/action", {"name": "notify"})),
        (raw_action.list_public_actions(client), ("GET", "/api/action/public", None)),
        (raw_action.get_action(client, 11), ("GET", "/api/action/11", None)),
        (raw_action.delete_action(client, 11), ("DELETE", "/api/action/11", None)),
        (raw_action.get_action_execute(client, 11, parameters={"id": 1}), ("GET", "/api/action/11/execute", None)),
        (raw_action.update_action(client, 11, {"name": "notify"}), ("PUT", "/api/action/11", {"name": "notify"})),
        (
            raw_action.execute_action(client, 11, parameters={"id": 1}),
            ("POST", "/api/action/11/execute", {"parameters": {"id": 1}}),
        ),
        (raw_action.create_action_public_link(client, 11), ("POST", "/api/action/11/public_link", None)),
        (raw_action.delete_action_public_link(client, 11), ("DELETE", "/api/action/11/public_link", None)),
        (raw_bookmark.list_bookmarks(client), ("GET", "/api/bookmark", None)),
        (raw_bookmark.update_bookmark_ordering(client, {"ids": [1]}), ("PUT", "/api/bookmark/ordering", {"ids": [1]})),
        (raw_bookmark.create_bookmark(client, "card", 1), ("POST", "/api/bookmark/card/1", None)),
        (raw_bookmark.delete_bookmark(client, "card", 1), ("DELETE", "/api/bookmark/card/1", None)),
        (
            raw_cache.get_cache(client, limit=10, offset=20, sort_column="name", sort_direction="asc"),
            ("GET", "/api/cache", None),
        ),
        (raw_cache.put_cache(client, {"type": "lru"}), ("PUT", "/api/cache", {"type": "lru"})),
        (raw_cache.delete_cache(client), ("DELETE", "/api/cache", None)),
        (raw_cache.delete_cache(client, {"status": "all"}), ("DELETE", "/api/cache", {"status": "all"})),
        (
            raw_cache.invalidate_cache(client, {"dashboard": [15], "include": ["question"]}),
            ("POST", "/api/cache/invalidate", None),
        ),
        (
            raw_bug_reporting.bug_reporting_connection_pool_details(client),
            ("GET", "/api/bug-reporting/connection-pool-details", None),
        ),
        (raw_bug_reporting.bug_reporting_details(client), ("GET", "/api/bug-reporting/details", None)),
        (
            raw_automagic.automagic_database_candidates(client, 1),
            ("GET", "/api/automagic-dashboards/database/1/candidates", None),
        ),
        (
            raw_automagic.automagic_model_index_primary_key(client, 2, 3),
            ("GET", "/api/automagic-dashboards/model_index/2/primary_key/3", None),
        ),
        (raw_automagic.automagic_entity(client, "table", "4"), ("GET", "/api/automagic-dashboards/table/4", None)),
        (
            raw_api_key.create_api_key(client, {"name": "key", "group_id": 1}),
            ("POST", "/api/api-key", {"name": "key", "group_id": 1}),
        ),
        (raw_api_key.list_api_keys(client), ("GET", "/api/api-key", None)),
        (raw_api_key.count_api_keys(client), ("GET", "/api/api-key/count", None)),
        (raw_api_key.update_api_key(client, 7, {"name": "key"}), ("PUT", "/api/api-key/7", {"name": "key"})),
        (raw_api_key.delete_api_key(client, 7), ("DELETE", "/api/api-key/7", None)),
        (raw_comment.get_comment(client), ("GET", "/api/comment", None)),
        (raw_comment.create_comment(client, {"text": "Hello"}), ("POST", "/api/comment", {"text": "Hello"})),
        (raw_comment.get_comment_mentions(client), ("GET", "/api/comment/mentions", None)),
        (raw_comment.update_comment(client, 7, {"text": "updated"}), ("PUT", "/api/comment/7", {"text": "updated"})),
        (
            raw_comment.post_comment_reaction(client, 7, {"emoji": "👍"}),
            ("POST", "/api/comment/7/reaction", {"emoji": "👍"}),
        ),
        (raw_comment.delete_comment(client, 7), ("DELETE", "/api/comment/7", None)),
        (raw_api_key.regenerate_api_key(client, 7), ("PUT", "/api/api-key/7/regenerate", None)),
        (
            raw_analytics.analyze_chart(client, {"image": "base64"}),
            ("POST", "/api/ai-entity-analysis/analyze-chart", {"image": "base64"}),
        ),
        (raw_alert.list_alerts(client), ("GET", "/api/alert", None)),
        (raw_alert.get_alert(client, 7), ("GET", "/api/alert/7", None)),
        (raw_alert.delete_alert_subscription(client, 7), ("DELETE", "/api/alert/7/subscription", None)),
        (raw_analytics.anonymous_stats(client), ("GET", "/api/analytics/anonymous-stats", None)),
        (
            raw_analytics.create_analytics_event_batch(client, {"events": []}),
            ("POST", "/api/analytics/internal", {"events": []}),
        ),
        (raw_agent.agent_execute(client, {"query": "abc"}), ("POST", "/api/agent/v1/execute", {"query": "abc"})),
        (raw_agent.get_agent_metric(client, 1), ("GET", "/api/agent/v1/metric/1", None)),
        (raw_agent.get_agent_metric_field_values(client, 1, 2), ("GET", "/api/agent/v1/metric/1/field/2/values", None)),
        (raw_agent.agent_ping(client), ("GET", "/api/agent/v1/ping", None)),
        (raw_agent.agent_search(client, {"query": "orders"}), ("POST", "/api/agent/v1/search", {"query": "orders"})),
        (raw_agent.get_agent_table(client, 3), ("GET", "/api/agent/v1/table/3", None)),
        (raw_agent.get_agent_table_field_values(client, 3, 4), ("GET", "/api/agent/v1/table/3/field/4/values", None)),
        (
            raw_agent.agent_construct_query(client, {"source": "x"}),
            ("POST", "/api/agent/v2/construct-query", {"source": "x"}),
        ),
        (raw_agent.agent_query(client, {"source": "x"}), ("POST", "/api/agent/v2/query", {"source": "x"})),
        (
            raw_activity.most_recently_viewed_dashboard(client),
            ("GET", "/api/activity/most_recently_viewed_dashboard", None),
        ),
        (raw_activity.list_popular_items(client), ("GET", "/api/activity/popular_items", None)),
        (raw_activity.list_recent_views(client), ("GET", "/api/activity/recent_views", None)),
        (raw_activity.list_recents(client), ("GET", "/api/activity/recents", None)),
        (
            raw_activity.create_recent(client, {"model": "card", "model_id": 1}),
            ("POST", "/api/activity/recents", {"model": "card", "model_id": 1}),
        ),
        (raw_user.current_user(client), ("GET", "/api/user/current", None)),
        (raw_database.list_databases(client), ("GET", "/api/database", None)),
        (
            raw_data_studio.data_studio_table_discard_values(client, {"table_ids": [1]}),
            ("POST", "/api/data-studio/table/discard-values", {"table_ids": [1]}),
        ),
        (
            raw_data_studio.data_studio_table_edit(client, {"table_ids": [1]}),
            ("POST", "/api/data-studio/table/edit", {"table_ids": [1]}),
        ),
        (
            raw_data_studio.data_studio_table_rescan_values(client, {"table_ids": [1]}),
            ("POST", "/api/data-studio/table/rescan-values", {"table_ids": [1]}),
        ),
        (
            raw_data_studio.data_studio_table_selection(client, {"table_ids": [1]}),
            ("POST", "/api/data-studio/table/selection", {"table_ids": [1]}),
        ),
        (
            raw_data_studio.data_studio_table_sync_schema(client, {"table_ids": [1]}),
            ("POST", "/api/data-studio/table/sync-schema", {"table_ids": [1]}),
        ),
        (raw_channel.list_channels(client), ("GET", "/api/channel", None)),
        (raw_channel.create_channel(client, {"name": "Slack"}), ("POST", "/api/channel", {"name": "Slack"})),
        (raw_channel.test_channel(client, {"name": "Slack"}), ("POST", "/api/channel/test", {"name": "Slack"})),
        (raw_channel.get_channel(client, 11), ("GET", "/api/channel/11", None)),
        (raw_channel.update_channel(client, 11, {"name": "Slack"}), ("PUT", "/api/channel/11", {"name": "Slack"})),
        (
            raw_cloud_migration.create_cloud_migration(client, {"environment": "prod"}),
            ("POST", "/api/cloud-migration", {"environment": "prod"}),
        ),
        (raw_cloud_migration.get_cloud_migration(client), ("GET", "/api/cloud-migration", None)),
        (raw_cloud_migration.cancel_cloud_migration(client), ("PUT", "/api/cloud-migration/cancel", None)),
        (raw_collection.create_collection(client, {"name": "New"}), ("POST", "/api/collection", {"name": "New"})),
        (raw_dashboard.create_dashboard(client, {"name": "Sales"}), ("POST", "/api/dashboard", {"name": "Sales"})),
        (raw_collection.get_collection(client, "7"), ("GET", "/api/collection/7", None)),
        (
            raw_collection.update_collection(client, "7", {"name": "Updated"}),
            ("PUT", "/api/collection/7", {"name": "Updated"}),
        ),
        (raw_collection.delete_collection(client, "7"), ("DELETE", "/api/collection/7", None)),
        (raw_collection.get_collection_graph(client), ("GET", "/api/collection/graph", None)),
        (
            raw_collection.put_collection_graph(client, {"groups": ["admin"]}),
            ("PUT", "/api/collection/graph", {"groups": ["admin"]}),
        ),
        (raw_collection.get_collection_root(client), ("GET", "/api/collection/root", None)),
        (
            raw_collection.get_collection_root_dashboard_question_candidates(client),
            ("GET", "/api/collection/root/dashboard-question-candidates", None),
        ),
        (
            raw_collection.get_collection_root_items(client),
            ("GET", "/api/collection/root/items", None),
        ),
        (
            raw_collection.post_collection_root_move_dashboard_question_candidates(client, {"card_ids": [1]}),
            ("POST", "/api/collection/root/move-dashboard-question-candidates", {"card_ids": [1]}),
        ),
        (
            raw_collection.post_collection_move_dashboard_question_candidates(client, 7, {"card_ids": [1]}),
            ("POST", "/api/collection/7/move-dashboard-question-candidates", {"card_ids": [1]}),
        ),
        (
            raw_collection.get_collection_dashboard_question_candidates(client, 7),
            ("GET", "/api/collection/7/dashboard-question-candidates", None),
        ),
        (
            raw_collection.get_collection_items(client, 7),
            ("GET", "/api/collection/7/items", None),
        ),
        (raw_collection.get_collection_trash(client), ("GET", "/api/collection/trash", None)),
        (raw_collection.get_collection_tree(client), ("GET", "/api/collection/tree", None)),
        (
            raw_database.create_database(client, name="analytics", engine="postgres", details={"host": "db.local"}),
            (
                "POST",
                "/api/database",
                {"name": "analytics", "engine": "postgres", "details": {"host": "db.local"}},
            ),
        ),
        (raw_database.get_database(client, 12), ("GET", "/api/database/12", None)),
        (raw_card.list_cards(client), ("GET", "/api/card", None)),
        (
            raw_card.card_collections(client, card_ids=[1, 2], collection_id="root"),
            ("POST", "/api/card/collections", {"card_ids": [1, 2], "collection_id": "root"}),
        ),
        (raw_card.list_embeddable_cards(client), ("GET", "/api/card/embeddable", None)),
        (raw_card.pivot_query(client, 13, body={"x": 1}), ("POST", "/api/card/pivot/13/query", {"x": 1})),
        (raw_card.list_public_cards(client), ("GET", "/api/card/public", None)),
        (
            raw_card.get_card_param_search_values(client, 13, "abc", "Orange"),
            ("GET", "/api/card/13/params/abc/search/Orange", None),
        ),
        (raw_card.get_card_param_values(client, 13, "abc"), ("GET", "/api/card/13/params/abc/values", None)),
        (raw_card.create_card_public_link(client, 13), ("POST", "/api/card/13/public_link", None)),
        (raw_card.delete_card_public_link(client, 13), ("DELETE", "/api/card/13/public_link", None)),
        (raw_card.query_card(client, 13, body={"x": 1}), ("POST", "/api/card/13/query", {"x": 1})),
        (
            raw_card.query_card_export(client, 13, "csv", body={"x": 1}, pivot_results=True, format_rows=False),
            ("POST", "/api/card/13/query/csv", {"x": 1}),
        ),
        (
            raw_card.create_question(
                client,
                name="Orders",
                dataset_query={"database": 1, "type": "query", "query": {"source-table": 2}},
                display="table",
                visualization_settings={"table.pivot": False},
                collection_id="root",
                description="Orders question",
            ),
            (
                "POST",
                "/api/card",
                {
                    "name": "Orders",
                    "dataset_query": {"database": 1, "type": "query", "query": {"source-table": 2}},
                    "display": "table",
                    "visualization_settings": {"table.pivot": False},
                    "type": "question",
                    "collection_id": "root",
                    "description": "Orders question",
                },
            ),
        ),
        (raw_card.get_card(client, 13), ("GET", "/api/card/13", None)),
        (raw_card.update_card(client, 13, {"name": "Updated"}), ("PUT", "/api/card/13", {"name": "Updated"})),
        (raw_card.delete_card(client, 13), ("DELETE", "/api/card/13", None)),
        (raw_card.copy_card(client, 13), ("POST", "/api/card/13/copy", None)),
        (raw_card.cards_dashboards(client, [1, 2]), ("POST", "/api/cards/dashboards", {"card_ids": [1, 2]})),
        (
            raw_card.move_cards(client, {"card_ids": [1], "collection_id": "root"}),
            ("POST", "/api/cards/move", {"card_ids": [1], "collection_id": "root"}),
        ),
        (raw_card.get_card_dashboards(client, 13), ("GET", "/api/card/13/dashboards", None)),
        (raw_card.get_card_param_remapping(client, 13, "abc"), ("GET", "/api/card/13/params/abc/remapping", None)),
        (raw_card.get_card_query_metadata(client, 13), ("GET", "/api/card/13/query_metadata", None)),
        (raw_card.get_card_series(client, 13), ("GET", "/api/card/13/series", None)),
        (raw_dashboard.list_dashboards(client), ("GET", "/api/dashboard", None)),
        (raw_dashboard.get_dashboard(client, 14), ("GET", "/api/dashboard/14", None)),
        (
            raw_dashboard.query_dashboard_card(client, 14, "22", "33", {"x": 1}),
            ("POST", "/api/dashboard/14/dashcard/22/card/33/query", {"x": 1}),
        ),
        (
            raw_dashboard.query_dashboard_card_export(
                client, 14, "22", "33", "xlsx", {"x": 1}, pivot_results=True, format_rows=False
            ),
            ("POST", "/api/dashboard/14/dashcard/22/card/33/query/xlsx", {"x": 1}),
        ),
        (
            raw_dashboard.query_dashboard_card_pivot(client, 14, "22", "33", {"x": 1}),
            ("POST", "/api/dashboard/pivot/14/dashcard/22/card/33/query", {"x": 1}),
        ),
        (raw_dashboard.save_dashboard(client, {"name": "Sales"}), ("POST", "/api/dashboard/save", {"name": "Sales"})),
        (
            raw_dashboard.save_dashboard_to_collection(client, "root", {"name": "Sales"}),
            ("POST", "/api/dashboard/save/collection/root", {"name": "Sales"}),
        ),
        (
            raw_dashboard.get_dashboard_dashcard_execute(client, 14, "22", parameters={"id": 1}),
            ("GET", "/api/dashboard/14/dashcard/22/execute", None),
        ),
        (
            raw_dashboard.execute_dashboard_dashcard(client, 14, "22", parameters={"id": 1}),
            ("POST", "/api/dashboard/14/dashcard/22/execute", {"parameters": {"id": 1}}),
        ),
        (raw_dashboard.create_dashboard_public_link(client, 14), ("POST", "/api/dashboard/14/public_link", None)),
        (raw_dashboard.delete_dashboard_public_link(client, 14), ("DELETE", "/api/dashboard/14/public_link", None)),
        (raw_dashboard.copy_dashboard(client, 14), ("POST", "/api/dashboard/14/copy", None)),
        (raw_dashboard.delete_dashboard(client, 14), ("DELETE", "/api/dashboard/14", None)),
        (
            raw_dashboard.update_dashboard(client, 14, {"name": "Sales"}),
            ("PUT", "/api/dashboard/14", {"name": "Sales"}),
        ),
        (
            raw_dashboard.update_dashboard_cards(client, 14, {"cards": []}),
            ("PUT", "/api/dashboard/14/cards", {"cards": []}),
        ),
        (raw_dashboard.get_dashboard_items(client, 14), ("GET", "/api/dashboard/14/items", None)),
        (
            raw_dashboard.get_dashboard_param_remapping(client, 14, "abc"),
            ("GET", "/api/dashboard/14/params/abc/remapping", None),
        ),
        (
            raw_dashboard.get_dashboard_param_search_values(client, 14, "abc", "Orange"),
            ("GET", "/api/dashboard/14/params/abc/search/Orange", None),
        ),
        (
            raw_dashboard.get_dashboard_param_values(client, 14, "abc"),
            ("GET", "/api/dashboard/14/params/abc/values", None),
        ),
        (raw_dashboard.get_dashboard_query_metadata(client, 14), ("GET", "/api/dashboard/14/query_metadata", None)),
        (raw_dashboard.get_dashboard_related(client, 14), ("GET", "/api/dashboard/14/related", None)),
        (
            raw_dashboard.get_dashboard_params_valid_filter_fields(client, filtered=[11], filtering=[22]),
            ("GET", "/api/dashboard/params/valid-filter-fields", None),
        ),
        (raw_dashboard.get_dashboard_embeddable(client), ("GET", "/api/dashboard/embeddable", None)),
        (raw_dashboard.get_dashboard_public(client), ("GET", "/api/dashboard/public", None)),
        (raw_user.list_users(client), ("GET", "/api/user", None)),
        (raw_user.get_user(client, 15), ("GET", "/api/user/15", None)),
        (
            raw_user_key_value.get_user_key_value_namespace(client, "user"),
            ("GET", "/api/user-key-value/namespace/user", None),
        ),
        (
            raw_user_key_value.put_user_key_value_namespace_key(client, "user", "foo", {"value": "bar"}),
            ("PUT", "/api/user-key-value/namespace/user/key/foo", {"value": "bar"}),
        ),
        (
            raw_user_key_value.get_user_key_value_namespace_key(client, "user", "foo"),
            ("GET", "/api/user-key-value/namespace/user/key/foo", None),
        ),
        (
            raw_user_key_value.delete_user_key_value_namespace_key(client, "user", "foo"),
            ("DELETE", "/api/user-key-value/namespace/user/key/foo", None),
        ),
        (raw_collection.list_collections(client), ("GET", "/api/collection", None)),
        (raw_collection.get_collection(client, "root"), ("GET", "/api/collection/root", None)),
        (raw_schema.list_tables(client), ("GET", "/api/table", None)),
        (raw_schema.get_table(client, 16), ("GET", "/api/table/16", None)),
        (raw_schema.get_field(client, 17), ("GET", "/api/field/17", None)),
    ]

    for coro, _expected in calls:
        _run(coro)

    assert captured == [expected for _coro, expected in calls]


def test_http_error_is_mapped_to_client_error() -> None:
    async def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"message": "not found"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseHTTPStatusError) as exc:
        _run(client.get("/api/card/1"))

    assert exc.value.status_code == 404


def test_decode_error_for_invalid_json() -> None:
    async def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"not-json", headers={"content-type": "application/json"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseDecodeError):
        _run(client.get("/api/card/1"))


def test_non_json_payload_is_wrapped_as_json_text() -> None:
    async def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"ok", headers={"content-type": "text/plain"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result = _run(client.get("/api/health"))
    assert result == {"content_type": "text/plain", "text": "ok"}


class _RunRequest:
    async def do(self, client: MetabaseClient) -> str:
        _ = client
        return "ok"


def test_run_seam_executes_request_model() -> None:
    client = MetabaseClient(base_url="http://localhost:3000", api_key="abc")
    request = _RunRequest()

    result = _run(client.run(request))

    assert result == "ok"


def test_network_error_is_mapped() -> None:
    async def handler(_request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("timeout")

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseNetworkError):
        _run(client.get("/api/card/1"))
