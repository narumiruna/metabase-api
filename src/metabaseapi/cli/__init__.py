from __future__ import annotations

from metabaseapi.cli.runtime import app

__all__ = ["app"]


def _register_commands() -> None:
    from metabaseapi.cli.commands import _register_commands as register_commands

    register_commands()


_register_commands()

if __name__ == "__main__":
    app()
