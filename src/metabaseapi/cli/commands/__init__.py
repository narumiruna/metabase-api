from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Final

_COMMAND_MODULES: Final[tuple[str, ...]] = (
    "action",
    "activity",
    "ai_entity_analysis",
    "alert",
    "analytics",
    "api_key",
    "agent",
    "automagic",
    "bookmark",
    "comment",
    "user",
    "user_key_value",
    "collection",
    "collection_graph",
    "collection_root",
    "database",
    "card",
    "card_query",
    "dashboard",
    "table",
    "field",
    "dashboard_query",
    "data_studio",
    "bug_reporting",
    "cache",
    "channel",
    "cloud_migration",
)

_COMMAND_MODULE_IMPORT_PATHS = tuple(f"metabaseapi.cli.commands.{module}" for module in _COMMAND_MODULES)


def _command_module_objects() -> tuple[ModuleType, ...]:
    """Return imported CLI command modules in seam order."""
    return tuple(import_module(module_path) for module_path in _COMMAND_MODULE_IMPORT_PATHS)


def _command_module_names() -> tuple[str, ...]:
    """Return CLI command module suffix names."""
    return _COMMAND_MODULES


def _command_module_paths() -> tuple[str, ...]:
    """Return fully-qualified CLI command module import paths."""
    return _COMMAND_MODULE_IMPORT_PATHS


def _register_commands() -> None:
    """Register CLI command modules in one import seam."""
    _command_module_objects()


__all__: list[str] = []
