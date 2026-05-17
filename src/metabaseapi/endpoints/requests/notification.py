from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.notification import ListNotificationsResponse
from metabaseapi.endpoints.responses.notification import NotificationResponse
from metabaseapi.endpoints.responses.notification import NotificationSendResponse
from metabaseapi.endpoints.responses.notification import NotificationUnsubscribeResponse
from metabaseapi.endpoints.responses.notification import NotificationUnsubscribeUndoResponse
from metabaseapi.wire import QueryParamValue


class ListNotificationsRequest(EndpointRequest[ListNotificationsResponse]):
    creator_id: int | str | None = None
    recipient_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/notification"
    response_model = ListNotificationsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.creator_id is not None:
            params["creator_id"] = self.creator_id
        if self.recipient_id is not None:
            params["recipient_id"] = self.recipient_id
        return params


class CreateNotificationRequest(EndpointRequest[NotificationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification"
    response_model = NotificationResponse


class SendUnsavedNotificationRequest(EndpointRequest[NotificationSendResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification/send"
    response_model = NotificationSendResponse


class GetNotificationRequest(EndpointRequest[NotificationResponse]):
    notification_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/notification/{notification_id}"
    response_model = NotificationResponse


class UpdateNotificationRequest(EndpointRequest[NotificationResponse]):
    notification_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/notification/{notification_id}"
    response_model = NotificationResponse


class SendNotificationRequest(EndpointRequest[NotificationSendResponse]):
    notification_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification/{notification_id}/send"
    response_model = NotificationSendResponse


class UnsubscribeNotificationRequest(EndpointRequest[NotificationUnsubscribeResponse]):
    notification_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification/{notification_id}/unsubscribe"
    response_model = NotificationUnsubscribeResponse


class UnsubscribeNotificationByHashRequest(EndpointRequest[NotificationUnsubscribeResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification/unsubscribe"
    response_model = NotificationUnsubscribeResponse


class UndoNotificationUnsubscribeRequest(EndpointRequest[NotificationUnsubscribeUndoResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notification/unsubscribe/undo"
    response_model = NotificationUnsubscribeUndoResponse
