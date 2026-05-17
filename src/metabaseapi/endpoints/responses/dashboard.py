from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.wire import JSONValue


class ListDashboardsResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "dashboards")


class _DashboardOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class _DashboardStatusResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    uuid: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {}

        dict_values = cast(dict[str, object], values)
        return {key: dict_values[key] for key in cls.model_fields if key in dict_values}


class DashboardEmbeddableResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "dashboards")


class DashboardPublicResponse(DashboardEmbeddableResponse):
    pass


class SaveDashboardResponse(_DashboardStatusResponse):
    id: int | str | None = None


class SaveDashboardToCollectionResponse(_DashboardStatusResponse):
    id: int | str | None = None


class CreateDashboardPublicLinkResponse(_DashboardStatusResponse):
    uuid: str | None = None


class DeleteDashboardPublicLinkResponse(_DashboardStatusResponse):
    ok: bool | None = None


class DeleteDashboardResponse(_DashboardStatusResponse):
    ok: bool | None = None


class UpdateDashboardCardsResponse(_DashboardStatusResponse):
    ok: bool | None = None


class DashboardItemsResponse(BaseModel):
    items: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "items")


class DashboardQueryResponse(_DashboardOperationResponse):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class DashboardQueryExportResponse(_DashboardOperationResponse):
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class DashboardParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class DashboardRemappingResponse(_DashboardOperationResponse):
    data: JSONValue | None = None


class DashboardQueryMetadataResponse(_DashboardOperationResponse):
    metadata: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_known_payload(values, cls.model_fields, "result")
        if set(payload) == {"result"}:
            return {"metadata": payload["result"]}
        return payload


class DashboardRelatedResponse(DashboardItemsResponse):
    pass


class DashboardValidFilterFieldsResponse(BaseModel):
    fields: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "fields")
