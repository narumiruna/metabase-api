from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.session import DeleteSessionResponse
from metabaseapi.endpoints.responses.session import ForgotPasswordResponse
from metabaseapi.endpoints.responses.session import GoogleAuthResponse
from metabaseapi.endpoints.responses.session import PasswordCheckResponse
from metabaseapi.endpoints.responses.session import PasswordResetTokenValidResponse
from metabaseapi.endpoints.responses.session import ResetPasswordResponse
from metabaseapi.endpoints.responses.session import SessionPropertiesResponse
from metabaseapi.endpoints.responses.session import SessionResponse
from metabaseapi.wire import QueryParamValue


class CreateSessionRequest(EndpointRequest[SessionResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/session"
    response_model = SessionResponse


class DeleteSessionRequest(EndpointRequest[DeleteSessionResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/session"
    response_model = DeleteSessionResponse


class ForgotPasswordRequest(EndpointRequest[ForgotPasswordResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/session/forgot_password"
    response_model = ForgotPasswordResponse


class GoogleAuthRequest(EndpointRequest[GoogleAuthResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/session/google_auth"
    response_model = GoogleAuthResponse


class PasswordCheckRequest(EndpointRequest[PasswordCheckResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/session/password-check"
    response_model = PasswordCheckResponse


class PasswordResetTokenValidRequest(EndpointRequest[PasswordResetTokenValidResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/session/password_reset_token_valid"
    response_model = PasswordResetTokenValidResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {"token": self.token}


class GetSessionPropertiesRequest(EndpointRequest[SessionPropertiesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/session/properties"
    response_model = SessionPropertiesResponse


class ResetPasswordRequest(EndpointRequest[ResetPasswordResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/session/reset_password"
    response_model = ResetPasswordResponse
