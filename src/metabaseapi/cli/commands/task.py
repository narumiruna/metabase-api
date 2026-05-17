from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.task import GetTaskInfoRequest
from metabaseapi.endpoints.requests.task import GetTaskRequest
from metabaseapi.endpoints.requests.task import GetTaskRunRequest
from metabaseapi.endpoints.requests.task import GetUniqueTasksRequest
from metabaseapi.endpoints.requests.task import ListTaskRunEntitiesRequest
from metabaseapi.endpoints.requests.task import ListTaskRunsRequest
from metabaseapi.endpoints.requests.task import ListTasksRequest


@app.command("get-task")
def get_task(
    ctx: typer.Context,
    status: str | None = typer.Option(None, "--status"),
    task: str | None = typer.Option(None, "--task"),
    limit: int | None = typer.Option(None, "--limit"),
    offset: int | None = typer.Option(None, "--offset"),
    sort_column: str | None = typer.Option(None, "--sort-column"),
    sort_direction: str | None = typer.Option(None, "--sort-direction"),
) -> None:
    run_endpoint_command(
        ctx,
        ListTasksRequest(
            status=status,
            task=task,
            limit=limit,
            offset=offset,
            sort_column=sort_column,
            sort_direction=sort_direction,
        ),
    )


@app.command("get-task-info")
def get_task_info(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetTaskInfoRequest())


@app.command("get-task-runs")
def get_task_runs(
    ctx: typer.Context,
    run_type: str | None = typer.Option(None, "--run-type"),
    entity_type: str | None = typer.Option(None, "--entity-type"),
    entity_id: int | None = typer.Option(None, "--entity-id"),
    status: str | None = typer.Option(None, "--status"),
    started_at: str | None = typer.Option(None, "--started-at"),
    limit: int | None = typer.Option(None, "--limit"),
    offset: int | None = typer.Option(None, "--offset"),
) -> None:
    run_endpoint_command(
        ctx,
        ListTaskRunsRequest(
            run_type=run_type,
            entity_type=entity_type,
            entity_id=entity_id,
            status=status,
            started_at=started_at,
            limit=limit,
            offset=offset,
        ),
    )


@app.command("get-task-runs-entities")
def get_task_runs_entities(
    ctx: typer.Context,
    run_type: str = typer.Option(..., "--run-type"),
    started_at: str = typer.Option(..., "--started-at"),
) -> None:
    run_endpoint_command(ctx, ListTaskRunEntitiesRequest(run_type=run_type, started_at=started_at))


@app.command("get-task-runs-id")
def get_task_runs_id(ctx: typer.Context, id: int = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetTaskRunRequest(id=id))


@app.command("get-task-unique-tasks")
def get_task_unique_tasks(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetUniqueTasksRequest())


@app.command("get-task-id")
def get_task_id(ctx: typer.Context, id: int = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetTaskRequest(id=id))
