from __future__ import annotations

import importlib
import os
import re
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

import pytest

import metabaseapi.cli
import metabaseapi.cli.commands
import metabaseapi.cli.runtime
import metabaseapi.client
import metabaseapi.client.http
import metabaseapi.client.raw
import metabaseapi.endpoints
import metabaseapi.endpoints.entities
import metabaseapi.endpoints.execution
import metabaseapi.endpoints.requests
import metabaseapi.endpoints.requests.action
import metabaseapi.endpoints.requests.activity
import metabaseapi.endpoints.requests.agent
import metabaseapi.endpoints.requests.ai_entity_analysis
import metabaseapi.endpoints.requests.alert
import metabaseapi.endpoints.requests.analytics
import metabaseapi.endpoints.requests.api_key
import metabaseapi.endpoints.requests.automagic
import metabaseapi.endpoints.requests.bookmark
import metabaseapi.endpoints.requests.bug_reporting
import metabaseapi.endpoints.requests.cache
import metabaseapi.endpoints.requests.card
import metabaseapi.endpoints.requests.channel
import metabaseapi.endpoints.requests.cloud_migration
import metabaseapi.endpoints.requests.collection
import metabaseapi.endpoints.requests.comment
import metabaseapi.endpoints.requests.dashboard
import metabaseapi.endpoints.requests.data_studio
import metabaseapi.endpoints.requests.database
import metabaseapi.endpoints.requests.schema
import metabaseapi.endpoints.requests.user
import metabaseapi.endpoints.requests.user_key_value
import metabaseapi.endpoints.responses
import metabaseapi.endpoints.responses.action
import metabaseapi.endpoints.responses.activity
import metabaseapi.endpoints.responses.agent
import metabaseapi.endpoints.responses.alert
import metabaseapi.endpoints.responses.api_key
import metabaseapi.endpoints.responses.bookmark
import metabaseapi.endpoints.responses.card
import metabaseapi.endpoints.responses.channel
import metabaseapi.endpoints.responses.collection
import metabaseapi.endpoints.responses.common
import metabaseapi.endpoints.responses.dashboard
import metabaseapi.endpoints.responses.database
import metabaseapi.endpoints.responses.schema
import metabaseapi.endpoints.responses.user
import metabaseapi.wire

REQUEST_MODULE_CONTRACTS = {
    "action": (
        "ListActionsRequest",
        "CreateActionRequest",
        "ListPublicActionsRequest",
        "GetActionRequest",
        "DeleteActionRequest",
        "GetActionExecuteRequest",
        "UpdateActionRequest",
        "ExecuteActionRequest",
        "CreateActionPublicLinkRequest",
        "DeleteActionPublicLinkRequest",
    ),
    "activity": (
        "GetMostRecentlyViewedDashboardRequest",
        "ListPopularItemsRequest",
        "ListRecentViewsRequest",
        "ListRecentsRequest",
        "CreateRecentRequest",
    ),
    "ai_entity_analysis": ("AnalyzeChartRequest",),
    "agent": (
        "AgentExecuteRequest",
        "GetAgentMetricRequest",
        "GetAgentMetricFieldValuesRequest",
        "AgentPingRequest",
        "AgentSearchRequest",
        "GetAgentTableRequest",
        "GetAgentTableFieldValuesRequest",
        "AgentConstructQueryRequest",
        "AgentQueryRequest",
    ),
    "alert": (
        "ListAlertsRequest",
        "GetAlertRequest",
        "DeleteAlertSubscriptionRequest",
    ),
    "analytics": (
        "GetAnonymousStatsRequest",
        "CreateAnalyticsEventBatchRequest",
    ),
    "api_key": (
        "CreateApiKeyRequest",
        "ListApiKeysRequest",
        "CountApiKeysRequest",
        "UpdateApiKeyRequest",
        "DeleteApiKeyRequest",
        "RegenerateApiKeyRequest",
    ),
    "automagic": (
        "AutomagicDashboardRequest",
        "AutomagicDatabaseCandidatesRequest",
        "AutomagicModelIndexPrimaryKeyRequest",
    ),
    "bookmark": (
        "ListBookmarksRequest",
        "UpdateBookmarkOrderingRequest",
        "CreateBookmarkRequest",
        "DeleteBookmarkRequest",
    ),
    "bug_reporting": (
        "GetBugReportingConnectionPoolDetailsRequest",
        "GetBugReportingDetailsRequest",
    ),
    "cache": (
        "GetCacheRequest",
        "PutCacheRequest",
        "DeleteCacheRequest",
        "InvalidateCacheRequest",
    ),
    "card": (
        "ListCardsRequest",
        "CreateCardRequest",
        "GetCardRequest",
        "GetCardCollectionsRequest",
        "GetCardEmbeddableRequest",
        "PostCardPivotQueryRequest",
        "GetCardPublicRequest",
        "CardParamsSearchRequest",
        "CardParamsValuesRequest",
        "CreateCardPublicLinkRequest",
        "DeleteCardPublicLinkRequest",
        "CardQueryRequest",
        "CardQueryExportRequest",
        "UpdateCardRequest",
        "DeleteCardRequest",
        "CopyCardRequest",
        "GetCardDashboardsRequest",
        "CardRemappingRequest",
        "GetCardQueryMetadataRequest",
        "GetCardSeriesRequest",
        "CardsDashboardsRequest",
        "MoveCardsRequest",
    ),
    "channel": (
        "ListChannelsRequest",
        "CreateChannelRequest",
        "TestChannelRequest",
        "GetChannelRequest",
        "UpdateChannelRequest",
    ),
    "comment": (
        "GetCommentMentionsRequest",
        "UpdateCommentRequest",
        "GetCommentRequest",
        "PostCommentRequest",
        "DeleteCommentRequest",
        "PostCommentReactionRequest",
    ),
    "cloud_migration": (
        "CreateCloudMigrationRequest",
        "GetCloudMigrationRequest",
        "CancelCloudMigrationRequest",
    ),
    "collection": (
        "CreateCollectionRequest",
        "GetCollectionGraphRequest",
        "PutCollectionGraphRequest",
        "GetCollectionRootRequest",
        "GetCollectionTreeRequest",
        "GetCollectionRootDashboardQuestionCandidatesRequest",
        "GetCollectionRootItemsRequest",
        "GetCollectionDashboardQuestionCandidatesRequest",
        "GetCollectionItemsRequest",
        "GetCollectionTrashRequest",
        "PostCollectionRootMoveDashboardQuestionCandidatesRequest",
        "PostCollectionMoveDashboardQuestionCandidatesRequest",
        "ListCollectionsRequest",
        "GetCollectionRequest",
        "PutCollectionRequest",
        "DeleteCollectionRequest",
    ),
    "database": (
        "ListDatabasesRequest",
        "CreateDatabaseRequest",
        "GetDatabaseRequest",
    ),
    "data_studio": (
        "DataStudioTableDiscardValuesRequest",
        "DataStudioTableEditRequest",
        "DataStudioTableRescanValuesRequest",
        "DataStudioTableSelectionRequest",
        "DataStudioTableSyncSchemaRequest",
    ),
    "dashboard": (
        "ListDashboardsRequest",
        "PostDashboardRequest",
        "GetDashboardRequest",
        "GetDashboardEmbeddableRequest",
        "GetDashboardPublicRequest",
        "PostDashboardPivotQueryRequest",
        "SaveDashboardRequest",
        "SaveDashboardToCollectionRequest",
        "GetDashboardDashcardExecuteRequest",
        "ExecuteDashboardDashcardRequest",
        "CreateDashboardPublicLinkRequest",
        "DeleteDashboardPublicLinkRequest",
        "CopyDashboardRequest",
        "DeleteDashboardRequest",
        "UpdateDashboardRequest",
        "UpdateDashboardCardsRequest",
        "GetDashboardItemsRequest",
        "DashboardParamRemappingRequest",
        "DashboardParamSearchRequest",
        "DashboardParamValuesRequest",
        "GetDashboardQueryMetadataRequest",
        "GetDashboardRelatedRequest",
    ),
    "schema": (
        "ListTablesRequest",
        "GetTableRequest",
        "GetFieldRequest",
    ),
    "user": (
        "CurrentUserRequest",
        "ListUsersRequest",
        "GetUserRequest",
    ),
    "user_key_value": (
        "GetUserKeyValueNamespaceRequest",
        "PutUserKeyValueNamespaceKeyRequest",
        "GetUserKeyValueNamespaceKeyRequest",
        "DeleteUserKeyValueNamespaceKeyRequest",
    ),
}

RESPONSE_MODULE_CONTRACTS = {
    "action": ("ActionExecutionResponse", "ListActionsResponse"),
    "activity": ("ActivityMutationResponse", "ListActivityItemsResponse"),
    "agent": ("AgentResponse",),
    "alert": ("ListAlertsResponse",),
    "api_key": ("ListApiKeysResponse",),
    "bookmark": ("ListBookmarksResponse",),
    "card": ("CardsDashboardsResponse", "ListCardsResponse"),
    "channel": ("ListChannelsResponse",),
    "collection": ("ListCollectionsResponse",),
    "common": ("GenericOperationResponse",),
    "dashboard": ("ListDashboardsResponse",),
    "database": ("ListDatabasesResponse",),
    "schema": ("ListTablesResponse",),
    "user": ("ListUsersResponse",),
}


def test_cli_command_modules_import_from_package() -> None:
    assert len(metabaseapi.cli.commands.command_module_names()) == len(metabaseapi.cli.commands.command_module_paths())
    assert len(metabaseapi.cli.commands.command_module_objects()) == len(
        metabaseapi.cli.commands.command_module_paths()
    )
    assert metabaseapi.cli.commands.DATA_STUDIO_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.ACTION_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.ACTIVITY_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.AUTOMAGIC_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.API_KEY_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.AGENT_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.ALERT_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.BOOKMARK_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.COMMENT_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.ANALYTICS_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.CARD_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.CARD_QUERY_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.COLLECTION_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.DATABASE_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.DASHBOARD_QUERY_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.USER_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.USER_KEY_VALUE_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.SCHEMA_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.PLATFORM_BUG_REPORTING_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.PLATFORM_CACHE_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.PLATFORM_CHANNEL_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.DASHBOARD_COMMAND_MODULE in metabaseapi.cli.commands.COMMAND_MODULES
    assert {module.__name__ for module in metabaseapi.cli.commands.command_module_objects()} == set(
        metabaseapi.cli.commands.command_module_paths()
    )
    module_names = metabaseapi.cli.commands.command_module_names()
    module_paths = metabaseapi.cli.commands.command_module_paths()
    assert all(path.endswith(f".{module}") for module, path in zip(module_names, module_paths, strict=True))
    for module_path in module_paths:
        importlib.import_module(module_path)


def test_cli_command_module_groups_are_complete_and_disjoint() -> None:
    grouped = (
        *metabaseapi.cli.commands.CORE_RESOURCE_MODULES,
        *metabaseapi.cli.commands.ASSET_AUTHORING_MODULES,
        *metabaseapi.cli.commands.QUERY_AND_EXECUTION_MODULES,
        *metabaseapi.cli.commands.PLATFORM_OPERATIONS_MODULES,
    )
    assert grouped == metabaseapi.cli.commands.COMMAND_MODULES
    assert len(grouped) == len(set(grouped))
    assert tuple(module.name for module in metabaseapi.cli.commands.COMMAND_MODULE_REGISTRY) == grouped
    assert {
        module.group for module in metabaseapi.cli.commands.COMMAND_MODULE_REGISTRY
    } == set(metabaseapi.cli.commands.COMMAND_MODULE_GROUP_ORDER)


def test_cli_command_registry_matches_package_files() -> None:
    command_package_path = Path(metabaseapi.cli.commands.__file__).parent
    command_module_files = tuple(
        sorted(path.stem for path in command_package_path.glob("*.py") if path.stem != "__init__")
    )
    assert command_module_files == tuple(sorted(metabaseapi.cli.commands.COMMAND_MODULES))


def test_cli_command_group_registry_tracks_declared_modules() -> None:
    registry = metabaseapi.cli.commands.COMMAND_MODULE_GROUPS
    assert registry is metabaseapi.cli.commands.COMMAND_MODULE_GROUP_REGISTRY
    assert tuple(registry.keys()) == (
        "core_resource",
        "asset_authoring",
        "query_and_execution",
        "platform_operations",
    )
    flattened_modules = tuple(module for modules in registry.values() for module in modules)
    assert flattened_modules == metabaseapi.cli.commands.COMMAND_MODULES
    assert metabaseapi.cli.commands.command_group_names() == metabaseapi.cli.commands.COMMAND_MODULE_GROUP_ORDER
    assert metabaseapi.cli.commands.COMMAND_MODULE_GROUP_ORDER == (
        "core_resource",
        "asset_authoring",
        "query_and_execution",
        "platform_operations",
    )
    for group_name in metabaseapi.cli.commands.COMMAND_MODULE_GROUP_ORDER:
        assert metabaseapi.cli.commands.command_modules_in_group(group_name) == registry[group_name]
    assert metabaseapi.cli.commands.command_modules_in_group("platform_operations") == (
        metabaseapi.cli.commands.PLATFORM_BUG_REPORTING_COMMAND_MODULE,
        metabaseapi.cli.commands.PLATFORM_CACHE_COMMAND_MODULE,
        metabaseapi.cli.commands.PLATFORM_CHANNEL_COMMAND_MODULE,
        metabaseapi.cli.commands.PLATFORM_CLOUD_MIGRATION_COMMAND_MODULE,
    )


def test_cli_command_legacy_shims_are_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands_core")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands_dashboard")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands.action_commands")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.cli_commands.platform_cache_commands")


def test_legacy_endpoint_package_name_is_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.metabase")


def test_legacy_wire_module_name_is_not_importable() -> None:
    assert metabaseapi.wire.APIRequestModel.__module__ == "metabaseapi.wire"
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.models")


def test_client_public_exports_use_http_implementation() -> None:
    assert metabaseapi.client.__all__ == ["MetabaseClient"]
    assert metabaseapi.client.MetabaseClient is metabaseapi.client.http.MetabaseClient
    assert not hasattr(metabaseapi.client, "_MetabaseClientRawMixin")
    assert not hasattr(metabaseapi.client, "_MetabaseClientTypedMixin")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.mixins")


def test_client_raw_package_does_not_reexport_aggregate_mixins() -> None:
    assert metabaseapi.client.raw.__all__ == [
        "RAW_MODULES",
        "raw_module_names",
        "raw_module_paths",
    ]
    assert not hasattr(metabaseapi.client.raw, "_MetabaseClientRawMixin")


def test_client_typed_package_is_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.typed")


def test_client_data_studio_replaces_misc_module_name() -> None:
    importlib.import_module("metabaseapi.client.raw.data_studio")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.raw.misc")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.typed.misc")


def test_client_domain_modules_use_singular_names() -> None:
    singular_domains = (
        "action",
        "alert",
        "bookmark",
        "card",
        "channel",
        "cloud_migration",
        "collection",
        "comment",
        "dashboard",
        "database",
        "schema",
        "user",
        "user_key_value",
    )
    legacy_domains = (
        "actions",
        "alerts",
        "bookmarks",
        "cards",
        "channels",
        "cloud",
        "collections",
        "comments",
        "dashboards",
        "databases",
        "tables",
        "users",
    )
    for domain in singular_domains:
        importlib.import_module(f"metabaseapi.client.raw.{domain}")
    for domain in legacy_domains:
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module(f"metabaseapi.client.raw.{domain}")
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module(f"metabaseapi.client.typed.{domain}")


def _client_module_stems(package: object) -> tuple[str, ...]:
    package_file = getattr(package, "__file__", None)
    assert package_file is not None
    package_path = Path(package_file).parent
    return tuple(sorted(path.stem for path in package_path.glob("*.py") if path.stem != "__init__"))


def test_client_raw_module_names_match_registry() -> None:
    raw_modules = _client_module_stems(metabaseapi.client.raw)

    assert raw_modules == tuple(sorted(metabaseapi.client.raw.RAW_MODULES))
    assert metabaseapi.client.raw.raw_module_names() == metabaseapi.client.raw.RAW_MODULES
    assert metabaseapi.client.raw.raw_module_paths() == tuple(
        f"metabaseapi.client.raw.{module_name}" for module_name in metabaseapi.client.raw.RAW_MODULES
    )


def test_cli_command_modules_depend_on_runtime_not_cli_facade() -> None:
    command_package_path = Path(metabaseapi.cli.commands.__file__).parent
    for source_path in command_package_path.glob("*.py"):
        if source_path.stem == "__init__":
            continue
        source = source_path.read_text(encoding="utf-8")
        assert "from metabaseapi.cli import " not in source


def test_client_domain_modules_expose_functions_not_mixins() -> None:
    package_path = Path(metabaseapi.client.raw.__file__).parent
    for source_path in package_path.glob("*.py"):
        if source_path.stem == "__init__":
            continue
        source = source_path.read_text(encoding="utf-8")
        assert "class _" not in source
        assert "Mixin" not in source


def test_cli_entrypoint_importable() -> None:
    assert hasattr(metabaseapi.cli, "app")


def test_client_public_module_exports_concrete_http_implementation() -> None:
    assert metabaseapi.client.MetabaseClient.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client.__all__ == ["MetabaseClient"]
    assert not hasattr(metabaseapi.client, "_MetabaseClientRawMixin")
    assert not hasattr(metabaseapi.client, "_MetabaseClientTypedMixin")


def test_endpoints_execution_owns_request_interface() -> None:
    assert metabaseapi.endpoints.execution.__all__ == ["EndpointRequest", "MetabaseRequestClient"]
    assert not hasattr(metabaseapi.endpoints.execution, "_BaseMetabaseRequest")
    assert metabaseapi.endpoints.requests.card.ListCardsRequest.__mro__[1].__module__ == (
        "metabaseapi.endpoints.execution"
    )
    assert (
        metabaseapi.endpoints.requests.card.ListCardsRequest.__mro__[1].__name__
        == "EndpointRequest[ListCardsResponse]"
    )


def test_endpoints_public_exports_are_submodules_only() -> None:
    assert metabaseapi.endpoints.__all__ == ["entities", "execution", "requests", "responses"]
    assert metabaseapi.endpoints.entities is metabaseapi.endpoints.entities
    assert metabaseapi.endpoints.execution is metabaseapi.endpoints.execution
    assert metabaseapi.endpoints.requests is metabaseapi.endpoints.requests
    assert metabaseapi.endpoints.responses is metabaseapi.endpoints.responses
    assert not hasattr(metabaseapi.endpoints, "ListCardsRequest")


def test_endpoints_response_package_does_not_reexport_response_classes() -> None:
    assert metabaseapi.endpoints.responses.__all__ == [
        "RESPONSE_MODULES",
        "response_module_names",
        "response_module_paths",
    ]
    assert not hasattr(metabaseapi.endpoints.responses, "ListCardsResponse")


def test_endpoints_response_registry_matches_package_files() -> None:
    response_package_path = Path(metabaseapi.endpoints.responses.__file__).parent
    response_module_files = tuple(
        sorted(path.stem for path in response_package_path.glob("*.py") if path.stem != "__init__")
    )
    assert response_module_files == tuple(sorted(metabaseapi.endpoints.responses.RESPONSE_MODULES))
    assert tuple(RESPONSE_MODULE_CONTRACTS) == metabaseapi.endpoints.responses.response_module_names()
    assert metabaseapi.endpoints.responses.response_module_paths() == tuple(
        f"metabaseapi.endpoints.responses.{module_name}"
        for module_name in metabaseapi.endpoints.responses.RESPONSE_MODULES
    )


def test_endpoints_response_modules_own_response_classes() -> None:
    for module_name, response_names in RESPONSE_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.responses.{module_name}")
        for response_name in response_names:
            assert getattr(domain_module, response_name).__module__ == domain_module.__name__


def test_endpoints_request_package_does_not_reexport_request_classes() -> None:
    assert metabaseapi.endpoints.requests.__all__ == [
        "REQUEST_MODULES",
        "request_module_names",
        "request_module_paths",
    ]
    assert not hasattr(metabaseapi.endpoints.requests, "ListCardsRequest")


def test_endpoints_request_modules_own_request_classes() -> None:
    for module_name, request_names in REQUEST_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.requests.{module_name}")
        for request_name in request_names:
            assert getattr(domain_module, request_name).__module__ == domain_module.__name__


def test_endpoints_request_registry_matches_package_files() -> None:
    endpoint_package_path = Path(metabaseapi.endpoints.requests.__file__).parent
    endpoint_module_files = tuple(
        sorted(path.stem for path in endpoint_package_path.glob("*.py") if path.stem != "__init__")
    )
    assert endpoint_module_files == tuple(sorted(metabaseapi.endpoints.requests.REQUEST_MODULES))
    assert tuple(REQUEST_MODULE_CONTRACTS) == metabaseapi.endpoints.requests.request_module_names()
    assert metabaseapi.endpoints.requests.request_module_paths() == tuple(
        f"metabaseapi.endpoints.requests.{module_name}"
        for module_name in metabaseapi.endpoints.requests.REQUEST_MODULES
    )


def _command_names_from_sources() -> list[str]:
    command_names: list[str] = []
    for module in metabaseapi.cli.commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        if source_path is None:
            continue
        source = source_path.read_text(encoding="utf-8")
        command_names.extend(re.findall(r'@app\.command\("([^"]+)"\)', source))
    return command_names


def _command_names_by_module() -> dict[str, tuple[str, ...]]:
    command_names: dict[str, tuple[str, ...]] = {}
    for module in metabaseapi.cli.commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        if source_path is None:
            continue
        source = source_path.read_text(encoding="utf-8")
        command_names[module.__name__.rsplit(".", maxsplit=1)[-1]] = tuple(
            re.findall(r'@app\.command\("([^"]+)"\)', source)
        )
    return command_names


def test_cli_command_names_are_unique_across_modules() -> None:
    command_names = _command_names_from_sources()
    assert len(command_names) == len(set(command_names))


def test_database_lifecycle_commands_share_database_module() -> None:
    command_names = _command_names_by_module()
    assert "create-database" in command_names[metabaseapi.cli.commands.DATABASE_COMMAND_MODULE]
    assert "get-database" in command_names[metabaseapi.cli.commands.DATABASE_COMMAND_MODULE]
    assert "list-databases" in command_names[metabaseapi.cli.commands.DATABASE_COMMAND_MODULE]
    assert "create-database" not in command_names[metabaseapi.cli.commands.SCHEMA_COMMAND_MODULE]


def test_resource_list_commands_live_with_resource_modules() -> None:
    command_names = _command_names_by_module()
    assert "list-cards" in command_names[metabaseapi.cli.commands.CARD_COMMAND_MODULE]
    assert "list-collections" in command_names[metabaseapi.cli.commands.COLLECTION_COMMAND_MODULE]
    assert "list-dashboards" in command_names[metabaseapi.cli.commands.DASHBOARD_COMMAND_MODULE]
    assert "list-users" in command_names[metabaseapi.cli.commands.USER_COMMAND_MODULE]
    assert "list-tables" in command_names[metabaseapi.cli.commands.SCHEMA_COMMAND_MODULE]


def test_current_user_command_lives_with_user_commands() -> None:
    command_names = _command_names_by_module()
    assert "current-user" in command_names[metabaseapi.cli.commands.USER_COMMAND_MODULE]
    assert "get-user-key-value-namespace" not in command_names[metabaseapi.cli.commands.USER_COMMAND_MODULE]
    assert "current-user" not in command_names[metabaseapi.cli.commands.ANALYTICS_COMMAND_MODULE]


def test_user_key_value_commands_live_with_user_key_value_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "get-user-key-value-namespace",
        "put-user-key-value-namespace-key",
        "get-user-key-value-namespace-key",
        "delete-user-key-value-namespace-key",
    ):
        assert command_name in command_names[metabaseapi.cli.commands.USER_KEY_VALUE_COMMAND_MODULE]
        assert command_name not in command_names[metabaseapi.cli.commands.USER_COMMAND_MODULE]


def test_activity_commands_live_with_activity_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "most-recently-viewed-dashboard",
        "list-popular-items",
        "list-recent-views",
        "list-recents",
        "create-recent",
    ):
        assert command_name in command_names[metabaseapi.cli.commands.ACTIVITY_COMMAND_MODULE]
        assert command_name not in command_names[metabaseapi.cli.commands.ANALYTICS_COMMAND_MODULE]


def test_bookmark_commands_live_with_bookmark_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "list-bookmarks",
        "update-bookmark-ordering",
        "create-bookmark",
        "delete-bookmark",
    ):
        assert command_name in command_names[metabaseapi.cli.commands.BOOKMARK_COMMAND_MODULE]
        assert command_name not in command_names[metabaseapi.cli.commands.ACTION_COMMAND_MODULE]


def test_cli_app_registers_all_declared_commands() -> None:
    source_command_names = sorted(_command_names_from_sources())
    app_command_names = sorted(
        [command.name for command in metabaseapi.cli.app.registered_commands if command.name is not None]
    )

    assert len(app_command_names) == len(source_command_names)
    assert app_command_names == source_command_names


def test_cli_command_modules_are_compact() -> None:
    for module in metabaseapi.cli.commands.command_module_objects():
        source_path = Path(module.__file__) if module.__file__ else None
        assert source_path is not None
        line_count = len(source_path.read_text(encoding="utf-8").splitlines())
        assert line_count < 1000, f"{module.__name__} has {line_count} lines"


def test_cli_command_module_objects_are_cached() -> None:
    first = metabaseapi.cli.commands.command_module_objects()
    second = metabaseapi.cli.commands.command_module_objects()
    assert first is second


def test_cli_command_modules_importable_in_multiple_orders() -> None:
    project_root = Path(__file__).resolve().parents[1]
    python_path = str(project_root / "src")
    env = dict(os.environ)
    env["PYTHONPATH"] = python_path if not env.get("PYTHONPATH") else f"{python_path}{os.pathsep}{env['PYTHONPATH']}"

    import_order_cases = [
        dedent(
            """
            import metabaseapi.cli.commands
            import metabaseapi.cli
            print(len(metabaseapi.cli.commands.command_module_objects()), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            import metabaseapi.cli
            import metabaseapi.cli.commands
            print(len(metabaseapi.cli.commands.command_module_objects()), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            from metabaseapi.cli.commands import *  # noqa: F401
            import metabaseapi.cli
            print(len(COMMAND_MODULES), len(COMMAND_MODULES_OBJECTS), len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
    ]

    for script in import_order_cases:
        result = subprocess.run(
            [sys.executable, "-c", script],
            check=True,
            env=env,
            capture_output=True,
            text=True,
        )
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 1
        values = [int(item) for item in lines[0].split()]
        assert len(values) in (2, 3)
        assert all(value > 0 for value in values)
        expected_modules = len(metabaseapi.cli.commands.command_module_objects())
        assert values[0] == expected_modules
