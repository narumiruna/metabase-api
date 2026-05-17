from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.pulse import ListPulsesResponse
from metabaseapi.endpoints.responses.pulse import PulseFormInputResponse
from metabaseapi.endpoints.responses.pulse import PulseResponse
from metabaseapi.endpoints.responses.pulse import PulseSubscriptionDeleteResponse
from metabaseapi.endpoints.responses.pulse import PulseTestResponse
from metabaseapi.endpoints.responses.pulse import PulseUnsubscribeResponse
from metabaseapi.endpoints.responses.pulse import PulseUnsubscribeUndoResponse
from metabaseapi.wire import QueryParamValue


class ListPulsesRequest(EndpointRequest[ListPulsesResponse]):
    archived: bool | None = None
    dashboard_id: int | str | None = None
    creator_or_recipient: bool | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/pulse"
    response_model = ListPulsesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.archived is not None:
            params["archived"] = self.archived
        if self.dashboard_id is not None:
            params["dashboard_id"] = self.dashboard_id
        if self.creator_or_recipient is not None:
            params["creator_or_recipient"] = self.creator_or_recipient
        return params


class CreatePulseRequest(EndpointRequest[PulseResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/pulse"
    response_model = PulseResponse


class GetPulseFormInputRequest(EndpointRequest[PulseFormInputResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/pulse/form_input"
    response_model = PulseFormInputResponse


class TestPulseRequest(EndpointRequest[PulseTestResponse]):
    __test__ = False
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/pulse/test"
    response_model = PulseTestResponse


class GetPulseRequest(EndpointRequest[PulseResponse]):
    pulse_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/pulse/{pulse_id}"
    response_model = PulseResponse


class UpdatePulseRequest(EndpointRequest[PulseResponse]):
    pulse_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/pulse/{pulse_id}"
    response_model = PulseResponse


class DeletePulseSubscriptionRequest(EndpointRequest[PulseSubscriptionDeleteResponse]):
    pulse_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/pulse/{pulse_id}/subscription"
    response_model = PulseSubscriptionDeleteResponse


class UnsubscribePulseRequest(EndpointRequest[PulseUnsubscribeResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/pulse/unsubscribe"
    response_model = PulseUnsubscribeResponse


class UndoPulseUnsubscribeRequest(EndpointRequest[PulseUnsubscribeUndoResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/pulse/unsubscribe/undo"
    response_model = PulseUnsubscribeUndoResponse
