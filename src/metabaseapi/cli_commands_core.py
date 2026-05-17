from __future__ import annotations

# Migration shim for command module discovery.
# The concrete command implementations live in ``metabaseapi.cli_commands.core``.
from metabaseapi.cli_commands import core as _core  # noqa: F401
