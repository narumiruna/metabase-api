from __future__ import annotations

# Migration shim for command module discovery.
# The concrete dashboard command implementations live in ``metabaseapi.cli_commands.dashboard``.
from metabaseapi.cli_commands import dashboard as _dashboard  # noqa: F401
