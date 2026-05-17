from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Action
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.action import ActionExecutionResponse
from metabaseapi.endpoints.responses.action import ListActionsResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListActionsRequest(EndpointRequest[ListActionsResponse]):
    model_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action"
    response_model = ListActionsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.model_id is None:
            return {}
        return {"model-id": self.model_id}


class CreateActionRequest(EndpointRequest[Action]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action"
    response_model = Action


class ListPublicActionsRequest(EndpointRequest[ListActionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/public"
    response_model = ListActionsResponse


class GetActionRequest(EndpointRequest[Action]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}"
    response_model = Action


class DeleteActionRequest(EndpointRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}"
    response_model = ActionExecutionResponse


class GetActionExecuteRequest(EndpointRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}/execute"
    response_model = ActionExecutionResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class UpdateActionRequest(EndpointRequest[Action]):
    action_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}"
    response_model = Action


class ExecuteActionRequest(EndpointRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}/execute"
    response_model = ActionExecutionResponse

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class CreateActionPublicLinkRequest(EndpointRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}/public_link"
    response_model = ActionExecutionResponse


class DeleteActionPublicLinkRequest(EndpointRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{action_id}/public_link"
    response_model = ActionExecutionResponse
