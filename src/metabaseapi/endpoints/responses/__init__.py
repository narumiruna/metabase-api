"""Typed endpoint response model modules."""

from __future__ import annotations

RESPONSE_MODULES = (
    "action",
    "activity",
    "agent",
    "alert",
    "api_key",
    "bookmark",
    "card",
    "channel",
    "collection",
    "common",
    "dashboard",
    "database",
    "table",
    "user",
)


def response_module_names() -> tuple[str, ...]:
    return RESPONSE_MODULES


def response_module_paths() -> tuple[str, ...]:
    return tuple(f"{__name__}.{module_name}" for module_name in RESPONSE_MODULES)


__all__ = [
    "RESPONSE_MODULES",
    "response_module_names",
    "response_module_paths",
]
