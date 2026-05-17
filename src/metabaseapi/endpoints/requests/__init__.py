"""Domain-sliced endpoint request model registry."""

from __future__ import annotations

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
    "channel",
    "comment",
    "cloud_migration",
    "collection",
    "database",
    "data_studio",
    "dashboard",
    "field",
    "schema",
    "user",
    "user_key_value",
)


def request_module_names() -> tuple[str, ...]:
    return REQUEST_MODULES


def request_module_paths() -> tuple[str, ...]:
    return tuple(f"{__name__}.{module_name}" for module_name in REQUEST_MODULES)


__all__ = [
    "REQUEST_MODULES",
    "request_module_names",
    "request_module_paths",
]
