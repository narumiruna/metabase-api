from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Final

COMMAND_MODULES: Final[tuple[str, ...]] = (
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

COMMAND_MODULES_IMPORT_PATHS = tuple(f"metabaseapi.cli.commands.{module}" for module in COMMAND_MODULES)

_COMMAND_MODULES_OBJECTS: tuple[ModuleType, ...] | None = None


def command_module_objects() -> tuple[ModuleType, ...]:
    """Return imported CLI command modules in seam order."""
    global _COMMAND_MODULES_OBJECTS
    if _COMMAND_MODULES_OBJECTS is None:
        _COMMAND_MODULES_OBJECTS = tuple(import_module(module_path) for module_path in COMMAND_MODULES_IMPORT_PATHS)
    return _COMMAND_MODULES_OBJECTS


def command_module_names() -> tuple[str, ...]:
    """Return CLI command module suffix names."""
    return COMMAND_MODULES


def command_module_paths() -> tuple[str, ...]:
    """Return fully-qualified CLI command module import paths."""
    return COMMAND_MODULES_IMPORT_PATHS


def register_commands() -> None:
    """Register CLI command modules in one import seam."""
    command_module_objects()


__all__ = [
    "COMMAND_MODULES",
    "COMMAND_MODULES_IMPORT_PATHS",
    "command_module_names",
    "command_module_objects",
    "command_module_paths",
    "register_commands",
]
