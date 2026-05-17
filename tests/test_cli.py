from __future__ import annotations

import json

import pytest
from pydantic import BaseModel
from typer.testing import CliRunner

from metabaseapi import cli
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.errors import MetabaseHTTPStatusError

runner = CliRunner()
_LAST_CALL: dict[str, object] = {}


def _contains_mapping(payload: object, expected: dict[str, object]) -> bool:
    if isinstance(payload, dict):
        mapping = dict(payload)
        if all(mapping.get(key) == value for key, value in expected.items()):
            return True
        return any(_contains_mapping(value, expected) for value in mapping.values())
    if isinstance(payload, list):
        return any(_contains_mapping(item, expected) for item in payload)
    return False


def _assert_json_contains(stdout: str, expected: dict[str, object]) -> None:
    payload = json.loads(stdout)
    assert _contains_mapping(payload, expected) or _contains_mapping(_LAST_CALL, expected)


class _ClientWithRequestMethods:
    async def __aenter__(self) -> _ClientWithRequestMethods:
        return self

    async def __aexit__(self, *_: object) -> None:
        return None

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: object | None = None,
        json_data: object | None = None,
    ) -> dict[str, object]:
        if path == "/api/user/current":
            return {"name": "Alice"}
        call = {"method": method, "path": path, "params": params, "body": json_data}
        _LAST_CALL.clear()
        _LAST_CALL.update(call)
        return {
            **call,
            "actions": [call],
            "alerts": [call],
            "api_keys": [call],
            "bookmarks": [call],
            "candidates": [call],
            "cards": [call],
            "channels": [call],
            "collections": [call],
            "comments": [call],
            "dashboards": [call],
            "databases": [call],
            "fields": [call],
            "items": [call],
            "mentions": [call],
            "series": [call],
            "tables": [call],
            "users": [call],
            "values": [call],
        }

    async def run(self, request_model: EndpointRequest[BaseModel]) -> object:
        return await request_model.do(self)


class _ErrorClient(_ClientWithRequestMethods):
    async def _request(self, *_: object, **__: object) -> dict[str, object]:
        raise MetabaseHTTPStatusError(401, {"message": "unauthorized"})


class _RunSpyClient:
    def __init__(self) -> None:
        self.request_model: EndpointRequest[BaseModel] | None = None

    async def __aenter__(self) -> _RunSpyClient:
        return self

    async def __aexit__(self, *_: object) -> None:
        return None

    async def run(self, request_model: EndpointRequest[BaseModel]) -> BaseModel:
        self.request_model = request_model
        return request_model.response_model.model_validate({})


def test_help_omits_raw_request_commands() -> None:
    result = runner.invoke(cli.app, ["--help"])

    assert result.exit_code == 0
    assert "request" not in result.stdout
    assert "invoke" not in result.stdout


def test_help_lists_every_endpoint_command() -> None:
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
        "data-studio-table-discard-values",
        "data-studio-table-edit",
        "data-studio-table-rescan-values",
        "data-studio-table-selection",
        "data-studio-table-sync-schema",
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
        "query-dashboard-card",
        "query-dashboard-card-export",
        "query-dashboard-card-pivot",
        "get-dashboard-embeddable",
        "get-dashboard-public",
        "create-dashboard",
        "save-dashboard",
        "save-dashboard-to-collection",
        "get-dashboard-dashcard-execute",
        "execute-dashboard-dashcard",
        "create-dashboard-public-link",
        "delete-dashboard-public-link",
        "copy-dashboard",
        "delete-dashboard",
        "update-dashboard",
        "update-dashboard-cards",
        "get-dashboard-items",
        "get-dashboard-param-remapping",
        "get-dashboard-param-search",
        "get-dashboard-param-values",
        "get-dashboard-query-metadata",
        "get-dashboard-related",
        "list-users",
        "get-user",
        "get-user-key-value-namespace",
        "put-user-key-value-namespace-key",
        "get-user-key-value-namespace-key",
        "delete-user-key-value-namespace-key",
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
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    _assert_json_contains(result.stdout, {"method": "GET", "path": "/api/database/12"})


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
        (
            ["get-dashboard-params-valid-filter-fields", "--filtered", "11", "--filtering", "22"],
            "/api/dashboard/params/valid-filter-fields",
        ),
        (["get-dashboard-dashcard-execute", "14", "22"], "/api/dashboard/14/dashcard/22/execute"),
        (["get-dashboard-embeddable"], "/api/dashboard/embeddable"),
        (["get-dashboard-public"], "/api/dashboard/public"),
        (["get-dashboard-items", "14"], "/api/dashboard/14/items"),
        (["get-dashboard-param-remapping", "14", "abc"], "/api/dashboard/14/params/abc/remapping"),
        (["get-dashboard-param-search", "14", "abc", "Orange"], "/api/dashboard/14/params/abc/search/Orange"),
        (["get-dashboard-param-values", "14", "abc"], "/api/dashboard/14/params/abc/values"),
        (["get-dashboard-query-metadata", "14"], "/api/dashboard/14/query_metadata"),
        (["get-dashboard-related", "14"], "/api/dashboard/14/related"),
        (["get-user", "15"], "/api/user/15"),
        (["get-user-key-value-namespace", "user"], "/api/user-key-value/namespace/user"),
        (["get-user-key-value-namespace-key", "user", "foo"], "/api/user-key-value/namespace/user/key/foo"),
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
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

    result = runner.invoke(
        cli.app,
        ["--base-url", "http://localhost:3000", "--api-key", "abc", *command],
    )

    assert result.exit_code == 0
    _assert_json_contains(result.stdout, {"method": "GET", "path": expected_path})


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
        (["create-dashboard", '{"name":"Sales"}'], "POST", "/api/dashboard"),
        (["query-dashboard-card", "14", "22", "33", '{"x":1}'], "POST", "/api/dashboard/14/dashcard/22/card/33/query"),
        (
            ["query-dashboard-card-export", "14", "22", "33", "xlsx", '{"x":1}'],
            "POST",
            "/api/dashboard/14/dashcard/22/card/33/query/xlsx",
        ),
        (
            ["query-dashboard-card-pivot", "14", "22", "33", '{"x":1}'],
            "POST",
            "/api/dashboard/pivot/14/dashcard/22/card/33/query",
        ),
        (["save-dashboard", '{"name":"Sales"}'], "POST", "/api/dashboard/save"),
        (["save-dashboard-to-collection", "root", '{"name":"Sales"}'], "POST", "/api/dashboard/save/collection/root"),
        (
            ["execute-dashboard-dashcard", "14", "22", "--parameters", '{"id":1}'],
            "POST",
            "/api/dashboard/14/dashcard/22/execute",
        ),
        (["create-dashboard-public-link", "14"], "POST", "/api/dashboard/14/public_link"),
        (["delete-dashboard-public-link", "14"], "DELETE", "/api/dashboard/14/public_link"),
        (["copy-dashboard", "14"], "POST", "/api/dashboard/14/copy"),
        (["delete-dashboard", "14"], "DELETE", "/api/dashboard/14"),
        (["update-dashboard", "14", '{"name":"Sales"}'], "PUT", "/api/dashboard/14"),
        (["update-dashboard-cards", "14", '{"cards":[]}'], "PUT", "/api/dashboard/14/cards"),
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
        (
            ["data-studio-table-discard-values", '{"table_ids":[1]}'],
            "POST",
            "/api/data-studio/table/discard-values",
        ),
        (["data-studio-table-edit", '{"table_ids":[1]}'], "POST", "/api/data-studio/table/edit"),
        (
            ["data-studio-table-rescan-values", '{"table_ids":[1]}'],
            "POST",
            "/api/data-studio/table/rescan-values",
        ),
        (["data-studio-table-selection", '{"table_ids":[1]}'], "POST", "/api/data-studio/table/selection"),
        (["data-studio-table-sync-schema", '{"table_ids":[1]}'], "POST", "/api/data-studio/table/sync-schema"),
        (
            ["put-user-key-value-namespace-key", "user", "foo", '{"value":"bar"}'],
            "PUT",
            "/api/user-key-value/namespace/user/key/foo",
        ),
        (
            ["delete-user-key-value-namespace-key", "user", "foo"],
            "DELETE",
            "/api/user-key-value/namespace/user/key/foo",
        ),
    ],
)
def test_action_mutation_commands_cover_handwritten_surface(
    monkeypatch: pytest.MonkeyPatch,
    command: list[str],
    expected_method: str,
    expected_path: str,
) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

    result = runner.invoke(cli.app, ["--base-url", "http://localhost:3000", "--api-key", "abc", *command])

    assert result.exit_code == 0
    _assert_json_contains(result.stdout, {"method": expected_method, "path": expected_path})


@pytest.mark.parametrize(
    ("command", "expected_body"),
    [
        (["card-collections", "1,abc", "--collection-id", "root"], {"card_ids": [1, "abc"], "collection_id": "root"}),
        (["cards-dashboards", "1,abc"], {"card_ids": [1, "abc"]}),
    ],
)
def test_card_id_csv_commands_coerce_numeric_ids(
    monkeypatch: pytest.MonkeyPatch,
    command: list[str],
    expected_body: dict[str, object],
) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

    result = runner.invoke(cli.app, ["--base-url", "http://localhost:3000", "--api-key", "abc", *command])

    assert result.exit_code == 0
    assert _LAST_CALL["body"] == expected_body


@pytest.mark.parametrize(
    "command",
    [
        ["pivot-query", "13"],
        ["query-card", "13"],
        ["query-card-export", "13", "csv"],
    ],
)
def test_card_query_commands_default_missing_body_to_empty_object(
    monkeypatch: pytest.MonkeyPatch,
    command: list[str],
) -> None:
    spy = _RunSpyClient()
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: spy)

    result = runner.invoke(cli.app, ["--base-url", "http://localhost:3000", "--api-key", "abc", *command])

    assert result.exit_code == 0
    assert spy.request_model is not None
    assert spy.request_model.model_dump()["body"] == {}


def test_create_question_command_posts_card_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    _assert_json_contains(result.stdout, {"method": "POST", "path": "/api/card"})
    assert _LAST_CALL["body"] == {
        "name": "Orders",
        "dataset_query": {"database": 1, "type": "query", "query": {"source-table": 2}},
        "display": "table",
        "visualization_settings": {"table.pivot": False},
        "type": "question",
        "collection_id": "root",
        "description": "Orders question",
    }


def test_create_card_command_preserves_card_type(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "create-card",
            "Orders",
            '{"database": 1, "type": "query", "query": {"source-table": 2}}',
            "--type",
            "model",
        ],
    )

    assert result.exit_code == 0
    assert _LAST_CALL["body"] == {
        "name": "Orders",
        "dataset_query": {"database": 1, "type": "query", "query": {"source-table": 2}},
        "display": "table",
        "visualization_settings": {},
        "type": "model",
    }


def test_create_card_command_rejects_non_object_dataset_query(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    _assert_json_contains(result.stdout, {"method": "POST", "path": "/api/database"})
    assert _LAST_CALL["body"] == {
        "name": "analytics",
        "engine": "postgres",
        "details": {"host": "db.local", "port": 5432},
    }


def test_create_database_command_invalid_details_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ClientWithRequestMethods())

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
    monkeypatch.setattr(cli.runtime, "create_client", lambda _settings: _ErrorClient())

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

    monkeypatch.setattr(cli.runtime, "create_client", should_not_be_called)

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "current-user",
        ],
    )

    assert result.exit_code != 0
