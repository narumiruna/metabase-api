from __future__ import annotations

from collections.abc import Mapping
from importlib import import_module
from types import MappingProxyType
from types import ModuleType
from typing import Final
from typing import Literal

ACTION_COMMAND_MODULE = "action"
ACTIVITY_COMMAND_MODULE = "activity"
ALERT_COMMAND_MODULE = "alert"
ANALYTICS_COMMAND_MODULE = "analytics"
API_KEY_COMMAND_MODULE = "api_key"
AUTOMAGIC_COMMAND_MODULE = "automagic"
AGENT_COMMAND_MODULE = "agent"
COMMENT_COMMAND_MODULE = "comment"
USER_COMMAND_MODULE = "user"
COLLECTION_COMMAND_MODULE = "collection"
CARD_COMMAND_MODULE = "card"
CARD_QUERY_COMMAND_MODULE = "card_query"
DATABASE_COMMAND_MODULE = "database"
DASHBOARD_COMMAND_MODULE = "dashboard"
SCHEMA_COMMAND_MODULE = "schema"
DASHBOARD_QUERY_COMMAND_MODULE = "dashboard_query"
DATA_STUDIO_COMMAND_MODULE = "data_studio"
PLATFORM_BUG_REPORTING_COMMAND_MODULE = "bug_reporting"
PLATFORM_CACHE_COMMAND_MODULE = "cache"
PLATFORM_CHANNEL_COMMAND_MODULE = "channel"
PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE = "cloud_migration"

CORE_RESOURCE_MODULES = (
    ACTION_COMMAND_MODULE,
    ACTIVITY_COMMAND_MODULE,
    ALERT_COMMAND_MODULE,
    ANALYTICS_COMMAND_MODULE,
    API_KEY_COMMAND_MODULE,
    AGENT_COMMAND_MODULE,
    AUTOMAGIC_COMMAND_MODULE,
    COMMENT_COMMAND_MODULE,
)

ASSET_AUTHORING_MODULES = (
    USER_COMMAND_MODULE,
    COLLECTION_COMMAND_MODULE,
    DATABASE_COMMAND_MODULE,
    CARD_COMMAND_MODULE,
    CARD_QUERY_COMMAND_MODULE,
    DASHBOARD_COMMAND_MODULE,
    SCHEMA_COMMAND_MODULE,
)

PLATFORM_OPERATIONS_MODULES = (
    PLATFORM_BUG_REPORTING_COMMAND_MODULE,
    PLATFORM_CACHE_COMMAND_MODULE,
    PLATFORM_CHANNEL_COMMAND_MODULE,
    PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE,
)

QUERY_AND_EXECUTION_MODULES = (
    DASHBOARD_QUERY_COMMAND_MODULE,
    DATA_STUDIO_COMMAND_MODULE,
)

CommandModuleGroup = Literal["core_resource", "asset_authoring", "query_and_execution", "platform_operations"]
COMMAND_MODULE_GROUP_ORDER: Final[tuple[CommandModuleGroup, ...]] = (
    "core_resource",
    "asset_authoring",
    "query_and_execution",
    "platform_operations",
)
COMMAND_MODULE_GROUP_REGISTRY: Final[Mapping[CommandModuleGroup, tuple[str, ...]]] = MappingProxyType(
    {
        "core_resource": CORE_RESOURCE_MODULES,
        "asset_authoring": ASSET_AUTHORING_MODULES,
        "query_and_execution": QUERY_AND_EXECUTION_MODULES,
        "platform_operations": PLATFORM_OPERATIONS_MODULES,
    }
)
COMMAND_MODULE_GROUPS = COMMAND_MODULE_GROUP_REGISTRY

COMMAND_MODULES = tuple(
    module for module_group in COMMAND_MODULE_GROUP_ORDER for module in COMMAND_MODULE_GROUP_REGISTRY[module_group]
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


def command_group_names() -> tuple[CommandModuleGroup, ...]:
    """Return command module group names."""
    return COMMAND_MODULE_GROUP_ORDER


def command_modules_in_group(group_name: CommandModuleGroup) -> tuple[str, ...]:
    """Return module names for a command group."""
    return COMMAND_MODULE_GROUP_REGISTRY[group_name]


def register_commands() -> None:
    """Register CLI command modules in one import seam."""
    command_module_objects()


def __getattr__(name: str) -> object:
    if name == "COMMAND_MODULES_OBJECTS":
        return command_module_objects()
    raise AttributeError(f"{__name__!r} has no attribute {name!r}")


__all__ = [
    "ACTION_COMMAND_MODULE",
    "ACTIVITY_COMMAND_MODULE",
    "AGENT_COMMAND_MODULE",
    "ALERT_COMMAND_MODULE",
    "ANALYTICS_COMMAND_MODULE",
    "API_KEY_COMMAND_MODULE",
    "ASSET_AUTHORING_MODULES",
    "AUTOMAGIC_COMMAND_MODULE",
    "CARD_COMMAND_MODULE",
    "CARD_QUERY_COMMAND_MODULE",
    "COLLECTION_COMMAND_MODULE",
    "COMMAND_MODULES",
    "COMMAND_MODULES_IMPORT_PATHS",
    "COMMAND_MODULES_OBJECTS",
    "COMMAND_MODULE_GROUPS",
    "COMMAND_MODULE_GROUP_ORDER",
    "COMMAND_MODULE_GROUP_REGISTRY",
    "COMMENT_COMMAND_MODULE",
    "CORE_RESOURCE_MODULES",
    "DASHBOARD_COMMAND_MODULE",
    "DASHBOARD_QUERY_COMMAND_MODULE",
    "DATABASE_COMMAND_MODULE",
    "DATA_STUDIO_COMMAND_MODULE",
    "PLATFORM_BUG_REPORTING_COMMAND_MODULE",
    "PLATFORM_CACHE_COMMAND_MODULE",
    "PLATFORM_CHANNEL_COMMAND_MODULE",
    "PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE",
    "PLATFORM_OPERATIONS_MODULES",
    "QUERY_AND_EXECUTION_MODULES",
    "SCHEMA_COMMAND_MODULE",
    "USER_COMMAND_MODULE",
    "command_group_names",
    "command_module_names",
    "command_module_objects",
    "command_module_paths",
    "command_modules_in_group",
    "register_commands",
]
