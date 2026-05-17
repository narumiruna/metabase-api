from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.task import GetTaskResponse
from metabaseapi.endpoints.responses.task import ListTaskRunsResponse
from metabaseapi.endpoints.responses.task import ListTasksResponse
from metabaseapi.endpoints.responses.task import TaskInfoResponse
from metabaseapi.endpoints.responses.task import TaskRunEntitiesResponse
from metabaseapi.endpoints.responses.task import TaskRunWithTasksResponse
from metabaseapi.endpoints.responses.task import UniqueTasksResponse
from metabaseapi.wire import QueryParamValue


class ListTasksRequest(EndpointRequest[ListTasksResponse]):
    status: str | None = None
    task: str | None = None
    limit: int | None = None
    offset: int | None = None
    sort_column: str | None = None
    sort_direction: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task"
    response_model = ListTasksResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.status is not None:
            params["status"] = self.status
        if self.task is not None:
            params["task"] = self.task
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.sort_column is not None:
            params["sort_column"] = self.sort_column
        if self.sort_direction is not None:
            params["sort_direction"] = self.sort_direction
        return params


class GetTaskInfoRequest(EndpointRequest[TaskInfoResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/info"
    response_model = TaskInfoResponse


class ListTaskRunsRequest(EndpointRequest[ListTaskRunsResponse]):
    run_type: str | None = None
    entity_type: str | None = None
    entity_id: int | None = None
    status: str | None = None
    started_at: str | None = None
    limit: int | None = None
    offset: int | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/runs"
    response_model = ListTaskRunsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.run_type is not None:
            params["run-type"] = self.run_type
        if self.entity_type is not None:
            params["entity-type"] = self.entity_type
        if self.entity_id is not None:
            params["entity-id"] = self.entity_id
        if self.status is not None:
            params["status"] = self.status
        if self.started_at is not None:
            params["started-at"] = self.started_at
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        return params


class ListTaskRunEntitiesRequest(EndpointRequest[TaskRunEntitiesResponse]):
    run_type: str
    started_at: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/runs/entities"
    response_model = TaskRunEntitiesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {
            "run-type": self.run_type,
            "started-at": self.started_at,
        }


class GetTaskRunRequest(EndpointRequest[TaskRunWithTasksResponse]):
    id: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/runs/{id}"
    response_model = TaskRunWithTasksResponse


class GetUniqueTasksRequest(EndpointRequest[UniqueTasksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/unique-tasks"
    response_model = UniqueTasksResponse


class GetTaskRequest(EndpointRequest[GetTaskResponse]):
    id: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/task/{id}"
    response_model = GetTaskResponse
