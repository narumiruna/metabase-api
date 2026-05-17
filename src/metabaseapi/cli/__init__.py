from __future__ import annotations

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import configure
from metabaseapi.cli.runtime import create_client

__all__ = ["app", "configure", "create_client"]


def _register_commands() -> None:
    from metabaseapi.cli.commands import register_commands

    register_commands()


_register_commands()

if __name__ == "__main__":
    app()
