from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.entities import CurrentUserResponse
from metabaseapi.endpoints.entities import User
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.user import ListUsersResponse


class CurrentUserRequest(EndpointRequest[CurrentUserResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/current"
    response_model: ClassVar[object] = CurrentUserResponse


class ListUsersRequest(EndpointRequest[ListUsersResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user"
    response_model: ClassVar[object] = ListUsersResponse


class GetUserRequest(EndpointRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"
    response_model: ClassVar[object] = User

    def resolve_path(self) -> str:
        return f"/api/user/{self.user_id}"
