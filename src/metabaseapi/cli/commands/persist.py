from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.persist import DisableDatabasePersistenceRequest
from metabaseapi.endpoints.requests.persist import DisablePersistenceRequest
from metabaseapi.endpoints.requests.persist import EnableDatabasePersistenceRequest
from metabaseapi.endpoints.requests.persist import EnablePersistenceRequest
from metabaseapi.endpoints.requests.persist import GetPersistedInfoByCardRequest
from metabaseapi.endpoints.requests.persist import GetPersistedInfoRequest
from metabaseapi.endpoints.requests.persist import ListPersistedInfoRequest
from metabaseapi.endpoints.requests.persist import PersistCardRequest
from metabaseapi.endpoints.requests.persist import RefreshPersistedCardRequest
from metabaseapi.endpoints.requests.persist import SetPersistenceRefreshScheduleRequest
from metabaseapi.endpoints.requests.persist import UnpersistCardRequest


@app.command("list-persisted-info")
def list_persisted_info(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListPersistedInfoRequest())


@app.command("get-persisted-info-by-card")
def get_persisted_info_by_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPersistedInfoByCardRequest(card_id=card_id))


@app.command("persist-card")
def persist_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, PersistCardRequest(card_id=card_id))


@app.command("refresh-persisted-card")
def refresh_persisted_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, RefreshPersistedCardRequest(card_id=card_id))


@app.command("unpersist-card")
def unpersist_card(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, UnpersistCardRequest(card_id=card_id))


@app.command("enable-database-persistence")
def enable_database_persistence(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, EnableDatabasePersistenceRequest(id=id))


@app.command("disable-database-persistence")
def disable_database_persistence(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DisableDatabasePersistenceRequest(id=id))


@app.command("disable-persistence")
def disable_persistence(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, DisablePersistenceRequest())


@app.command("enable-persistence")
def enable_persistence(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, EnablePersistenceRequest())


@app.command("set-persistence-refresh-schedule")
def set_persistence_refresh_schedule(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Persistence refresh schedule JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: SetPersistenceRefreshScheduleRequest(body=payload))


@app.command("get-persisted-info")
def get_persisted_info(ctx: typer.Context, persisted_info_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPersistedInfoRequest(persisted_info_id=persisted_info_id))
