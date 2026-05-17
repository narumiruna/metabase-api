from __future__ import annotations

from typing import Annotated

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.metabot import DeleteMetabotPromptSuggestionRequest
from metabaseapi.endpoints.requests.metabot import DeleteMetabotPromptSuggestionsRequest
from metabaseapi.endpoints.requests.metabot import GenerateMetabotDocumentContentRequest
from metabaseapi.endpoints.requests.metabot import GetMetabotPromptSuggestionsRequest
from metabaseapi.endpoints.requests.metabot import GetMetabotRequest
from metabaseapi.endpoints.requests.metabot import GetMetabotSettingsRequest
from metabaseapi.endpoints.requests.metabot import GetMetabotUserPermissionsRequest
from metabaseapi.endpoints.requests.metabot import ListMetabotsRequest
from metabaseapi.endpoints.requests.metabot import MetabotAgentStreamingRequest
from metabaseapi.endpoints.requests.metabot import MetabotFeedbackRequest
from metabaseapi.endpoints.requests.metabot import MetabotSlackEventsRequest
from metabaseapi.endpoints.requests.metabot import MetabotSlackInteractiveRequest
from metabaseapi.endpoints.requests.metabot import RegenerateMetabotPromptSuggestionsRequest
from metabaseapi.endpoints.requests.metabot import UpdateMetabotRequest
from metabaseapi.endpoints.requests.metabot import UpdateMetabotSettingsRequest
from metabaseapi.endpoints.requests.metabot import UpdateMetabotSlackSettingsRequest


@app.command("post-api-metabot-agent-streaming")
def post_api_metabot_agent_streaming(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot agent streaming JSON object"),
) -> None:
    """Send a chat message to the LLM via the AI Proxy."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetabotAgentStreamingRequest(body=payload))


@app.command("post-api-metabot-feedback")
def post_api_metabot_feedback(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot feedback JSON object"),
) -> None:
    """Proxy Metabot feedback to Harbormaster."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetabotFeedbackRequest(body=payload))


@app.command("get-api-metabot-settings")
def get_api_metabot_settings(
    ctx: typer.Context,
    provider: Annotated[str | None, typer.Option("--provider")] = None,
) -> None:
    """Return Metabot settings and available models."""

    run_endpoint_command(ctx, GetMetabotSettingsRequest(provider=provider))


@app.command("put-api-metabot-settings")
def put_api_metabot_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot settings JSON object"),
) -> None:
    """Update the Metabot provider API key and/or model setting."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateMetabotSettingsRequest(body=payload))


@app.command("post-api-metabot-document-generate-content")
def post_api_metabot_document_generate_content(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot document content JSON object"),
) -> None:
    """Generate content to insert into a document."""

    run_json_body_endpoint_command(ctx, body, lambda payload: GenerateMetabotDocumentContentRequest(body=payload))


@app.command("get-api-metabot-metabot")
def get_api_metabot_metabot(ctx: typer.Context) -> None:
    """List configured metabot instances."""

    run_endpoint_command(ctx, ListMetabotsRequest())


@app.command("get-api-metabot-metabot-id")
def get_api_metabot_metabot_id(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Retrieve one metabot instance."""

    run_endpoint_command(ctx, GetMetabotRequest(id=id))


@app.command("put-api-metabot-metabot-id")
def put_api_metabot_metabot_id(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Metabot update JSON object"),
) -> None:
    """Update a metabot instance."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateMetabotRequest(id=id, body=payload))


@app.command("get-api-metabot-metabot-id-prompt-suggestions")
def get_api_metabot_metabot_id_prompt_suggestions(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Return prompt suggestions for a metabot instance."""

    run_endpoint_command(ctx, GetMetabotPromptSuggestionsRequest(id=id))


@app.command("delete-api-metabot-metabot-id-prompt-suggestions")
def delete_api_metabot_metabot_id_prompt_suggestions(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Delete all prompt suggestions for a metabot instance."""

    run_endpoint_command(ctx, DeleteMetabotPromptSuggestionsRequest(id=id))


@app.command("post-api-metabot-metabot-id-prompt-suggestions-regenerate")
def post_api_metabot_metabot_id_prompt_suggestions_regenerate(
    ctx: typer.Context,
    id: str = typer.Argument(...),
) -> None:
    """Regenerate prompt suggestions for a metabot instance."""

    run_endpoint_command(ctx, RegenerateMetabotPromptSuggestionsRequest(id=id))


@app.command("delete-api-metabot-metabot-id-prompt-suggestions-prompt-id")
def delete_api_metabot_metabot_id_prompt_suggestions_prompt_id(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    prompt_id: str = typer.Argument(...),
) -> None:
    """Delete one prompt suggestion for a metabot instance."""

    run_endpoint_command(ctx, DeleteMetabotPromptSuggestionRequest(id=id, prompt_id=prompt_id))


@app.command("get-api-metabot-permissions-user-permissions")
def get_api_metabot_permissions_user_permissions(ctx: typer.Context) -> None:
    """Return the current user's resolved metabot permissions."""

    run_endpoint_command(ctx, GetMetabotUserPermissionsRequest())


@app.command("post-api-metabot-slack-events")
def post_api_metabot_slack_events(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot Slack events JSON object"),
) -> None:
    """Respond to activities in Slack."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetabotSlackEventsRequest(body=payload))


@app.command("post-api-metabot-slack-interactive")
def post_api_metabot_slack_interactive(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot Slack interactive JSON object"),
) -> None:
    """Handle interactive payloads from Slack."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetabotSlackInteractiveRequest(body=payload))


@app.command("put-api-metabot-slack-settings")
def put_api_metabot_slack_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metabot Slack settings JSON object"),
) -> None:
    """Update Metabot Slack settings atomically."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateMetabotSlackSettingsRequest(body=payload))
