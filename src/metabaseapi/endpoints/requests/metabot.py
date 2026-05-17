from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.metabot import DeleteMetabotPromptSuggestionResponse
from metabaseapi.endpoints.responses.metabot import DeleteMetabotPromptSuggestionsResponse
from metabaseapi.endpoints.responses.metabot import ListMetabotConversationsResponse
from metabaseapi.endpoints.responses.metabot import ListMetabotsResponse
from metabaseapi.endpoints.responses.metabot import MetabotAgentStreamingResponse
from metabaseapi.endpoints.responses.metabot import MetabotConversationResponse
from metabaseapi.endpoints.responses.metabot import MetabotFeedbackResponse
from metabaseapi.endpoints.responses.metabot import MetabotGenerateContentResponse
from metabaseapi.endpoints.responses.metabot import MetabotPermissionsResponse
from metabaseapi.endpoints.responses.metabot import MetabotPromptSuggestionsResponse
from metabaseapi.endpoints.responses.metabot import MetabotResponse
from metabaseapi.endpoints.responses.metabot import MetabotSettingsResponse
from metabaseapi.endpoints.responses.metabot import MetabotSlackEventsResponse
from metabaseapi.endpoints.responses.metabot import MetabotSlackInteractiveResponse
from metabaseapi.endpoints.responses.metabot import MetabotSlackSettingsResponse
from metabaseapi.endpoints.responses.metabot import MetabotSourceFeedbackResponse
from metabaseapi.endpoints.responses.metabot import RegenerateMetabotPromptSuggestionsResponse
from metabaseapi.wire import QueryParamValue


class MetabotAgentStreamingRequest(EndpointRequest[MetabotAgentStreamingResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/agent-streaming"
    response_model = MetabotAgentStreamingResponse


class MetabotFeedbackRequest(EndpointRequest[MetabotFeedbackResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/feedback"
    response_model = MetabotFeedbackResponse


class ListMetabotConversationsRequest(EndpointRequest[ListMetabotConversationsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/conversations"
    response_model = ListMetabotConversationsResponse


class GetMetabotConversationRequest(EndpointRequest[MetabotConversationResponse]):
    id: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/conversations/{id}"
    response_model = MetabotConversationResponse


class MetabotSourceFeedbackRequest(EndpointRequest[MetabotSourceFeedbackResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/source-feedback"
    response_model = MetabotSourceFeedbackResponse


class GetMetabotSettingsRequest(EndpointRequest[MetabotSettingsResponse]):
    provider: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/settings"
    response_model = MetabotSettingsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.provider is None:
            return {}
        return {"provider": self.provider}


class UpdateMetabotSettingsRequest(EndpointRequest[MetabotSettingsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/metabot/settings"
    response_model = MetabotSettingsResponse


class GenerateMetabotDocumentContentRequest(EndpointRequest[MetabotGenerateContentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/document/generate-content"
    response_model = MetabotGenerateContentResponse


class ListMetabotsRequest(EndpointRequest[ListMetabotsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot"
    response_model = ListMetabotsResponse


class GetMetabotRequest(EndpointRequest[MetabotResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}"
    response_model = MetabotResponse


class UpdateMetabotRequest(EndpointRequest[MetabotResponse]):
    id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}"
    response_model = MetabotResponse


class GetMetabotPromptSuggestionsRequest(EndpointRequest[MetabotPromptSuggestionsResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}/prompt-suggestions"
    response_model = MetabotPromptSuggestionsResponse


class DeleteMetabotPromptSuggestionsRequest(EndpointRequest[DeleteMetabotPromptSuggestionsResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}/prompt-suggestions"
    response_model = DeleteMetabotPromptSuggestionsResponse


class RegenerateMetabotPromptSuggestionsRequest(EndpointRequest[RegenerateMetabotPromptSuggestionsResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}/prompt-suggestions/regenerate"
    response_model = RegenerateMetabotPromptSuggestionsResponse


class DeleteMetabotPromptSuggestionRequest(EndpointRequest[DeleteMetabotPromptSuggestionResponse]):
    id: int | str
    prompt_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/metabot/metabot/{id}/prompt-suggestions/{prompt_id}"
    response_model = DeleteMetabotPromptSuggestionResponse


class GetMetabotUserPermissionsRequest(EndpointRequest[MetabotPermissionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metabot/permissions/user-permissions"
    response_model = MetabotPermissionsResponse


class MetabotSlackEventsRequest(EndpointRequest[MetabotSlackEventsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/slack/events"
    response_model = MetabotSlackEventsResponse


class MetabotSlackInteractiveRequest(EndpointRequest[MetabotSlackInteractiveResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metabot/slack/interactive"
    response_model = MetabotSlackInteractiveResponse


class UpdateMetabotSlackSettingsRequest(EndpointRequest[MetabotSlackSettingsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/metabot/slack/settings"
    response_model = MetabotSlackSettingsResponse
