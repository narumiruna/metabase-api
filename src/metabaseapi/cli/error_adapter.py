from __future__ import annotations

from metabaseapi.errors import MetabaseError
from metabaseapi.wire import JSONValue


def error_payload(exc: Exception) -> JSONValue:
    if isinstance(exc, MetabaseError):
        return {"error": str(exc)}
    return {"error": str(exc)}


def normalize_error_payload(exc: Exception) -> JSONValue:
    return error_payload(exc)
