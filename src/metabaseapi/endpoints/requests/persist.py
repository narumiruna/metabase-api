from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.persist import ListPersistedInfoResponse
from metabaseapi.endpoints.responses.persist import PersistedInfo
from metabaseapi.endpoints.responses.persist import PersistOperationResponse
from metabaseapi.endpoints.responses.persist import PersistRefreshScheduleResponse


class ListPersistedInfoRequest(EndpointRequest[ListPersistedInfoResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/persist"
    response_model = ListPersistedInfoResponse


class GetPersistedInfoByCardRequest(EndpointRequest[PersistedInfo]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/persist/card/{card_id}"
    response_model = PersistedInfo


class PersistCardRequest(EndpointRequest[PersistOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/card/{card_id}/persist"
    response_model = PersistOperationResponse


class RefreshPersistedCardRequest(EndpointRequest[PersistOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/card/{card_id}/refresh"
    response_model = PersistOperationResponse


class UnpersistCardRequest(EndpointRequest[PersistOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/card/{card_id}/unpersist"
    response_model = PersistOperationResponse


class EnableDatabasePersistenceRequest(EndpointRequest[PersistOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/database/{id}/persist"
    response_model = PersistOperationResponse


class DisableDatabasePersistenceRequest(EndpointRequest[PersistOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/database/{id}/unpersist"
    response_model = PersistOperationResponse


class DisablePersistenceRequest(EndpointRequest[PersistOperationResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/disable"
    response_model = PersistOperationResponse


class EnablePersistenceRequest(EndpointRequest[PersistOperationResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/enable"
    response_model = PersistOperationResponse


class SetPersistenceRefreshScheduleRequest(EndpointRequest[PersistRefreshScheduleResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/persist/set-refresh-schedule"
    response_model = PersistRefreshScheduleResponse


class GetPersistedInfoRequest(EndpointRequest[PersistedInfo]):
    persisted_info_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/persist/{persisted_info_id}"
    response_model = PersistedInfo
