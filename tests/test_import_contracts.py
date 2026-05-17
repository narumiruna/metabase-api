from __future__ import annotations

import importlib

import metabaseapi.cli
import metabaseapi.client
import metabaseapi.client.http
import metabaseapi.client.raw
import metabaseapi.client.typed


def test_cli_command_modules_import_from_package() -> None:
    importlib.import_module("metabaseapi.cli_commands.core")
    importlib.import_module("metabaseapi.cli_commands.dashboard")


def test_cli_command_migration_shims_importable() -> None:
    importlib.import_module("metabaseapi.cli_commands_core")
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
