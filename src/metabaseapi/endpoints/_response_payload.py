from __future__ import annotations

from typing import Any
from typing import cast


def normalize_unstructured_payload(values: object) -> dict[str, Any]:
    if isinstance(values, dict):
        return cast(dict[str, Any], values)
    return {"raw": values}


def normalize_strict_list_payload(values: object, list_key: str) -> dict[str, Any]:
    if values is None:
        return {list_key: []}

    if isinstance(values, list):
        return {list_key: values}

    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        if list_key in dict_values and isinstance(dict_values[list_key], list):
            return {list_key: dict_values[list_key]}
        if "data" in dict_values and isinstance(dict_values["data"], list):
            return {list_key: dict_values["data"]}
        if "items" in dict_values and isinstance(dict_values["items"], list):
            return {list_key: dict_values["items"]}

    return {list_key: []}
