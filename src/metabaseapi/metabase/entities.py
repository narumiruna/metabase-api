from __future__ import annotations

from datetime import UTC
from datetime import datetime
from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import field_validator


class _MetabaseResponseBase(BaseModel):
    model_config = ConfigDict(extra="allow")

    @field_validator("created_at", "updated_at", mode="before", check_fields=False)
    @classmethod
    def parse_epoch_datetime(cls, value: object) -> datetime | None:
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, (int, float)):
            seconds = value / 1000 if value > 10_000_000_000 else value
            return datetime.fromtimestamp(seconds, tz=UTC)
        if isinstance(value, str):
            try:
                normalized = value.replace("Z", "+00:00")
                return datetime.fromisoformat(normalized)
            except ValueError as exc:
                msg = f"invalid timestamp: {value}"
                raise TypeError(msg) from exc

        msg = f"invalid timestamp: {value!r}"
        raise TypeError(msg)


class _MetabaseEntity(_MetabaseResponseBase):
    id: int | str | None = None
    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CurrentUserResponse(_MetabaseEntity):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    common_name: str | None = None
    is_superuser: bool | None = None
    locale: str | None = None


class Database(_MetabaseEntity):
    engine: str | None = None
    details: dict[str, Any] = PydanticField(default_factory=dict)


class Action(_MetabaseEntity):
    model_id: int | str | None = None
    type: str | None = None
    description: str | None = None


class ActivityItem(_MetabaseEntity):
    model: str | None = None
    model_id: int | str | None = None
    timestamp: datetime | None = None


class Card(_MetabaseEntity):
    display: str | None = None
    description: str | None = None
    dataset_query: dict[str, Any] | None = None


class Dashboard(_MetabaseEntity):
    description: str | None = None
    collection_id: int | str | None = None


class User(_MetabaseEntity):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_superuser: bool | None = None


class Collection(_MetabaseEntity):
    slug: str | None = None
    authority_level: int | None = None


class Table(_MetabaseEntity):
    db_id: int | str | None = None
    db_name: str | None = None


class MetabaseField(_MetabaseEntity):
    table_id: int | str | None = None


__all__ = [
    "Action",
    "ActivityItem",
    "Card",
    "Collection",
    "CurrentUserResponse",
    "Dashboard",
    "Database",
    "MetabaseField",
    "Table",
    "User",
]
