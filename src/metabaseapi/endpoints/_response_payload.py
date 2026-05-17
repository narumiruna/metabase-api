from __future__ import annotations

from collections.abc import Iterable
from typing import Any
from typing import cast


def normalize_named_payload(values: object, payload_key: str) -> dict[str, Any]:
    if values is None:
        return {}

    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        if payload_key in dict_values:
            return {payload_key: dict_values[payload_key]}
        return {payload_key: dict_values}

    return {payload_key: values}


def normalize_known_payload(values: object, field_names: Iterable[str], fallback_key: str) -> dict[str, Any]:
    field_name_set = set(field_names)
    if not isinstance(values, dict):
        return {fallback_key: values}

    dict_values = cast(dict[str, object], values)
    known_payload = {key: dict_values[key] for key in field_name_set if key != fallback_key and key in dict_values}
    if fallback_key in dict_values:
        known_payload[fallback_key] = dict_values[fallback_key]

    remainder = {key: value for key, value in dict_values.items() if key not in known_payload and key != fallback_key}
    if remainder:
        known_payload[fallback_key] = remainder
    if not known_payload:
        known_payload[fallback_key] = dict_values
    return known_payload


def normalize_model_fields_payload(values: object, field_names: Iterable[str]) -> dict[str, Any]:
    if not isinstance(values, dict):
        return {}

    dict_values = cast(dict[str, object], values)
    return {key: dict_values[key] for key in field_names if key in dict_values}


def normalize_model_list_payload(values: object, field_names: Iterable[str], list_key: str) -> dict[str, Any]:
    if values is None:
        return {list_key: []}

    if isinstance(values, list):
        return {list_key: values}

    payload = normalize_model_fields_payload(values, field_names)
    if list_key in payload and isinstance(payload[list_key], list):
        return payload

    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        if "data" in dict_values and isinstance(dict_values["data"], list):
            payload[list_key] = dict_values["data"]
        elif "items" in dict_values and isinstance(dict_values["items"], list):
            payload[list_key] = dict_values["items"]

    if list_key not in payload:
        payload[list_key] = []
    return payload


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
