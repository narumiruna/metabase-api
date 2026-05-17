from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload


class _CloudMigrationResponse(BaseModel):
    id: int | str | None = None
    status: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class CreateCloudMigrationResponse(_CloudMigrationResponse):
    pass


class CloudMigrationStatusResponse(_CloudMigrationResponse):
    pass


class CancelCloudMigrationResponse(_CloudMigrationResponse):
    pass
