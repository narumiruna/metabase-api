from __future__ import annotations

import pytest

from metabaseapi import settings


def test_load_runtime_settings_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("METABASE_URL", "https://metabase.local")
    monkeypatch.setenv("METABASE_API_KEY", "env-key")
    monkeypatch.setenv("METABASE_TIMEOUT_SECONDS", "12.5")
    monkeypatch.setenv("METABASE_VERIFY_SSL", "false")

    loaded = settings.load_runtime_settings()

    assert loaded.base_url == "https://metabase.local"
    assert loaded.api_key == "env-key"
    assert loaded.timeout_seconds == 12.5
    assert loaded.verify_ssl is False


def test_load_runtime_settings_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("METABASE_URL", "https://metabase.local")
    monkeypatch.setenv("METABASE_API_KEY", "env-key")

    loaded = settings.load_runtime_settings(
        base_url="https://override.local",
        api_key="override-key",
        timeout_seconds=9.5,
        verify_ssl=True,
    )

    assert loaded.base_url == "https://override.local"
    assert loaded.api_key == "override-key"
    assert loaded.timeout_seconds == 9.5
    assert loaded.verify_ssl is True


def test_requires_api_key_errors_without_key() -> None:
    config = settings.Settings(METABASE_URL="https://metabase.local", METABASE_API_KEY=None)
    with pytest.raises(ValueError, match="METABASE_API_KEY is required"):
        config.requires_api_key()
