from __future__ import annotations

import importlib

import pytest

import metabaseapi.cli
import metabaseapi.cli_commands
import metabaseapi.client
import metabaseapi.client.http
import metabaseapi.client.raw
import metabaseapi.client.typed


def test_cli_command_modules_import_from_package() -> None:
    assert len(metabaseapi.cli_commands.command_module_names()) == len(metabaseapi.cli_commands.command_module_paths())
    assert len(metabaseapi.cli_commands.COMMAND_MODULES_OBJECTS) == len(metabaseapi.cli_commands.command_module_paths())
    assert metabaseapi.cli_commands.DATA_STUDIO_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ACTION_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.AUTOMAGIC_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.API_KEY_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.AGENT_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ALERTS_COMMENTS_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ANALYTICS_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.CATALOG_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_BUG_REPORTING_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CACHE_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CHANNEL_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.DASHBOARD_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert {module.__name__ for module in metabaseapi.cli_commands.COMMAND_MODULES_OBJECTS} == set(
        metabaseapi.cli_commands.command_module_paths()
    )
    module_names = metabaseapi.cli_commands.command_module_names()
    module_paths = metabaseapi.cli_commands.command_module_paths()
    assert all(path.endswith(f".{module}") for module, path in zip(module_names, module_paths, strict=True))
    for module_path in module_paths:
        importlib.import_module(module_path)


def test_cli_command_legacy_shims_are_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands_core")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands_dashboard")


def test_client_public_exports_use_http_implementation() -> None:
    assert metabaseapi.client.MetabaseClient is metabaseapi.client.http.MetabaseClient
    assert metabaseapi.client._MetabaseClientRawMixin is metabaseapi.client.http._MetabaseClientRawMixin
    assert metabaseapi.client._MetabaseClientTypedMixin is metabaseapi.client.http._MetabaseClientTypedMixin


def test_client_raw_shim_reuses_http_export() -> None:
    assert metabaseapi.client.raw._MetabaseClientRawMixin is metabaseapi.client.http._MetabaseClientRawMixin
    assert metabaseapi.client.typed._MetabaseClientTypedMixin is metabaseapi.client.http._MetabaseClientTypedMixin


def test_cli_entrypoint_importable() -> None:
    assert hasattr(metabaseapi.cli, "app")


def test_client_public_module_exports_concrete_http_implementation() -> None:
    assert metabaseapi.client.MetabaseClient.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client._MetabaseClientRawMixin.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client._MetabaseClientTypedMixin.__module__ == "metabaseapi.client.http"
