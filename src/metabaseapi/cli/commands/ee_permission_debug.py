from __future__ import annotations

from typing import Annotated
from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_permission_debug import GetEePermissionDebugRequest
from metabaseapi.wire import QueryParamValue


@app.command("get-api-ee-permission_debug")
def get_api_ee_permission_debug(
    ctx: typer.Context,
    user_id: Annotated[str, typer.Option("--user-id")],
    model_id: Annotated[str, typer.Option("--model-id")],
    action_type: Annotated[str, typer.Option("--action-type")],
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(
        ctx,
        GetEePermissionDebugRequest(
            user_id=user_id,
            model_id=model_id,
            action_type=action_type,
            extra_params=cast(
                "dict[str, QueryParamValue]",
                parse_optional_json_object_or_empty(extra_params, "extra_params"),
            ),
        ),
    )
