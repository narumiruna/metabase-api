from __future__ import annotations

import json

from metabaseapi.wire import JSONValue


def format_json(payload: JSONValue) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True)


def render_payload(payload: JSONValue | None) -> str:
    if payload is None:
        return "null"
    return format_json(payload)
