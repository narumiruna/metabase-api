from __future__ import annotations

from typing import Any
from typing import cast


def normalize_unstructured_payload(values: object) -> dict[str, Any]:
    if isinstance(values, dict):
        return cast(dict[str, Any], values)
    return {"raw": values}


def normalize_list_payload(values: object, list_key: str) -> dict[str, Any]:
    if values is None:
        return {list_key: []}

    if isinstance(values, list):
        return {list_key: values}

    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        if list_key in dict_values and isinstance(dict_values[list_key], list):
            return cast(dict[str, Any], dict_values)
        if "data" in dict_values and isinstance(dict_values["data"], list):
            remainder = dict(dict_values)
            del remainder["data"]
            return {list_key: dict_values["data"], **remainder}
        if "items" in dict_values and isinstance(dict_values["items"], list):
            remainder = dict(dict_values)
            del remainder["items"]
            return {list_key: dict_values["items"], **remainder}
        return {list_key: [], "raw": dict_values}

    return {list_key: [], "raw": values}


__all__ = [
    "normalize_list_payload",
    "normalize_unstructured_payload",
]
