from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_transforms_python import GetEeTransformsPythonLibraryPathRequest
from metabaseapi.endpoints.requests.ee_transforms_python import PostEeTransformsPythonTestRunRequest
from metabaseapi.endpoints.requests.ee_transforms_python import PutEeTransformsPythonLibraryPathRequest


@app.command("get-api-ee-transforms-python-library-path")
def get_api_ee_transforms_python_library_path(ctx: typer.Context, path: str = typer.Argument(...)) -> None:
    """Fetch Python transform library source."""

    run_endpoint_command(ctx, GetEeTransformsPythonLibraryPathRequest(path=path))


@app.command("put-api-ee-transforms-python-library-path")
def put_api_ee_transforms_python_library_path(
    ctx: typer.Context,
    path: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Python library update JSON object"),
) -> None:
    """Update Python transform library source."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutEeTransformsPythonLibraryPathRequest(path=path, body=payload),
    )


@app.command("post-api-ee-transforms-python-test-run")
def post_api_ee_transforms_python_test_run(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Python transform test-run JSON object"),
) -> None:
    """Run an ad-hoc Python transform test."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostEeTransformsPythonTestRunRequest(body=payload))
