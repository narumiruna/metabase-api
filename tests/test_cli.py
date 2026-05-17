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

    async def get_collection(self, collection_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/collection/{collection_id}"}

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
        "create-database",
        "get-database",
        "list-cards",
        "create-card",
        "create-question",
        "get-card",
        "list-dashboards",
        "get-dashboard",
        "list-users",
        "get-user",
        "list-collections",
        "get-collection",
        "list-tables",
        "get-table",
        "get-field",
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
        (["get-agent-metric", "1"], "/api/agent/v1/metric/1"),
        (["get-agent-metric-field-values", "1", "2"], "/api/agent/v1/metric/1/field/2/values"),
        (["agent-ping"], "/api/agent/v1/ping"),
        (["get-agent-table", "3"], "/api/agent/v1/table/3"),
        (["get-agent-table-field-values", "3", "4"], "/api/agent/v1/table/3/field/4/values"),
        (["most-recently-viewed-dashboard"], "/api/activity/most_recently_viewed_dashboard"),
        (["list-popular-items"], "/api/activity/popular_items"),
        (["list-recent-views"], "/api/activity/recent_views"),
        (["list-recents"], "/api/activity/recents"),
        (["list-databases"], "/api/database"),
        (["list-cards"], "/api/card"),
        (["list-dashboards"], "/api/dashboard"),
        (["list-users"], "/api/user"),
        (["list-collections"], "/api/collection"),
        (["list-tables"], "/api/table"),
        (["get-database", "12"], "/api/database/12"),
        (["get-card", "13"], "/api/card/13"),
        (["get-dashboard", "14"], "/api/dashboard/14"),
        (["get-user", "15"], "/api/user/15"),
        (["get-collection", "root"], "/api/collection/root"),
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
        (["delete-action", "11"], "DELETE", "/api/action/11"),
        (["update-action", "11", '{"name":"action"}'], "PUT", "/api/action/11"),
        (["execute-action", "11", "--parameters", '{"id":1}'], "POST", "/api/action/11/execute"),
        (["create-action-public-link", "11"], "POST", "/api/action/11/public_link"),
        (["delete-action-public-link", "11"], "DELETE", "/api/action/11/public_link"),
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
