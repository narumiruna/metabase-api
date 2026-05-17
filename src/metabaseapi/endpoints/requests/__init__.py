"""Domain-sliced endpoint request model registry."""

from __future__ import annotations

from importlib import import_module
from types import ModuleType

REQUEST_MODULES = (
    "action",
    "activity",
    "ai_entity_analysis",
    "agent",
    "alert",
    "analytics",
    "api_key",
    "automagic",
    "bookmark",
    "bug_reporting",
    "cache",
    "card",
    "card_query",
    "channel",
    "comment",
    "cloud_migration",
    "collection",
    "collection_graph",
    "collection_root",
    "database",
    "data_studio",
    "dashboard",
    "dashboard_query",
    "field",
    "table",
    "user",
    "user_key_value",
)


def request_module_names() -> tuple[str, ...]:
    return REQUEST_MODULES


def request_module_paths() -> tuple[str, ...]:
    return tuple(f"{__name__}.{module_name}" for module_name in REQUEST_MODULES)


def request_module_objects() -> tuple[ModuleType, ...]:
    return tuple(import_module(module_path) for module_path in request_module_paths())


__all__ = [
    "REQUEST_MODULES",
    "request_module_names",
    "request_module_objects",
    "request_module_paths",
]
