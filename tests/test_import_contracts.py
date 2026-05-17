from __future__ import annotations

import importlib
import os
import re
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

import pytest

import metabaseapi.cli
import metabaseapi.cli_commands
import metabaseapi.client
import metabaseapi.client.http
import metabaseapi.client.raw
import metabaseapi.client.typed


def test_cli_command_modules_import_from_package() -> None:
    assert len(metabaseapi.cli_commands.command_module_names()) == len(metabaseapi.cli_commands.command_module_paths())
    assert len(metabaseapi.cli_commands.command_module_objects()) == len(
        metabaseapi.cli_commands.command_module_paths()
    )
    assert metabaseapi.cli_commands.DATA_STUDIO_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ACTION_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ACTIVITY_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.AUTOMAGIC_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.API_KEY_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.AGENT_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ALERT_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.COMMENT_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.ANALYTICS_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.CARD_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.CARD_QUERY_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.COLLECTION_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.DATABASE_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.DASHBOARD_QUERY_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.USER_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.SCHEMA_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_BUG_REPORTING_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CACHE_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CHANNEL_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.DASHBOARD_COMMAND_MODULE in metabaseapi.cli_commands.COMMAND_MODULES
    assert {module.__name__ for module in metabaseapi.cli_commands.command_module_objects()} == set(
        metabaseapi.cli_commands.command_module_paths()
    )
    module_names = metabaseapi.cli_commands.command_module_names()
    module_paths = metabaseapi.cli_commands.command_module_paths()
    assert all(path.endswith(f".{module}") for module, path in zip(module_names, module_paths, strict=True))
    for module_path in module_paths:
        importlib.import_module(module_path)


def test_cli_command_module_groups_are_complete_and_disjoint() -> None:
    grouped = (
        *metabaseapi.cli_commands.CORE_RESOURCE_MODULES,
        *metabaseapi.cli_commands.ASSET_AUTHORING_MODULES,
        *metabaseapi.cli_commands.QUERY_AND_EXECUTION_MODULES,
        *metabaseapi.cli_commands.PLATFORM_OPERATIONS_MODULES,
    )
    assert grouped == metabaseapi.cli_commands.COMMAND_MODULES
    assert len(grouped) == len(set(grouped))


def test_cli_command_registry_matches_package_files() -> None:
    command_package_path = Path(metabaseapi.cli_commands.__file__).parent
    command_module_files = tuple(sorted(path.stem for path in command_package_path.glob("*_commands.py")))
    assert command_module_files == tuple(sorted(metabaseapi.cli_commands.COMMAND_MODULES))


def test_cli_command_group_registry_tracks_declared_modules() -> None:
    registry = metabaseapi.cli_commands.COMMAND_MODULE_GROUPS
    assert registry is metabaseapi.cli_commands.COMMAND_MODULE_GROUP_REGISTRY
    assert tuple(registry.keys()) == (
        "core_resource",
        "asset_authoring",
        "query_and_execution",
        "platform_operations",
    )
    flattened_modules = tuple(module for modules in registry.values() for module in modules)
    assert flattened_modules == metabaseapi.cli_commands.COMMAND_MODULES
    assert metabaseapi.cli_commands.command_group_names() == metabaseapi.cli_commands.COMMAND_MODULE_GROUP_ORDER
    assert metabaseapi.cli_commands.COMMAND_MODULE_GROUP_ORDER == (
        "core_resource",
        "asset_authoring",
        "query_and_execution",
        "platform_operations",
    )
    for group_name in metabaseapi.cli_commands.COMMAND_MODULE_GROUP_ORDER:
        assert metabaseapi.cli_commands.command_modules_in_group(group_name) == registry[group_name]
    assert metabaseapi.cli_commands.command_modules_in_group("platform_operations") == (
        metabaseapi.cli_commands.PLATFORM_BUG_REPORTING_COMMAND_MODULE,
        metabaseapi.cli_commands.PLATFORM_CACHE_COMMAND_MODULE,
        metabaseapi.cli_commands.PLATFORM_CHANNEL_COMMAND_MODULE,
        metabaseapi.cli_commands.PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE,
    )


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


def test_client_data_studio_replaces_misc_module_name() -> None:
    importlib.import_module("metabaseapi.client.raw.data_studio")
    importlib.import_module("metabaseapi.client.typed.data_studio")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.raw.misc")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.typed.misc")


def _client_module_stems(package: object) -> tuple[str, ...]:
    package_file = getattr(package, "__file__", None)
    assert package_file is not None
    package_path = Path(package_file).parent
    return tuple(sorted(path.stem for path in package_path.glob("*.py") if path.stem != "__init__"))


def test_client_raw_and_typed_module_names_match_registry() -> None:
    raw_modules = _client_module_stems(metabaseapi.client.raw)
    typed_modules = _client_module_stems(metabaseapi.client.typed)
    registry_modules = tuple(sorted(metabaseapi.client.http.client_mixin_group_names()))

    assert raw_modules == typed_modules
    assert raw_modules == registry_modules


def test_client_mixin_groups_are_explicit_and_stable() -> None:
    assert metabaseapi.client.http.client_mixin_layers() == metabaseapi.client.http.CLIENT_MIXIN_LAYERS
    assert tuple(metabaseapi.client.http.client_mixin_group_names()) == (
        "actions",
        "users",
        "analytics",
        "alerts",
        "api_key",
        "agent",
        "activity",
        "bookmarks",
        "cache",
        "collections",
        "channels",
        "cloud",
        "cards",
        "databases",
        "automagic",
        "dashboards",
        "comments",
        "bug_reporting",
        "data_studio",
        "tables",
    )
    raw_groups = metabaseapi.client.http.CLIENT_RAW_MIXIN_GROUPS
    typed_groups = metabaseapi.client.http.CLIENT_TYPED_MIXIN_GROUPS
    assert metabaseapi.client.http.client_mixin_layers() == ("raw", "typed")
    assert tuple(raw_groups.keys()) == tuple(typed_groups.keys())
    assert tuple(raw_groups.keys()) == metabaseapi.client.http.client_mixin_group_names()
    assert tuple(raw_groups.keys()) == metabaseapi.client.http.client_mixin_group_names(layer="raw")
    assert tuple(typed_groups.keys()) == metabaseapi.client.http.client_mixin_group_names(layer="typed")
    raw_mixins_flat = tuple(mixin for mixins in raw_groups.values() for mixin in mixins)
    typed_mixins_flat = tuple(mixin for mixins in typed_groups.values() for mixin in mixins)
    assert raw_mixins_flat == metabaseapi.client.http.CLIENT_RAW_MIXINS
    assert typed_mixins_flat == metabaseapi.client.http.CLIENT_TYPED_MIXINS
    assert raw_mixins_flat == metabaseapi.client.http.client_mixins_in_layer()
    assert typed_mixins_flat == metabaseapi.client.http.client_mixins_in_layer(layer="typed")
    for group_name in metabaseapi.client.http.client_mixin_group_names():
        assert metabaseapi.client.http.client_mixins_for_group(group_name) == raw_groups[group_name]
    for group_name in metabaseapi.client.http.client_mixin_group_names(layer="typed"):
        assert metabaseapi.client.http.client_mixins_for_group(group_name, layer="typed") == typed_groups[group_name]
    assert metabaseapi.client.http._MetabaseClientRawMixin.__bases__ == metabaseapi.client.http.CLIENT_RAW_MIXINS
    assert metabaseapi.client.http._MetabaseClientTypedMixin.__bases__ == (
        metabaseapi.client.http._MetabaseClientRawMixin,
        *metabaseapi.client.http.CLIENT_TYPED_MIXINS,
    )


def test_cli_entrypoint_importable() -> None:
    assert hasattr(metabaseapi.cli, "app")


def test_client_public_module_exports_concrete_http_implementation() -> None:
    assert metabaseapi.client.MetabaseClient.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client._MetabaseClientRawMixin.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client._MetabaseClientTypedMixin.__module__ == "metabaseapi.client.http"


def _command_names_from_sources() -> list[str]:
    command_names: list[str] = []
    for module in metabaseapi.cli_commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        if source_path is None:
            continue
        source = source_path.read_text(encoding="utf-8")
        command_names.extend(re.findall(r'@app\.command\("([^"]+)"\)', source))
    return command_names


def _command_names_by_module() -> dict[str, tuple[str, ...]]:
    command_names: dict[str, tuple[str, ...]] = {}
    for module in metabaseapi.cli_commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        if source_path is None:
            continue
        source = source_path.read_text(encoding="utf-8")
        command_names[module.__name__.rsplit(".", maxsplit=1)[-1]] = tuple(
            re.findall(r'@app\.command\("([^"]+)"\)', source)
        )
    return command_names


def test_cli_command_names_are_unique_across_modules() -> None:
    command_names = _command_names_from_sources()
    assert len(command_names) == len(set(command_names))


def test_database_lifecycle_commands_share_database_module() -> None:
    command_names = _command_names_by_module()
    assert "create-database" in command_names[metabaseapi.cli_commands.DATABASE_COMMAND_MODULE]
    assert "get-database" in command_names[metabaseapi.cli_commands.DATABASE_COMMAND_MODULE]
    assert "list-databases" in command_names[metabaseapi.cli_commands.DATABASE_COMMAND_MODULE]
    assert "create-database" not in command_names[metabaseapi.cli_commands.SCHEMA_COMMAND_MODULE]


def test_resource_list_commands_live_with_resource_modules() -> None:
    command_names = _command_names_by_module()
    assert "list-cards" in command_names[metabaseapi.cli_commands.CARD_COMMAND_MODULE]
    assert "list-collections" in command_names[metabaseapi.cli_commands.COLLECTION_COMMAND_MODULE]
    assert "list-dashboards" in command_names[metabaseapi.cli_commands.DASHBOARD_COMMAND_MODULE]
    assert "list-users" in command_names[metabaseapi.cli_commands.USER_COMMAND_MODULE]
    assert "list-tables" in command_names[metabaseapi.cli_commands.SCHEMA_COMMAND_MODULE]


def test_current_user_command_lives_with_user_commands() -> None:
    command_names = _command_names_by_module()
    assert "current-user" in command_names[metabaseapi.cli_commands.USER_COMMAND_MODULE]
    assert "current-user" not in command_names[metabaseapi.cli_commands.ANALYTICS_COMMAND_MODULE]


def test_activity_commands_live_with_activity_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "most-recently-viewed-dashboard",
        "list-popular-items",
        "list-recent-views",
        "list-recents",
        "create-recent",
    ):
        assert command_name in command_names[metabaseapi.cli_commands.ACTIVITY_COMMAND_MODULE]
        assert command_name not in command_names[metabaseapi.cli_commands.ANALYTICS_COMMAND_MODULE]


def test_cli_app_registers_all_declared_commands() -> None:
    source_command_names = sorted(_command_names_from_sources())
    app_command_names = sorted(
        [command.name for command in metabaseapi.cli.app.registered_commands if command.name is not None]
    )

    assert len(app_command_names) == len(source_command_names)
    assert app_command_names == source_command_names


def test_cli_command_modules_are_compact() -> None:
    for module in metabaseapi.cli_commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        assert source_path is not None
        line_count = len(source_path.read_text(encoding="utf-8").splitlines())
        assert line_count < 1000, f"{module.__name__} has {line_count} lines"


def test_cli_command_module_objects_are_cached() -> None:
    first = metabaseapi.cli_commands.command_module_objects()
    second = metabaseapi.cli_commands.command_module_objects()
    assert first is second


def test_cli_command_modules_importable_in_multiple_orders() -> None:
    project_root = Path(__file__).resolve().parents[1]
    python_path = str(project_root / "src")
    env = dict(os.environ)
    env["PYTHONPATH"] = python_path if not env.get("PYTHONPATH") else f"{python_path}{os.pathsep}{env['PYTHONPATH']}"

    import_order_cases = [
        dedent(
            """
            import metabaseapi.cli_commands
            import metabaseapi.cli
            print(len(metabaseapi.cli_commands.command_module_objects()), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            import metabaseapi.cli
            import metabaseapi.cli_commands
            print(len(metabaseapi.cli_commands.command_module_objects()), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            from metabaseapi.cli_commands import *  # noqa: F401
            import metabaseapi.cli
            print(len(COMMAND_MODULES), len(COMMAND_MODULES_OBJECTS), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
    ]

    for script in import_order_cases:
        result = subprocess.run(
            [sys.executable, "-c", script],
            check=True,
            env=env,
            capture_output=True,
            text=True,
        )
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 1
        values = [int(item) for item in lines[0].split()]
        assert len(values) in (2, 3)
        assert all(value > 0 for value in values)
        expected_modules = len(metabaseapi.cli_commands.command_module_objects())
        assert values[0] == expected_modules
