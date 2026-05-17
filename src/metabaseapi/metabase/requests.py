from __future__ import annotations

from metabaseapi.metabase.endpoint_requests.action import CreateActionPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.action import CreateActionRequest
from metabaseapi.metabase.endpoint_requests.action import DeleteActionPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.action import DeleteActionRequest
from metabaseapi.metabase.endpoint_requests.action import ExecuteActionRequest
from metabaseapi.metabase.endpoint_requests.action import GetActionExecuteRequest
from metabaseapi.metabase.endpoint_requests.action import GetActionRequest
from metabaseapi.metabase.endpoint_requests.action import ListActionsRequest
from metabaseapi.metabase.endpoint_requests.action import ListPublicActionsRequest
from metabaseapi.metabase.endpoint_requests.action import UpdateActionRequest
from metabaseapi.metabase.endpoint_requests.activity import CreateRecentRequest
from metabaseapi.metabase.endpoint_requests.activity import GetMostRecentlyViewedDashboardRequest
from metabaseapi.metabase.endpoint_requests.activity import ListPopularItemsRequest
from metabaseapi.metabase.endpoint_requests.activity import ListRecentsRequest
from metabaseapi.metabase.endpoint_requests.activity import ListRecentViewsRequest
from metabaseapi.metabase.endpoint_requests.agent import AgentConstructQueryRequest
from metabaseapi.metabase.endpoint_requests.agent import AgentExecuteRequest
from metabaseapi.metabase.endpoint_requests.agent import AgentPingRequest
from metabaseapi.metabase.endpoint_requests.agent import AgentQueryRequest
from metabaseapi.metabase.endpoint_requests.agent import AgentSearchRequest
from metabaseapi.metabase.endpoint_requests.agent import GetAgentMetricFieldValuesRequest
from metabaseapi.metabase.endpoint_requests.agent import GetAgentMetricRequest
from metabaseapi.metabase.endpoint_requests.agent import GetAgentTableFieldValuesRequest
from metabaseapi.metabase.endpoint_requests.agent import GetAgentTableRequest
from metabaseapi.metabase.endpoint_requests.ai_entity_analysis import AnalyzeChartRequest
from metabaseapi.metabase.endpoint_requests.alert import DeleteAlertSubscriptionRequest
from metabaseapi.metabase.endpoint_requests.alert import GetAlertRequest
from metabaseapi.metabase.endpoint_requests.alert import ListAlertsRequest
from metabaseapi.metabase.endpoint_requests.analytics import CreateAnalyticsEventBatchRequest
from metabaseapi.metabase.endpoint_requests.analytics import GetAnonymousStatsRequest
from metabaseapi.metabase.endpoint_requests.api_key import CountApiKeysRequest
from metabaseapi.metabase.endpoint_requests.api_key import CreateApiKeyRequest
from metabaseapi.metabase.endpoint_requests.api_key import DeleteApiKeyRequest
from metabaseapi.metabase.endpoint_requests.api_key import ListApiKeysRequest
from metabaseapi.metabase.endpoint_requests.api_key import RegenerateApiKeyRequest
from metabaseapi.metabase.endpoint_requests.api_key import UpdateApiKeyRequest
from metabaseapi.metabase.endpoint_requests.automagic import AutomagicDashboardRequest
from metabaseapi.metabase.endpoint_requests.automagic import AutomagicDatabaseCandidatesRequest
from metabaseapi.metabase.endpoint_requests.automagic import AutomagicModelIndexPrimaryKeyRequest
from metabaseapi.metabase.endpoint_requests.bookmark import CreateBookmarkRequest
from metabaseapi.metabase.endpoint_requests.bookmark import DeleteBookmarkRequest
from metabaseapi.metabase.endpoint_requests.bookmark import ListBookmarksRequest
from metabaseapi.metabase.endpoint_requests.bookmark import UpdateBookmarkOrderingRequest
from metabaseapi.metabase.endpoint_requests.bug_reporting import GetBugReportingConnectionPoolDetailsRequest
from metabaseapi.metabase.endpoint_requests.bug_reporting import GetBugReportingDetailsRequest
from metabaseapi.metabase.endpoint_requests.cache import DeleteCacheRequest
from metabaseapi.metabase.endpoint_requests.cache import GetCacheRequest
from metabaseapi.metabase.endpoint_requests.cache import InvalidateCacheRequest
from metabaseapi.metabase.endpoint_requests.cache import PutCacheRequest
from metabaseapi.metabase.endpoint_requests.card import CardParamsSearchRequest
from metabaseapi.metabase.endpoint_requests.card import CardParamsValuesRequest
from metabaseapi.metabase.endpoint_requests.card import CardQueryExportRequest
from metabaseapi.metabase.endpoint_requests.card import CardQueryRequest
from metabaseapi.metabase.endpoint_requests.card import CardRemappingRequest
from metabaseapi.metabase.endpoint_requests.card import CardsDashboardsRequest
from metabaseapi.metabase.endpoint_requests.card import CopyCardRequest
from metabaseapi.metabase.endpoint_requests.card import CreateCardPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.card import CreateCardRequest
from metabaseapi.metabase.endpoint_requests.card import DeleteCardPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.card import DeleteCardRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardCollectionsRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardDashboardsRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardEmbeddableRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardPublicRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardQueryMetadataRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardRequest
from metabaseapi.metabase.endpoint_requests.card import GetCardSeriesRequest
from metabaseapi.metabase.endpoint_requests.card import ListCardsRequest
from metabaseapi.metabase.endpoint_requests.card import MoveCardsRequest
from metabaseapi.metabase.endpoint_requests.card import PostCardPivotQueryRequest
from metabaseapi.metabase.endpoint_requests.card import UpdateCardRequest
from metabaseapi.metabase.endpoint_requests.channel import CreateChannelRequest
from metabaseapi.metabase.endpoint_requests.channel import GetChannelRequest
from metabaseapi.metabase.endpoint_requests.channel import ListChannelsRequest
from metabaseapi.metabase.endpoint_requests.channel import TestChannelRequest
from metabaseapi.metabase.endpoint_requests.channel import UpdateChannelRequest
from metabaseapi.metabase.endpoint_requests.cloud_migration import CancelCloudMigrationRequest
from metabaseapi.metabase.endpoint_requests.cloud_migration import CreateCloudMigrationRequest
from metabaseapi.metabase.endpoint_requests.cloud_migration import GetCloudMigrationRequest
from metabaseapi.metabase.endpoint_requests.collection import CreateCollectionRequest
from metabaseapi.metabase.endpoint_requests.collection import DeleteCollectionRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionGraphRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionItemsRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionRootItemsRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionRootRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionTrashRequest
from metabaseapi.metabase.endpoint_requests.collection import GetCollectionTreeRequest
from metabaseapi.metabase.endpoint_requests.collection import ListCollectionsRequest
from metabaseapi.metabase.endpoint_requests.collection import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase.endpoint_requests.collection import PostCollectionRootMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase.endpoint_requests.collection import PutCollectionGraphRequest
from metabaseapi.metabase.endpoint_requests.collection import PutCollectionRequest
from metabaseapi.metabase.endpoint_requests.comment import DeleteCommentRequest
from metabaseapi.metabase.endpoint_requests.comment import GetCommentMentionsRequest
from metabaseapi.metabase.endpoint_requests.comment import GetCommentRequest
from metabaseapi.metabase.endpoint_requests.comment import PostCommentReactionRequest
from metabaseapi.metabase.endpoint_requests.comment import PostCommentRequest
from metabaseapi.metabase.endpoint_requests.comment import UpdateCommentRequest
from metabaseapi.metabase.endpoint_requests.dashboard import CopyDashboardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import CreateDashboardPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.dashboard import DashboardParamRemappingRequest
from metabaseapi.metabase.endpoint_requests.dashboard import DashboardParamSearchRequest
from metabaseapi.metabase.endpoint_requests.dashboard import DashboardParamValuesRequest
from metabaseapi.metabase.endpoint_requests.dashboard import DeleteDashboardPublicLinkRequest
from metabaseapi.metabase.endpoint_requests.dashboard import DeleteDashboardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import ExecuteDashboardDashcardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardDashcardExecuteRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardEmbeddableRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardItemsRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardPublicRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardQueryMetadataRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardRelatedRequest
from metabaseapi.metabase.endpoint_requests.dashboard import GetDashboardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import ListDashboardsRequest
from metabaseapi.metabase.endpoint_requests.dashboard import PostDashboardPivotQueryRequest
from metabaseapi.metabase.endpoint_requests.dashboard import PostDashboardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import SaveDashboardRequest
from metabaseapi.metabase.endpoint_requests.dashboard import SaveDashboardToCollectionRequest
from metabaseapi.metabase.endpoint_requests.dashboard import UpdateDashboardCardsRequest
from metabaseapi.metabase.endpoint_requests.dashboard import UpdateDashboardRequest
from metabaseapi.metabase.endpoint_requests.data_studio import DataStudioTableDiscardValuesRequest
from metabaseapi.metabase.endpoint_requests.data_studio import DataStudioTableEditRequest
from metabaseapi.metabase.endpoint_requests.data_studio import DataStudioTableRescanValuesRequest
from metabaseapi.metabase.endpoint_requests.data_studio import DataStudioTableSelectionRequest
from metabaseapi.metabase.endpoint_requests.data_studio import DataStudioTableSyncSchemaRequest
from metabaseapi.metabase.endpoint_requests.database import CreateDatabaseRequest
from metabaseapi.metabase.endpoint_requests.database import GetDatabaseRequest
from metabaseapi.metabase.endpoint_requests.database import ListDatabasesRequest
from metabaseapi.metabase.endpoint_requests.schema import GetFieldRequest
from metabaseapi.metabase.endpoint_requests.schema import GetTableRequest
from metabaseapi.metabase.endpoint_requests.schema import ListTablesRequest
from metabaseapi.metabase.endpoint_requests.user import CurrentUserRequest
from metabaseapi.metabase.endpoint_requests.user import GetUserRequest
from metabaseapi.metabase.endpoint_requests.user import ListUsersRequest
from metabaseapi.metabase.endpoint_requests.user_key_value import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase.endpoint_requests.user_key_value import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase.endpoint_requests.user_key_value import GetUserKeyValueNamespaceRequest
from metabaseapi.metabase.endpoint_requests.user_key_value import PutUserKeyValueNamespaceKeyRequest
from metabaseapi.metabase.request_base import MetabaseRequestClient

__all__ = [
    "AgentConstructQueryRequest",
    "AgentExecuteRequest",
    "AgentPingRequest",
    "AgentQueryRequest",
    "AgentSearchRequest",
    "AnalyzeChartRequest",
    "AutomagicDashboardRequest",
    "AutomagicDatabaseCandidatesRequest",
    "AutomagicModelIndexPrimaryKeyRequest",
    "CancelCloudMigrationRequest",
    "CardParamsSearchRequest",
    "CardParamsValuesRequest",
    "CardQueryExportRequest",
    "CardQueryRequest",
    "CardRemappingRequest",
    "CardsDashboardsRequest",
    "CopyCardRequest",
    "CopyDashboardRequest",
    "CountApiKeysRequest",
    "CreateActionPublicLinkRequest",
    "CreateActionRequest",
    "CreateAnalyticsEventBatchRequest",
    "CreateApiKeyRequest",
    "CreateBookmarkRequest",
    "CreateCardPublicLinkRequest",
    "CreateCardRequest",
    "CreateChannelRequest",
    "CreateCloudMigrationRequest",
    "CreateCollectionRequest",
    "CreateDashboardPublicLinkRequest",
    "CreateDatabaseRequest",
    "CreateRecentRequest",
    "CurrentUserRequest",
    "DashboardParamRemappingRequest",
    "DashboardParamSearchRequest",
    "DashboardParamValuesRequest",
    "DataStudioTableDiscardValuesRequest",
    "DataStudioTableEditRequest",
    "DataStudioTableRescanValuesRequest",
    "DataStudioTableSelectionRequest",
    "DataStudioTableSyncSchemaRequest",
    "DeleteActionPublicLinkRequest",
    "DeleteActionRequest",
    "DeleteAlertSubscriptionRequest",
    "DeleteApiKeyRequest",
    "DeleteBookmarkRequest",
    "DeleteCacheRequest",
    "DeleteCardPublicLinkRequest",
    "DeleteCardRequest",
    "DeleteCollectionRequest",
    "DeleteCommentRequest",
    "DeleteDashboardPublicLinkRequest",
    "DeleteDashboardRequest",
    "DeleteUserKeyValueNamespaceKeyRequest",
    "ExecuteActionRequest",
    "ExecuteDashboardDashcardRequest",
    "GetActionExecuteRequest",
    "GetActionRequest",
    "GetAgentMetricFieldValuesRequest",
    "GetAgentMetricRequest",
    "GetAgentTableFieldValuesRequest",
    "GetAgentTableRequest",
    "GetAlertRequest",
    "GetAnonymousStatsRequest",
    "GetBugReportingConnectionPoolDetailsRequest",
    "GetBugReportingDetailsRequest",
    "GetCacheRequest",
    "GetCardCollectionsRequest",
    "GetCardDashboardsRequest",
    "GetCardEmbeddableRequest",
    "GetCardPublicRequest",
    "GetCardQueryMetadataRequest",
    "GetCardRequest",
    "GetCardSeriesRequest",
    "GetChannelRequest",
    "GetCloudMigrationRequest",
    "GetCollectionDashboardQuestionCandidatesRequest",
    "GetCollectionGraphRequest",
    "GetCollectionItemsRequest",
    "GetCollectionRequest",
    "GetCollectionRootDashboardQuestionCandidatesRequest",
    "GetCollectionRootItemsRequest",
    "GetCollectionRootRequest",
    "GetCollectionTrashRequest",
    "GetCollectionTreeRequest",
    "GetCommentMentionsRequest",
    "GetCommentRequest",
    "GetDashboardDashcardExecuteRequest",
    "GetDashboardEmbeddableRequest",
    "GetDashboardItemsRequest",
    "GetDashboardPublicRequest",
    "GetDashboardQueryMetadataRequest",
    "GetDashboardRelatedRequest",
    "GetDashboardRequest",
    "GetDatabaseRequest",
    "GetFieldRequest",
    "GetMostRecentlyViewedDashboardRequest",
    "GetTableRequest",
    "GetUserKeyValueNamespaceKeyRequest",
    "GetUserKeyValueNamespaceRequest",
    "GetUserRequest",
    "InvalidateCacheRequest",
    "ListActionsRequest",
    "ListAlertsRequest",
    "ListApiKeysRequest",
    "ListBookmarksRequest",
    "ListCardsRequest",
    "ListChannelsRequest",
    "ListCollectionsRequest",
    "ListDashboardsRequest",
    "ListDatabasesRequest",
    "ListPopularItemsRequest",
    "ListPublicActionsRequest",
    "ListRecentViewsRequest",
    "ListRecentsRequest",
    "ListTablesRequest",
    "ListUsersRequest",
    "MetabaseRequestClient",
    "MoveCardsRequest",
    "PostCardPivotQueryRequest",
    "PostCollectionMoveDashboardQuestionCandidatesRequest",
    "PostCollectionRootMoveDashboardQuestionCandidatesRequest",
    "PostCommentReactionRequest",
    "PostCommentRequest",
    "PostDashboardPivotQueryRequest",
    "PostDashboardRequest",
    "PutCacheRequest",
    "PutCollectionGraphRequest",
    "PutCollectionRequest",
    "PutUserKeyValueNamespaceKeyRequest",
    "RegenerateApiKeyRequest",
    "SaveDashboardRequest",
    "SaveDashboardToCollectionRequest",
    "TestChannelRequest",
    "UpdateActionRequest",
    "UpdateApiKeyRequest",
    "UpdateBookmarkOrderingRequest",
    "UpdateCardRequest",
    "UpdateChannelRequest",
    "UpdateCommentRequest",
    "UpdateDashboardCardsRequest",
    "UpdateDashboardRequest",
]
