from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload


class TaskResponse(BaseModel):
    id: int | None = None
    task: str | None = None
    started_at: Any | None = None
    ended_at: Any | None = None
    duration: int | None = None
    status: str | None = None
    db_id: int | str | None = None
    task_details: dict[str, Any] | None = None
    run_id: int | None = None
    logs: Any | None = None
    model_config = ConfigDict(extra="allow")


class ListTasksResponse(BaseModel):
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    data: list[TaskResponse] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class TaskInfoResponse(BaseModel):
    scheduler: list[str] = PydanticField(default_factory=list)
    jobs: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class UniqueTasksResponse(BaseModel):
    tasks: list[Any] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "tasks")


class TaskRunResponse(BaseModel):
    id: int | None = None
    run_type: str | None = None
    entity_type: str | None = None
    entity_id: int | None = None
    started_at: Any | None = None
    ended_at: Any | None = None
    status: str | None = None
    entity_name: str | None = None
    task_count: int | None = None
    success_count: int | None = None
    failed_count: int | None = None
    model_config = ConfigDict(extra="allow")


class ListTaskRunsResponse(BaseModel):
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    data: list[TaskRunResponse] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class TaskRunWithTasksResponse(TaskRunResponse):
    tasks: list[TaskResponse] = PydanticField(default_factory=list)


class TaskRunEntityResponse(BaseModel):
    entity_type: str | None = None
    entity_id: int | None = None
    entity_name: str | None = None
    model_config = ConfigDict(extra="allow")


class TaskRunEntitiesResponse(BaseModel):
    entities: list[TaskRunEntityResponse] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "entities")


class GetTaskResponse(BaseModel):
    task: TaskResponse
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "task")
