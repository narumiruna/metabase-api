"""Metabase typed endpoint models and request helpers."""

from __future__ import annotations

from metabaseapi.metabase import entities as _entities
from metabaseapi.metabase import requests as _requests
from metabaseapi.metabase import responses as _responses
from metabaseapi.metabase.request_base import MetabaseRequestClient as MetabaseRequestClient


def _export_public_symbols(module: object, names: tuple[str, ...] | list[str]) -> None:
    globals().update({name: getattr(module, name) for name in names})


_export_public_symbols(_entities, _entities.__all__)
_export_public_symbols(_requests, _requests.__all__)
_export_public_symbols(_responses, _responses.__all__)

__all__ = sorted(
    (
        *_entities.__all__,
        *_requests.__all__,
        *_responses.__all__,
        "MetabaseRequestClient",
    )
)
