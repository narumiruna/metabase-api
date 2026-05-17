# OpenAPI Coverage Snapshot

- total endpoints: 600
- convenience coverage: 462/600

## Method Counts

| method | count |
|---|---:|
| DELETE | 45 |
| GET | 300 |
| PATCH | 1 |
| POST | 189 |
| PUT | 65 |

## Missing Convenience Candidates

| method | path | operationId | hasBody | hasParams | expectedConvenience |
|---|---|---|---:|---:|---|
| GET | `/api/action` | get-api-action | N | Y | `list_action` |
| POST | `/api/action` | post-api-action | Y | Y | `create_action` |
| GET | `/api/action/{action-id}` | get-api-action-action-id | N | Y | `get_action` |
| DELETE | `/api/action/{action-id}` | delete-api-action-action-id | N | Y | `delete_action` |
| PUT | `/api/action/{id}` | put-api-action-id | Y | Y | `update_action` |
| GET | `/api/alert` | get-api-alert | N | Y | `list_alert` |
| GET | `/api/alert/{id}` | get-api-alert-id | N | Y | `get_alert` |
| POST | `/api/api-key` | post-api-api-key | Y | Y | `create_api-key` |
| GET | `/api/api-key` | get-api-api-key | N | Y | `list_api-key` |
| PUT | `/api/api-key/{id}` | put-api-api-key-id | Y | Y | `update_api-key` |
| DELETE | `/api/api-key/{id}` | delete-api-api-key-id | N | Y | `delete_api-key` |
| GET | `/api/bookmark` | get-api-bookmark | N | Y | `list_bookmark` |
| GET | `/api/cache` | get-api-cache | N | Y | `list_cache` |
| PUT | `/api/cache` | put-api-cache | Y | Y | `create_cache` |
| GET | `/api/card` | get-api-card | N | Y | `list_card` |
| POST | `/api/card` | post-api-card | Y | Y | `create_card` |
| GET | `/api/card/{id}` | get-api-card-id | N | Y | `get_card` |
| PUT | `/api/card/{id}` | put-api-card-id | Y | Y | `update_card` |
| DELETE | `/api/card/{id}` | delete-api-card-id | N | Y | `delete_card` |
| GET | `/api/channel` | get-api-channel | Y | Y | `list_channel` |
| POST | `/api/channel` | post-api-channel | Y | Y | `create_channel` |
| GET | `/api/channel/{id}` | get-api-channel-id | N | Y | `get_channel` |
| PUT | `/api/channel/{id}` | put-api-channel-id | Y | Y | `update_channel` |
| POST | `/api/cloud-migration` | post-api-cloud-migration | N | Y | `create_cloud-migration` |
| GET | `/api/cloud-migration` | get-api-cloud-migration | N | Y | `list_cloud-migration` |
| GET | `/api/collection` | get-api-collection | N | Y | `list_collection` |
| POST | `/api/collection` | post-api-collection | Y | Y | `create_collection` |
| GET | `/api/collection/{id}` | get-api-collection-id | N | Y | `get_collection` |
| PUT | `/api/collection/{id}` | put-api-collection-id | Y | Y | `update_collection` |
| DELETE | `/api/collection/{id}` | delete-api-collection-id | N | Y | `delete_collection` |
| GET | `/api/comment` | get-api-comment | N | Y | `list_comment` |
| POST | `/api/comment` | post-api-comment | Y | Y | `create_comment` |
| PUT | `/api/comment/{comment-id}` | put-api-comment-comment-id | Y | Y | `update_comment` |
| DELETE | `/api/comment/{comment-id}` | delete-api-comment-comment-id | N | Y | `delete_comment` |
| GET | `/api/dashboard` | get-api-dashboard | N | Y | `list_dashboard` |
| POST | `/api/dashboard` | post-api-dashboard | Y | Y | `create_dashboard` |
| GET | `/api/dashboard/{id}` | get-api-dashboard-id | N | Y | `get_dashboard` |
| DELETE | `/api/dashboard/{id}` | delete-api-dashboard-id | N | Y | `delete_dashboard` |
| PUT | `/api/dashboard/{id}` | put-api-dashboard-id | Y | Y | `update_dashboard` |
| GET | `/api/database` | get-api-database | N | Y | `list_database` |
| POST | `/api/database` | post-api-database | Y | Y | `create_database` |
| GET | `/api/database/{id}` | get-api-database-id | N | Y | `get_database` |
| PUT | `/api/database/{id}` | put-api-database-id | Y | Y | `update_database` |
| DELETE | `/api/database/{id}` | delete-api-database-id | N | Y | `delete_database` |
| POST | `/api/dataset` | post-api-dataset | Y | Y | `create_dataset` |
| GET | `/api/document` | get-api-document | N | Y | `list_document` |
| POST | `/api/document` | post-api-document | Y | Y | `create_document` |
| GET | `/api/document/{document-id}` | get-api-document-document-id | N | Y | `get_document` |
| PUT | `/api/document/{document-id}` | put-api-document-document-id | Y | Y | `update_document` |
| DELETE | `/api/document/{document-id}` | delete-api-document-document-id | N | Y | `delete_document` |
| PUT | `/api/email` | put-api-email | Y | Y | `create_email` |
| GET | `/api/embed-theme` | get-api-embed-theme | N | Y | `list_embed-theme` |
| POST | `/api/embed-theme` | post-api-embed-theme | Y | Y | `create_embed-theme` |
| GET | `/api/embed-theme/{id}` | get-api-embed-theme-id | N | Y | `get_embed-theme` |
| PUT | `/api/embed-theme/{id}` | put-api-embed-theme-id | Y | Y | `update_embed-theme` |
| DELETE | `/api/embed-theme/{id}` | delete-api-embed-theme-id | N | Y | `delete_embed-theme` |
| GET | `/api/field/{id}` | get-api-field-id | N | Y | `get_field` |
| PUT | `/api/field/{id}` | put-api-field-id | Y | Y | `update_field` |
| POST | `/api/frontend-errors` | post-api-frontend-errors | Y | Y | `create_frontend-error` |
| GET | `/api/geojson` | get-api-geojson | N | Y | `list_geojson` |
| GET | `/api/geojson/{key}` | get-api-geojson-key | N | Y | `get_geojson` |
| GET | `/api/glossary` | get-api-glossary | N | Y | `list_glossary` |
| POST | `/api/glossary` | post-api-glossary | Y | Y | `create_glossary` |
| PUT | `/api/glossary/{id}` | put-api-glossary-id | Y | Y | `update_glossary` |
| DELETE | `/api/glossary/{id}` | delete-api-glossary-id | N | Y | `delete_glossary` |
| POST | `/api/measure` | post-api-measure | Y | Y | `create_measure` |
| GET | `/api/measure` | get-api-measure | N | Y | `list_measure` |
| GET | `/api/measure/{id}` | get-api-measure-id | N | Y | `get_measure` |
| PUT | `/api/measure/{id}` | put-api-measure-id | Y | Y | `update_measure` |
| GET | `/api/metric` | get-api-metric | N | Y | `list_metric` |
| GET | `/api/metric/{id}` | get-api-metric-id | N | Y | `get_metric` |
| POST | `/api/model-index` | post-api-model-index | Y | Y | `create_model-index` |
| GET | `/api/model-index` | get-api-model-index | N | Y | `list_model-index` |
| GET | `/api/model-index/{id}` | get-api-model-index-id | N | Y | `get_model-index` |
| DELETE | `/api/model-index/{id}` | delete-api-model-index-id | N | Y | `delete_model-index` |
| POST | `/api/moderation-review` | post-api-moderation-review | Y | Y | `create_moderation-review` |
| GET | `/api/native-query-snippet` | get-api-native-query-snippet | N | Y | `list_native-query-snippet` |
| POST | `/api/native-query-snippet` | post-api-native-query-snippet | Y | Y | `create_native-query-snippet` |
| GET | `/api/native-query-snippet/{id}` | get-api-native-query-snippet-id | N | Y | `get_native-query-snippet` |
| PUT | `/api/native-query-snippet/{id}` | put-api-native-query-snippet-id | Y | Y | `update_native-query-snippet` |
| GET | `/api/notification` | get-api-notification | N | Y | `list_notification` |
| POST | `/api/notification` | post-api-notification | Y | Y | `create_notification` |
| GET | `/api/notification/{id}` | get-api-notification-id | N | Y | `get_notification` |
| PUT | `/api/notification/{id}` | put-api-notification-id | Y | Y | `update_notification` |
| GET | `/api/persist` | get-api-persist | N | Y | `list_persist` |
| GET | `/api/persist/{persisted-info-id}` | get-api-persist-persisted-info-id | N | Y | `get_persist` |
| POST | `/api/product-feedback` | post-api-product-feedback | Y | Y | `create_product-feedback` |
| GET | `/api/pulse` | get-api-pulse | N | Y | `list_pulse` |
| POST | `/api/pulse` | post-api-pulse | Y | Y | `create_pulse` |
| GET | `/api/pulse/{id}` | get-api-pulse-id | N | Y | `get_pulse` |
| PUT | `/api/pulse/{id}` | put-api-pulse-id | Y | Y | `update_pulse` |
| GET | `/api/revision` | get-api-revision | N | Y | `list_revision` |
| GET | `/api/search` | get-api-search | N | Y | `list_search` |
| POST | `/api/segment` | post-api-segment | Y | Y | `create_segment` |
| GET | `/api/segment` | get-api-segment | N | Y | `list_segment` |
| GET | `/api/segment/{id}` | get-api-segment-id | N | Y | `get_segment` |
| PUT | `/api/segment/{id}` | put-api-segment-id | Y | Y | `update_segment` |
| DELETE | `/api/segment/{id}` | delete-api-segment-id | N | Y | `delete_segment` |
| POST | `/api/session` | post-api-session | Y | Y | `create_session` |
| GET | `/api/setting` | get-api-setting | N | Y | `list_setting` |
| PUT | `/api/setting` | put-api-setting | Y | Y | `create_setting` |
| GET | `/api/setting/{key}` | get-api-setting-key | N | Y | `get_setting` |
| PUT | `/api/setting/{key}` | put-api-setting-key | Y | Y | `update_setting` |
| POST | `/api/setup` | post-api-setup | Y | Y | `create_setup` |
| GET | `/api/table` | get-api-table | N | Y | `list_table` |
| PUT | `/api/table` | put-api-table | Y | Y | `create_table` |
| GET | `/api/table/{id}` | get-api-table-id | N | Y | `get_table` |
| PUT | `/api/table/{id}` | put-api-table-id | Y | Y | `update_table` |
| GET | `/api/task` | get-api-task | N | Y | `list_task` |
| GET | `/api/task/{id}` | get-api-task-id | N | Y | `get_task` |
| POST | `/api/timeline` | post-api-timeline | Y | Y | `create_timeline` |
| GET | `/api/timeline` | get-api-timeline | N | Y | `list_timeline` |
| POST | `/api/timeline-event` | post-api-timeline-event | Y | Y | `create_timeline-event` |
| GET | `/api/timeline-event/{id}` | get-api-timeline-event-id | N | Y | `get_timeline-event` |
| PUT | `/api/timeline-event/{id}` | put-api-timeline-event-id | Y | Y | `update_timeline-event` |
| DELETE | `/api/timeline-event/{id}` | delete-api-timeline-event-id | N | Y | `delete_timeline-event` |
| GET | `/api/timeline/{id}` | get-api-timeline-id | N | Y | `get_timeline` |
| PUT | `/api/timeline/{id}` | put-api-timeline-id | Y | Y | `update_timeline` |
| DELETE | `/api/timeline/{id}` | delete-api-timeline-id | N | Y | `delete_timeline` |
| GET | `/api/transform` | get-api-transform | N | Y | `list_transform` |
| POST | `/api/transform` | post-api-transform | Y | Y | `create_transform` |
| POST | `/api/transform-job` | post-api-transform-job | Y | Y | `create_transform-job` |
| GET | `/api/transform-job` | get-api-transform-job | N | Y | `list_transform-job` |
| PUT | `/api/transform-job/{job-id}` | put-api-transform-job-job-id | Y | Y | `update_transform-job` |
| DELETE | `/api/transform-job/{job-id}` | delete-api-transform-job-job-id | N | Y | `delete_transform-job` |
| GET | `/api/transform-job/{job-id}` | get-api-transform-job-job-id | N | Y | `get_transform-job` |
| POST | `/api/transform-tag` | post-api-transform-tag | Y | Y | `create_transform-tag` |
| GET | `/api/transform-tag` | get-api-transform-tag | N | Y | `list_transform-tag` |
| PUT | `/api/transform-tag/{tag-id}` | put-api-transform-tag-tag-id | Y | Y | `update_transform-tag` |
| DELETE | `/api/transform-tag/{tag-id}` | delete-api-transform-tag-tag-id | N | Y | `delete_transform-tag` |
| GET | `/api/transform/{id}` | get-api-transform-id | N | Y | `get_transform` |
| PUT | `/api/transform/{id}` | put-api-transform-id | Y | Y | `update_transform` |
| DELETE | `/api/transform/{id}` | delete-api-transform-id | N | Y | `delete_transform` |
| GET | `/api/user` | get-api-user | N | Y | `list_user` |
| POST | `/api/user` | post-api-user | Y | Y | `create_user` |
| GET | `/api/user/{id}` | get-api-user-id | N | Y | `get_user` |
| PUT | `/api/user/{id}` | put-api-user-id | Y | Y | `update_user` |
| DELETE | `/api/user/{id}` | delete-api-user-id | N | Y | `delete_user` |
