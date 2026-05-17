from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_scim import EeScimApiKeyResponse
from metabaseapi.endpoints.responses.ee_scim import EeScimDeleteResponse
from metabaseapi.endpoints.responses.ee_scim import EeScimGroup
from metabaseapi.endpoints.responses.ee_scim import EeScimGroupsResponse
from metabaseapi.endpoints.responses.ee_scim import EeScimUser
from metabaseapi.endpoints.responses.ee_scim import EeScimUsersResponse
from metabaseapi.wire import QueryParamValue


def _scim_list_params(
    *,
    filter: str | None,
    start_index: int | None,
    count: int | None,
) -> dict[str, QueryParamValue]:
    return {
        key: cast("QueryParamValue", value)
        for key, value in (
            ("filter", filter),
            ("startIndex", start_index),
            ("count", count),
        )
        if value is not None
    }


class GetEeScimApiKeyRequest(EndpointRequest[EeScimApiKeyResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/scim/api_key"
    response_model = EeScimApiKeyResponse


class CreateEeScimApiKeyRequest(EndpointRequest[EeScimApiKeyResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/scim/api_key"
    response_model = EeScimApiKeyResponse


class ListEeScimV2GroupsRequest(EndpointRequest[EeScimGroupsResponse]):
    filter: str | None = None
    start_index: int | None = None
    count: int | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Groups"
    response_model = EeScimGroupsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return _scim_list_params(filter=self.filter, start_index=self.start_index, count=self.count)


class CreateEeScimV2GroupRequest(EndpointRequest[EeScimGroup]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Groups"
    response_model = EeScimGroup


class GetEeScimV2GroupRequest(EndpointRequest[EeScimGroup]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Groups/{group_id}"
    response_model = EeScimGroup


class UpdateEeScimV2GroupRequest(EndpointRequest[EeScimGroup]):
    group_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Groups/{group_id}"
    response_model = EeScimGroup


class DeleteEeScimV2GroupRequest(EndpointRequest[EeScimDeleteResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Groups/{group_id}"
    response_model = EeScimDeleteResponse


class ListEeScimV2UsersRequest(EndpointRequest[EeScimUsersResponse]):
    filter: str | None = None
    start_index: int | None = None
    count: int | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Users"
    response_model = EeScimUsersResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return _scim_list_params(filter=self.filter, start_index=self.start_index, count=self.count)


class CreateEeScimV2UserRequest(EndpointRequest[EeScimUser]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Users"
    response_model = EeScimUser


class GetEeScimV2UserRequest(EndpointRequest[EeScimUser]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Users/{user_id}"
    response_model = EeScimUser


class UpdateEeScimV2UserRequest(EndpointRequest[EeScimUser]):
    user_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Users/{user_id}"
    response_model = EeScimUser


class PatchEeScimV2UserRequest(EndpointRequest[EeScimUser]):
    user_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PATCH"
    endpoint_path: ClassVar[str] = "/api/ee/scim/v2/Users/{user_id}"
    response_model = EeScimUser
