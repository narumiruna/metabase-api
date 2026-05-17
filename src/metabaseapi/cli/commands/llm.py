from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.llm import ExtractLlmTablesRequest
from metabaseapi.endpoints.requests.llm import GenerateLlmSqlRequest
from metabaseapi.endpoints.requests.llm import ListLlmModelsRequest


@app.command("post-api-llm-extract-tables")
def post_api_llm_extract_tables(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="LLM table extraction JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: ExtractLlmTablesRequest(body=payload))


@app.command("post-api-llm-generate-sql")
def post_api_llm_generate_sql(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="LLM SQL generation JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: GenerateLlmSqlRequest(body=payload))


@app.command("get-api-llm-list-models")
def get_api_llm_list_models(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListLlmModelsRequest())
