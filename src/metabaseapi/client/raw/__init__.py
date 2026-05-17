"""Raw JSON client method adapters by domain."""

from __future__ import annotations

RAW_MODULES = (
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
    "cloud_migration",
    "collection",
    "collection_graph",
    "comment",
    "dashboard",
    "dashboard_query",
    "data_studio",
    "database",
    "field",
    "table",
    "user",
    "user_key_value",
)


def raw_module_names() -> tuple[str, ...]:
    return RAW_MODULES


def raw_module_paths() -> tuple[str, ...]:
    return tuple(f"{__name__}.{module_name}" for module_name in RAW_MODULES)


__all__ = [
    "RAW_MODULES",
    "raw_module_names",
    "raw_module_paths",
]
