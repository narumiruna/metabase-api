from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class MetabotGenericResponse(BaseModel):
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class MetabotSettingsResponse(MetabotGenericResponse):
    provider: str | None = None
    model: str | None = None
    models: list[JSONValue] = PydanticField(default_factory=list)
    available_models: list[JSONValue] = PydanticField(default_factory=list)


class MetabotInstance(BaseModel):
    id: int | str | None = None
    name: str | None = None
    entity_id: str | None = None
    description: str | None = None
    model_config = ConfigDict(extra="allow")


class MetabotConversationSummary(BaseModel):
    conversation_id: str | None = None
    created_at: Any | None = None
    last_message_at: Any | None = None
    message_count: int | None = None
    summary: str | None = None
    user_id: int | None = None
    model_config = ConfigDict(extra="allow")


class ListMetabotConversationsResponse(BaseModel):
    data: list[MetabotConversationSummary] = PydanticField(default_factory=list)
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "data")


class MetabotConversationResponse(MetabotConversationSummary):
    chat_messages: list[JSONValue] = PydanticField(default_factory=list)


class MetabotSourceFeedbackResponse(MetabotGenericResponse):
    status: int | None = None
    body: JSONValue | None = None


class ListMetabotsResponse(BaseModel):
    metabots: list[MetabotInstance] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "metabots")


class MetabotResponse(MetabotInstance):
    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            dict_values = cast(dict[str, Any], values)
            if "metabot" in dict_values and isinstance(dict_values["metabot"], dict):
                return cast(dict[str, Any], dict_values["metabot"])
            return dict_values
        return {}


class MetabotPromptSuggestion(BaseModel):
    id: int | str | None = None
    prompt_id: int | str | None = None
    prompt: str | None = None
    title: str | None = None
    description: str | None = None
    model_config = ConfigDict(extra="allow")


class MetabotPromptSuggestionsResponse(BaseModel):
    prompt_suggestions: list[MetabotPromptSuggestion] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "prompt_suggestions")


class MetabotPermissionsResponse(MetabotGenericResponse):
    permissions: dict[str, Any] = PydanticField(default_factory=dict)


class MetabotSlackSettingsResponse(MetabotGenericResponse):
    is_enabled: bool | None = None
    bot_user_token: str | None = None
    signing_secret: str | None = None
    app_token: str | None = None


class MetabotAgentStreamingResponse(MetabotGenericResponse):
    pass


class MetabotFeedbackResponse(MetabotGenericResponse):
    pass


class MetabotGenerateContentResponse(MetabotGenericResponse):
    pass


class DeleteMetabotPromptSuggestionsResponse(MetabotGenericResponse):
    pass


class RegenerateMetabotPromptSuggestionsResponse(MetabotPromptSuggestionsResponse):
    pass


class DeleteMetabotPromptSuggestionResponse(MetabotGenericResponse):
    pass


class MetabotSlackEventsResponse(MetabotGenericResponse):
    pass


class MetabotSlackInteractiveResponse(MetabotGenericResponse):
    pass
