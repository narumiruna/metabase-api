from __future__ import annotations

from importlib import import_module
from types import ModuleType

ACTION_COMMAND_MODULE = "actions_commands"
ALERTS_COMMENTS_COMMAND_MODULE = "alerts_comments_commands"
ANALYTICS_COMMAND_MODULE = "analytics_commands"
API_KEY_COMMAND_MODULE = "api_key_commands"
AUTOMAGIC_COMMAND_MODULE = "automagic_commands"
AGENT_COMMAND_MODULE = "agent_commands"
CATALOG_COMMAND_MODULE = "catalog_commands"
DASHBOARD_COMMAND_MODULE = "dashboard_commands"
DATA_STUDIO_COMMAND_MODULE = "data_studio_commands"
PLATFORM_BUG_REPORTING_COMMAND_MODULE = "platform_bug_reporting_commands"
PLATFORM_CACHE_COMMAND_MODULE = "platform_cache_commands"
PLATFORM_CHANNEL_COMMAND_MODULE = "platform_channel_commands"
PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE = "platform_cloud_migration_commands"

COMMAND_MODULES = (
    ACTION_COMMAND_MODULE,
    ALERTS_COMMENTS_COMMAND_MODULE,
    ANALYTICS_COMMAND_MODULE,
    API_KEY_COMMAND_MODULE,
    AGENT_COMMAND_MODULE,
    AUTOMAGIC_COMMAND_MODULE,
    CATALOG_COMMAND_MODULE,
    DASHBOARD_COMMAND_MODULE,
    DATA_STUDIO_COMMAND_MODULE,
    PLATFORM_BUG_REPORTING_COMMAND_MODULE,
    PLATFORM_CACHE_COMMAND_MODULE,
    PLATFORM_CHANNEL_COMMAND_MODULE,
    PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE,
)

COMMAND_MODULES_IMPORT_PATHS = tuple(f"metabaseapi.cli_commands.{module}" for module in COMMAND_MODULES)
COMMAND_MODULES_OBJECTS: tuple[ModuleType, ...] = tuple(
    import_module(module_path) for module_path in COMMAND_MODULES_IMPORT_PATHS
)


def command_module_names() -> tuple[str, ...]:
    """Return CLI command module suffix names."""
    return COMMAND_MODULES


def command_module_paths() -> tuple[str, ...]:
    """Return fully-qualified CLI command module import paths."""
    return COMMAND_MODULES_IMPORT_PATHS


def register_commands() -> None:
    """Register CLI command modules in one import seam."""
    for module_name in COMMAND_MODULES_IMPORT_PATHS:
        import_module(module_name)


__all__ = [
    "ACTION_COMMAND_MODULE",
    "AGENT_COMMAND_MODULE",
    "ALERTS_COMMENTS_COMMAND_MODULE",
    "ANALYTICS_COMMAND_MODULE",
    "API_KEY_COMMAND_MODULE",
    "AUTOMAGIC_COMMAND_MODULE",
    "CATALOG_COMMAND_MODULE",
    "COMMAND_MODULES",
    "COMMAND_MODULES_IMPORT_PATHS",
    "COMMAND_MODULES_OBJECTS",
    "DASHBOARD_COMMAND_MODULE",
    "DATA_STUDIO_COMMAND_MODULE",
    "PLATFORM_BUG_REPORTING_COMMAND_MODULE",
    "PLATFORM_CACHE_COMMAND_MODULE",
    "PLATFORM_CHANNEL_COMMAND_MODULE",
    "PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE",
    "command_module_names",
    "command_module_paths",
    "register_commands",
]
