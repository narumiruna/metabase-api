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


class _RequestClient(_ClientWithRequestMethods):
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, str] | None = None,
        json_data: dict[str, object] | list[object] | str | int | float | bool | None = None,
    ) -> dict[str, object]:
        return {"method": method, "path": path, "params": params, "body": json_data}

    async def get(self, path: str, *, params: dict[str, str] | None = None) -> dict[str, object]:
        return {"method": "GET", "path": path, "params": params}

    async def post(
        self,
        path: str,
        *,
        params: dict[str, str] | None = None,
        body: dict[str, object] | list[object] | str | int | float | bool | None = None,
    ) -> dict[str, object]:
        return {"method": "POST", "path": path, "params": params, "body": body}


class _ConvenienceClient(_ClientWithRequestMethods):
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

    async def list_fields(self) -> dict[str, object]:
        return {"method": "GET", "path": "/api/field"}

    async def get_field(self, field_id: str) -> dict[str, object]:
        return {"method": "GET", "path": f"/api/field/{field_id}"}


class _ErrorClient(_ClientWithRequestMethods):
    async def get(self, *_: object, **__: object) -> dict[str, str]:
        raise MetabaseHTTPStatusError(401, {"message": "unauthorized"})

    async def current_user(self) -> dict[str, str]:
        raise MetabaseHTTPStatusError(401, {"message": "unauthorized"})


def test_request_command_outputs_json(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _RequestClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "request",
            "GET",
            "/api/user/current",
            "-q",
            "a=1",
            "-q",
            "b=2",
        ],
    )

    assert result.exit_code == 0
    assert '\n  "path": "/api/user/current"' in result.stdout
    assert '\n  "method": "GET"' in result.stdout


def test_invoke_command_behaves_like_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _RequestClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "invoke",
            "POST",
            "/api/database",
            "--body",
            '{"name": "analytics"}',
        ],
    )

    assert result.exit_code == 0
    assert '\n  "method": "POST"' in result.stdout
    assert '\n  "path": "/api/database"' in result.stdout


def test_help_lists_every_convenience_command() -> None:
    result = runner.invoke(cli.app, ["--help"])

    assert result.exit_code == 0
    for command in [
        "current-user",
        "list-databases",
        "create-database",
        "get-database",
        "list-cards",
        "get-card",
        "list-dashboards",
        "get-dashboard",
        "list-users",
        "get-user",
        "list-collections",
        "get-collection",
        "list-tables",
        "get-table",
        "list-fields",
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
        (["list-databases"], "/api/database"),
        (["list-cards"], "/api/card"),
        (["list-dashboards"], "/api/dashboard"),
        (["list-users"], "/api/user"),
        (["list-collections"], "/api/collection"),
        (["list-tables"], "/api/table"),
        (["list-fields"], "/api/field"),
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
    monkeypatch.setattr(cli, "create_client", lambda _settings: _RequestClient())

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


def test_invoke_rejects_unknown_method(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "create_client", lambda _settings: _RequestClient())

    result = runner.invoke(
        cli.app,
        [
            "--base-url",
            "http://localhost:3000",
            "--api-key",
            "abc",
            "invoke",
            "OPTIONS",
            "/api/user/current",
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
            "request",
            "GET",
            "/api/user/current",
        ],
    )

    assert result.exit_code != 0
