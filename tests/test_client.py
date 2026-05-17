from __future__ import annotations

import asyncio
import json
from collections.abc import Coroutine

import httpx
import pytest

from metabaseapi.client import MetabaseClient
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


def test_convenience_paths_cover_handwritten_endpoint_surface() -> None:
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
        (client.list_actions(), ("GET", "/api/action", None)),
        (client.create_action({"name": "notify"}), ("POST", "/api/action", {"name": "notify"})),
        (client.list_public_actions(), ("GET", "/api/action/public", None)),
        (client.get_action(11), ("GET", "/api/action/11", None)),
        (client.delete_action(11), ("DELETE", "/api/action/11", None)),
        (client.get_action_execute(11, parameters={"id": 1}), ("GET", "/api/action/11/execute", None)),
        (client.update_action(11, {"name": "notify"}), ("PUT", "/api/action/11", {"name": "notify"})),
        (
            client.execute_action(11, parameters={"id": 1}),
            ("POST", "/api/action/11/execute", {"parameters": {"id": 1}}),
        ),
        (client.create_action_public_link(11), ("POST", "/api/action/11/public_link", None)),
        (client.delete_action_public_link(11), ("DELETE", "/api/action/11/public_link", None)),
        (client.list_bookmarks(), ("GET", "/api/bookmark", None)),
        (client.update_bookmark_ordering({"ids": [1]}), ("PUT", "/api/bookmark/ordering", {"ids": [1]})),
        (client.create_bookmark("card", 1), ("POST", "/api/bookmark/card/1", None)),
        (client.delete_bookmark("card", 1), ("DELETE", "/api/bookmark/card/1", None)),
        (client.get_cache(limit=10, offset=20, sort_column="name", sort_direction="asc"), ("GET", "/api/cache", None)),
        (client.put_cache({"type": "lru"}), ("PUT", "/api/cache", {"type": "lru"})),
        (client.delete_cache(), ("DELETE", "/api/cache", None)),
        (client.delete_cache({"status": "all"}), ("DELETE", "/api/cache", {"status": "all"})),
        (
            client.invalidate_cache({"dashboard": [15], "include": ["question"]}),
            ("POST", "/api/cache/invalidate", None),
        ),
        (client.bug_reporting_connection_pool_details(), ("GET", "/api/bug-reporting/connection-pool-details", None)),
        (client.bug_reporting_details(), ("GET", "/api/bug-reporting/details", None)),
        (client.automagic_database_candidates(1), ("GET", "/api/automagic-dashboards/database/1/candidates", None)),
        (
            client.automagic_model_index_primary_key(2, 3),
            ("GET", "/api/automagic-dashboards/model_index/2/primary_key/3", None),
        ),
        (client.automagic_entity("table", "4"), ("GET", "/api/automagic-dashboards/table/4", None)),
        (
            client.create_api_key({"name": "key", "group_id": 1}),
            ("POST", "/api/api-key", {"name": "key", "group_id": 1}),
        ),
        (client.list_api_keys(), ("GET", "/api/api-key", None)),
        (client.count_api_keys(), ("GET", "/api/api-key/count", None)),
        (client.update_api_key(7, {"name": "key"}), ("PUT", "/api/api-key/7", {"name": "key"})),
        (client.delete_api_key(7), ("DELETE", "/api/api-key/7", None)),
        (client.regenerate_api_key(7), ("PUT", "/api/api-key/7/regenerate", None)),
        (
            client.analyze_chart({"image": "base64"}),
            ("POST", "/api/ai-entity-analysis/analyze-chart", {"image": "base64"}),
        ),
        (client.list_alerts(), ("GET", "/api/alert", None)),
        (client.get_alert(7), ("GET", "/api/alert/7", None)),
        (client.delete_alert_subscription(7), ("DELETE", "/api/alert/7/subscription", None)),
        (client.anonymous_stats(), ("GET", "/api/analytics/anonymous-stats", None)),
        (client.create_analytics_event_batch({"events": []}), ("POST", "/api/analytics/internal", {"events": []})),
        (client.agent_execute({"query": "abc"}), ("POST", "/api/agent/v1/execute", {"query": "abc"})),
        (client.get_agent_metric(1), ("GET", "/api/agent/v1/metric/1", None)),
        (client.get_agent_metric_field_values(1, 2), ("GET", "/api/agent/v1/metric/1/field/2/values", None)),
        (client.agent_ping(), ("GET", "/api/agent/v1/ping", None)),
        (client.agent_search({"query": "orders"}), ("POST", "/api/agent/v1/search", {"query": "orders"})),
        (client.get_agent_table(3), ("GET", "/api/agent/v1/table/3", None)),
        (client.get_agent_table_field_values(3, 4), ("GET", "/api/agent/v1/table/3/field/4/values", None)),
        (client.agent_construct_query({"source": "x"}), ("POST", "/api/agent/v2/construct-query", {"source": "x"})),
        (client.agent_query({"source": "x"}), ("POST", "/api/agent/v2/query", {"source": "x"})),
        (client.most_recently_viewed_dashboard(), ("GET", "/api/activity/most_recently_viewed_dashboard", None)),
        (client.list_popular_items(), ("GET", "/api/activity/popular_items", None)),
        (client.list_recent_views(), ("GET", "/api/activity/recent_views", None)),
        (client.list_recents(), ("GET", "/api/activity/recents", None)),
        (
            client.create_recent({"model": "card", "model_id": 1}),
            ("POST", "/api/activity/recents", {"model": "card", "model_id": 1}),
        ),
        (client.current_user(), ("GET", "/api/user/current", None)),
        (client.list_databases(), ("GET", "/api/database", None)),
        (client.list_channels(), ("GET", "/api/channel", None)),
        (client.create_channel({"name": "Slack"}), ("POST", "/api/channel", {"name": "Slack"})),
        (client.test_channel({"name": "Slack"}), ("POST", "/api/channel/test", {"name": "Slack"})),
        (client.get_channel(11), ("GET", "/api/channel/11", None)),
        (client.update_channel(11, {"name": "Slack"}), ("PUT", "/api/channel/11", {"name": "Slack"})),
        (
            client.create_cloud_migration({"environment": "prod"}),
            ("POST", "/api/cloud-migration", {"environment": "prod"}),
        ),
        (client.get_cloud_migration(), ("GET", "/api/cloud-migration", None)),
        (client.cancel_cloud_migration(), ("PUT", "/api/cloud-migration/cancel", None)),
        (client.create_collection({"name": "New"}), ("POST", "/api/collection", {"name": "New"})),
        (client.get_collection_graph(), ("GET", "/api/collection/graph", None)),
        (client.put_collection_graph({"groups": ["admin"]}), ("PUT", "/api/collection/graph", {"groups": ["admin"]})),
        (client.get_collection_root(), ("GET", "/api/collection/root", None)),
        (
            client.get_collection_root_dashboard_question_candidates(),
            ("GET", "/api/collection/root/dashboard-question-candidates", None),
        ),
        (
            client.get_collection_root_items(),
            ("GET", "/api/collection/root/items", None),
        ),
        (
            client.post_collection_root_move_dashboard_question_candidates({"card_ids": [1]}),
            ("POST", "/api/collection/root/move-dashboard-question-candidates", {"card_ids": [1]}),
        ),
        (
            client.create_database(name="analytics", engine="postgres", details={"host": "db.local"}),
            (
                "POST",
                "/api/database",
                {"name": "analytics", "engine": "postgres", "details": {"host": "db.local"}},
            ),
        ),
        (client.get_database(12), ("GET", "/api/database/12", None)),
        (client.list_cards(), ("GET", "/api/card", None)),
        (
            client.card_collections(card_ids=[1, 2], collection_id="root"),
            ("POST", "/api/card/collections", {"card_ids": [1, 2], "collection_id": "root"}),
        ),
        (client.list_embeddable_cards(), ("GET", "/api/card/embeddable", None)),
        (client.pivot_query(13, body={"x": 1}), ("POST", "/api/card/pivot/13/query", {"x": 1})),
        (client.list_public_cards(), ("GET", "/api/card/public", None)),
        (
            client.get_card_param_search_values(13, "abc", "Orange"),
            ("GET", "/api/card/13/params/abc/search/Orange", None),
        ),
        (client.get_card_param_values(13, "abc"), ("GET", "/api/card/13/params/abc/values", None)),
        (client.create_card_public_link(13), ("POST", "/api/card/13/public_link", None)),
        (client.delete_card_public_link(13), ("DELETE", "/api/card/13/public_link", None)),
        (client.query_card(13, body={"x": 1}), ("POST", "/api/card/13/query", {"x": 1})),
        (
            client.query_card_export(13, "csv", body={"x": 1}, pivot_results=True, format_rows=False),
            ("POST", "/api/card/13/query/csv", {"x": 1}),
        ),
        (
            client.create_question(
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
        (client.get_card(13), ("GET", "/api/card/13", None)),
        (client.update_card(13, {"name": "Updated"}), ("PUT", "/api/card/13", {"name": "Updated"})),
        (client.delete_card(13), ("DELETE", "/api/card/13", None)),
        (client.copy_card(13), ("POST", "/api/card/13/copy", None)),
        (client.cards_dashboards([1, 2]), ("POST", "/api/cards/dashboards", {"card_ids": [1, 2]})),
        (
            client.move_cards({"card_ids": [1], "collection_id": "root"}),
            ("POST", "/api/cards/move", {"card_ids": [1], "collection_id": "root"}),
        ),
        (client.get_card_dashboards(13), ("GET", "/api/card/13/dashboards", None)),
        (client.get_card_param_remapping(13, "abc"), ("GET", "/api/card/13/params/abc/remapping", None)),
        (client.get_card_query_metadata(13), ("GET", "/api/card/13/query_metadata", None)),
        (client.get_card_series(13), ("GET", "/api/card/13/series", None)),
        (client.list_dashboards(), ("GET", "/api/dashboard", None)),
        (client.get_dashboard(14), ("GET", "/api/dashboard/14", None)),
        (client.list_users(), ("GET", "/api/user", None)),
        (client.get_user(15), ("GET", "/api/user/15", None)),
        (client.list_collections(), ("GET", "/api/collection", None)),
        (client.get_collection("root"), ("GET", "/api/collection/root", None)),
        (client.list_tables(), ("GET", "/api/table", None)),
        (client.get_table(16), ("GET", "/api/table/16", None)),
        (client.get_field(17), ("GET", "/api/field/17", None)),
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
