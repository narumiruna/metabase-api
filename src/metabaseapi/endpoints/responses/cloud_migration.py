from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator


class _CloudMigrationResponse(BaseModel):
    id: int | str | None = None
    status: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {}

        dict_values = cast(dict[str, object], values)
        return {key: dict_values[key] for key in cls.model_fields if key in dict_values}


class CreateCloudMigrationResponse(_CloudMigrationResponse):
    pass


class CloudMigrationStatusResponse(_CloudMigrationResponse):
    pass


class CancelCloudMigrationResponse(_CloudMigrationResponse):
    pass
