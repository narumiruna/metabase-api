from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.database import CreateDatabaseRequest
from metabaseapi.endpoints.requests.database import CreateSampleDatabaseRequest
from metabaseapi.endpoints.requests.database import DeleteDatabaseRequest
from metabaseapi.endpoints.requests.database import DiscardDatabaseValuesRequest
from metabaseapi.endpoints.requests.database import DismissDatabaseSpinnerRequest
from metabaseapi.endpoints.requests.database import GetDatabaseAutocompleteSuggestionsRequest
from metabaseapi.endpoints.requests.database import GetDatabaseCardAutocompleteSuggestionsRequest
from metabaseapi.endpoints.requests.database import GetDatabaseDetailMetadataRequest
from metabaseapi.endpoints.requests.database import GetDatabaseFieldsRequest
from metabaseapi.endpoints.requests.database import GetDatabaseFieldValuesRequest
from metabaseapi.endpoints.requests.database import GetDatabaseHealthcheckRequest
from metabaseapi.endpoints.requests.database import GetDatabaseIdFieldsRequest
from metabaseapi.endpoints.requests.database import GetDatabaseMetadataRequest
from metabaseapi.endpoints.requests.database import GetDatabaseRequest
from metabaseapi.endpoints.requests.database import GetDatabaseSchemaRequest
from metabaseapi.endpoints.requests.database import GetDatabaseSchemasRequest
from metabaseapi.endpoints.requests.database import GetDatabaseSchemaTablesRequest
from metabaseapi.endpoints.requests.database import GetDatabaseSettingsAvailableRequest
from metabaseapi.endpoints.requests.database import GetDatabaseSyncableSchemasRequest
from metabaseapi.endpoints.requests.database import GetDatabaseUsageInfoRequest
from metabaseapi.endpoints.requests.database import GetVirtualDatabaseDatasetsRequest
from metabaseapi.endpoints.requests.database import GetVirtualDatabaseMetadataRequest
from metabaseapi.endpoints.requests.database import GetVirtualDatabaseSchemaDatasetsRequest
from metabaseapi.endpoints.requests.database import GetVirtualDatabaseSchemaRequest
from metabaseapi.endpoints.requests.database import GetVirtualDatabaseSchemasRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest
from metabaseapi.endpoints.requests.database import PostDatabaseMetadataRequest
from metabaseapi.endpoints.requests.database import RescanDatabaseValuesRequest
from metabaseapi.endpoints.requests.database import SyncDatabaseSchemaRequest
from metabaseapi.endpoints.requests.database import UpdateDatabaseRequest
from metabaseapi.endpoints.requests.database import ValidateDatabaseRequest
from metabaseapi.wire import QueryParamPrimitive
from metabaseapi.wire import QueryParamValue


def _parse_query_param_value(value: object) -> QueryParamValue | None:
    if isinstance(value, str | int | float | bool) or value is None:
        return value
    if isinstance(value, list):
        parsed_values: list[QueryParamPrimitive] = [
            item for item in value if isinstance(item, str | int | float | bool) or item is None
        ]
        return parsed_values
    return None


def _parse_query_params(raw: str | None) -> dict[str, QueryParamValue]:
    payload = parse_optional_json_object(raw, "params") or {}
    params: dict[str, QueryParamValue] = {}
    for key, value in payload.items():
        parsed_value = _parse_query_param_value(value)
        if parsed_value is not None:
            params[key] = parsed_value
    return params


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    run_endpoint_command(ctx, ListDatabasesRequest())


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    run_endpoint_command(ctx, GetDatabaseRequest(database_id=database_id))


@app.command("create-database")
def create_database(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Name of the database to create"),
    engine: str = typer.Argument(..., help="Database engine type"),
    details: str | None = typer.Option(None, "--details", "-d", help="Database details JSON object"),
) -> None:
    """Create a new database."""

    run_endpoint_command(
        ctx,
        CreateDatabaseRequest(
            name=name,
            engine=engine,
            details=parse_optional_json_object_or_empty(details, "details"),
        ),
    )


@app.command("create-sample-database")
def create_sample_database(ctx: typer.Context) -> None:
    """Create Metabase's sample database."""

    run_endpoint_command(ctx, CreateSampleDatabaseRequest())


@app.command("validate-database")
def validate_database(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Database validation JSON object"),
) -> None:
    """Validate database connection details."""

    run_json_body_endpoint_command(ctx, body, lambda payload: ValidateDatabaseRequest(body=payload))


@app.command("update-database")
def update_database(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Database update JSON object"),
) -> None:
    """Update a database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateDatabaseRequest(database_id=database_id, body=payload),
    )


@app.command("delete-database")
def delete_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Delete a database."""

    run_endpoint_command(ctx, DeleteDatabaseRequest(database_id=database_id))


@app.command("get-database-field-values")
def get_database_field_values(ctx: typer.Context) -> None:
    """Get sampled field values for every field."""

    run_endpoint_command(ctx, GetDatabaseFieldValuesRequest())


@app.command("export-database-metadata")
def export_database_metadata(ctx: typer.Context) -> None:
    """Export database, table, and field metadata."""

    run_endpoint_command(ctx, GetDatabaseMetadataRequest())


@app.command("import-database-metadata")
def import_database_metadata(ctx: typer.Context, body: str = typer.Argument(..., help="Metadata JSON object")) -> None:
    """Import database, table, and field metadata."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostDatabaseMetadataRequest(body=payload))


@app.command("get-database-autocomplete-suggestions")
def get_database_autocomplete_suggestions(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Autocomplete query params JSON object"),
) -> None:
    """Get SQL autocomplete suggestions for a database."""

    run_endpoint_command(
        ctx,
        GetDatabaseAutocompleteSuggestionsRequest(database_id=database_id, params=_parse_query_params(params)),
    )


@app.command("get-database-card-autocomplete-suggestions")
def get_database_card_autocomplete_suggestions(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Card autocomplete query params JSON object"),
) -> None:
    """Get card autocomplete suggestions for a database."""

    run_endpoint_command(
        ctx,
        GetDatabaseCardAutocompleteSuggestionsRequest(database_id=database_id, params=_parse_query_params(params)),
    )


@app.command("discard-database-values")
def discard_database_values(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Discard saved field values for a database."""

    run_endpoint_command(ctx, DiscardDatabaseValuesRequest(database_id=database_id))


@app.command("dismiss-database-spinner")
def dismiss_database_spinner(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Dismiss the database sync spinner."""

    run_endpoint_command(ctx, DismissDatabaseSpinnerRequest(database_id=database_id))


@app.command("get-database-fields")
def get_database_fields(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get all fields in a database."""

    run_endpoint_command(ctx, GetDatabaseFieldsRequest(database_id=database_id))


@app.command("get-database-healthcheck")
def get_database_healthcheck(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Check whether a database can connect."""

    run_endpoint_command(ctx, GetDatabaseHealthcheckRequest(database_id=database_id))


@app.command("get-database-id-fields")
def get_database_id_fields(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get primary key fields for a database."""

    run_endpoint_command(ctx, GetDatabaseIdFieldsRequest(database_id=database_id))


@app.command("get-database-metadata")
def get_database_metadata(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Metadata query params JSON object"),
) -> None:
    """Get metadata for a database."""

    run_endpoint_command(
        ctx,
        GetDatabaseDetailMetadataRequest(database_id=database_id, params=_parse_query_params(params)),
    )


@app.command("rescan-database-values")
def rescan_database_values(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Rescan saved field values for a database."""

    run_endpoint_command(ctx, RescanDatabaseValuesRequest(database_id=database_id))


@app.command("get-database-schema")
def get_database_schema(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Schema query params JSON object"),
) -> None:
    """Get tables for the empty schema in a database."""

    run_endpoint_command(ctx, GetDatabaseSchemaRequest(database_id=database_id, params=_parse_query_params(params)))


@app.command("get-database-schema-tables")
def get_database_schema_tables(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    schema_name: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Schema query params JSON object"),
) -> None:
    """Get tables for a database schema."""

    run_endpoint_command(
        ctx,
        GetDatabaseSchemaTablesRequest(
            database_id=database_id,
            schema_name=schema_name,
            params=_parse_query_params(params),
        ),
    )


@app.command("list-database-schemas")
def list_database_schemas(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Schemas query params JSON object"),
) -> None:
    """List schemas for a database."""

    run_endpoint_command(ctx, GetDatabaseSchemasRequest(database_id=database_id, params=_parse_query_params(params)))


@app.command("get-database-settings-available")
def get_database_settings_available(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get database-local settings availability."""

    run_endpoint_command(ctx, GetDatabaseSettingsAvailableRequest(database_id=database_id))


@app.command("sync-database-schema")
def sync_database_schema(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Trigger a schema sync for a database."""

    run_endpoint_command(ctx, SyncDatabaseSchemaRequest(database_id=database_id))


@app.command("get-database-syncable-schemas")
def get_database_syncable_schemas(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """List syncable schemas for a database."""

    run_endpoint_command(ctx, GetDatabaseSyncableSchemasRequest(database_id=database_id))


@app.command("get-database-usage-info")
def get_database_usage_info(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get database usage info."""

    run_endpoint_command(ctx, GetDatabaseUsageInfoRequest(database_id=database_id))


@app.command("list-virtual-database-datasets")
def list_virtual_database_datasets(ctx: typer.Context, virtual_database: str = typer.Argument(...)) -> None:
    """List datasets for a saved questions virtual database."""

    run_endpoint_command(ctx, GetVirtualDatabaseDatasetsRequest(virtual_database=virtual_database))


@app.command("list-virtual-database-dataset-tables")
def list_virtual_database_dataset_tables(
    ctx: typer.Context,
    virtual_database: str = typer.Argument(...),
    schema_name: str = typer.Argument(...),
) -> None:
    """List tables for a virtual database dataset schema."""

    run_endpoint_command(
        ctx,
        GetVirtualDatabaseSchemaDatasetsRequest(virtual_database=virtual_database, schema_name=schema_name),
    )


@app.command("get-virtual-database-metadata")
def get_virtual_database_metadata(ctx: typer.Context, virtual_database: str = typer.Argument(...)) -> None:
    """Get metadata for a saved questions virtual database."""

    run_endpoint_command(ctx, GetVirtualDatabaseMetadataRequest(virtual_database=virtual_database))


@app.command("list-virtual-database-schema-tables")
def list_virtual_database_schema_tables(
    ctx: typer.Context,
    virtual_database: str = typer.Argument(...),
    schema_name: str = typer.Argument(...),
) -> None:
    """List tables for a virtual database schema."""

    run_endpoint_command(
        ctx,
        GetVirtualDatabaseSchemaRequest(virtual_database=virtual_database, schema_name=schema_name),
    )


@app.command("list-virtual-database-schemas")
def list_virtual_database_schemas(ctx: typer.Context, virtual_database: str = typer.Argument(...)) -> None:
    """List schemas for a saved questions virtual database."""

    run_endpoint_command(ctx, GetVirtualDatabaseSchemasRequest(virtual_database=virtual_database))
