from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from metabaseapi.client.http import _MetabaseClientTypedMixin


__all__ = ["_MetabaseClientTypedMixin"]


def __getattr__(name: str) -> object:
    if name == "_MetabaseClientTypedMixin":
        from metabaseapi.client.http import _MetabaseClientTypedMixin

        return _MetabaseClientTypedMixin
    raise AttributeError(f"module {__name__} has no attribute {name!r}")
