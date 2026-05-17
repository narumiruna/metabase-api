from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncBranchesResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncDirtyResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncHasRemoteChangesResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncIsDirtyResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncOperationResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncSettingsResponse
from metabaseapi.endpoints.responses.ee_remote_sync import EeRemoteSyncTaskResponse


class GetEeRemoteSyncBranchesRequest(EndpointRequest[EeRemoteSyncBranchesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/branches"
    response_model = EeRemoteSyncBranchesResponse


class PostEeRemoteSyncCreateBranchRequest(EndpointRequest[EeRemoteSyncOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/create-branch"
    response_model = EeRemoteSyncOperationResponse


class GetEeRemoteSyncCurrentTaskRequest(EndpointRequest[EeRemoteSyncTaskResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/current-task"
    response_model = EeRemoteSyncTaskResponse


class PostEeRemoteSyncCurrentTaskCancelRequest(EndpointRequest[EeRemoteSyncTaskResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/current-task/cancel"
    response_model = EeRemoteSyncTaskResponse


class GetEeRemoteSyncDirtyRequest(EndpointRequest[EeRemoteSyncDirtyResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/dirty"
    response_model = EeRemoteSyncDirtyResponse


class PostEeRemoteSyncExportRequest(EndpointRequest[EeRemoteSyncTaskResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/export"
    response_model = EeRemoteSyncTaskResponse


class GetEeRemoteSyncHasRemoteChangesRequest(EndpointRequest[EeRemoteSyncHasRemoteChangesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/has-remote-changes"
    response_model = EeRemoteSyncHasRemoteChangesResponse


class PostEeRemoteSyncImportRequest(EndpointRequest[EeRemoteSyncTaskResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/import"
    response_model = EeRemoteSyncTaskResponse


class GetEeRemoteSyncIsDirtyRequest(EndpointRequest[EeRemoteSyncIsDirtyResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/is-dirty"
    response_model = EeRemoteSyncIsDirtyResponse


class PutEeRemoteSyncSettingsRequest(EndpointRequest[EeRemoteSyncSettingsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/settings"
    response_model = EeRemoteSyncSettingsResponse


class PostEeRemoteSyncStashRequest(EndpointRequest[EeRemoteSyncOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/remote-sync/stash"
    response_model = EeRemoteSyncOperationResponse
