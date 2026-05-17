from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import CurrentUserResponse
from metabaseapi.endpoints.entities import User
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.user import DeleteUserResponse
from metabaseapi.endpoints.responses.user import ListUsersResponse
from metabaseapi.endpoints.responses.user import UserModalResponse
from metabaseapi.endpoints.responses.user import UserPasswordResetUrlResponse
from metabaseapi.endpoints.responses.user import UserPasswordUpdateResponse
from metabaseapi.endpoints.responses.user import UserRecipientsResponse


class CurrentUserRequest(EndpointRequest[CurrentUserResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/current"
    response_model = CurrentUserResponse


class ListUsersRequest(EndpointRequest[ListUsersResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user"
    response_model = ListUsersResponse


class CreateUserRequest(EndpointRequest[User]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/user"
    response_model = User


class GetUserRecipientsRequest(EndpointRequest[UserRecipientsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/recipients"
    response_model = UserRecipientsResponse


class GetUserRequest(EndpointRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"
    response_model = User


class UpdateUserRequest(EndpointRequest[User]):
    user_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"
    response_model = User


class DeleteUserRequest(EndpointRequest[DeleteUserResponse]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"
    response_model = DeleteUserResponse


class UpdateUserModalRequest(EndpointRequest[UserModalResponse]):
    user_id: int | str
    modal: str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}/modal/{modal}"
    response_model = UserModalResponse


class UpdateUserPasswordRequest(EndpointRequest[UserPasswordUpdateResponse]):
    user_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}/password"
    response_model = UserPasswordUpdateResponse


class CreateUserPasswordResetUrlRequest(EndpointRequest[UserPasswordResetUrlResponse]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}/password-reset-url"
    response_model = UserPasswordResetUrlResponse


class ReactivateUserRequest(EndpointRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}/reactivate"
    response_model = User
