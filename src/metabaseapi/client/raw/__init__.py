from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from metabaseapi.client.http import _MetabaseClientRawMixin

__all__ = ["_MetabaseClientRawMixin"]


def __getattr__(name: str) -> object:
    if name == "_MetabaseClientRawMixin":
        from metabaseapi.client.http import _MetabaseClientRawMixin

        return _MetabaseClientRawMixin
    raise AttributeError(f"module {__name__} has no attribute {name!r}")
