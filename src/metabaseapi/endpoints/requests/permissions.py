from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.permissions import DeletePermissionsGroupResponse
from metabaseapi.endpoints.responses.permissions import DeletePermissionsMembershipResponse
from metabaseapi.endpoints.responses.permissions import PermissionsGraphResponse
from metabaseapi.endpoints.responses.permissions import PermissionsGroupResponse
from metabaseapi.endpoints.responses.permissions import PermissionsGroupsResponse
from metabaseapi.endpoints.responses.permissions import PermissionsMembershipListResponse
from metabaseapi.endpoints.responses.permissions import PermissionsMembershipResponse
from metabaseapi.endpoints.responses.permissions import PermissionsMembershipsResponse


class GetPermissionsGraphRequest(EndpointRequest[PermissionsGraphResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/graph"
    response_model = PermissionsGraphResponse


class PutPermissionsGraphRequest(EndpointRequest[PermissionsGraphResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/permissions/graph"
    response_model = PermissionsGraphResponse


class GetPermissionsGraphDbRequest(EndpointRequest[PermissionsGraphResponse]):
    db_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/graph/db/{db_id}"
    response_model = PermissionsGraphResponse


class GetPermissionsGraphGroupRequest(EndpointRequest[PermissionsGraphResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/graph/group/{group_id}"
    response_model = PermissionsGraphResponse


class ListPermissionsGroupsRequest(EndpointRequest[PermissionsGroupsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/group"
    response_model = PermissionsGroupsResponse


class CreatePermissionsGroupRequest(EndpointRequest[PermissionsGroupResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/permissions/group"
    response_model = PermissionsGroupResponse


class UpdatePermissionsGroupRequest(EndpointRequest[PermissionsGroupResponse]):
    group_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/permissions/group/{group_id}"
    response_model = PermissionsGroupResponse


class DeletePermissionsGroupRequest(EndpointRequest[DeletePermissionsGroupResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/permissions/group/{group_id}"
    response_model = DeletePermissionsGroupResponse


class GetPermissionsGroupRequest(EndpointRequest[PermissionsGroupResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/group/{group_id}"
    response_model = PermissionsGroupResponse


class GetPermissionsMembershipRequest(EndpointRequest[PermissionsMembershipsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/permissions/membership"
    response_model = PermissionsMembershipsResponse


class CreatePermissionsMembershipRequest(EndpointRequest[PermissionsMembershipListResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/permissions/membership"
    response_model = PermissionsMembershipListResponse


class ClearPermissionsMembershipRequest(EndpointRequest[PermissionsMembershipListResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/permissions/membership/{group_id}/clear"
    response_model = PermissionsMembershipListResponse


class UpdatePermissionsMembershipRequest(EndpointRequest[PermissionsMembershipResponse]):
    membership_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/permissions/membership/{membership_id}"
    response_model = PermissionsMembershipResponse


class DeletePermissionsMembershipRequest(EndpointRequest[DeletePermissionsMembershipResponse]):
    membership_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/permissions/membership/{membership_id}"
    response_model = DeletePermissionsMembershipResponse
