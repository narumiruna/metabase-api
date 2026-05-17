from __future__ import annotations

import importlib
import inspect
import os
import re
import subprocess
import sys
from pathlib import Path
from textwrap import dedent
from types import ModuleType

import pytest

import metabaseapi.cli
import metabaseapi.cli.commands
import metabaseapi.cli.runtime
import metabaseapi.client
import metabaseapi.client.http
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
import metabaseapi.endpoints.requests.card_query
import metabaseapi.endpoints.requests.channel
import metabaseapi.endpoints.requests.cloud_migration
import metabaseapi.endpoints.requests.collection
import metabaseapi.endpoints.requests.collection_graph
import metabaseapi.endpoints.requests.collection_root
import metabaseapi.endpoints.requests.comment
import metabaseapi.endpoints.requests.dashboard
import metabaseapi.endpoints.requests.dashboard_query
import metabaseapi.endpoints.requests.data_studio
import metabaseapi.endpoints.requests.database
import metabaseapi.endpoints.requests.dataset
import metabaseapi.endpoints.requests.document
import metabaseapi.endpoints.requests.ee_action_v2
import metabaseapi.endpoints.requests.ee_advanced_permissions
import metabaseapi.endpoints.requests.ee_ai_controls
import metabaseapi.endpoints.requests.ee_audit_app
import metabaseapi.endpoints.requests.ee_billing
import metabaseapi.endpoints.requests.ee_cloud
import metabaseapi.endpoints.requests.ee_content_translation
import metabaseapi.endpoints.requests.ee_data_complexity_score
import metabaseapi.endpoints.requests.ee_data_studio
import metabaseapi.endpoints.requests.ee_database_replication
import metabaseapi.endpoints.requests.ee_database_routing
import metabaseapi.endpoints.requests.ee_dependencies
import metabaseapi.endpoints.requests.ee_email
import metabaseapi.endpoints.requests.ee_embedding_hub
import metabaseapi.endpoints.requests.ee_gsheets
import metabaseapi.endpoints.requests.ee_library
import metabaseapi.endpoints.requests.ee_logs
import metabaseapi.endpoints.requests.ee_metabot
import metabaseapi.endpoints.requests.ee_permission_debug
import metabaseapi.endpoints.requests.ee_remote_sync
import metabaseapi.endpoints.requests.ee_replacement
import metabaseapi.endpoints.requests.ee_scim
import metabaseapi.endpoints.requests.ee_security_center
import metabaseapi.endpoints.requests.ee_semantic_search
import metabaseapi.endpoints.requests.ee_serialization
import metabaseapi.endpoints.requests.ee_stale
import metabaseapi.endpoints.requests.ee_support_access_grant
import metabaseapi.endpoints.requests.ee_tenant
import metabaseapi.endpoints.requests.ee_transforms
import metabaseapi.endpoints.requests.ee_transforms_python
import metabaseapi.endpoints.requests.ee_upload_management
import metabaseapi.endpoints.requests.eid_translation
import metabaseapi.endpoints.requests.email
import metabaseapi.endpoints.requests.embed
import metabaseapi.endpoints.requests.embed_theme
import metabaseapi.endpoints.requests.field
import metabaseapi.endpoints.requests.frontend_errors
import metabaseapi.endpoints.requests.geojson
import metabaseapi.endpoints.requests.glossary
import metabaseapi.endpoints.requests.google
import metabaseapi.endpoints.requests.ldap
import metabaseapi.endpoints.requests.llm
import metabaseapi.endpoints.requests.logger
import metabaseapi.endpoints.requests.login_history
import metabaseapi.endpoints.requests.measure
import metabaseapi.endpoints.requests.metabot
import metabaseapi.endpoints.requests.metric
import metabaseapi.endpoints.requests.model_index
import metabaseapi.endpoints.requests.moderation_review
import metabaseapi.endpoints.requests.mt_gtap
import metabaseapi.endpoints.requests.mt_user
import metabaseapi.endpoints.requests.native_query_snippet
import metabaseapi.endpoints.requests.notification
import metabaseapi.endpoints.requests.notify
import metabaseapi.endpoints.requests.permissions
import metabaseapi.endpoints.requests.persist
import metabaseapi.endpoints.requests.premium_features
import metabaseapi.endpoints.requests.preview_embed
import metabaseapi.endpoints.requests.product_feedback
import metabaseapi.endpoints.requests.public
import metabaseapi.endpoints.requests.pulse
import metabaseapi.endpoints.requests.revision
import metabaseapi.endpoints.requests.search
import metabaseapi.endpoints.requests.segment
import metabaseapi.endpoints.requests.session
import metabaseapi.endpoints.requests.setting
import metabaseapi.endpoints.requests.setup
import metabaseapi.endpoints.requests.slack
import metabaseapi.endpoints.requests.table
import metabaseapi.endpoints.requests.task
import metabaseapi.endpoints.requests.tiles
import metabaseapi.endpoints.requests.timeline
import metabaseapi.endpoints.requests.timeline_event
import metabaseapi.endpoints.requests.transform
import metabaseapi.endpoints.requests.transform_job
import metabaseapi.endpoints.requests.transform_tag
import metabaseapi.endpoints.requests.upload
import metabaseapi.endpoints.requests.user
import metabaseapi.endpoints.requests.user_key_value
import metabaseapi.endpoints.requests.util
import metabaseapi.endpoints.responses
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
        "CreateAgentDashboardRequest",
        "CreateAgentQuestionRequest",
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
        "AutomagicEntityRequest",
        "AutomagicEntityCellRequest",
        "AutomagicEntityCellCompareRequest",
        "AutomagicEntityCellRuleRequest",
        "AutomagicEntityCellRuleCompareRequest",
        "AutomagicEntityCompareRequest",
        "AutomagicEntityQueryMetadataRequest",
        "AutomagicEntityRuleRequest",
        "AutomagicEntityRuleCompareRequest",
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
        "GetCardPublicRequest",
        "CreateCardPublicLinkRequest",
        "DeleteCardPublicLinkRequest",
        "UpdateCardRequest",
        "DeleteCardRequest",
        "CopyCardRequest",
        "MoveCardsRequest",
    ),
    "card_query": (
        "PostCardPivotQueryRequest",
        "CardParamsSearchRequest",
        "CardParamsValuesRequest",
        "CardQueryRequest",
        "CardQueryExportRequest",
        "GetCardDashboardsRequest",
        "CardRemappingRequest",
        "GetCardQueryMetadataRequest",
        "GetCardSeriesRequest",
        "CardsDashboardsRequest",
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
        "GetCollectionTreeRequest",
        "GetCollectionDashboardQuestionCandidatesRequest",
        "GetCollectionItemsRequest",
        "GetCollectionTrashRequest",
        "PostCollectionMoveDashboardQuestionCandidatesRequest",
        "ListCollectionsRequest",
        "GetCollectionRequest",
        "PutCollectionRequest",
        "DeleteCollectionRequest",
    ),
    "collection_graph": (
        "GetCollectionGraphRequest",
        "PutCollectionGraphRequest",
    ),
    "collection_root": (
        "GetCollectionRootRequest",
        "GetCollectionRootDashboardQuestionCandidatesRequest",
        "GetCollectionRootItemsRequest",
        "PostCollectionRootMoveDashboardQuestionCandidatesRequest",
    ),
    "database": (
        "ListDatabasesRequest",
        "CreateDatabaseRequest",
        "CreateSampleDatabaseRequest",
        "GetDatabaseRequest",
        "UpdateDatabaseRequest",
        "DeleteDatabaseRequest",
        "ValidateDatabaseRequest",
        "GetDatabaseFieldValuesRequest",
        "GetDatabaseMetadataRequest",
        "PostDatabaseMetadataRequest",
        "GetDatabaseAutocompleteSuggestionsRequest",
        "GetDatabaseCardAutocompleteSuggestionsRequest",
        "DiscardDatabaseValuesRequest",
        "DismissDatabaseSpinnerRequest",
        "GetDatabaseFieldsRequest",
        "GetDatabaseHealthcheckRequest",
        "GetDatabaseIdFieldsRequest",
        "GetDatabaseDetailMetadataRequest",
        "RescanDatabaseValuesRequest",
        "GetDatabaseSchemaRequest",
        "GetDatabaseSchemaTablesRequest",
        "GetDatabaseSchemasRequest",
        "GetDatabaseSettingsAvailableRequest",
        "SyncDatabaseSchemaRequest",
        "GetDatabaseSyncableSchemasRequest",
        "GetDatabaseUsageInfoRequest",
        "GetVirtualDatabaseDatasetsRequest",
        "GetVirtualDatabaseSchemaDatasetsRequest",
        "GetVirtualDatabaseMetadataRequest",
        "GetVirtualDatabaseSchemaRequest",
        "GetVirtualDatabaseSchemasRequest",
    ),
    "dataset": (
        "DatasetQueryRequest",
        "DatasetNativeRequest",
        "DatasetParameterRemappingRequest",
        "DatasetParameterSearchRequest",
        "DatasetParameterValuesRequest",
        "DatasetPivotRequest",
        "DatasetQueryMetadataRequest",
        "DatasetExportRequest",
    ),
    "document": (
        "ListDocumentsRequest",
        "CreateDocumentRequest",
        "ListPublicDocumentsRequest",
        "GetDocumentRequest",
        "UpdateDocumentRequest",
        "DeleteDocumentRequest",
        "DocumentCardQueryExportRequest",
        "CreateDocumentPublicLinkRequest",
        "DeleteDocumentPublicLinkRequest",
        "CopyDocumentRequest",
    ),
    "ee_action_v2": (
        "EeActionV2ExecuteRequest",
        "EeActionV2ExecuteBulkRequest",
        "EeActionV2ExecuteFormRequest",
    ),
    "ee_advanced_permissions": (
        "GetEeApplicationPermissionsGraphRequest",
        "PutEeApplicationPermissionsGraphRequest",
        "GetEeImpersonationRequest",
        "DeleteEeImpersonationRequest",
    ),
    "ee_ai_controls": (
        "GetEeAiControlsPermissionsRequest",
        "PutEeAiControlsPermissionsRequest",
        "EnableEeAiControlsAdvancedPermissionsRequest",
        "DisableEeAiControlsAdvancedPermissionsRequest",
        "GetEeAiControlsUsageInstanceRequest",
        "PutEeAiControlsUsageInstanceRequest",
        "GetEeAiControlsUsageTenantRequest",
        "GetEeAiControlsUsageTenantIdRequest",
        "PutEeAiControlsUsageTenantIdRequest",
        "GetEeAiControlsUsageGroupRequest",
        "GetEeAiControlsUsageGroupIdRequest",
        "PutEeAiControlsUsageGroupIdRequest",
    ),
    "ee_audit_app": (
        "PostEeAuditAppAnalyticsDevExportRequest",
        "GetEeAuditAppUserAuditInfoRequest",
        "DeleteEeAuditAppUserSubscriptionsRequest",
    ),
    "ee_billing": ("GetEeBillingRequest",),
    "ee_cloud": (
        "GetEeCloudAddOnsAddonsRequest",
        "GetEeCloudAddOnsPlansRequest",
        "PostEeCloudAddOnsProductTypeRequest",
        "DeleteEeCloudAddOnsProductTypeRequest",
        "PostEeCloudProxyOperationIdRequest",
    ),
    "ee_content_translation": (
        "GetEeContentTranslationCsvRequest",
        "GetEeContentTranslationDictionaryRequest",
        "GetEeContentTranslationDictionaryTokenRequest",
        "PostEeContentTranslationUploadDictionaryRequest",
    ),
    "ee_data_complexity_score": ("GetEeDataComplexityScoreComplexityRequest",),
    "ee_data_studio": (
        "PostEeDataStudioTablePublishTablesRequest",
        "PostEeDataStudioTableUnpublishTablesRequest",
    ),
    "ee_database_replication": (
        "PostEeDatabaseReplicationConnectionDatabaseIdRequest",
        "DeleteEeDatabaseReplicationConnectionDatabaseIdRequest",
        "PostEeDatabaseReplicationConnectionDatabaseIdPreviewRequest",
    ),
    "ee_database_routing": (
        "PostEeDatabaseRoutingDestinationDatabaseRequest",
        "PutEeDatabaseRoutingRouterDatabaseIdRequest",
    ),
    "ee_dependencies": (
        "GetEeDependenciesBackfillStatusRequest",
        "CheckEeDependenciesCardRequest",
        "CheckEeDependenciesSnippetRequest",
        "CheckEeDependenciesTransformRequest",
        "GetEeDependenciesGraphRequest",
        "GetEeDependenciesGraphBreakingRequest",
        "GetEeDependenciesGraphBrokenRequest",
        "GetEeDependenciesGraphDependentsRequest",
        "GetEeDependenciesGraphUnreferencedRequest",
    ),
    "ee_email": (
        "PutEeEmailOverrideRequest",
        "DeleteEeEmailOverrideRequest",
    ),
    "ee_embedding_hub": ("GetEeEmbeddingHubChecklistRequest",),
    "ee_gsheets": (
        "CreateEeGsheetsConnectionRequest",
        "GetEeGsheetsConnectionRequest",
        "DeleteEeGsheetsConnectionRequest",
        "SyncEeGsheetsConnectionRequest",
        "GetEeGsheetsServiceAccountRequest",
    ),
    "ee_library": (
        "CreateEeLibraryRequest",
        "GetEeLibraryRequest",
        "GetEeLibraryTreeRequest",
    ),
    "ee_logs": ("GetEeLogsQueryExecutionRequest",),
    "ee_metabot": ("GetEeMetabotUsageRequest",),
    "ee_permission_debug": ("GetEePermissionDebugRequest",),
    "ee_remote_sync": (
        "GetEeRemoteSyncBranchesRequest",
        "PostEeRemoteSyncCreateBranchRequest",
        "GetEeRemoteSyncCurrentTaskRequest",
        "PostEeRemoteSyncCurrentTaskCancelRequest",
        "GetEeRemoteSyncDirtyRequest",
        "PostEeRemoteSyncExportRequest",
        "GetEeRemoteSyncHasRemoteChangesRequest",
        "PostEeRemoteSyncImportRequest",
        "GetEeRemoteSyncIsDirtyRequest",
        "PutEeRemoteSyncSettingsRequest",
        "PostEeRemoteSyncStashRequest",
    ),
    "ee_replacement": (
        "PostEeReplacementCheckReplaceSourceRequest",
        "PostEeReplacementReplaceModelWithTransformRequest",
        "PostEeReplacementReplaceSourceRequest",
        "GetEeReplacementRunsRequest",
        "GetEeReplacementRunsIdRequest",
        "PostEeReplacementRunsIdCancelRequest",
    ),
    "ee_scim": (
        "GetEeScimApiKeyRequest",
        "CreateEeScimApiKeyRequest",
        "ListEeScimV2GroupsRequest",
        "CreateEeScimV2GroupRequest",
        "GetEeScimV2GroupRequest",
        "UpdateEeScimV2GroupRequest",
        "DeleteEeScimV2GroupRequest",
        "ListEeScimV2UsersRequest",
        "CreateEeScimV2UserRequest",
        "GetEeScimV2UserRequest",
        "UpdateEeScimV2UserRequest",
        "PatchEeScimV2UserRequest",
    ),
    "ee_security_center": (
        "GetEeSecurityCenterRequest",
        "AcknowledgeEeSecurityCenterAdvisoriesRequest",
        "SyncEeSecurityCenterRequest",
        "TestEeSecurityCenterNotificationRequest",
        "AcknowledgeEeSecurityCenterAdvisoryRequest",
    ),
    "ee_semantic_search": ("GetEeSemanticSearchStatusRequest",),
    "ee_serialization": (
        "PostEeSerializationExportRequest",
        "PostEeSerializationImportRequest",
    ),
    "ee_stale": ("GetEeStaleIdRequest",),
    "ee_support_access_grant": (
        "PostEeSupportAccessGrantRequest",
        "GetEeSupportAccessGrantRequest",
        "GetEeSupportAccessGrantCurrentRequest",
        "PutEeSupportAccessGrantIdRevokeRequest",
    ),
    "ee_tenant": (
        "PostEeTenantRequest",
        "GetEeTenantRequest",
        "PutEeTenantIdRequest",
        "GetEeTenantIdRequest",
    ),
    "ee_transforms": (
        "GetEeTransformsIdInspectRequest",
        "GetEeTransformsIdInspectLensIdRequest",
        "PostEeTransformsIdInspectLensIdQueryRequest",
    ),
    "ee_transforms_python": (
        "GetEeTransformsPythonLibraryPathRequest",
        "PutEeTransformsPythonLibraryPathRequest",
        "PostEeTransformsPythonTestRunRequest",
    ),
    "ee_upload_management": (
        "GetEeUploadManagementTablesRequest",
        "DeleteEeUploadManagementTablesIdRequest",
    ),
    "eid_translation": ("TranslateEntityIdsRequest",),
    "email": (
        "UpdateEmailSettingsRequest",
        "DeleteEmailSettingsRequest",
        "TestEmailRequest",
    ),
    "embed": (
        "GetEmbedCardRequest",
        "GetEmbedCardParamRemappingRequest",
        "GetEmbedCardParamSearchRequest",
        "GetEmbedCardParamValuesRequest",
        "GetEmbedCardQueryRequest",
        "GetEmbedCardQueryExportRequest",
        "GetEmbedDashboardRequest",
        "GetEmbedDashboardDashcardCardRequest",
        "GetEmbedDashboardDashcardCardExportRequest",
        "GetEmbedDashboardParamRemappingRequest",
        "GetEmbedDashboardParamSearchRequest",
        "GetEmbedDashboardParamValuesRequest",
        "GetEmbedPivotCardQueryRequest",
        "GetEmbedPivotDashboardDashcardCardRequest",
        "GetEmbedTilesCardRequest",
        "GetEmbedTilesDashboardDashcardCardRequest",
    ),
    "embed_theme": (
        "ListEmbedThemesRequest",
        "CreateEmbedThemeRequest",
        "SeedDefaultEmbedThemesRequest",
        "GetEmbedThemeRequest",
        "UpdateEmbedThemeRequest",
        "DeleteEmbedThemeRequest",
        "CopyEmbedThemeRequest",
    ),
    "frontend_errors": ("ReportFrontendErrorRequest",),
    "geojson": (
        "GetGeojsonRequest",
        "GetGeojsonByKeyRequest",
    ),
    "glossary": (
        "GetGlossaryRequest",
        "CreateGlossaryEntryRequest",
        "UpdateGlossaryEntryRequest",
        "DeleteGlossaryEntryRequest",
    ),
    "google": ("UpdateGoogleSettingsRequest",),
    "ldap": ("UpdateLdapSettingsRequest",),
    "llm": (
        "ExtractLlmTablesRequest",
        "ExtractLlmSourcesRequest",
        "GenerateLlmSqlRequest",
        "ListLlmModelsRequest",
    ),
    "logger": (
        "CreateLoggerAdjustmentRequest",
        "DeleteLoggerAdjustmentRequest",
        "GetLoggerLogsRequest",
        "GetLoggerPresetsRequest",
    ),
    "login_history": ("GetCurrentLoginHistoryRequest",),
    "measure": (
        "CreateMeasureRequest",
        "ListMeasuresRequest",
        "GetMeasureRequest",
        "UpdateMeasureRequest",
        "GetMeasureDimensionRemappingRequest",
        "SearchMeasureDimensionValuesRequest",
        "GetMeasureDimensionValuesRequest",
    ),
    "metabot": (
        "MetabotAgentStreamingRequest",
        "MetabotFeedbackRequest",
        "ListMetabotConversationsRequest",
        "GetMetabotConversationRequest",
        "MetabotSourceFeedbackRequest",
        "GetMetabotSettingsRequest",
        "UpdateMetabotSettingsRequest",
        "GenerateMetabotDocumentContentRequest",
        "ListMetabotsRequest",
        "GetMetabotRequest",
        "UpdateMetabotRequest",
        "GetMetabotPromptSuggestionsRequest",
        "DeleteMetabotPromptSuggestionsRequest",
        "RegenerateMetabotPromptSuggestionsRequest",
        "DeleteMetabotPromptSuggestionRequest",
        "GetMetabotUserPermissionsRequest",
        "MetabotSlackEventsRequest",
        "MetabotSlackInteractiveRequest",
        "UpdateMetabotSlackSettingsRequest",
    ),
    "metric": (
        "ListMetricsRequest",
        "MetricBreakoutValuesRequest",
        "MetricDatasetRequest",
        "GetMetricRequest",
        "GetMetricDimensionRemappingRequest",
        "SearchMetricDimensionValuesRequest",
        "GetMetricDimensionValuesRequest",
    ),
    "model_index": (
        "CreateModelIndexRequest",
        "ListModelIndexesRequest",
        "GetModelIndexRequest",
        "DeleteModelIndexRequest",
    ),
    "moderation_review": ("CreateModerationReviewRequest",),
    "mt_gtap": (
        "GetMtGtapRequest",
        "PostMtGtapRequest",
        "PostMtGtapValidateRequest",
        "GetMtGtapIdRequest",
        "PutMtGtapIdRequest",
        "DeleteMtGtapIdRequest",
    ),
    "mt_user": (
        "GetMtUserAttributesRequest",
        "PutMtUserIdAttributesRequest",
    ),
    "native_query_snippet": (
        "ListNativeQuerySnippetsRequest",
        "CreateNativeQuerySnippetRequest",
        "GetNativeQuerySnippetRequest",
        "UpdateNativeQuerySnippetRequest",
    ),
    "notification": (
        "ListNotificationsRequest",
        "CreateNotificationRequest",
        "SendUnsavedNotificationRequest",
        "GetNotificationRequest",
        "UpdateNotificationRequest",
        "SendNotificationRequest",
        "UnsubscribeNotificationRequest",
        "UnsubscribeNotificationByHashRequest",
        "UndoNotificationUnsubscribeRequest",
    ),
    "notify": (
        "NotifyAttachedDatawarehouseRequest",
        "NotifyDatabaseRequest",
        "NotifyDatabaseNewTableRequest",
    ),
    "permissions": (
        "GetPermissionsGraphRequest",
        "PutPermissionsGraphRequest",
        "GetPermissionsGraphDbRequest",
        "GetPermissionsGraphGroupRequest",
        "ListPermissionsGroupsRequest",
        "CreatePermissionsGroupRequest",
        "UpdatePermissionsGroupRequest",
        "DeletePermissionsGroupRequest",
        "GetPermissionsGroupRequest",
        "GetPermissionsMembershipRequest",
        "CreatePermissionsMembershipRequest",
        "ClearPermissionsMembershipRequest",
        "UpdatePermissionsMembershipRequest",
        "DeletePermissionsMembershipRequest",
    ),
    "persist": (
        "ListPersistedInfoRequest",
        "GetPersistedInfoByCardRequest",
        "PersistCardRequest",
        "RefreshPersistedCardRequest",
        "UnpersistCardRequest",
        "EnableDatabasePersistenceRequest",
        "DisableDatabasePersistenceRequest",
        "DisablePersistenceRequest",
        "EnablePersistenceRequest",
        "SetPersistenceRefreshScheduleRequest",
        "GetPersistedInfoRequest",
    ),
    "premium_features": (
        "RefreshPremiumFeaturesTokenRequest",
        "GetPremiumFeaturesTokenStatusRequest",
    ),
    "preview_embed": (
        "GetPreviewEmbedCardRequest",
        "GetPreviewEmbedCardParamRemappingRequest",
        "GetPreviewEmbedCardParamValuesRequest",
        "GetPreviewEmbedCardQueryRequest",
        "GetPreviewEmbedDashboardRequest",
        "GetPreviewEmbedDashboardDashcardCardRequest",
        "GetPreviewEmbedDashboardParamRemappingRequest",
        "GetPreviewEmbedDashboardParamSearchRequest",
        "GetPreviewEmbedDashboardParamValuesRequest",
        "GetPreviewEmbedPivotCardQueryRequest",
        "GetPreviewEmbedPivotDashboardDashcardCardRequest",
        "GetPreviewEmbedTilesCardRequest",
        "GetPreviewEmbedTilesDashboardDashcardCardRequest",
    ),
    "product_feedback": ("CreateProductFeedbackRequest",),
    "data_studio": (
        "DataStudioTableDiscardValuesRequest",
        "DataStudioTableEditRequest",
        "DataStudioTableRescanValuesRequest",
        "DataStudioTableSelectionRequest",
        "DataStudioTableSyncSchemaRequest",
    ),
    "public": (
        "GetPublicActionRequest",
        "ExecutePublicActionRequest",
        "GetPublicCardRequest",
        "GetPublicCardParamRemappingRequest",
        "GetPublicCardParamSearchRequest",
        "GetPublicCardParamValuesRequest",
        "GetPublicCardQueryRequest",
        "GetPublicCardQueryExportRequest",
        "GetPublicDashboardRequest",
        "GetPublicDashboardCardRequest",
        "ExportPublicDashboardCardRequest",
        "GetPublicDashboardDashcardExecuteRequest",
        "ExecutePublicDashboardDashcardRequest",
        "GetPublicDashboardParamRemappingRequest",
        "GetPublicDashboardParamSearchRequest",
        "GetPublicDashboardParamValuesRequest",
        "GetPublicDocumentRequest",
        "GetPublicDocumentCardRequest",
        "ExportPublicDocumentCardRequest",
        "GetPublicOEmbedRequest",
        "GetPublicPivotCardQueryRequest",
        "GetPublicPivotDashboardCardRequest",
        "GetPublicCardTileRequest",
        "GetPublicDashboardCardTileRequest",
    ),
    "pulse": (
        "ListPulsesRequest",
        "CreatePulseRequest",
        "GetPulseFormInputRequest",
        "TestPulseRequest",
        "GetPulseRequest",
        "UpdatePulseRequest",
        "DeletePulseSubscriptionRequest",
        "UnsubscribePulseRequest",
        "UndoPulseUnsubscribeRequest",
    ),
    "revision": (
        "GetRevisionsRequest",
        "RevertRevisionRequest",
        "GetEntityRevisionsRequest",
    ),
    "search": (
        "SearchRequest",
        "ForceSearchReindexRequest",
        "ReInitSearchRequest",
        "GetSearchWeightsRequest",
        "UpdateSearchWeightsRequest",
    ),
    "segment": (
        "CreateSegmentRequest",
        "ListSegmentsRequest",
        "GetSegmentRequest",
        "UpdateSegmentRequest",
        "DeleteSegmentRequest",
        "GetSegmentRelatedRequest",
    ),
    "session": (
        "CreateSessionRequest",
        "DeleteSessionRequest",
        "ForgotPasswordRequest",
        "GoogleAuthRequest",
        "PasswordCheckRequest",
        "PasswordResetTokenValidRequest",
        "GetSessionPropertiesRequest",
        "ResetPasswordRequest",
    ),
    "setting": (
        "ListSettingsRequest",
        "UpdateSettingsRequest",
        "GetSettingRequest",
        "UpdateSettingRequest",
    ),
    "setup": ("SetupRequest",),
    "slack": (
        "GetSlackAppInfoRequest",
        "CreateSlackBugReportRequest",
        "GetSlackManifestRequest",
        "UpdateSlackSettingsRequest",
    ),
    "task": (
        "ListTasksRequest",
        "GetTaskInfoRequest",
        "ListTaskRunsRequest",
        "ListTaskRunEntitiesRequest",
        "GetTaskRunRequest",
        "GetUniqueTasksRequest",
        "GetTaskRequest",
    ),
    "tiles": (
        "GetSavedCardTileRequest",
        "GetDashboardCardTileRequest",
        "GetAdHocQueryTileRequest",
    ),
    "timeline": (
        "CreateTimelineRequest",
        "ListTimelinesRequest",
        "GetTimelineCollectionRootRequest",
        "GetTimelineCollectionRequest",
        "GetTimelineRequest",
        "UpdateTimelineRequest",
        "DeleteTimelineRequest",
    ),
    "timeline_event": (
        "CreateTimelineEventRequest",
        "GetTimelineEventRequest",
        "UpdateTimelineEventRequest",
        "DeleteTimelineEventRequest",
    ),
    "transform": (
        "ListTransformsRequest",
        "CreateTransformRequest",
        "ListTransformRunsRequest",
        "GetTransformRunRequest",
        "GetTransformRequest",
        "UpdateTransformRequest",
        "DeleteTransformRequest",
        "CancelTransformRequest",
        "GetTransformDependenciesRequest",
        "ResetTransformCheckpointRequest",
        "RunTransformRequest",
        "DeleteTransformTableRequest",
    ),
    "transform_job": (
        "CreateTransformJobRequest",
        "ListTransformJobsRequest",
        "UpdateTransformJobRequest",
        "UpdateTransformJobsActiveRequest",
        "DeleteTransformJobRequest",
        "GetTransformJobRequest",
        "RunTransformJobRequest",
        "GetTransformJobTransformsRequest",
    ),
    "transform_tag": (
        "CreateTransformTagRequest",
        "ListTransformTagsRequest",
        "UpdateTransformTagRequest",
        "DeleteTransformTagRequest",
    ),
    "upload": ("UploadCsvRequest",),
    "util": ("GetRandomTokenRequest",),
    "dashboard": (
        "ListDashboardsRequest",
        "PostDashboardRequest",
        "GetDashboardRequest",
        "GetDashboardEmbeddableRequest",
        "GetDashboardPublicRequest",
        "SaveDashboardRequest",
        "SaveDashboardToCollectionRequest",
        "CreateDashboardPublicLinkRequest",
        "DeleteDashboardPublicLinkRequest",
        "CopyDashboardRequest",
        "DeleteDashboardRequest",
        "UpdateDashboardRequest",
        "UpdateDashboardCardsRequest",
        "GetDashboardItemsRequest",
    ),
    "dashboard_query": (
        "DashboardParamsValidFilterFieldsRequest",
        "DashboardCardQueryRequest",
        "DashboardCardQueryExportRequest",
        "PostDashboardPivotQueryRequest",
        "GetDashboardDashcardExecuteRequest",
        "ExecuteDashboardDashcardRequest",
        "DashboardParamRemappingRequest",
        "DashboardParamSearchRequest",
        "DashboardParamValuesRequest",
        "GetDashboardQueryMetadataRequest",
        "GetDashboardRelatedRequest",
    ),
    "field": (
        "GetFieldRequest",
        "GetFieldTableIdsRequest",
        "UpdateFieldRequest",
        "SetFieldDimensionRequest",
        "DeleteFieldDimensionRequest",
        "DiscardFieldValuesRequest",
        "GetFieldRelatedRequest",
        "GetFieldRemappingRequest",
        "RescanFieldValuesRequest",
        "SearchFieldValuesRequest",
        "GetFieldSummaryRequest",
        "GetFieldValuesRequest",
        "UpdateFieldValuesRequest",
    ),
    "table": (
        "ListTablesRequest",
        "UpdateTablesRequest",
        "GetTableRequest",
        "UpdateTableRequest",
        "AppendTableCsvRequest",
        "DiscardTableValuesRequest",
        "UpdateTableFieldsOrderRequest",
        "GetTableForeignKeysRequest",
        "GetCardTableForeignKeysRequest",
        "GetTableQueryMetadataRequest",
        "GetCardTableQueryMetadataRequest",
        "GetTableRelatedRequest",
        "ReplaceTableCsvRequest",
        "RescanTableValuesRequest",
        "SyncTableSchemaRequest",
        "GetTableDataRequest",
    ),
    "user": (
        "CurrentUserRequest",
        "ListUsersRequest",
        "CreateUserRequest",
        "GetUserRecipientsRequest",
        "GetUserRequest",
        "UpdateUserRequest",
        "DeleteUserRequest",
        "UpdateUserModalRequest",
        "UpdateUserPasswordRequest",
        "CreateUserPasswordResetUrlRequest",
        "ReactivateUserRequest",
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
    "ai_entity_analysis": ("AnalyzeChartResponse",),
    "alert": ("AlertSubscriptionDeleteResponse", "ListAlertsResponse"),
    "analytics": ("AnalyticsEventBatchResponse", "AnonymousStatsResponse"),
    "api_key": ("ApiKeyCountResponse", "DeleteApiKeyResponse", "ListApiKeysResponse"),
    "automagic": ("AutomagicDashboardResponse", "AutomagicDatabaseCandidatesResponse"),
    "bookmark": ("BookmarkOrderingUpdateResponse", "DeleteBookmarkResponse", "ListBookmarksResponse"),
    "bug_reporting": ("BugReportingConnectionPoolDetailsResponse", "BugReportingDetailsResponse"),
    "cache": (
        "CacheDeleteResponse",
        "CacheInvalidationResponse",
        "CacheResponse",
        "CacheUpdateResponse",
    ),
    "card": (
        "CardCollectionsResponse",
        "CardDashboardsResponse",
        "CardEmbeddableResponse",
        "CardParameterValuesResponse",
        "CardPublicResponse",
        "CardQueryExportResponse",
        "CardQueryMetadataResponse",
        "CardQueryResponse",
        "CardRemappingResponse",
        "CardSeriesResponse",
        "CardsDashboardsResponse",
        "CreateCardPublicLinkResponse",
        "DeleteCardPublicLinkResponse",
        "DeleteCardResponse",
        "ListCardsResponse",
        "MoveCardsResponse",
    ),
    "channel": (
        "ChannelResponse",
        "CreateChannelResponse",
        "ListChannelsResponse",
        "ChannelTestResponse",
        "UpdateChannelResponse",
    ),
    "cloud_migration": (
        "CancelCloudMigrationResponse",
        "CloudMigrationStatusResponse",
        "CreateCloudMigrationResponse",
    ),
    "collection": (
        "CollectionDashboardQuestionCandidatesResponse",
        "CollectionGraphResponse",
        "CollectionItemsResponse",
        "CollectionMoveDashboardQuestionCandidatesResponse",
        "CollectionTreeResponse",
        "DeleteCollectionResponse",
        "ListCollectionsResponse",
    ),
    "comment": (
        "CommentMentionsResponse",
        "CommentReactionResponse",
        "CreateCommentResponse",
        "DeleteCommentResponse",
        "ListCommentsResponse",
        "UpdateCommentResponse",
    ),
    "dashboard": (
        "CreateDashboardPublicLinkResponse",
        "DashboardEmbeddableResponse",
        "DashboardItemsResponse",
        "DashboardParameterValuesResponse",
        "DashboardPublicResponse",
        "DashboardQueryExportResponse",
        "DashboardQueryMetadataResponse",
        "DashboardQueryResponse",
        "DashboardRelatedResponse",
        "DashboardRemappingResponse",
        "DashboardValidFilterFieldsResponse",
        "DeleteDashboardPublicLinkResponse",
        "DeleteDashboardResponse",
        "ListDashboardsResponse",
        "SaveDashboardResponse",
        "SaveDashboardToCollectionResponse",
        "UpdateDashboardCardsResponse",
    ),
    "data_studio": ("DataStudioTableOperationResponse",),
    "database": (
        "DatabaseAutocompleteSuggestionsResponse",
        "DatabaseCardAutocompleteSuggestionsResponse",
        "DatabaseFieldValuesResponse",
        "DatabaseFieldsResponse",
        "DatabaseHealthcheckResponse",
        "DatabaseMetadataResponse",
        "DatabaseOperationResponse",
        "DatabaseSchemaTablesResponse",
        "DatabaseSchemasResponse",
        "DatabaseSettingsAvailableResponse",
        "DatabaseUsageInfoResponse",
        "DeleteDatabaseResponse",
        "ImportDatabaseMetadataResponse",
        "ListDatabasesResponse",
        "ValidateDatabaseResponse",
    ),
    "dataset": (
        "DatasetExportResponse",
        "DatasetNativeResponse",
        "DatasetParameterRemappingResponse",
        "DatasetParameterSearchResponse",
        "DatasetParameterValuesResponse",
        "DatasetPivotResponse",
        "DatasetQueryMetadataResponse",
        "DatasetQueryResponse",
    ),
    "document": (
        "CreateDocumentPublicLinkResponse",
        "DeleteDocumentPublicLinkResponse",
        "DeleteDocumentResponse",
        "DocumentQueryExportResponse",
        "DocumentResponse",
        "ListDocumentsResponse",
        "ListPublicDocumentsResponse",
    ),
    "ee_action_v2": (
        "EeActionV2ExecuteFormResponse",
        "EeActionV2ExecuteResponse",
    ),
    "ee_advanced_permissions": (
        "DeleteEeImpersonationResponse",
        "EeApplicationPermissionsGraphResponse",
        "EeImpersonationResponse",
    ),
    "ee_ai_controls": (
        "EeAiControlsGroupUsageLimitsResponse",
        "EeAiControlsPermissionsResponse",
        "EeAiControlsTenantUsageLimitsResponse",
        "EeAiControlsUsageLimitResponse",
    ),
    "ee_audit_app": (
        "EeAuditAppExportResponse",
        "EeAuditAppUserAuditInfoResponse",
        "EeAuditAppUserSubscriptionsDeleteResponse",
    ),
    "ee_billing": ("EeBillingResponse",),
    "ee_cloud": (
        "EeCloudAddOnOperationResponse",
        "EeCloudAddOnsResponse",
        "EeCloudPlansResponse",
        "EeCloudProxyResponse",
    ),
    "ee_content_translation": (
        "EeContentTranslationCsvResponse",
        "EeContentTranslationDictionaryResponse",
        "EeContentTranslationUploadResponse",
    ),
    "ee_data_complexity_score": ("EeDataComplexityScoreResponse",),
    "ee_data_studio": ("EeDataStudioTablePublishResponse",),
    "ee_database_replication": ("EeDatabaseReplicationConnectionResponse",),
    "ee_database_routing": ("EeDatabaseRoutingDatabaseResponse",),
    "ee_dependencies": (
        "EeDependencyBackfillStatusResponse",
        "EeDependencyCheckResponse",
        "EeDependencyEntitiesResponse",
        "EeDependencyGraphResponse",
    ),
    "ee_email": (
        "DeleteEeEmailOverrideResponse",
        "EeEmailOverrideResponse",
    ),
    "ee_embedding_hub": ("EeEmbeddingHubChecklistResponse",),
    "ee_gsheets": (
        "EeGsheetsConnectionResponse",
        "EeGsheetsDeleteConnectionResponse",
        "EeGsheetsServiceAccountResponse",
    ),
    "ee_library": (
        "EeLibraryResponse",
        "EeLibraryTreeResponse",
    ),
    "ee_logs": ("EeQueryExecutionLogsResponse",),
    "ee_metabot": ("EeMetabotUsageResponse",),
    "ee_permission_debug": ("EePermissionDebugResponse",),
    "ee_remote_sync": (
        "EeRemoteSyncBranchesResponse",
        "EeRemoteSyncDirtyResponse",
        "EeRemoteSyncHasRemoteChangesResponse",
        "EeRemoteSyncIsDirtyResponse",
        "EeRemoteSyncOperationResponse",
        "EeRemoteSyncSettingsResponse",
        "EeRemoteSyncTaskResponse",
    ),
    "ee_replacement": (
        "EeReplacementCheckReplaceSourceResponse",
        "EeReplacementOperationResponse",
        "EeReplacementRunResponse",
        "EeReplacementRunsResponse",
    ),
    "ee_scim": (
        "EeScimApiKeyResponse",
        "EeScimDeleteResponse",
        "EeScimGroupsResponse",
        "EeScimUsersResponse",
    ),
    "ee_security_center": (
        "EeSecurityCenterAdvisoriesResponse",
        "EeSecurityCenterOperationResponse",
    ),
    "ee_semantic_search": ("EeSemanticSearchStatusResponse",),
    "ee_serialization": (
        "EeSerializationExportResponse",
        "EeSerializationImportResponse",
    ),
    "ee_stale": ("EeStaleResponse",),
    "ee_support_access_grant": (
        "EeSupportAccessGrantResponse",
        "EeSupportAccessGrantsResponse",
    ),
    "ee_tenant": (
        "EeTenantResponse",
        "EeTenantsResponse",
    ),
    "ee_transforms": (
        "EeTransformInspectQueryResponse",
        "EeTransformInspectResponse",
    ),
    "ee_transforms_python": (
        "EeTransformsPythonLibraryResponse",
        "EeTransformsPythonTestRunResponse",
    ),
    "ee_upload_management": (
        "EeUploadManagementDeleteTableResponse",
        "EeUploadManagementTablesResponse",
    ),
    "eid_translation": ("EidTranslationResponse",),
    "email": (
        "DeleteEmailSettingsResponse",
        "EmailSettingsResponse",
        "TestEmailResponse",
    ),
    "embed": (
        "GetEmbedCardParamRemappingResponse",
        "GetEmbedCardParamSearchResponse",
        "GetEmbedCardParamValuesResponse",
        "GetEmbedCardQueryExportResponse",
        "GetEmbedCardQueryResponse",
        "GetEmbedCardResponse",
        "GetEmbedDashboardDashcardCardExportResponse",
        "GetEmbedDashboardDashcardCardResponse",
        "GetEmbedDashboardParamRemappingResponse",
        "GetEmbedDashboardParamSearchResponse",
        "GetEmbedDashboardParamValuesResponse",
        "GetEmbedDashboardResponse",
        "GetEmbedPivotCardQueryResponse",
        "GetEmbedPivotDashboardDashcardCardResponse",
        "GetEmbedTilesCardResponse",
        "GetEmbedTilesDashboardDashcardCardResponse",
    ),
    "embed_theme": (
        "DeleteEmbedThemeResponse",
        "ListEmbedThemesResponse",
        "SeedDefaultEmbedThemesResponse",
    ),
    "frontend_errors": ("FrontendErrorReportResponse",),
    "geojson": (
        "GeojsonByKeyResponse",
        "GeojsonResponse",
    ),
    "glossary": (
        "CreateGlossaryEntryResponse",
        "DeleteGlossaryEntryResponse",
        "GlossaryEntriesResponse",
        "UpdateGlossaryEntryResponse",
    ),
    "google": ("GoogleSettingsResponse",),
    "ldap": ("LdapSettingsResponse",),
    "llm": (
        "ExtractLlmTablesResponse",
        "ExtractLlmSourcesResponse",
        "GenerateLlmSqlResponse",
        "ListLlmModelsResponse",
    ),
    "logger": (
        "LoggerAdjustmentDeleteResponse",
        "LoggerAdjustmentResponse",
        "LoggerLogsResponse",
        "LoggerPresetsResponse",
    ),
    "login_history": ("CurrentLoginHistoryResponse",),
    "measure": (
        "ListMeasuresResponse",
        "MeasureDimensionRemappingResponse",
        "MeasureDimensionSearchResponse",
        "MeasureDimensionValuesResponse",
    ),
    "metabot": (
        "DeleteMetabotPromptSuggestionResponse",
        "DeleteMetabotPromptSuggestionsResponse",
        "ListMetabotConversationsResponse",
        "ListMetabotsResponse",
        "MetabotAgentStreamingResponse",
        "MetabotConversationResponse",
        "MetabotFeedbackResponse",
        "MetabotGenerateContentResponse",
        "MetabotGenericResponse",
        "MetabotPermissionsResponse",
        "MetabotPromptSuggestionsResponse",
        "MetabotResponse",
        "MetabotSettingsResponse",
        "MetabotSlackEventsResponse",
        "MetabotSlackInteractiveResponse",
        "MetabotSlackSettingsResponse",
        "MetabotSourceFeedbackResponse",
        "RegenerateMetabotPromptSuggestionsResponse",
    ),
    "metric": (
        "ListMetricsResponse",
        "MetricBreakoutValuesResponse",
        "MetricDatasetResponse",
        "MetricDimensionRemappingResponse",
        "MetricDimensionSearchResponse",
        "MetricDimensionValuesResponse",
    ),
    "model_index": (
        "DeleteModelIndexResponse",
        "ListModelIndexesResponse",
    ),
    "moderation_review": ("ModerationReviewResponse",),
    "mt_gtap": (
        "MtGtapDeleteResponse",
        "MtGtapResponse",
        "MtGtapsResponse",
        "MtGtapValidationResponse",
    ),
    "mt_user": (
        "MtUserAttributesResponse",
        "MtUserUpdateAttributesResponse",
    ),
    "native_query_snippet": ("ListNativeQuerySnippetsResponse",),
    "notification": (
        "ListNotificationsResponse",
        "NotificationResponse",
        "NotificationSendResponse",
        "NotificationUnsubscribeResponse",
        "NotificationUnsubscribeUndoResponse",
    ),
    "notify": (
        "NotifyAttachedDatawarehouseResponse",
        "NotifyDatabaseNewTableResponse",
        "NotifyDatabaseResponse",
    ),
    "permissions": (
        "DeletePermissionsGroupResponse",
        "DeletePermissionsMembershipResponse",
        "PermissionsGraphResponse",
        "PermissionsGroupResponse",
        "PermissionsGroupsResponse",
        "PermissionsMembershipListResponse",
        "PermissionsMembershipResponse",
        "PermissionsMembershipsResponse",
    ),
    "persist": (
        "ListPersistedInfoResponse",
        "PersistOperationResponse",
        "PersistRefreshScheduleResponse",
    ),
    "premium_features": (
        "PremiumFeaturesTokenResponse",
        "PremiumFeaturesTokenStatusResponse",
        "RefreshPremiumFeaturesTokenResponse",
    ),
    "preview_embed": (
        "GetPreviewEmbedCardParamRemappingResponse",
        "GetPreviewEmbedCardParamValuesResponse",
        "GetPreviewEmbedCardQueryResponse",
        "GetPreviewEmbedCardResponse",
        "GetPreviewEmbedDashboardDashcardCardResponse",
        "GetPreviewEmbedDashboardParamRemappingResponse",
        "GetPreviewEmbedDashboardParamSearchResponse",
        "GetPreviewEmbedDashboardParamValuesResponse",
        "GetPreviewEmbedDashboardResponse",
        "GetPreviewEmbedPivotCardQueryResponse",
        "GetPreviewEmbedPivotDashboardDashcardCardResponse",
        "GetPreviewEmbedTilesCardResponse",
        "GetPreviewEmbedTilesDashboardDashcardCardResponse",
    ),
    "product_feedback": ("ProductFeedbackResponse",),
    "field": (
        "DeleteFieldDimensionResponse",
        "FieldDimensionResponse",
        "FieldOperationResponse",
        "FieldRelatedResponse",
        "FieldRemappingResponse",
        "FieldSearchResponse",
        "FieldSummaryResponse",
        "FieldTableIdsResponse",
        "FieldValuesResponse",
        "UpdateFieldValuesResponse",
    ),
    "public": (
        "PublicActionExecutionResponse",
        "PublicActionResponse",
        "PublicCardQueryResponse",
        "PublicCardResponse",
        "PublicDashboardCardResponse",
        "PublicDashboardExecuteResponse",
        "PublicDashboardResponse",
        "PublicDocumentCardResponse",
        "PublicDocumentResponse",
        "PublicExportResponse",
        "PublicOEmbedResponse",
        "PublicParameterValuesResponse",
        "PublicRemappingResponse",
        "PublicTileResponse",
    ),
    "pulse": (
        "ListPulsesResponse",
        "PulseFormInputResponse",
        "PulseResponse",
        "PulseSubscriptionDeleteResponse",
        "PulseTestResponse",
        "PulseUnsubscribeResponse",
        "PulseUnsubscribeUndoResponse",
    ),
    "revision": (
        "RevertRevisionResponse",
        "RevisionsResponse",
    ),
    "search": (
        "SearchReindexResponse",
        "SearchResponse",
        "SearchWeightsResponse",
        "UpdateSearchWeightsResponse",
    ),
    "segment": (
        "DeleteSegmentResponse",
        "ListSegmentsResponse",
        "SegmentRelatedResponse",
    ),
    "session": (
        "DeleteSessionResponse",
        "ForgotPasswordResponse",
        "GoogleAuthResponse",
        "PasswordCheckResponse",
        "PasswordResetTokenValidResponse",
        "ResetPasswordResponse",
        "SessionPropertiesResponse",
        "SessionResponse",
    ),
    "setting": (
        "SettingResponse",
        "SettingsResponse",
        "UpdateSettingResponse",
        "UpdateSettingsResponse",
    ),
    "setup": ("SetupResponse",),
    "slack": (
        "SlackAppInfoResponse",
        "SlackBugReportResponse",
        "SlackManifestResponse",
        "SlackSettingsResponse",
    ),
    "task": (
        "GetTaskResponse",
        "ListTaskRunsResponse",
        "ListTasksResponse",
        "TaskInfoResponse",
        "TaskRunEntitiesResponse",
        "TaskRunEntityResponse",
        "TaskRunResponse",
        "TaskRunWithTasksResponse",
        "TaskResponse",
        "UniqueTasksResponse",
    ),
    "tiles": (
        "AdHocQueryTileResponse",
        "DashboardCardTileResponse",
        "SavedCardTileResponse",
        "TileResponse",
    ),
    "timeline": (
        "DeleteTimelineResponse",
        "ListTimelinesResponse",
        "TimelineResponse",
    ),
    "timeline_event": (
        "DeleteTimelineEventResponse",
        "TimelineEventResponse",
    ),
    "transform": (
        "DeleteTransformResponse",
        "ListTransformRunsResponse",
        "ListTransformsResponse",
        "TransformDependenciesResponse",
        "TransformOperationResponse",
        "TransformResponse",
        "TransformRunResponse",
    ),
    "transform_job": (
        "DeleteTransformJobResponse",
        "ListTransformJobsResponse",
        "TransformJobOperationResponse",
        "TransformJobResponse",
        "TransformJobsActiveResponse",
        "TransformJobTransformsResponse",
    ),
    "transform_tag": (
        "DeleteTransformTagResponse",
        "ListTransformTagsResponse",
        "TransformTagResponse",
    ),
    "upload": ("UploadCsvResponse",),
    "util": ("RandomTokenResponse",),
    "table": (
        "ListTablesResponse",
        "TableDataResponse",
        "TableForeignKeysResponse",
        "TableOperationResponse",
        "TableQueryMetadataResponse",
        "TableRelatedResponse",
    ),
    "user": (
        "DeleteUserResponse",
        "ListUsersResponse",
        "UserModalResponse",
        "UserPasswordResetUrlResponse",
        "UserPasswordUpdateResponse",
        "UserRecipientsResponse",
    ),
    "user_key_value": (
        "DeleteUserKeyValueResponse",
        "UserKeyValueNamespaceResponse",
        "UserKeyValueResponse",
        "UserKeyValueStoreResponse",
    ),
}


def test_cli_command_package_exposes_no_registry_api() -> None:
    assert metabaseapi.cli.commands.__all__ == []
    assert not hasattr(metabaseapi.cli.commands, "command_module_names")
    assert not hasattr(metabaseapi.cli.commands, "command_module_paths")
    assert not hasattr(metabaseapi.cli.commands, "command_module_objects")
    assert not hasattr(metabaseapi.cli.commands, "register_commands")


def test_cli_command_inventory_matches_package_files() -> None:
    module_names = tuple(module.__name__.rsplit(".", maxsplit=1)[-1] for module in _command_modules())
    assert module_names == _command_module_names()


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
    assert metabaseapi.wire.__all__ == [
        "APIRequestModel",
        "APIResponseModel",
        "JSONValue",
        "QueryParamPrimitive",
        "QueryParamValue",
    ]
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.models")


def test_client_public_exports_use_http_implementation() -> None:
    assert metabaseapi.client.__all__ == ["MetabaseClient"]
    assert metabaseapi.client.http.__all__ == ["MetabaseClient"]
    assert metabaseapi.client.MetabaseClient is metabaseapi.client.http.MetabaseClient
    assert _client_module_stems(metabaseapi.client) == ("http",)
    assert not hasattr(metabaseapi.client, "_MetabaseClientRawMixin")
    assert not hasattr(metabaseapi.client, "_MetabaseClientTypedMixin")
    assert not hasattr(metabaseapi.client.MetabaseClient, "get")
    assert not hasattr(metabaseapi.client.MetabaseClient, "post")
    assert not hasattr(metabaseapi.client.MetabaseClient, "put")
    assert not hasattr(metabaseapi.client.MetabaseClient, "patch")
    assert not hasattr(metabaseapi.client.MetabaseClient, "delete")
    assert not hasattr(metabaseapi.client.MetabaseClient, "request")
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.mixins")


def test_client_typed_package_is_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.typed")


def test_client_raw_package_is_not_importable() -> None:
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("metabaseapi.client.raw")


def _client_module_stems(package: object) -> tuple[str, ...]:
    package_path = _package_path(package)
    return tuple(sorted(path.stem for path in package_path.glob("*.py") if path.stem != "__init__"))


def _package_path(package: object) -> Path:
    package_file = getattr(package, "__file__", None)
    assert package_file is not None
    return Path(package_file).parent


def test_cli_command_modules_depend_on_runtime_not_cli_facade() -> None:
    command_package_path = _package_path(metabaseapi.cli.commands)
    for source_path in command_package_path.glob("*.py"):
        if source_path.stem == "__init__":
            continue
        source = source_path.read_text(encoding="utf-8")
        assert "from metabaseapi.cli import " not in source


def test_cli_entrypoint_importable() -> None:
    assert hasattr(metabaseapi.cli, "app")
    assert metabaseapi.cli.__all__ == ["app"]
    assert not hasattr(metabaseapi.cli, "configure")
    assert not hasattr(metabaseapi.cli, "create_client")


def test_client_public_module_exports_concrete_http_implementation() -> None:
    assert metabaseapi.client.MetabaseClient.__module__ == "metabaseapi.client.http"
    assert metabaseapi.client.__all__ == ["MetabaseClient"]
    assert not hasattr(metabaseapi.client, "_MetabaseClientRawMixin")
    assert not hasattr(metabaseapi.client, "_MetabaseClientTypedMixin")


def test_endpoints_execution_owns_request_interface() -> None:
    assert metabaseapi.endpoints.execution.__all__ == ["EndpointRequest"]
    assert not hasattr(metabaseapi.endpoints.execution, "_BaseMetabaseRequest")
    assert not hasattr(metabaseapi.endpoints.execution.EndpointRequest, "do_sync")
    assert metabaseapi.endpoints.requests.card.ListCardsRequest.__mro__[1].__module__ == (
        "metabaseapi.endpoints.execution"
    )
    assert (
        metabaseapi.endpoints.requests.card.ListCardsRequest.__mro__[1].__name__ == "EndpointRequest[ListCardsResponse]"
    )


def test_endpoints_public_exports_are_submodules_only() -> None:
    assert metabaseapi.endpoints.__all__ == ["entities", "execution", "requests", "responses"]
    assert metabaseapi.endpoints.entities is metabaseapi.endpoints.entities
    assert metabaseapi.endpoints.execution is metabaseapi.endpoints.execution
    assert metabaseapi.endpoints.requests is metabaseapi.endpoints.requests
    assert metabaseapi.endpoints.responses is metabaseapi.endpoints.responses
    assert not hasattr(metabaseapi.endpoints, "ListCardsRequest")
    public_names = {name for name in vars(metabaseapi.endpoints) if not name.startswith("_") and name != "annotations"}
    assert public_names == {"entities", "execution", "requests", "responses"}


def test_endpoints_entities_public_exports_match_entity_models() -> None:
    assert metabaseapi.endpoints.entities.__all__ == [
        "Action",
        "ActivityItem",
        "AgentResource",
        "Alert",
        "ApiKey",
        "Bookmark",
        "Card",
        "Collection",
        "CurrentUserResponse",
        "Dashboard",
        "Database",
        "MetabaseField",
        "Table",
        "User",
    ]
    assert "_MetabaseEntity" not in metabaseapi.endpoints.entities.__all__
    assert "_MetabaseResponseBase" not in metabaseapi.endpoints.entities.__all__


def test_endpoints_response_package_does_not_reexport_response_classes() -> None:
    assert metabaseapi.endpoints.responses.__all__ == []
    assert not hasattr(metabaseapi.endpoints.responses, "ListCardsResponse")


def test_endpoints_response_inventory_matches_package_files() -> None:
    response_package_path = _package_path(metabaseapi.endpoints.responses)
    response_module_files = tuple(
        sorted(path.stem for path in response_package_path.glob("*.py") if path.stem != "__init__")
    )
    assert response_module_files == tuple(sorted(RESPONSE_MODULE_CONTRACTS))


def test_endpoints_response_modules_own_response_classes() -> None:
    for module_name, response_names in RESPONSE_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.responses.{module_name}")
        for response_name in response_names:
            assert getattr(domain_module, response_name).__module__ == domain_module.__name__


def test_endpoints_response_contracts_cover_module_response_classes() -> None:
    for module_name, response_names in RESPONSE_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.responses.{module_name}")
        module_response_names = tuple(
            sorted(
                name
                for name, value in inspect.getmembers(domain_module, inspect.isclass)
                if name.endswith("Response") and not name.startswith("_") and value.__module__ == domain_module.__name__
            )
        )

        assert module_response_names == tuple(sorted(response_names))


def test_endpoints_request_package_does_not_reexport_request_classes() -> None:
    assert metabaseapi.endpoints.requests.__all__ == []
    assert not hasattr(metabaseapi.endpoints.requests, "ListCardsRequest")


def test_endpoints_request_modules_own_request_classes() -> None:
    for module_name, request_names in REQUEST_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.requests.{module_name}")
        for request_name in request_names:
            assert getattr(domain_module, request_name).__module__ == domain_module.__name__


def test_endpoints_request_contracts_cover_module_request_classes() -> None:
    for module_name, request_names in REQUEST_MODULE_CONTRACTS.items():
        domain_module = importlib.import_module(f"metabaseapi.endpoints.requests.{module_name}")
        module_request_names = tuple(
            sorted(
                name
                for name, value in inspect.getmembers(domain_module, inspect.isclass)
                if name.endswith("Request") and value.__module__ == domain_module.__name__
            )
        )

        assert module_request_names == tuple(sorted(request_names))


def test_endpoints_request_inventory_matches_package_files() -> None:
    endpoint_package_path = _package_path(metabaseapi.endpoints.requests)
    endpoint_module_files = tuple(
        sorted(path.stem for path in endpoint_package_path.glob("*.py") if path.stem != "__init__")
    )
    assert endpoint_module_files == tuple(sorted(REQUEST_MODULE_CONTRACTS))


def test_endpoint_requests_use_base_execution_methods() -> None:
    for module_name, request_names in REQUEST_MODULE_CONTRACTS.items():
        module = importlib.import_module(f"metabaseapi.endpoints.requests.{module_name}")
        for request_name in request_names:
            request_class = getattr(module, request_name)
            assert "response_model" in request_class.__dict__
            assert "execute" not in request_class.__dict__
            assert "do" not in request_class.__dict__
            assert "do_sync" not in request_class.__dict__


def test_endpoint_request_paths_use_python_field_placeholders() -> None:
    for module_name, request_names in REQUEST_MODULE_CONTRACTS.items():
        module = importlib.import_module(f"metabaseapi.endpoints.requests.{module_name}")
        for request_name in request_names:
            request_class = getattr(module, request_name)
            assert not re.search(r"\{[^}]*-[^}]*\}", request_class.endpoint_path)


def _command_module_names() -> tuple[str, ...]:
    command_package_path = _package_path(metabaseapi.cli.commands)
    return tuple(sorted(path.stem for path in command_package_path.glob("*.py") if path.stem != "__init__"))


def _command_modules() -> tuple[ModuleType, ...]:
    return tuple(importlib.import_module(f"metabaseapi.cli.commands.{module}") for module in _command_module_names())


def _command_names_from_sources() -> list[str]:
    command_names: list[str] = []
    for module in _command_modules():
        source_path = Path(module.__file__) if module.__file__ else None
        if source_path is None:
            continue
        source = source_path.read_text(encoding="utf-8")
        command_names.extend(re.findall(r'@app\.command\("([^"]+)"\)', source))
    return command_names


def _command_names_by_module() -> dict[str, tuple[str, ...]]:
    command_names: dict[str, tuple[str, ...]] = {}
    for module in _command_modules():
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
    assert "create-database" in command_names["database"]
    assert "create-sample-database" in command_names["database"]
    assert "delete-database" in command_names["database"]
    assert "get-database" in command_names["database"]
    assert "list-databases" in command_names["database"]
    assert "update-database" in command_names["database"]
    assert "validate-database" in command_names["database"]
    assert "create-database" not in command_names["table"]


def test_resource_list_commands_live_with_resource_modules() -> None:
    command_names = _command_names_by_module()
    assert "list-cards" in command_names["card"]
    assert "list-collections" in command_names["collection"]
    assert "list-dashboards" in command_names["dashboard"]
    assert "list-users" in command_names["user"]
    assert "list-tables" in command_names["table"]


def test_dashboard_resource_commands_live_with_dashboard_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "get-dashboard",
        "get-dashboard-embeddable",
        "get-dashboard-public",
    ):
        assert command_name in command_names["dashboard"]
        assert command_name not in command_names["dashboard_query"]


def test_collection_graph_commands_live_with_collection_graph_module() -> None:
    command_names = _command_names_by_module()
    assert "get-collection-graph" in command_names["collection_graph"]
    assert "put-collection-graph" in command_names["collection_graph"]
    assert "get-collection-graph" not in command_names["collection"]
    assert "put-collection-graph" not in command_names["collection"]


def test_collection_root_commands_live_with_collection_root_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "get-collection-root",
        "get-collection-root-dashboard-question-candidates",
        "get-collection-root-items",
        "post-collection-root-move-dashboard-question-candidates",
    ):
        assert command_name in command_names["collection_root"]
        assert command_name not in command_names["collection"]


def test_field_commands_live_with_field_module() -> None:
    command_names = _command_names_by_module()
    assert "get-field" in command_names["field"]
    assert "get-field" not in command_names["table"]


def test_current_user_command_lives_with_user_commands() -> None:
    command_names = _command_names_by_module()
    assert "current-user" in command_names["user"]
    assert "get-user-key-value-namespace" not in command_names["user"]
    assert "current-user" not in command_names["analytics"]


def test_user_key_value_commands_live_with_user_key_value_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "get-user-key-value-namespace",
        "put-user-key-value-namespace-key",
        "get-user-key-value-namespace-key",
        "delete-user-key-value-namespace-key",
    ):
        assert command_name in command_names["user_key_value"]
        assert command_name not in command_names["user"]


def test_activity_commands_live_with_activity_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "most-recently-viewed-dashboard",
        "list-popular-items",
        "list-recent-views",
        "list-recents",
        "create-recent",
    ):
        assert command_name in command_names["activity"]
        assert command_name not in command_names["analytics"]


def test_ai_entity_analysis_commands_live_with_ai_entity_analysis_module() -> None:
    command_names = _command_names_by_module()
    assert "analyze-chart" in command_names["ai_entity_analysis"]
    assert "analyze-chart" not in command_names["analytics"]


def test_bookmark_commands_live_with_bookmark_module() -> None:
    command_names = _command_names_by_module()
    for command_name in (
        "list-bookmarks",
        "update-bookmark-ordering",
        "create-bookmark",
        "delete-bookmark",
    ):
        assert command_name in command_names["bookmark"]
        assert command_name not in command_names["action"]


def test_cli_app_registers_all_declared_commands() -> None:
    source_command_names = sorted(_command_names_from_sources())
    app_command_names = sorted(
        [command.name for command in metabaseapi.cli.app.registered_commands if command.name is not None]
    )

    assert len(app_command_names) == len(source_command_names)
    assert app_command_names == source_command_names


def test_cli_command_modules_are_compact() -> None:
    for module in _command_modules():
        source_path = Path(module.__file__) if module.__file__ else None
        assert source_path is not None
        line_count = len(source_path.read_text(encoding="utf-8").splitlines())
        assert line_count < 1000, f"{module.__name__} has {line_count} lines"


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
            print(len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            import metabaseapi.cli
            import metabaseapi.cli.commands
            print(len(metabaseapi.cli.app.registered_commands))
            """
        ).strip(),
        dedent(
            """
            from metabaseapi.cli.commands import *  # noqa: F401
            import metabaseapi.cli
            print(
                len(metabaseapi.cli.app.registered_commands),
                "command_module_names" in globals(),
                "command_module_objects" in globals(),
            )
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
        values = lines[0].split()
        assert int(values[0]) > 0
        if len(values) == 3:
            assert values[1:] == ["False", "False"]
