from __future__ import annotations

from importlib import import_module


def register_commands() -> None:
    """Register CLI command modules in one import seam."""

    import_module("metabaseapi.cli_commands_core")
    import_module("metabaseapi.cli_commands_dashboard")
