from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.setting import SettingResponse
from metabaseapi.endpoints.responses.setting import SettingsResponse
from metabaseapi.endpoints.responses.setting import UpdateSettingResponse
from metabaseapi.endpoints.responses.setting import UpdateSettingsResponse
from metabaseapi.wire import JSONValue


class ListSettingsRequest(EndpointRequest[SettingsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/setting"
    response_model = SettingsResponse


class UpdateSettingsRequest(EndpointRequest[UpdateSettingsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/setting"
    response_model = UpdateSettingsResponse


class GetSettingRequest(EndpointRequest[SettingResponse]):
    key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/setting/{key}"
    response_model = SettingResponse


class UpdateSettingRequest(EndpointRequest[UpdateSettingResponse]):
    key: str
    body: JSONValue | None = None

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/setting/{key}"
    response_model = UpdateSettingResponse
