from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.entities import CurrentUserResponse
from metabaseapi.endpoints.entities import User
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.user import ListUsersResponse


class CurrentUserRequest(EndpointRequest[CurrentUserResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/current"

    async def do(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return await self.execute(client, CurrentUserResponse)

    def do_sync(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return self.execute_sync(client, CurrentUserResponse)


class ListUsersRequest(EndpointRequest[ListUsersResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user"

    async def do(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return await self.execute(client, ListUsersResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return self.execute_sync(client, ListUsersResponse)


class GetUserRequest(EndpointRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"

    async def do(self, client: MetabaseRequestClient) -> User:
        return await self.execute(client, User)

    def do_sync(self, client: MetabaseRequestClient) -> User:
        return self.execute_sync(client, User)

    def resolve_path(self) -> str:
        return f"/api/user/{self.user_id}"
