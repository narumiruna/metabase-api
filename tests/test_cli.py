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

    async def list_databases(self) -> list[dict[str, object]]:
        return [{"id": 1, "name": "Main"}]


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
    monkeypatch.setattr(cli, "create_client", lambda _settings: _RequestClient())

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


def test_create_database_command_posts_json(monkeypatch: pytest.MonkeyPatch) -> None:
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
