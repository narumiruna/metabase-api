"""Domain-sliced endpoint request models."""

from __future__ import annotations

ENDPOINT_REQUEST_MODULES = (
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
    "schema",
    "user",
    "user_key_value",
)


def endpoint_request_module_names() -> tuple[str, ...]:
    return ENDPOINT_REQUEST_MODULES


def endpoint_request_module_paths() -> tuple[str, ...]:
    return tuple(f"{__name__}.{module_name}" for module_name in ENDPOINT_REQUEST_MODULES)
