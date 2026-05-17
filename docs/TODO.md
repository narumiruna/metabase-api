# Metabase API TODO

Source page: <https://www.metabase.com/docs/latest/api>
Source OpenAPI document: <https://www.metabase.com/docs/latest/api.json>
Reviewed: 2026-05-17

This file is a static implementation checklist derived from the latest Metabase API documentation. It is not a runtime endpoint registry and must not be imported by package code.

## Legend

- `[x]` = this endpoint has all required hand-written support: a focused client method, request `BaseModel`, response `BaseModel`, CLI command, and tests.
- `[ ]` = this endpoint is not complete yet. Raw `request` / `invoke` usage is intentionally forbidden and does not count as completion.
- Add focused models and convenience commands by hand only; do not add `api.json`, generated endpoint modules, runtime endpoint registries, or file-scanning endpoint discovery.

## Coverage summary

- Documented operations: 600
- Complete hand-written endpoint implementations: 121
- Remaining documented operations: 479
- Raw `request` / `invoke`: disabled for CLI users and does not count toward TODO completion.

## Endpoint checklist

### /api/action (10/10 complete)

- [x] `GET /api/action` — `get-api-action` — Returns actions that can be used for QueryActions. By default lists all viewable actions. Pass optional `?model-id=<model-id>` to limit to actions on a parti...
- [x] `POST /api/action` — `post-api-action` — Create a new action.
- [x] `GET /api/action/public` — `get-api-action-public` — Fetch a list of Actions with public UUIDs. These actions are publicly-accessible *if* public sharing is enabled.
- [x] `GET /api/action/{action-id}` — `get-api-action-action-id` — Fetch an Action.
- [x] `DELETE /api/action/{action-id}` — `delete-api-action-action-id` — Delete an Action.
- [x] `GET /api/action/{action-id}/execute` — `get-api-action-action-id-execute` — Fetches the values for filling in execution parameters. Pass PK parameters and values to select.
- [x] `PUT /api/action/{id}` — `put-api-action-id` — Update an Action.
- [x] `POST /api/action/{id}/execute` — `post-api-action-id-execute` — Execute the Action. `parameters` should be the mapped dashboard parameters with values.
- [x] `POST /api/action/{id}/public_link` — `post-api-action-id-public_link` — Generate publicly-accessible links for this Action. Returns UUID to be used in public links. (If this Action has already been shared, it will return the exis...
- [x] `DELETE /api/action/{id}/public_link` — `delete-api-action-id-public_link` — Delete the publicly-accessible link to this Dashboard.

### /api/activity (5/5 complete)

- [x] `GET /api/activity/most_recently_viewed_dashboard` — `get-api-activity-most_recently_viewed_dashboard` — Get the most recently viewed dashboard for the current user. Returns a 204 if the user has not viewed any dashboards in the last 24 hours.
- [x] `GET /api/activity/popular_items` — `get-api-activity-popular_items` — Get the list of 5 popular things on the instance. Query takes 8 and limits to 5 so that if it finds anything archived, deleted, etc it can usually still get 5.
- [x] `GET /api/activity/recent_views` — `get-api-activity-recent_views` — Get a list of 100 models (cards, models, tables, dashboards, and collections) that the current user has been viewing most recently. Return a maximum of 20 mo...
- [x] `GET /api/activity/recents` — `get-api-activity-recents` — Get a list of recent items the current user has been viewing most recently under the `:recents` key. Allows for filtering by context: views or selections
- [x] `POST /api/activity/recents` — `post-api-activity-recents` — Adds a model to the list of recently selected items.

### /api/agent (9/9 complete)

- [x] `POST /api/agent/v1/execute` — `post-api-agent-v1-execute` — Execute an MBQL query and return results. Accepts a base64-encoded MBQL query (as returned by /v1/construct-query) and executes it, returning results with co...
- [x] `GET /api/agent/v1/metric/{id}` — `get-api-agent-v1-metric-id` — Get details for a metric by ID.
- [x] `GET /api/agent/v1/metric/{id}/field/{field-id}/values` — `get-api-agent-v1-metric-id-field-field-id-values` — Get statistics and sample values for a metric field.
- [x] `GET /api/agent/v1/ping` — `get-api-agent-v1-ping` — Health check endpoint for the Agent API.
- [x] `POST /api/agent/v1/search` — `post-api-agent-v1-search` — Search for tables and metrics. Supports both term-based and semantic search queries. Results are ranked using Reciprocal Rank Fusion when both query types ar...
- [x] `GET /api/agent/v1/table/{id}` — `get-api-agent-v1-table-id` — Get details for a table by ID.
- [x] `GET /api/agent/v1/table/{id}/field/{field-id}/values` — `get-api-agent-v1-table-id-field-field-id-values` — Get statistics and sample values for a table field.
- [x] `POST /api/agent/v2/construct-query` — `post-api-agent-v2-construct-query` — Construct an MBQL query from a structured agent-lib program. The body is the program itself: a JSON object with `source` (identifying the table/card/dataset/...
- [x] `POST /api/agent/v2/query` — `post-api-agent-v2-query` — Execute a structured program and stream the results, with continuation-token pagination. Accepts either a program (same shape as /v2/construct-query) or a `c...

### /api/ai-entity-analysis (1/1 complete)

- [x] `POST /api/ai-entity-analysis/analyze-chart` — `post-api-ai-entity-analysis-analyze-chart` — Analyze a chart image using an AI vision model. This function sends the image data to a separate external AI service for analysis.

### /api/alert (3/3 complete)

- [x] `GET /api/alert` — `get-api-alert` — Fetch alerts which the current user has created or will receive, or all alerts if the user is an admin. The optional `user_id` will return alerts created by...
- [x] `GET /api/alert/{id}` — `get-api-alert-id` — Fetch an alert by ID
- [x] `DELETE /api/alert/{id}/subscription` — `delete-api-alert-id-subscription` — For users to unsubscribe themselves from the given alert.

### /api/analytics (2/2 complete)

- [x] `GET /api/analytics/anonymous-stats` — `get-api-analytics-anonymous-stats` — Anonymous usage stats. Endpoint for testing, and eventually exposing this to instance admins to let them see what is being phoned home.
- [x] `POST /api/analytics/internal` — `post-api-analytics-internal` — Receive a batch of internal analytics events from the frontend and record them as Prometheus metrics.

### /api/api-key (6/6 complete)

- [x] `POST /api/api-key` — `post-api-api-key` — Create a new API key (and an associated `User`) with the provided name and group ID.
- [x] `GET /api/api-key` — `get-api-api-key` — Get a list of API keys with the default scope. Non-paginated.
- [x] `GET /api/api-key/count` — `get-api-api-key-count` — Get the count of API keys in the DB with the default scope.
- [x] `PUT /api/api-key/{id}` — `put-api-api-key-id` — Update an API key by changing its group and/or its name
- [x] `DELETE /api/api-key/{id}` — `delete-api-api-key-id` — Delete an ApiKey
- [x] `PUT /api/api-key/{id}/regenerate` — `put-api-api-key-id-regenerate` — Regenerate an API Key

### /api/automagic-dashboards (11/11 complete)

- [x] `GET /api/automagic-dashboards/database/{id}/candidates` — `get-api-automagic-dashboards-database-id-candidates` — Return a list of candidates for automagic dashboards ordered by interestingness.
- [x] `GET /api/automagic-dashboards/model_index/{model-index-id}/primary_key/{pk-id}` — `get-api-automagic-dashboards-model_index-model-index-id-primary_key-pk-id` — Return an automagic dashboard for an entity detail specified by `entity` with id `id` and a primary key of `indexed-value`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query` — Return an automagic dashboard for entity `entity` with id `id`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/cell/{cell-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query-cell-cell-query` — Return an automagic dashboard analyzing cell in automagic dashboard for entity `entity` defined by query `cell-query`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/cell/{cell-query}/compare/{comparison-entity}/{comparison-entity-id-or-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query-cell-cell-query-compare-comparison-entity-comparison-entity-id-or-query` — Return an automagic comparison dashboard for cell in automagic dashboard for entity `entity` with id `id` defined by query `cell-query`; compared with entity...
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/cell/{cell-query}/rule/{prefix}/{dashboard-template}` — `get-api-automagic-dashboards-entity-entity-id-or-query-cell-cell-query-rule-prefix-dashboard-template` — Return an automagic dashboard analyzing cell in question with id `id` defined by query `cell-query` using dashboard-template `dashboard-template`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/cell/{cell-query}/rule/{prefix}/{dashboard-template}/compare/{comparison-entity}/{comparison-entity-id-or-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query-cell-cell-query-rule-prefix-dashboard-template-compare-comparison-entity-comparison-entity-id-or-query` — Return an automagic comparison dashboard for cell in automagic dashboard for entity `entity` with id `id` defined by query `cell-query` using dashboard-templ...
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/compare/{comparison-entity}/{comparison-entity-id-or-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query-compare-comparison-entity-comparison-entity-id-or-query` — Return an automagic comparison dashboard for entity `entity` with id `id` compared with entity `comparison-entity` with id `comparison-entity-id-or-query.`
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/query_metadata` — `get-api-automagic-dashboards-entity-entity-id-or-query-query_metadata` — Return all metadata for an automagic dashboard for entity `entity` with id `id`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/rule/{prefix}/{dashboard-template}` — `get-api-automagic-dashboards-entity-entity-id-or-query-rule-prefix-dashboard-template` — Return an automagic dashboard for entity `entity` with id `id` using dashboard-template `dashboard-template`.
- [x] `GET /api/automagic-dashboards/{entity}/{entity-id-or-query}/rule/{prefix}/{dashboard-template}/compare/{comparison-entity}/{comparison-entity-id-or-query}` — `get-api-automagic-dashboards-entity-entity-id-or-query-rule-prefix-dashboard-template-compare-comparison-entity-comparison-entity-id-or-query` — Return an automagic comparison dashboard for entity `entity` with id `id` using dashboard-template `dashboard-template`; compared with entity `comparison-ent...

### /api/bookmark (4/4 complete)

- [x] `GET /api/bookmark` — `get-api-bookmark` — Fetch all bookmarks for the user
- [x] `PUT /api/bookmark/ordering` — `put-api-bookmark-ordering` — Sets the order of bookmarks for user.
- [x] `POST /api/bookmark/{model}/{id}` — `post-api-bookmark-model-id` — Create a new bookmark for user.
- [x] `DELETE /api/bookmark/{model}/{id}` — `delete-api-bookmark-model-id` — Delete a bookmark. Will delete a bookmark assigned to the user making the request by model and id.

### /api/bug-reporting (2/2 complete)

- [x] `GET /api/bug-reporting/connection-pool-details` — `get-api-bug-reporting-connection-pool-details` — Returns database connection pool info for the current Metabase instance.
- [x] `GET /api/bug-reporting/details` — `get-api-bug-reporting-details` — Returns version and system information relevant to filing a bug report against Metabase.

### /api/cache (4/4 complete)

- [x] `GET /api/cache` — `get-api-cache` — Return cache configuration. Supports pagination via `limit` and `offset` query parameters, and sorting via `sort_column` and `sort_direction`.
- [x] `PUT /api/cache` — `put-api-cache` — Store cache configuration.
- [x] `DELETE /api/cache` — `delete-api-cache` — Delete cache configurations.
- [x] `POST /api/cache/invalidate` — `post-api-cache-invalidate` — Invalidate cache entries. Use it like `/api/cache/invalidate?database=1&dashboard=15` (any number of database/dashboard/question can be supplied). `&include=...

### /api/card (20/20 complete)

- [x] `GET /api/card` — `get-api-card` — Get all the Cards. Option filter param `f` can be used to change the set of Cards that are returned; default is `all`, but other options include `mine`, `boo...
- [x] `POST /api/card` — `post-api-card` — Create a new `Card`. Card `type` can be `question`, `metric`, or `model`.
- [x] `POST /api/card/collections` — `post-api-card-collections` — Bulk update endpoint for Card Collections. Move a set of `Cards` with `card_ids` into a `Collection` with `collection_id`, or remove them from any Collection...
- [x] `GET /api/card/embeddable` — `get-api-card-embeddable` — Fetch a list of Cards where `enable_embedding` is `true`. The cards can be embedded using the embedding endpoints and a signed JWT.
- [x] `POST /api/card/pivot/{card-id}/query` — `post-api-card-pivot-card-id-query` — Run the query associated with a Card.
- [x] `GET /api/card/public` — `get-api-card-public` — Fetch a list of Cards with public UUIDs. These cards are publicly-accessible *if* public sharing is enabled.
- [x] `GET /api/card/{card-id}/params/{param-key}/search/{query}` — `get-api-card-card-id-params-param-key-search-query` — Fetch possible values of the parameter whose ID is `:param-key` that contain `:query`. ;; fetch values for Card 1 parameter 'abc' that contain 'Orange'; GET...
- [x] `GET /api/card/{card-id}/params/{param-key}/values` — `get-api-card-card-id-params-param-key-values` — Fetch possible values of the parameter whose ID is `:param-key`. ;; fetch values for Card 1 parameter 'abc' that are possible GET /api/queries/1/params/abc/v...
- [x] `POST /api/card/{card-id}/public_link` — `post-api-card-card-id-public_link` — Generate publicly-accessible links for this Card. Returns UUID to be used in public links. (If this Card has already been shared, it will return the existing...
- [x] `DELETE /api/card/{card-id}/public_link` — `delete-api-card-card-id-public_link` — Delete the publicly-accessible link to this Card.
- [x] `POST /api/card/{card-id}/query` — `post-api-card-card-id-query` — Run the query associated with a Card.
- [x] `POST /api/card/{card-id}/query/{export-format}` — `post-api-card-card-id-query-export-format` — Run the query associated with a Card, and return its results as a file in the specified format. `parameters`, `pivot-results?` and `format-rows?` should be p...
- [x] `GET /api/card/{id}` — `get-api-card-id` — Get `Card` with ID. As of v57, returns the MBQL query (`dataset_query`) as MBQL 5; to return the query as MBQL 4 (aka legacy MBQL) instead, you can specify `...
- [x] `PUT /api/card/{id}` — `put-api-card-id` — Update a `Card`.
- [x] `DELETE /api/card/{id}` — `delete-api-card-id` — Hard delete a Card. To soft delete, use `PUT /api/queries/:id`
- [x] `POST /api/card/{id}/copy` — `post-api-card-id-copy` — Copy a `Card`, with the new name 'Copy of _name_'
- [x] `GET /api/card/{id}/dashboards` — `get-api-card-id-dashboards` — Get a list of `{:name ... :id ...}` pairs for all the dashboards this card appears in.
- [x] `GET /api/card/{id}/params/{param-key}/remapping` — `get-api-card-id-params-param-key-remapping` — Fetch the remapped value for a given value of the parameter with ID `:param-key`. ;; fetch the remapped value for Card 1 parameter 'abc' for value 100 GET /a...
- [x] `GET /api/card/{id}/query_metadata` — `get-api-card-id-query_metadata` — Get all of the required query metadata for a card.
- [x] `GET /api/card/{id}/series` — `get-api-card-id-series` — Fetches a list of compatible series with the card with id `card_id`. - `last_cursor` with value is the id of the last card from the previous page to fetch th...

### /api/cards (2/2 complete)

- [x] `POST /api/cards/dashboards` — `post-api-cards-dashboards` — Get the dashboards that multiple cards appear in. The response is a sequence of maps, each of which has a `card_id` and `dashboards`. `dashboard` may include...
- [x] `POST /api/cards/move` — `post-api-cards-move` — Moves a number of Cards to a single collection or dashboard. For now, just either succeed or fail as a batch - we can think more about error handling later d...

### /api/channel (5/5 complete)

- [x] `GET /api/channel` — `get-api-channel` — Get all channels
- [x] `POST /api/channel` — `post-api-channel` — Create a channel
- [x] `POST /api/channel/test` — `post-api-channel-test` — Test a channel connection
- [x] `GET /api/channel/{id}` — `get-api-channel-id` — Get a channel
- [x] `PUT /api/channel/{id}` — `put-api-channel-id` — Update a channel

### /api/cloud-migration (3/3 complete)

- [x] `POST /api/cloud-migration` — `post-api-cloud-migration` — Initiate a new cloud migration.
- [x] `GET /api/cloud-migration` — `get-api-cloud-migration` — Get the latest cloud migration, if any.
- [x] `PUT /api/cloud-migration/cancel` — `put-api-cloud-migration-cancel` — Cancel any ongoing cloud migrations, if any.

### /api/collection (16/16 complete)

- [x] `GET /api/collection` — `get-api-collection` — Fetch a list of all Collections that the current user has read permissions for (`:can_write` is returned as an additional property of each Collection so you...
- [x] `POST /api/collection` — `post-api-collection` — Create a new Collection.
- [x] `GET /api/collection/graph` — `get-api-collection-graph` — Fetch a graph of all Collection Permissions.
- [x] `PUT /api/collection/graph` — `put-api-collection-graph` — Do a batch update of Collections Permissions by passing in a modified graph. Will overwrite parts of the graph that are present in the request, and leave the...
- [x] `GET /api/collection/root` — `get-api-collection-root` — Return the 'Root' Collection object with standard details added
- [x] `GET /api/collection/root/dashboard-question-candidates` — `get-api-collection-root-dashboard-question-candidates` — Find cards in the root collection that can be moved into dashboards in the root collection. (Same as the above endpoint, but for the root collection)
- [x] `GET /api/collection/root/items` — `get-api-collection-root-items` — Fetch objects that the user should see at their root level. As mentioned elsewhere, the 'Root' Collection doesn't actually exist as a row in the appl...
- [x] `POST /api/collection/root/move-dashboard-question-candidates` — `post-api-collection-root-move-dashboard-question-candidates` — Move candidate cards to the dashboards they appear in (for the root collection)
- [x] `GET /api/collection/trash` — `get-api-collection-trash` — Fetch the trash collection, as in `/api/collection/:trash-id`
- [x] `GET /api/collection/tree` — `get-api-collection-tree` — Similar to `GET /`, but returns Collections in a tree structure, e.g. ``` [{:name "A" :below #{:card :dataset} :children [{:name "B"} {:name "C" :here #{:dat...
- [x] `GET /api/collection/{id}` — `get-api-collection-id` — Fetch a specific Collection with standard details added
- [x] `PUT /api/collection/{id}` — `put-api-collection-id` — Modify an existing Collection, including archiving or unarchiving it, or moving it.
- [x] `DELETE /api/collection/{id}` — `delete-api-collection-id` — Deletes a collection permanently
- [x] `GET /api/collection/{id}/dashboard-question-candidates` — `get-api-collection-id-dashboard-question-candidates` — Find cards in this collection that can be moved into dashboards in this collection. To be eligible, a card must only appear in one dashboard (which is also i...
- [x] `GET /api/collection/{id}/items` — `get-api-collection-id-items` — Fetch a specific Collection's items with the following options: * `models` - only include objects of a specific set of `models`. If unspecified, returns obje...
- [x] `POST /api/collection/{id}/move-dashboard-question-candidates` — `post-api-collection-id-move-dashboard-question-candidates` — Move candidate cards to the dashboards they appear in.

### /api/comment (6/6 complete)

- [x] `GET /api/comment` — `get-api-comment` — Get comments for an entity
- [x] `POST /api/comment` — `post-api-comment` — Create a new comment
- [x] `GET /api/comment/mentions` — `get-api-comment-mentions` — Get a list of entities suitable for mentions. NOTE: only users for now.
- [x] `PUT /api/comment/{comment-id}` — `put-api-comment-comment-id` — Update a comment
- [x] `DELETE /api/comment/{comment-id}` — `delete-api-comment-comment-id` — Soft delete a comment
- [x] `POST /api/comment/{comment-id}/reaction` — `post-api-comment-comment-id-reaction` — Toggle a reaction on a comment

### /api/dashboard (3/25 complete)

- [x] `GET /api/dashboard` — `get-api-dashboard` — This endpoint is currently unused by the Metabase frontend and may be out of date with the rest of the application. It only exists for backwards compatibilit...
- [x] `POST /api/dashboard` — `post-api-dashboard` — Create a new Dashboard.
- [ ] `GET /api/dashboard/embeddable` — `get-api-dashboard-embeddable` — Fetch a list of Dashboards where `enable_embedding` is `true`. The dashboards can be embedded using the embedding endpoints and a signed JWT.
- [ ] `GET /api/dashboard/params/valid-filter-fields` — `get-api-dashboard-params-valid-filter-fields` — Utility endpoint for powering Dashboard UI. Given some set of `filtered` Field IDs (presumably Fields used in parameters) and a set of `filtering` Field IDs...
- [ ] `POST /api/dashboard/pivot/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query` — `post-api-dashboard-pivot-dashboard-id-dashcard-dashcard-id-card-card-id-query` — Run a pivot table query for a specific DashCard.
- [ ] `GET /api/dashboard/public` — `get-api-dashboard-public` — Fetch a list of Dashboards with public UUIDs. These dashboards are publicly-accessible *if* public sharing is enabled.
- [ ] `POST /api/dashboard/save` — `post-api-dashboard-save` — Save a denormalized description of dashboard.
- [ ] `POST /api/dashboard/save/collection/{parent-collection-id}` — `post-api-dashboard-save-collection-parent-collection-id` — Save a denormalized description of dashboard into collection with ID `:parent-collection-id`.
- [ ] `POST /api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query` — `post-api-dashboard-dashboard-id-dashcard-dashcard-id-card-card-id-query` — Run the query associated with a Saved Question (`Card`) in the context of a `Dashboard` that includes it.
- [ ] `POST /api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query/{export-format}` — `post-api-dashboard-dashboard-id-dashcard-dashcard-id-card-card-id-query-export-format` — Run the query associated with a Saved Question (`Card`) in the context of a `Dashboard` that includes it, and return its results as a file in the specified f...
- [ ] `GET /api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute` — `get-api-dashboard-dashboard-id-dashcard-dashcard-id-execute` — Fetches the values for filling in execution parameters. Pass PK parameters and values to select.
- [ ] `POST /api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute` — `post-api-dashboard-dashboard-id-dashcard-dashcard-id-execute` — Execute the associated Action in the context of a `Dashboard` and `DashboardCard` that includes it. `parameters` should be the mapped dashboard parameters wi...
- [ ] `POST /api/dashboard/{dashboard-id}/public_link` — `post-api-dashboard-dashboard-id-public_link` — Generate publicly-accessible links for this Dashboard. Returns UUID to be used in public links. (If this Dashboard has already been shared, it will return th...
- [ ] `DELETE /api/dashboard/{dashboard-id}/public_link` — `delete-api-dashboard-dashboard-id-public_link` — Delete the publicly-accessible link to this Dashboard.
- [ ] `POST /api/dashboard/{from-dashboard-id}/copy` — `post-api-dashboard-from-dashboard-id-copy` — Copy a Dashboard.
- [x] `GET /api/dashboard/{id}` — `get-api-dashboard-id` — Get Dashboard with ID.
- [ ] `DELETE /api/dashboard/{id}` — `delete-api-dashboard-id` — Hard delete a Dashboard. To soft delete, use `PUT /api/dashboard/:id` This will remove also any questions/models/segments/metrics that use this database.
- [ ] `PUT /api/dashboard/{id}` — `put-api-dashboard-id` — Update a Dashboard, and optionally the `dashcards` and `tabs` of a Dashboard. The request body should be a JSON object with the same structure as the respons...
- [ ] `PUT /api/dashboard/{id}/cards` — `put-api-dashboard-id-cards` — (DEPRECATED -- Use the `PUT /api/dashboard/:id` endpoint instead.) Update `Cards` and `Tabs` on a Dashboard. Request body should have the form: {:cards [{:id...
- [ ] `GET /api/dashboard/{id}/items` — `get-api-dashboard-id-items` — Get Dashboard with ID.
- [ ] `GET /api/dashboard/{id}/params/{param-key}/remapping` — `get-api-dashboard-id-params-param-key-remapping` — Fetch the remapped value for a given value of the parameter with ID `:param-key`. ;; fetch the remapped value for Dashboard 1 parameter 'abc' for value 100 G...
- [ ] `GET /api/dashboard/{id}/params/{param-key}/search/{query}` — `get-api-dashboard-id-params-param-key-search-query` — Fetch possible values of the parameter whose ID is `:param-key` that contain `:query`. Optionally restrict these values by passing query parameters like `oth...
- [ ] `GET /api/dashboard/{id}/params/{param-key}/values` — `get-api-dashboard-id-params-param-key-values` — Fetch possible values of the parameter whose ID is `:param-key`. If the values come directly from a query, optionally restrict these values by passing query...
- [ ] `GET /api/dashboard/{id}/query_metadata` — `get-api-dashboard-id-query_metadata` — Get all of the required query metadata for the cards on dashboard.
- [ ] `GET /api/dashboard/{id}/related` — `get-api-dashboard-id-related` — Return related entities.

### /api/data-studio/table (0/5 complete)

- [ ] `POST /api/data-studio/table/discard-values` — `post-api-data-studio-table-discard-values` — Batch version of /table/:id/discard_values. Takes an abstract table selection as /table/edit does.
- [ ] `POST /api/data-studio/table/edit` — `post-api-data-studio-table-edit` — Bulk updating tables.
- [ ] `POST /api/data-studio/table/rescan-values` — `post-api-data-studio-table-rescan-values` — Batch version of /table/:id/rescan_values. Takes an abstract table selection as /table/edit does.
- [ ] `POST /api/data-studio/table/selection` — `post-api-data-studio-table-selection` — Gets information about selected tables
- [ ] `POST /api/data-studio/table/sync-schema` — `post-api-data-studio-table-sync-schema` — Batch version of /table/:id/sync_schema. Takes an abstract table selection as /table/edit does. - Currently checks policy before returning (so you might rece...

### /api/database (3/31 complete)

- [x] `GET /api/database` — `get-api-database` — Fetch all `Databases`. * `include=tables` means we should hydrate the Tables belonging to each DB. Default: `false`. * `saved` means we should include the sa...
- [x] `POST /api/database` — `post-api-database` — Add a new `Database`.
- [ ] `GET /api/database/field-values` — `get-api-database-field-values` — Get sampled field values for every field in the instance, streamed as a single `{"field_values": [...]}` document. Each entry carries `field_id`, `values`, o...
- [ ] `GET /api/database/metadata` — `get-api-database-metadata` — Get metadata (databases, tables, and fields) for all databases visible to the current user. Returns a flat structure with three arrays: databases, tables, an...
- [ ] `POST /api/database/metadata` — `post-api-database-metadata` — Import database/table/field metadata previously exported from `GET /api/database/metadata`. Entities are matched by natural key — databases by `(name, engine...
- [ ] `POST /api/database/sample_database` — `post-api-database-sample_database` — Add the sample database as a new `Database`.
- [ ] `POST /api/database/validate` — `post-api-database-validate` — Validate that we can connect to a database given a set of details.
- [x] `GET /api/database/{id}` — `get-api-database-id` — Get a single Database with `id`. Optionally pass `?include=tables` or `?include=tables.fields` to include the Tables belonging to this database, or the Table...
- [ ] `PUT /api/database/{id}` — `put-api-database-id` — Update a `Database`.
- [ ] `DELETE /api/database/{id}` — `delete-api-database-id` — Delete a `Database`.
- [ ] `GET /api/database/{id}/autocomplete_suggestions` — `get-api-database-id-autocomplete_suggestions` — Return a list of autocomplete suggestions for a given `prefix`, or `substring`. Should only specify one, but `substring` will have priority if both are prese...
- [ ] `GET /api/database/{id}/card_autocomplete_suggestions` — `get-api-database-id-card_autocomplete_suggestions` — Return a list of `Card` autocomplete suggestions for a given `query` in a given `Database`. This is intended for use with the ACE Editor when the User is typ...
- [ ] `POST /api/database/{id}/discard_values` — `post-api-database-id-discard_values` — Discards all saved field values for this `Database`.
- [ ] `POST /api/database/{id}/dismiss_spinner` — `post-api-database-id-dismiss_spinner` — Manually set the initial sync status of the `Database` and corresponding tables to be `complete` (see #20863)
- [ ] `GET /api/database/{id}/fields` — `get-api-database-id-fields` — Get a list of all `Fields` in `Database`.
- [ ] `GET /api/database/{id}/healthcheck` — `get-api-database-id-healthcheck` — Reports whether the database can currently connect
- [ ] `GET /api/database/{id}/idfields` — `get-api-database-id-idfields` — Get a list of all primary key `Fields` for `Database`.
- [ ] `GET /api/database/{id}/metadata` — `get-api-database-id-metadata` — Get metadata about a `Database`, including all of its `Tables` and `Fields`. Returns DB, fields, and field values. By default only non-hidden tables and fiel...
- [ ] `POST /api/database/{id}/rescan_values` — `post-api-database-id-rescan_values` — Trigger a manual scan of the field values for this `Database`.
- [ ] `GET /api/database/{id}/schema` — `get-api-database-id-schema` — Return a list of Tables for a Database whose `schema` is `nil` or an empty string. Optional filters: - `can-query=true` - filter to only tables the user can...
- [ ] `GET /api/database/{id}/schema/{schema}` — `get-api-database-id-schema-schema` — Returns a list of Tables for the given Database `id` and `schema`. Optional filters: - `can-query=true` - filter to only tables the user can query - `can-wri...
- [ ] `GET /api/database/{id}/schemas` — `get-api-database-id-schemas` — Returns a list of all the schemas with tables found for the database `id`. Excludes schemas with no tables. Optional filters: - `can-query=true` - filter to...
- [ ] `GET /api/database/{id}/settings-available` — `get-api-database-id-settings-available` — Get all database-local settings and their availability for the given database.
- [ ] `POST /api/database/{id}/sync_schema` — `post-api-database-id-sync_schema` — Trigger a manual update of the schema metadata for this `Database`.
- [ ] `GET /api/database/{id}/syncable_schemas` — `get-api-database-id-syncable_schemas` — Returns a list of all syncable schemas found for the database `id`.
- [ ] `GET /api/database/{id}/usage_info` — `get-api-database-id-usage_info` — Get usage info for a database. Returns a map with keys are models and values are the number of entities that use this database.
- [ ] `GET /api/database/{virtual-db}/datasets` — `get-api-database-virtual-db-datasets` — Returns a list of all the datasets found for the saved questions virtual database.
- [ ] `GET /api/database/{virtual-db}/datasets/{schema}` — `get-api-database-virtual-db-datasets-schema` — Returns a list of Tables for the datasets virtual database.
- [ ] `GET /api/database/{virtual-db}/metadata` — `get-api-database-virtual-db-metadata` — Endpoint that provides metadata for the Saved Questions 'virtual' database. Used for fooling the frontend and allowing it to treat the Saved Questions virtua...
- [ ] `GET /api/database/{virtual-db}/schema/{schema}` — `get-api-database-virtual-db-schema-schema` — Returns a list of Tables for the saved questions virtual database.
- [ ] `GET /api/database/{virtual-db}/schemas` — `get-api-database-virtual-db-schemas` — Returns a list of all the schemas found for the saved questions virtual database.

### /api/dataset (0/8 complete)

- [ ] `POST /api/dataset` — `post-api-dataset` — Execute a query and retrieve the results in the usual format. The query will not use the cache.
- [ ] `POST /api/dataset/native` — `post-api-dataset-native` — Fetch a native version of an MBQL query.
- [ ] `POST /api/dataset/parameter/remapping` — `post-api-dataset-parameter-remapping` — Return the remapped parameter values for cards or dashboards that are being edited.
- [ ] `POST /api/dataset/parameter/search/{query}` — `post-api-dataset-parameter-search-query` — Return parameter values for cards or dashboards that are being edited. Expects a query string at `?query=foo`.
- [ ] `POST /api/dataset/parameter/values` — `post-api-dataset-parameter-values` — Return parameter values for cards or dashboards that are being edited.
- [ ] `POST /api/dataset/pivot` — `post-api-dataset-pivot` — Generate a pivoted dataset for an ad-hoc query
- [ ] `POST /api/dataset/query_metadata` — `post-api-dataset-query_metadata` — Get all of the required query metadata for an ad-hoc query. You can pass `{:settings {:include-sensitive-fields true}}` in the query to include fields with v...
- [ ] `POST /api/dataset/{export-format}` — `post-api-dataset-export-format` — Execute a query and download the result data as a file in the specified format.

### /api/document (0/10 complete)

- [ ] `GET /api/document` — `get-api-document` — Gets existing `Documents`.
- [ ] `POST /api/document` — `post-api-document` — Create a new `Document`.
- [ ] `GET /api/document/public` — `get-api-document-public` — List all Documents that have public links. Returns a sequence of Documents that have been publicly shared. Each Document includes its `:id`, `:name`, and `:p...
- [ ] `GET /api/document/{document-id}` — `get-api-document-document-id` — Returns an existing Document by ID.
- [ ] `PUT /api/document/{document-id}` — `put-api-document-document-id` — Updates an existing `Document`.
- [ ] `DELETE /api/document/{document-id}` — `delete-api-document-document-id` — Permanently deletes an archived Document.
- [ ] `POST /api/document/{document-id}/card/{card-id}/query/{export-format}` — `post-api-document-document-id-card-card-id-query-export-format` — Download query results for a Card embedded in a Document. Returns query results in the requested format. The user must have read access to the document to do...
- [ ] `POST /api/document/{document-id}/public-link` — `post-api-document-document-id-public-link` — Generate a publicly-accessible UUID for a Document. Creates a public link that allows viewing the Document without authentication. If the Document already ha...
- [ ] `DELETE /api/document/{document-id}/public-link` — `delete-api-document-document-id-public-link` — Remove the public link for a Document. Deletes the public UUID from the Document, making it no longer accessible via the public sharing endpoint. This revoke...
- [ ] `POST /api/document/{from-document-id}/copy` — `post-api-document-from-document-id-copy` — Copy a Document.

### /api/ee/action-v2 (0/3 complete)

- [ ] `POST /api/ee/action-v2/execute` — `post-api-ee-action-v2-execute` — Execute an action with a single input. Takes: - `action` - an identifier or an expression for what we want to execute. - `scope` - where the action is being...
- [ ] `POST /api/ee/action-v2/execute-bulk` — `post-api-ee-action-v2-execute-bulk` — Execute an action with multiple inputs. This is typically more efficient than calling execute with each input individually, for example by performing batch S...
- [ ] `POST /api/ee/action-v2/execute-form` — `post-api-ee-action-v2-execute-form` — Temporary endpoint for describing an actions parameters such that they can be presented correctly in a modal ahead of execution.

### /api/ee/advanced-permissions/application (0/2 complete)

- [ ] `GET /api/ee/advanced-permissions/application/graph` — `get-api-ee-advanced-permissions-application-graph` — Fetch a graph of Application Permissions.
- [ ] `PUT /api/ee/advanced-permissions/application/graph` — `put-api-ee-advanced-permissions-application-graph` — Do a batch update of Application Permissions by passing a modified graph.

### /api/ee/advanced-permissions/impersonation (0/2 complete)

- [ ] `GET /api/ee/advanced-permissions/impersonation` — `get-api-ee-advanced-permissions-impersonation` — Fetch a list of all Impersonation policies currently in effect, or a single policy if both `group_id` and `db_id` are provided.
- [ ] `DELETE /api/ee/advanced-permissions/impersonation/{id}` — `delete-api-ee-advanced-permissions-impersonation-id` — Delete a Connection Impersonation entry.

### /api/ee/ai-controls/permissions (0/2 complete)

- [ ] `GET /api/ee/ai-controls/permissions` — `get-api-ee-ai-controls-permissions` — List all metabot permissions for all groups, filling in defaults for missing entries.
- [ ] `PUT /api/ee/ai-controls/permissions` — `put-api-ee-ai-controls-permissions` — Update metabot permissions for all groups. Upserts each permission entry and returns the full permissions list with defaults filled in.

### /api/ee/ai-controls/usage (0/8 complete)

- [ ] `GET /api/ee/ai-controls/usage/group` — `get-api-ee-ai-controls-usage-group` — Get all group-level metabot usage limits.
- [ ] `GET /api/ee/ai-controls/usage/group/{group-id}` — `get-api-ee-ai-controls-usage-group-group-id` — Get the metabot usage limit for a specific group. Returns `max_usage: null` if no limit is set.
- [ ] `PUT /api/ee/ai-controls/usage/group/{group-id}` — `put-api-ee-ai-controls-usage-group-group-id` — Set or update the metabot usage limit for a specific group. Pass `max_usage: null` to remove the limit.
- [ ] `GET /api/ee/ai-controls/usage/instance` — `get-api-ee-ai-controls-usage-instance` — Get the instance-wide metabot usage limit. Returns `max_usage: null` if no limit is set (unlimited).
- [ ] `PUT /api/ee/ai-controls/usage/instance` — `put-api-ee-ai-controls-usage-instance` — Set or update the instance-wide metabot usage limit. Pass `max_usage: null` to remove the limit (unlimited).
- [ ] `GET /api/ee/ai-controls/usage/tenant` — `get-api-ee-ai-controls-usage-tenant` — Get all tenant-level metabot usage limits.
- [ ] `GET /api/ee/ai-controls/usage/tenant/{tenant-id}` — `get-api-ee-ai-controls-usage-tenant-tenant-id` — Get the metabot usage limit for a specific tenant. Returns `max_usage: null` if no limit is set.
- [ ] `PUT /api/ee/ai-controls/usage/tenant/{tenant-id}` — `put-api-ee-ai-controls-usage-tenant-tenant-id` — Set or update the metabot usage limit for a specific tenant. Pass `max_usage: null` to remove the limit.

### /api/ee/audit-app/analytics-dev (0/1 complete)

- [ ] `POST /api/ee/audit-app/analytics-dev/export` — `post-api-ee-audit-app-analytics-dev-export` — Export analytics content as a .tar.gz file for local development. Only available when MB_ANALYTICS_DEV_MODE=true. Returns a tarball containing the analytics...

### /api/ee/audit-app/user (0/2 complete)

- [ ] `GET /api/ee/audit-app/user/audit-info` — `get-api-ee-audit-app-user-audit-info` — Gets audit info for the current user if he has permissions to access the audit collection. Otherwise return an empty map.
- [ ] `DELETE /api/ee/audit-app/user/{id}/subscriptions` — `delete-api-ee-audit-app-user-id-subscriptions` — Delete all Alert and DashboardSubscription subscriptions for a User (i.e., so they will no longer receive them). Archive all Alerts and DashboardSubscription...

### /api/ee/billing (0/1 complete)

- [ ] `GET /api/ee/billing` — `get-api-ee-billing` — Get billing information. This acts as a proxy between `metabase-billing-info-url` and the client, using the embedding token and signed in user's email to fet...

### /api/ee/cloud-add-ons (0/4 complete)

- [ ] `GET /api/ee/cloud-add-ons/addons` — `get-api-ee-cloud-add-ons-addons` — Get addons information from the Metabase Store API.
- [ ] `GET /api/ee/cloud-add-ons/plans` — `get-api-ee-cloud-add-ons-plans` — Get plans information from the Metabase Store API.
- [ ] `POST /api/ee/cloud-add-ons/{product-type}` — `post-api-ee-cloud-add-ons-product-type` — Purchase an add-on.
- [ ] `DELETE /api/ee/cloud-add-ons/{product-type}` — `delete-api-ee-cloud-add-ons-product-type` — Remove an add-on.

### /api/ee/cloud-proxy (0/1 complete)

- [ ] `POST /api/ee/cloud-proxy/{operation-id}` — `post-api-ee-cloud-proxy-operation-id` — Proxy a call to the Metabase Store API via harbormaster client. This endpoint is used only for hosted instances, and calls Harbormaster Store using a OpenAPI...

### /api/ee/content-translation (0/4 complete)

- [ ] `GET /api/ee/content-translation/csv` — `get-api-ee-content-translation-csv` — Provides content translation dictionary in CSV
- [ ] `GET /api/ee/content-translation/dictionary` — `get-api-ee-content-translation-dictionary` — Fetch the content translation dictionary for authenticated users (auth-based embedding flows).
- [ ] `GET /api/ee/content-translation/dictionary/{token}` — `get-api-ee-content-translation-dictionary-token` — Fetch the content translation dictionary via a JSON Web Token signed with the `embedding-secret-key`.
- [ ] `POST /api/ee/content-translation/upload-dictionary` — `post-api-ee-content-translation-upload-dictionary` — Upload a CSV of content translations

### /api/ee/data-complexity-score (0/1 complete)

- [ ] `GET /api/ee/data-complexity-score/complexity` — `get-api-ee-data-complexity-score-complexity` — Return the current Data Complexity Score for this instance. Superuser-only, expensive, and emits Snowplow events for benchmark consumers. Concurrent requests...

### /api/ee/data-studio/table (0/2 complete)

- [ ] `POST /api/ee/data-studio/table/publish-tables` — `post-api-ee-data-studio-table-publish-tables` — Set collection for each of selected tables and all upstream dependencies recursively.
- [ ] `POST /api/ee/data-studio/table/unpublish-tables` — `post-api-ee-data-studio-table-unpublish-tables` — Unset collection for each of selected tables and all downstream dependents recursively.

### /api/ee/database-replication (0/3 complete)

- [ ] `POST /api/ee/database-replication/connection/{database-id}` — `post-api-ee-database-replication-connection-database-id` — Create a new PG replication connection for the specified database.
- [ ] `DELETE /api/ee/database-replication/connection/{database-id}` — `delete-api-ee-database-replication-connection-database-id` — Delete PG replication connection for the specified database.
- [ ] `POST /api/ee/database-replication/connection/{database-id}/preview` — `post-api-ee-database-replication-connection-database-id-preview` — Return info about pg-replication connection that is about to be created.

### /api/ee/database-routing (0/2 complete)

- [ ] `POST /api/ee/database-routing/destination-database` — `post-api-ee-database-routing-destination-database` — Create new Destination Databases. Note that unlike the normal `POST /api/database` endpoint, does NOT check the details before adding the Database. This is O...
- [ ] `PUT /api/ee/database-routing/router-database/{id}` — `put-api-ee-database-routing-router-database-id` — Updates an existing Database with the `user_attribute` to route on. Will either: - turn an existing Database into a Router database - change the `user_attrib...

### /api/ee/dependencies (0/9 complete)

- [ ] `GET /api/ee/dependencies/backfill-status` — `get-api-ee-dependencies-backfill-status` — Returns whether the dependency backfill has pending work. `complete` is true when there are no stale or outdated entities awaiting processing.
- [ ] `POST /api/ee/dependencies/check-card` — `post-api-ee-dependencies-check-card` — Check a proposed edit to a card, and return the card IDs for those cards this edit will break.
- [ ] `POST /api/ee/dependencies/check-snippet` — `post-api-ee-dependencies-check-snippet` — Check a proposed edit to a native snippet, and return the cards, etc. which will be broken.
- [ ] `POST /api/ee/dependencies/check-transform` — `post-api-ee-dependencies-check-transform` — Check a proposed edit to a transform, and return the card, transform, etc. IDs for things that will break.
- [ ] `GET /api/ee/dependencies/graph` — `get-api-ee-dependencies-graph` — This endpoint takes an :id and a supported entity :type, and returns a graph of all its upstream dependencies. The graph is represented by a list of :nodes a...
- [ ] `GET /api/ee/dependencies/graph/breaking` — `get-api-ee-dependencies-graph-breaking` — Returns a list of entities that are breaking other entities (sources of errors). These are tables or cards that other entities depend on, where those depende...
- [ ] `GET /api/ee/dependencies/graph/broken` — `get-api-ee-dependencies-graph-broken` — Returns the broken dependents for a specific source entity. These are entities that have validation errors traced back to the specified source. Required para...
- [ ] `GET /api/ee/dependencies/graph/dependents` — `get-api-ee-dependencies-graph-dependents` — Returns a list of dependents for the specified entity. Required parameters: - `id`: The ID of the entity - `type`: The type of the entity (card, table, dashb...
- [ ] `GET /api/ee/dependencies/graph/unreferenced` — `get-api-ee-dependencies-graph-unreferenced` — Returns a list of all unreferenced items in the instance. An unreferenced item is one that is not a dependency of any other item. Accepts optional parameters...

### /api/ee/email (0/2 complete)

- [ ] `PUT /api/ee/email/override` — `put-api-ee-email-override` — Update multiple cloud email Settings. You must be a superuser or have `setting` permission to do this. Calling this automatically sets `cloud-smtp-enabled` t...
- [ ] `DELETE /api/ee/email/override` — `delete-api-ee-email-override` — Clear all cloud email related settings. You must be a superuser or have `setting` permission to do this.

### /api/ee/embedding-hub (0/1 complete)

- [ ] `GET /api/ee/embedding-hub/checklist` — `get-api-ee-embedding-hub-checklist` — Get the embedding hub checklist status, indicating which setup steps have been completed.

### /api/ee/gsheets (0/5 complete)

- [ ] `POST /api/ee/gsheets/connection` — `post-api-ee-gsheets-connection` — Hook up a new google drive folder or sheet that will be watched and have its content ETL'd into Metabase.
- [ ] `GET /api/ee/gsheets/connection` — `get-api-ee-gsheets-connection` — Check the status of a connection. This endpoint gets polled by FE to determine when to stop showing the setup widget. Returns the gsheets shape, with the att...
- [ ] `DELETE /api/ee/gsheets/connection` — `delete-api-ee-gsheets-connection` — Disconnect the google service account. There is only one (or zero) at the time of writing.
- [ ] `POST /api/ee/gsheets/connection/sync` — `post-api-ee-gsheets-connection-sync` — Force a sync of the connection now. Returns the gsheets shape, with the attached datawarehouse db id at `:db_id`.
- [ ] `GET /api/ee/gsheets/service-account` — `get-api-ee-gsheets-service-account` — Checks to see if service-account is setup or not, delegates to HM only if we haven't set it from a metabase cluster before.

### /api/ee/library (0/3 complete)

- [ ] `POST /api/ee/library` — `post-api-ee-library` — Creates the Library if it doesn't exist. Returns the created collection. Requires data analyst or superuser permissions.
- [ ] `GET /api/ee/library` — `get-api-ee-library` — Get the Library. If no library exists, it doesn't fail but returns an empty response
- [ ] `GET /api/ee/library/tree` — `get-api-ee-library-tree` — This matches /api/collection/tree but only returns the library collection.

### /api/ee/logs (0/1 complete)

- [ ] `GET /api/ee/logs/query_execution/{yyyy-mm}` — `get-api-ee-logs-query_execution-yyyy-mm` — Fetch rows for the month specified by `:yyyy-mm` from the query_execution logs table. Must be a superuser.

### /api/ee/metabot (0/1 complete)

- [ ] `GET /api/ee/metabot/usage` — `get-api-ee-metabot-usage` — Fetch current Metabot token usage for the current billing period.

### /api/ee/permission_debug (0/1 complete)

- [ ] `GET /api/ee/permission_debug` — `get-api-ee-permission_debug` — This endpoint expects a `user_id`, a `model_id` to debug permissions against, and `action_type`. The type of model we are debugging against is inferred by th...

### /api/ee/remote-sync (0/11 complete)

- [ ] `GET /api/ee/remote-sync/branches` — `get-api-ee-remote-sync-branches` — Get list of branches from the configured source. Returns a JSON object with branch names under the :items key. Requires superuser permissions.
- [ ] `POST /api/ee/remote-sync/create-branch` — `post-api-ee-remote-sync-create-branch` — Create a new branch from the current remote-sync branch and switches the current remote-sync branch to it. Requires superuser permissions.
- [ ] `GET /api/ee/remote-sync/current-task` — `get-api-ee-remote-sync-current-task` — Get the current sync task
- [ ] `POST /api/ee/remote-sync/current-task/cancel` — `post-api-ee-remote-sync-current-task-cancel` — Cancels the current task if one is running
- [ ] `GET /api/ee/remote-sync/dirty` — `get-api-ee-remote-sync-dirty` — Return all models with changes that have not been pushed to the remote sync source in any remote-synced collection.
- [ ] `POST /api/ee/remote-sync/export` — `post-api-ee-remote-sync-export` — Export the current state of the Remote Sync collection to a Source. This endpoint will: - Fetch the latest changes from the source - Create a branch or subdi...
- [ ] `GET /api/ee/remote-sync/has-remote-changes` — `get-api-ee-remote-sync-has-remote-changes` — Check if there are new changes on the remote branch that can be pulled. Uses in-memory caching (configurable TTL via remote-sync-check-changes-cache-ttl-seco...
- [ ] `POST /api/ee/remote-sync/import` — `post-api-ee-remote-sync-import` — Import Metabase content from configured Remote Sync source. This endpoint will: - Fetch the latest changes from the configured source - Load the updated cont...
- [ ] `GET /api/ee/remote-sync/is-dirty` — `get-api-ee-remote-sync-is-dirty` — Check if any remote-synced collection or collection item has local changes that have not been pushed to the remote sync source.
- [ ] `PUT /api/ee/remote-sync/settings` — `put-api-ee-remote-sync-settings` — Update Remote Sync related settings. You must be a superuser to do this.
- [ ] `POST /api/ee/remote-sync/stash` — `post-api-ee-remote-sync-stash` — Stashes changes to a new branch, and changes the current branch to it. Requires superuser permissions.

### /api/ee/replacement (0/6 complete)

- [ ] `POST /api/ee/replacement/check-replace-source` — `post-api-ee-replacement-check-replace-source` — Check whether a source entity can be replaced by a target entity. Returns compatibility errors describing column mismatches, type mismatches, primary key mis...
- [ ] `POST /api/ee/replacement/replace-model-with-transform` — `post-api-ee-replacement-replace-model-with-transform` — Create a transform from a model, execute it, and replace all usages of the model with the output table. Un-persists the model and converts it to a saved ques...
- [ ] `POST /api/ee/replacement/replace-source` — `post-api-ee-replacement-replace-source` — Replace all usages of a source entity with a target entity asynchronously. Returns 202 with a run_id for polling. Returns 409 if a replacement is already run...
- [ ] `GET /api/ee/replacement/runs` — `get-api-ee-replacement-runs` — List replacement runs, optionally filtered by is-active.
- [ ] `GET /api/ee/replacement/runs/{id}` — `get-api-ee-replacement-runs-id` — Get the status of a source replacement run.
- [ ] `POST /api/ee/replacement/runs/{id}/cancel` — `post-api-ee-replacement-runs-id-cancel` — Cancel a running source replacement.

### /api/ee/scim (0/2 complete)

- [ ] `GET /api/ee/scim/api_key` — `get-api-ee-scim-api_key` — Fetch the SCIM API key if one exists. Does *not* return an unmasked key, since we don't have access to that after it is created.
- [ ] `POST /api/ee/scim/api_key` — `post-api-ee-scim-api_key` — Create a new SCIM API key, or refresh one that already exists. When called for the first time, this is equivalent to enabling SCIM.

### /api/ee/scim/v2 (0/10 complete)

- [ ] `GET /api/ee/scim/v2/Groups` — `get-api-ee-scim-v2-Groups` — Fetch a list of groups.
- [ ] `POST /api/ee/scim/v2/Groups` — `post-api-ee-scim-v2-Groups` — Create a single group, and populates it if necessary.
- [ ] `GET /api/ee/scim/v2/Groups/{id}` — `get-api-ee-scim-v2-Groups-id` — Fetch a single group.
- [ ] `PUT /api/ee/scim/v2/Groups/{id}` — `put-api-ee-scim-v2-Groups-id` — Update a group.
- [ ] `DELETE /api/ee/scim/v2/Groups/{id}` — `delete-api-ee-scim-v2-Groups-id` — Delete a group.
- [ ] `GET /api/ee/scim/v2/Users` — `get-api-ee-scim-v2-Users` — Fetch a list of users.
- [ ] `POST /api/ee/scim/v2/Users` — `post-api-ee-scim-v2-Users` — Create a single user.
- [ ] `GET /api/ee/scim/v2/Users/{id}` — `get-api-ee-scim-v2-Users-id` — Fetch a single user.
- [ ] `PUT /api/ee/scim/v2/Users/{id}` — `put-api-ee-scim-v2-Users-id` — Update a user.
- [ ] `PATCH /api/ee/scim/v2/Users/{id}` — `patch-api-ee-scim-v2-Users-id` — Activate or deactivate a user. Supports specific replace operations, but not arbitrary patches.

### /api/ee/security-center (0/5 complete)

- [ ] `GET /api/ee/security-center` — `get-api-ee-security-center` — List all security advisories with match status.
- [ ] `POST /api/ee/security-center/acknowledge` — `post-api-ee-security-center-acknowledge` — Acknowledge multiple security advisories. Skips already-acknowledged advisories.
- [ ] `POST /api/ee/security-center/sync` — `post-api-ee-security-center-sync` — Trigger an async advisory sync + re-evaluation. Returns immediately. If a sync is already running, the request is a no-op.
- [ ] `POST /api/ee/security-center/test-notification` — `post-api-ee-security-center-test-notification` — Send a test notification through the configured Security Center channels.
- [ ] `POST /api/ee/security-center/{advisory-id}/acknowledge` — `post-api-ee-security-center-advisory-id-acknowledge` — Acknowledge a security advisory. Stops repeat notifications.

### /api/ee/semantic-search (0/1 complete)

- [ ] `GET /api/ee/semantic-search/status` — `get-api-ee-semantic-search-status` — Fetch the indexing status of the currently active semantic search index table. Returns a map with keys: :indexed_count <number of indexed items> :total_est <...

### /api/ee/serialization (0/2 complete)

- [ ] `POST /api/ee/serialization/export` — `post-api-ee-serialization-export` — Serialize and retrieve Metabase instance. Outputs `.tar.gz` file with serialization results and an `export.log` file. On error outputs serialization logs dir...
- [ ] `POST /api/ee/serialization/import` — `post-api-ee-serialization-import` — Deserialize Metabase instance from an archive generated by /export. Parameters: - `file`: archive encoded as `multipart/form-data` (required). Returns logs o...

### /api/ee/stale (0/1 complete)

- [ ] `GET /api/ee/stale/{id}` — `get-api-ee-stale-id` — A flexible endpoint that returns stale entities, in the same shape as collections/items, with the following options: - `before_date` - only return entities t...

### /api/ee/support-access-grant (0/4 complete)

- [ ] `POST /api/ee/support-access-grant` — `post-api-ee-support-access-grant` — Create a new support access grant. Requires superuser permissions. Only one active grant can exist at a time.
- [ ] `GET /api/ee/support-access-grant` — `get-api-ee-support-access-grant` — List support access grants with optional filtering and pagination. Requires superuser permissions. Query parameters: - ticket-number: Filter by ticket number...
- [ ] `GET /api/ee/support-access-grant/current` — `get-api-ee-support-access-grant-current` — Get the currently active support access grant, if one exists. Requires superuser permissions.
- [ ] `PUT /api/ee/support-access-grant/{id}/revoke` — `put-api-ee-support-access-grant-id-revoke` — Revoke an existing support access grant. Requires superuser permissions. Any admin can revoke any grant.

### /api/ee/tenant (0/4 complete)

- [ ] `POST /api/ee/tenant` — `post-api-ee-tenant` — Create a new Tenant
- [ ] `GET /api/ee/tenant` — `get-api-ee-tenant` — Get all tenants
- [ ] `PUT /api/ee/tenant/{id}` — `put-api-ee-tenant-id` — Update a tenant, can set name, attributes, or whether this tenant is active.
- [ ] `GET /api/ee/tenant/{id}` — `get-api-ee-tenant-id` — Get info about a tenant

### /api/ee/transforms (0/3 complete)

- [ ] `GET /api/ee/transforms/{id}/inspect` — `get-api-ee-transforms-id-inspect` — Phase 1: Discover available lenses for a transform. Returns structural metadata and available lens types.
- [ ] `GET /api/ee/transforms/{id}/inspect/{lens-id}` — `get-api-ee-transforms-id-inspect-lens-id` — Phase 2: Get full lens contents for a transform. Returns sections, cards with dataset_query, and trigger definitions. Accepts optional params for drill lense...
- [ ] `POST /api/ee/transforms/{id}/inspect/{lens-id}/query` — `post-api-ee-transforms-id-inspect-lens-id-query` — Execute a query in the context of a transform inspector lens.

### /api/ee/transforms-python (0/3 complete)

- [ ] `GET /api/ee/transforms-python/library/{path}` — `get-api-ee-transforms-python-library-path` — Get the Python library for user modules.
- [ ] `PUT /api/ee/transforms-python/library/{path}` — `put-api-ee-transforms-python-library-path` — Update the Python library source code for user modules.
- [ ] `POST /api/ee/transforms-python/test-run` — `post-api-ee-transforms-python-test-run` — Evaluate an ad-hoc python transform on a sample of input data. Intended for short runs for early feedback. Input/output/timeout limits apply.

### /api/ee/upload-management (0/2 complete)

- [ ] `GET /api/ee/upload-management/tables` — `get-api-ee-upload-management-tables` — Get all `Tables` visible to the current user which were created by uploading a file.
- [ ] `DELETE /api/ee/upload-management/tables/{id}` — `delete-api-ee-upload-management-tables-id` — Delete the uploaded table from the database, optionally archiving cards for which it is the primary source.

### /api/eid-translation (0/1 complete)

- [ ] `POST /api/eid-translation/translate` — `post-api-eid-translation-translate` — Translate entity IDs to model IDs.

### /api/email (0/3 complete)

- [ ] `PUT /api/email` — `put-api-email` — Update multiple email Settings. You must be a superuser or have `setting` permission to do this.
- [ ] `DELETE /api/email` — `delete-api-email` — Clear all email related settings. You must be a superuser or have `setting` permission to do this.
- [ ] `POST /api/email/test` — `post-api-email-test` — Send a test email using the SMTP Settings. You must be a superuser or have `setting` permission to do this. Returns `{:ok true}` if we were able to send the...

### /api/embed (0/16 complete)

- [ ] `GET /api/embed/card/{token}` — `get-api-embed-card-token` — Fetch a Card via a JSON Web Token signed with the `embedding-secret-key`. Token should have the following format: {:resource {:question <card-id>}}
- [ ] `GET /api/embed/card/{token}/params/{param-key}/remapping` — `get-api-embed-card-token-params-param-key-remapping` — Embedded version of api.card filter values endpoint.
- [ ] `GET /api/embed/card/{token}/params/{param-key}/search/{prefix}` — `get-api-embed-card-token-params-param-key-search-prefix` — Embedded version of chain filter search endpoint.
- [ ] `GET /api/embed/card/{token}/params/{param-key}/values` — `get-api-embed-card-token-params-param-key-values` — Embedded version of api.card filter values endpoint.
- [ ] `GET /api/embed/card/{token}/query` — `get-api-embed-card-token-query` — Fetch the results of running a Card using a JSON Web Token signed with the `embedding-secret-key`. Token should have the following format: {:resource {:quest...
- [ ] `GET /api/embed/card/{token}/query/{export-format}` — `get-api-embed-card-token-query-export-format` — Like `GET /api/embed/card/query`, but returns the results as a file in the specified format.
- [ ] `GET /api/embed/dashboard/{token}` — `get-api-embed-dashboard-token` — Fetch a Dashboard via a JSON Web Token signed with the `embedding-secret-key`. Token should have the following format: {:resource {:dashboard <dashboard-id>}}
- [ ] `GET /api/embed/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-embed-dashboard-token-dashcard-dashcard-id-card-card-id` — Fetch the results of running a Card belonging to a Dashboard using a JSON Web Token signed with the `embedding-secret-key`
- [ ] `GET /api/embed/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}/{export-format}` — `get-api-embed-dashboard-token-dashcard-dashcard-id-card-card-id-export-format` — Fetch the results of running a Card belonging to a Dashboard using a JSON Web Token signed with the `embedding-secret-key` return the data in one of the expo...
- [ ] `GET /api/embed/dashboard/{token}/params/{param-key}/remapping` — `get-api-embed-dashboard-token-params-param-key-remapping` — Embedded version of the remapped dashboard param value endpoint.
- [ ] `GET /api/embed/dashboard/{token}/params/{param-key}/search/{prefix}` — `get-api-embed-dashboard-token-params-param-key-search-prefix` — Embedded version of chain filter search endpoint.
- [ ] `GET /api/embed/dashboard/{token}/params/{param-key}/values` — `get-api-embed-dashboard-token-params-param-key-values` — Embedded version of chain filter values endpoint.
- [ ] `GET /api/embed/pivot/card/{token}/query` — `get-api-embed-pivot-card-token-query` — Fetch the results of running a Card using a JSON Web Token signed with the `embedding-secret-key`. Token should have the following format: {:resource {:quest...
- [ ] `GET /api/embed/pivot/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-embed-pivot-dashboard-token-dashcard-dashcard-id-card-card-id` — Fetch the results of running a Card belonging to a Dashboard using a JSON Web Token signed with the `embedding-secret-key`
- [ ] `GET /api/embed/tiles/card/{token}/{zoom}/{x}/{y}` — `get-api-embed-tiles-card-token-zoom-x-y` — Generates a single tile image for an embedded Card using the map visualization.
- [ ] `GET /api/embed/tiles/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}/{zoom}/{x}/{y}` — `get-api-embed-tiles-dashboard-token-dashcard-dashcard-id-card-card-id-zoom-x-y` — Generates a single tile image for a Card on an embedded Dashboard using the map visualization.

### /api/embed-theme (0/7 complete)

- [ ] `GET /api/embed-theme` — `get-api-embed-theme` — Fetch a list of all embedding themes.
- [ ] `POST /api/embed-theme` — `post-api-embed-theme` — Create a new embedding theme.
- [ ] `POST /api/embed-theme/seed-defaults` — `post-api-embed-theme-seed-defaults` — Seed default embedding themes on first call, using the payloads built by the frontend from the `METABASE_LIGHT_THEME` / `METABASE_DARK_THEME` constants. Idem...
- [ ] `GET /api/embed-theme/{id}` — `get-api-embed-theme-id` — Fetch a single embedding theme by ID.
- [ ] `PUT /api/embed-theme/{id}` — `put-api-embed-theme-id` — Update an embedding theme.
- [ ] `DELETE /api/embed-theme/{id}` — `delete-api-embed-theme-id` — Delete an embedding theme.
- [ ] `POST /api/embed-theme/{id}/copy` — `post-api-embed-theme-id-copy` — Copy an embedding theme.

### /api/field (1/12 complete)

- [x] `GET /api/field/{id}` — `get-api-field-id` — Get `Field` with ID.
- [ ] `PUT /api/field/{id}` — `put-api-field-id` — Update `Field` with ID.
- [ ] `POST /api/field/{id}/dimension` — `post-api-field-id-dimension` — Sets the dimension for the given field at ID
- [ ] `DELETE /api/field/{id}/dimension` — `delete-api-field-id-dimension` — Remove the dimension associated to field at ID
- [ ] `POST /api/field/{id}/discard_values` — `post-api-field-id-discard_values` — Discard the FieldValues belonging to this Field. Only applies to fields that have FieldValues. If this Field's Database is set up to automatically sync Field...
- [ ] `GET /api/field/{id}/related` — `get-api-field-id-related` — Return related entities.
- [ ] `GET /api/field/{id}/remapping/{remapped-id}` — `get-api-field-id-remapping-remapped-id` — Fetch remapped Field values.
- [ ] `POST /api/field/{id}/rescan_values` — `post-api-field-id-rescan_values` — Manually trigger an update for the FieldValues for this Field. Only applies to Fields that are eligible for FieldValues.
- [ ] `GET /api/field/{id}/search/{search-id}` — `get-api-field-id-search-search-id` — Search for values of a Field with `search-id` that start with `value`. See docstring for [[metabase.parameters.field/search-values]] for a more detailed expl...
- [ ] `GET /api/field/{id}/summary` — `get-api-field-id-summary` — Get the count and distinct count of `Field` with ID.
- [ ] `GET /api/field/{id}/values` — `get-api-field-id-values` — If a Field's value of `has_field_values` is `:list`, return a list of all the distinct values of the Field (or remapped Field), and (if defined by a User) a...
- [ ] `POST /api/field/{id}/values` — `post-api-field-id-values` — Update the fields values and human-readable values for a `Field` whose semantic type is `category`/`city`/`state`/`country` or whose base type is `type/Boole...

### /api/frontend-errors (0/1 complete)

- [ ] `POST /api/frontend-errors` — `post-api-frontend-errors` — Endpoint for the frontend to report errors. Increments a Prometheus counter with the given `type` label.

### /api/geojson (0/2 complete)

- [ ] `GET /api/geojson` — `get-api-geojson` — Load a custom GeoJSON file based on a URL or file path provided as a query parameter. This behaves similarly to /api/geojson/:key but doesn't require the cus...
- [ ] `GET /api/geojson/{key}` — `get-api-geojson-key` — Fetch a custom GeoJSON file as defined in the [[metabase.geojson.settings/custom-geojson]] setting. (This just acts as a simple proxy for the file specified...

### /api/glossary (0/4 complete)

- [ ] `GET /api/glossary` — `get-api-glossary` — Fetch all glossary entries, optionally filtered by search term.
- [ ] `POST /api/glossary` — `post-api-glossary` — Create a new glossary entry.
- [ ] `PUT /api/glossary/{id}` — `put-api-glossary-id` — Update an existing glossary entry.
- [ ] `DELETE /api/glossary/{id}` — `delete-api-glossary-id` — Delete a glossary entry.

### /api/google (0/1 complete)

- [ ] `PUT /api/google/settings` — `put-api-google-settings` — Update Google Sign-In related settings. You must be a superuser to do this.

### /api/ldap (0/1 complete)

- [ ] `PUT /api/ldap/settings` — `put-api-ldap-settings` — Update LDAP related settings. You must be a superuser to do this.

### /api/llm (0/3 complete)

- [ ] `POST /api/llm/extract-tables` — `post-api-llm-extract-tables` — Parse SQL and return referenced tables with their columns. Uses Macaw to parse the SQL, resolves table names to IDs, and returns permission-filtered tables w...
- [ ] `POST /api/llm/generate-sql` — `post-api-llm-generate-sql` — Generate SQL from a natural language prompt. Requires: - LLM to be configured (Anthropic API key set in admin settings) - At least one table reference (expli...
- [ ] `GET /api/llm/list-models` — `get-api-llm-list-models` — List available LLM models from the configured provider. Requires LLM to be configured for the selected provider in admin settings.

### /api/logger (0/4 complete)

- [ ] `POST /api/logger/adjustment` — `post-api-logger-adjustment` — Temporarily adjust the log levels.
- [ ] `DELETE /api/logger/adjustment` — `delete-api-logger-adjustment` — Undo any log level adjustments.
- [ ] `GET /api/logger/logs` — `get-api-logger-logs` — Logs.
- [ ] `GET /api/logger/presets` — `get-api-logger-presets` — Get all known presets.

### /api/login-history (0/1 complete)

- [ ] `GET /api/login-history/current` — `get-api-login-history-current` — Fetch recent logins for the current user.

### /api/measure (0/7 complete)

- [ ] `POST /api/measure` — `post-api-measure` — Create a new `Measure`.
- [ ] `GET /api/measure` — `get-api-measure` — Fetch *all* `Measures`.
- [ ] `GET /api/measure/{id}` — `get-api-measure-id` — Fetch `Measure` with ID.
- [ ] `PUT /api/measure/{id}` — `put-api-measure-id` — Update a `Measure` with ID.
- [ ] `GET /api/measure/{id}/dimension/{dimension-key}/remapping` — `get-api-measure-id-dimension-dimension-key-remapping` — Fetch remapped value for a specific dimension value. Returns a pair [value, display-name] if remapping exists, or [value] otherwise.
- [ ] `GET /api/measure/{id}/dimension/{dimension-key}/search` — `get-api-measure-id-dimension-dimension-key-search` — Search for values of a dimension that contain the query string. Returns field values matching the search query in the same format as the field values API.
- [ ] `GET /api/measure/{id}/dimension/{dimension-key}/values` — `get-api-measure-id-dimension-dimension-key-values` — Fetch values for a dimension of a measure. Returns field values in the same format as the field values API: - values: list of [value] or [value, display-name...

### /api/metabot (0/4 complete)

- [ ] `POST /api/metabot/agent-streaming` — `post-api-metabot-agent-streaming` — Send a chat message to the LLM via the AI Proxy.
- [ ] `POST /api/metabot/feedback` — `post-api-metabot-feedback` — Proxy Metabot feedback to Harbormaster, adding the premium embedding token.
- [ ] `GET /api/metabot/settings` — `get-api-metabot-settings` — Return available models for a provider using its configured API key.
- [ ] `PUT /api/metabot/settings` — `put-api-metabot-settings` — Update the Metabot provider API key and/or model setting and return the refreshed settings payload.

### /api/metabot/document (0/1 complete)

- [ ] `POST /api/metabot/document/generate-content` — `post-api-metabot-document-generate-content` — Create a new piece of content to insert into the document. Kept for backwards compatibility; now uses the native Clojure agent.

### /api/metabot/metabot (0/7 complete)

- [ ] `GET /api/metabot/metabot` — `get-api-metabot-metabot` — List configured metabot instances
- [ ] `GET /api/metabot/metabot/{id}` — `get-api-metabot-metabot-id` — Retrieve one metabot instance
- [ ] `PUT /api/metabot/metabot/{id}` — `put-api-metabot-metabot-id` — Update a metabot instance
- [ ] `GET /api/metabot/metabot/{id}/prompt-suggestions` — `get-api-metabot-metabot-id-prompt-suggestions` — Return the prompt suggestions for the metabot instance with `id`.
- [ ] `DELETE /api/metabot/metabot/{id}/prompt-suggestions` — `delete-api-metabot-metabot-id-prompt-suggestions` — Delete all prompt suggestions for the metabot instance with `id`.
- [ ] `POST /api/metabot/metabot/{id}/prompt-suggestions/regenerate` — `post-api-metabot-metabot-id-prompt-suggestions-regenerate` — Remove any existing prompt suggestions for the Metabot instance with `id` and generate new ones.
- [ ] `DELETE /api/metabot/metabot/{id}/prompt-suggestions/{prompt-id}` — `delete-api-metabot-metabot-id-prompt-suggestions-prompt-id` — Delete the prompt suggestion with ID `prompt-id` for the metabot instance with `id`.

### /api/metabot/permissions (0/1 complete)

- [ ] `GET /api/metabot/permissions/user-permissions` — `get-api-metabot-permissions-user-permissions` — Return the current user's resolved metabot permissions, taking the most permissive value across all their groups.

### /api/metabot/slack (0/3 complete)

- [ ] `POST /api/metabot/slack/events` — `post-api-metabot-slack-events` — Respond to activities in Slack
- [ ] `POST /api/metabot/slack/interactive` — `post-api-metabot-slack-interactive` — Handle interactive payloads from Slack (button clicks, modal submissions).
- [ ] `PUT /api/metabot/slack/settings` — `put-api-metabot-slack-settings` — Update Metabot Slack settings atomically. All credential fields must be provided together. Setting values requires the metabot-v3 feature, but clearing value...

### /api/metric (0/7 complete)

- [ ] `GET /api/metric` — `get-api-metric` — Get a list of metrics. Returns metrics (Cards with type='metric') that the current user has read access to, filtered by collection visibility permissions.
- [ ] `POST /api/metric/breakout-values` — `post-api-metric-breakout-values` — Fetch distinct breakout dimension values for a metric or measure definition. Accepts the same definition format as POST /dataset. Returns extracted values an...
- [ ] `POST /api/metric/dataset` — `post-api-metric-dataset` — Execute a metric or measure-based query and stream the results. Request body requires a `definition` object containing: - expression: A metric math expressio...
- [ ] `GET /api/metric/{id}` — `get-api-metric-id` — Fetch a `Metric` with ID. Returns the metric with hydrated dimensions and dimension mappings.
- [ ] `GET /api/metric/{id}/dimension/{dimension-key}/remapping` — `get-api-metric-id-dimension-dimension-key-remapping` — Fetch remapped value for a specific dimension value. Returns a pair [value, display-name] if remapping exists, or [value] otherwise.
- [ ] `GET /api/metric/{id}/dimension/{dimension-key}/search` — `get-api-metric-id-dimension-dimension-key-search` — Search for values of a dimension that contain the query string. Returns field values matching the search query in the same format as the field values API.
- [ ] `GET /api/metric/{id}/dimension/{dimension-key}/values` — `get-api-metric-id-dimension-dimension-key-values` — Fetch values for a dimension of a metric. Returns field values in the same format as the field values API: - values: list of [value] or [value, display-name]...

### /api/model-index (0/4 complete)

- [ ] `POST /api/model-index` — `post-api-model-index` — Create ModelIndex.
- [ ] `GET /api/model-index` — `get-api-model-index` — Retrieve list of ModelIndex.
- [ ] `GET /api/model-index/{id}` — `get-api-model-index-id` — Retrieve ModelIndex.
- [ ] `DELETE /api/model-index/{id}` — `delete-api-model-index-id` — Delete ModelIndex.

### /api/moderation-review (0/1 complete)

- [ ] `POST /api/moderation-review` — `post-api-moderation-review` — Create a new `ModerationReview`.

### /api/mt/gtap (0/6 complete)

- [ ] `GET /api/mt/gtap` — `get-api-mt-gtap` — Fetch a list of all GTAPs currently in use, or a single GTAP if both `group_id` and `table_id` are provided.
- [ ] `POST /api/mt/gtap` — `post-api-mt-gtap` — Create a new GTAP.
- [ ] `POST /api/mt/gtap/validate` — `post-api-mt-gtap-validate` — Validate a sandbox which may not have yet been saved. This runs the same validation that is performed when the sandbox is saved, but doesn't actually save th...
- [ ] `GET /api/mt/gtap/{id}` — `get-api-mt-gtap-id` — Fetch GTAP by `id`
- [ ] `PUT /api/mt/gtap/{id}` — `put-api-mt-gtap-id` — Update a GTAP entry. The only things you're allowed to update for a GTAP are the Card being used (`card_id`) or the parameter mappings; changing `table_id` o...
- [ ] `DELETE /api/mt/gtap/{id}` — `delete-api-mt-gtap-id` — Delete a GTAP entry.

### /api/mt/user (0/2 complete)

- [ ] `GET /api/mt/user/attributes` — `get-api-mt-user-attributes` — Fetch a list of possible keys for User `login_attributes`. This includes keys from tenant model attributes and keys that have already been set for existing U...
- [ ] `PUT /api/mt/user/{id}/attributes` — `put-api-mt-user-id-attributes` — Update the `login_attributes` for a User.

### /api/native-query-snippet (0/4 complete)

- [ ] `GET /api/native-query-snippet` — `get-api-native-query-snippet` — Fetch all snippets
- [ ] `POST /api/native-query-snippet` — `post-api-native-query-snippet` — Create a new `NativeQuerySnippet`.
- [ ] `GET /api/native-query-snippet/{id}` — `get-api-native-query-snippet-id` — Fetch native query snippet with ID.
- [ ] `PUT /api/native-query-snippet/{id}` — `put-api-native-query-snippet-id` — Update an existing `NativeQuerySnippet`.

### /api/notification (0/7 complete)

- [ ] `GET /api/notification` — `get-api-notification` — List notifications. - `creator_id`: if provided returns only notifications created by this user - `recipient_id`: if provided returns only notification that...
- [ ] `POST /api/notification` — `post-api-notification` — Create a new notification, return the created notification.
- [ ] `POST /api/notification/send` — `post-api-notification-send` — Send an unsaved notification.
- [ ] `GET /api/notification/{id}` — `get-api-notification-id` — Get a notification by id.
- [ ] `PUT /api/notification/{id}` — `put-api-notification-id` — Update a notification, can also update its subscriptions, handlers. Return the updated notification.
- [ ] `POST /api/notification/{id}/send` — `post-api-notification-id-send` — Send a notification by id.
- [ ] `POST /api/notification/{id}/unsubscribe` — `post-api-notification-id-unsubscribe` — Unsubscribe current user from a notification.

### /api/notification/unsubscribe (0/2 complete)

- [ ] `POST /api/notification/unsubscribe` — `post-api-notification-unsubscribe` — Allow non-users to unsubscribe from notifications, with the hash given through email.
- [ ] `POST /api/notification/unsubscribe/undo` — `post-api-notification-unsubscribe-undo` — Allow non-users to undo an unsubscribe from notifications, with the hash given through email.

### /api/notify (0/3 complete)

- [ ] `POST /api/notify/db/attached_datawarehouse` — `post-api-notify-db-attached_datawarehouse` — Sync the attached datawarehouse. Can provide in the body: - table_name and schema_name: both strings. Will look for an existing table and sync it, otherwise...
- [ ] `POST /api/notify/db/{id}` — `post-api-notify-db-id` — Notification about a potential schema change to one of our `Databases`. Caller can optionally specify a `:table_id` or `:table_name` in the body to limit upd...
- [ ] `POST /api/notify/db/{id}/new-table` — `post-api-notify-db-id-new-table` — Sync a new table without running a full database sync. Requires `schema_name` and `table_name`. Will throw an error if the table already exists in Metabase o...

### /api/permissions (0/14 complete)

- [ ] `GET /api/permissions/graph` — `get-api-permissions-graph` — Fetch a graph of all Permissions.
- [ ] `PUT /api/permissions/graph` — `put-api-permissions-graph` — Do a batch update of Permissions by passing in a modified graph. This should return the same graph, in the same format, that you got from `GET /api/permissio...
- [ ] `GET /api/permissions/graph/db/{db-id}` — `get-api-permissions-graph-db-db-id` — Fetch a graph of all Permissions for db-id `db-id`.
- [ ] `GET /api/permissions/graph/group/{group-id}` — `get-api-permissions-graph-group-group-id` — Fetch a graph of all Permissions for group-id `group-id`.
- [ ] `GET /api/permissions/group` — `get-api-permissions-group` — Fetch all `PermissionsGroups`, including a count of the number of `:members` in that group. This API requires superuser or group manager of more than one gro...
- [ ] `POST /api/permissions/group` — `post-api-permissions-group` — Create a new `PermissionsGroup`.
- [ ] `PUT /api/permissions/group/{group-id}` — `put-api-permissions-group-group-id` — Update the name of a `PermissionsGroup`.
- [ ] `DELETE /api/permissions/group/{group-id}` — `delete-api-permissions-group-group-id` — Delete a specific `PermissionsGroup`.
- [ ] `GET /api/permissions/group/{id}` — `get-api-permissions-group-id` — Fetch the details for a certain permissions group.
- [ ] `GET /api/permissions/membership` — `get-api-permissions-membership` — Fetch a map describing the group memberships of various users. This map's format is: {<user-id> [{:membership_id <id> :group_id <id> :is_group_manager boolea...
- [ ] `POST /api/permissions/membership` — `post-api-permissions-membership` — Add a `User` to a `PermissionsGroup`. Returns updated list of members belonging to the group.
- [ ] `PUT /api/permissions/membership/{group-id}/clear` — `put-api-permissions-membership-group-id-clear` — Remove all members from a `PermissionsGroup`. Returns a 400 (Bad Request) if the group ID is for the admin group.
- [ ] `PUT /api/permissions/membership/{id}` — `put-api-permissions-membership-id` — Update a Permission Group membership. Returns the updated record.
- [ ] `DELETE /api/permissions/membership/{id}` — `delete-api-permissions-membership-id` — Remove a User from a PermissionsGroup (delete their membership).

### /api/persist (0/11 complete)

- [ ] `GET /api/persist` — `get-api-persist` — List the entries of [[PersistedInfo]] in order to show a status page.
- [ ] `GET /api/persist/card/{card-id}` — `get-api-persist-card-card-id` — Fetch a particular [[PersistedInfo]] by card-id.
- [ ] `POST /api/persist/card/{card-id}/persist` — `post-api-persist-card-card-id-persist` — Mark the model (card) as persisted. Runs the query and saves it to the database backing the card and hot swaps this query in place of the model's query.
- [ ] `POST /api/persist/card/{card-id}/refresh` — `post-api-persist-card-card-id-refresh` — Refresh the persisted model caching `card-id`.
- [ ] `POST /api/persist/card/{card-id}/unpersist` — `post-api-persist-card-card-id-unpersist` — Unpersist this model. Deletes the persisted table backing the model and all queries after this will use the card's query rather than the saved version of the...
- [ ] `POST /api/persist/database/{id}/persist` — `post-api-persist-database-id-persist` — Attempt to enable model persistence for a database. If already enabled returns a generic 204.
- [ ] `POST /api/persist/database/{id}/unpersist` — `post-api-persist-database-id-unpersist` — Attempt to disable model persistence for a database. If already not enabled, just returns a generic 204.
- [ ] `POST /api/persist/disable` — `post-api-persist-disable` — Disable global setting to allow databases to persist models. This will remove all tasks to refresh tables, remove that option from databases which might have...
- [ ] `POST /api/persist/enable` — `post-api-persist-enable` — Enable global setting to allow databases to persist models.
- [ ] `POST /api/persist/set-refresh-schedule` — `post-api-persist-set-refresh-schedule` — Set the cron schedule to refresh persisted models. Shape should be JSON like {cron: "0 30 1/8 * * ? *"}.
- [ ] `GET /api/persist/{persisted-info-id}` — `get-api-persist-persisted-info-id` — Fetch a particular [[PersistedInfo]] by id.

### /api/premium-features (0/2 complete)

- [ ] `POST /api/premium-features/token/refresh` — `post-api-premium-features-token-refresh` — Clear all token caches and re-check the premium features token against the MetaStore. Returns the fresh token status. Useful for the frontend after a purchas...
- [ ] `GET /api/premium-features/token/status` — `get-api-premium-features-token-status` — Fetch info about the current Premium-Features premium features token including whether it is `valid`, a `trial` token, its `features`, when it is `valid-thru...

### /api/preview_embed (0/13 complete)

- [ ] `GET /api/preview_embed/card/{token}` — `get-api-preview_embed-card-token` — Fetch a Card you're considering embedding by passing a JWT `token`.
- [ ] `GET /api/preview_embed/card/{token}/params/{param-key}/remapping` — `get-api-preview_embed-card-token-params-param-key-remapping` — Embedded version of api.card filter values endpoint.
- [ ] `GET /api/preview_embed/card/{token}/params/{param-key}/values` — `get-api-preview_embed-card-token-params-param-key-values` — Embedded version of api.card filter values endpoint.
- [ ] `GET /api/preview_embed/card/{token}/query` — `get-api-preview_embed-card-token-query` — Fetch the query results for a Card you're considering embedding by passing a JWT `token`.
- [ ] `GET /api/preview_embed/dashboard/{token}` — `get-api-preview_embed-dashboard-token` — Fetch a Dashboard you're considering embedding by passing a JWT `token`.
- [ ] `GET /api/preview_embed/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-preview_embed-dashboard-token-dashcard-dashcard-id-card-card-id` — Fetch the results of running a Card belonging to a Dashboard you're considering embedding with JWT `token`.
- [ ] `GET /api/preview_embed/dashboard/{token}/params/{param-key}/remapping` — `get-api-preview_embed-dashboard-token-params-param-key-remapping` — Embedded version of the remapped dashboard param value endpoint.
- [ ] `GET /api/preview_embed/dashboard/{token}/params/{param-key}/search/{prefix}` — `get-api-preview_embed-dashboard-token-params-param-key-search-prefix` — Embedded version of chain filter search endpoint.
- [ ] `GET /api/preview_embed/dashboard/{token}/params/{param-key}/values` — `get-api-preview_embed-dashboard-token-params-param-key-values` — Embedded version of chain filter values endpoint.
- [ ] `GET /api/preview_embed/pivot/card/{token}/query` — `get-api-preview_embed-pivot-card-token-query` — Fetch the query results for a Card you're considering embedding by passing a JWT `token`.
- [ ] `GET /api/preview_embed/pivot/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-preview_embed-pivot-dashboard-token-dashcard-dashcard-id-card-card-id` — Fetch the results of running a Card belonging to a Dashboard you're considering embedding with JWT `token`.
- [ ] `GET /api/preview_embed/tiles/card/{token}/{zoom}/{x}/{y}` — `get-api-preview_embed-tiles-card-token-zoom-x-y` — Generates a single tile image for an embedded Card using the map visualization.
- [ ] `GET /api/preview_embed/tiles/dashboard/{token}/dashcard/{dashcard-id}/card/{card-id}/{zoom}/{x}/{y}` — `get-api-preview_embed-tiles-dashboard-token-dashcard-dashcard-id-card-card-id-zoom-x-y` — Generates a single tile image for a Card on an embedded Dashboard using the map visualization.

### /api/product-feedback (0/1 complete)

- [ ] `POST /api/product-feedback` — `post-api-product-feedback` — Endpoint to provide feedback from the product

### /api/public (0/24 complete)

- [ ] `GET /api/public/action/{uuid}` — `get-api-public-action-uuid` — Fetch a publicly-accessible Action. Does not require auth credentials. Public sharing must be enabled.
- [ ] `POST /api/public/action/{uuid}/execute` — `post-api-public-action-uuid-execute` — Execute the Action. `parameters` should be the mapped dashboard parameters with values.
- [ ] `GET /api/public/card/{uuid}` — `get-api-public-card-uuid` — Fetch a publicly-accessible Card an return query results as well as `:card` information. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/card/{uuid}/params/{param-key}/remapping` — `get-api-public-card-uuid-params-param-key-remapping` — Fetch the remapped value for the given `value` of parameter with ID `:param-key` of card with UUID `uuid`.
- [ ] `GET /api/public/card/{uuid}/params/{param-key}/search/{query}` — `get-api-public-card-uuid-params-param-key-search-query` — Fetch values for a parameter on a public card containing `query`.
- [ ] `GET /api/public/card/{uuid}/params/{param-key}/values` — `get-api-public-card-uuid-params-param-key-values` — Fetch values for a parameter on a public card.
- [ ] `GET /api/public/card/{uuid}/query` — `get-api-public-card-uuid-query` — Fetch a publicly-accessible Card an return query results as well as `:card` information. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/card/{uuid}/query/{export-format}` — `get-api-public-card-uuid-query-export-format` — Fetch a publicly-accessible Card and return query results in the specified format. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/dashboard/{uuid}` — `get-api-public-dashboard-uuid` — Fetch a publicly-accessible Dashboard. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/dashboard/{uuid}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-public-dashboard-uuid-dashcard-dashcard-id-card-card-id` — Fetch the results for a Card in a publicly-accessible Dashboard. Does not require auth credentials. Public sharing must be enabled.
- [ ] `POST /api/public/dashboard/{uuid}/dashcard/{dashcard-id}/card/{card-id}/{export-format}` — `post-api-public-dashboard-uuid-dashcard-dashcard-id-card-card-id-export-format` — Fetch the results of running a publicly-accessible Card belonging to a Dashboard and return the data in one of the export formats. Does not require auth cred...
- [ ] `GET /api/public/dashboard/{uuid}/dashcard/{dashcard-id}/execute` — `get-api-public-dashboard-uuid-dashcard-dashcard-id-execute` — Fetches the values for filling in execution parameters. Pass PK parameters and values to select.
- [ ] `POST /api/public/dashboard/{uuid}/dashcard/{dashcard-id}/execute` — `post-api-public-dashboard-uuid-dashcard-dashcard-id-execute` — Execute the associated Action in the context of a `Dashboard` and `DashboardCard` that includes it. `parameters` should be the mapped dashboard parameters wi...
- [ ] `GET /api/public/dashboard/{uuid}/params/{param-key}/remapping` — `get-api-public-dashboard-uuid-params-param-key-remapping` — Fetch the remapped value for the given `value` of parameter with ID `:param-key` of dashboard with UUID `uuid`.
- [ ] `GET /api/public/dashboard/{uuid}/params/{param-key}/search/{query}` — `get-api-public-dashboard-uuid-params-param-key-search-query` — Fetch filter values for dashboard parameter `param-key`, containing specified `query`.
- [ ] `GET /api/public/dashboard/{uuid}/params/{param-key}/values` — `get-api-public-dashboard-uuid-params-param-key-values` — Fetch filter values for dashboard parameter `param-key`.
- [ ] `GET /api/public/document/{uuid}` — `get-api-public-document-uuid` — Fetch a publicly-accessible Document. Does not require auth credentials. Public sharing must be enabled. Returns a Document with sensitive fields removed (ex...
- [ ] `GET /api/public/document/{uuid}/card/{card-id}` — `get-api-public-document-uuid-card-card-id` — Run a query for a Card that's embedded in a public Document. Doesn't require auth credentials. Public sharing must be enabled.
- [ ] `POST /api/public/document/{uuid}/card/{card-id}/{export-format}` — `post-api-public-document-uuid-card-card-id-export-format` — Fetch a Card embedded in a public Document and return query results in the specified format. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/oembed` — `get-api-public-oembed` — oEmbed endpoint used to retrieve embed code and metadata for a (public) Metabase URL.
- [ ] `GET /api/public/pivot/card/{uuid}/query` — `get-api-public-pivot-card-uuid-query` — Fetch a publicly-accessible Card an return query results as well as `:card` information. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/pivot/dashboard/{uuid}/dashcard/{dashcard-id}/card/{card-id}` — `get-api-public-pivot-dashboard-uuid-dashcard-dashcard-id-card-card-id` — Fetch the results for a Card in a publicly-accessible Dashboard. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/tiles/card/{uuid}/{zoom}/{x}/{y}` — `get-api-public-tiles-card-uuid-zoom-x-y` — Generates a single tile image for a publicly-accessible Card using the map visualization. Does not require auth credentials. Public sharing must be enabled.
- [ ] `GET /api/public/tiles/dashboard/{uuid}/dashcard/{dashcard-id}/card/{card-id}/{zoom}/{x}/{y}` — `get-api-public-tiles-dashboard-uuid-dashcard-dashcard-id-card-card-id-zoom-x-y` — Generates a single tile image for a Card using the map visualization in a publicly-accessible Dashboard. Does not require auth credentials. Public sharing mu...

### /api/pulse (0/7 complete)

- [ ] `GET /api/pulse` — `get-api-pulse` — Fetch all dashboard subscriptions. By default, returns only subscriptions for which the current user has write permissions. For admins, this is all subscript...
- [ ] `POST /api/pulse` — `post-api-pulse` — Create a new `Pulse`.
- [ ] `GET /api/pulse/form_input` — `get-api-pulse-form_input` — Provides relevant configuration information and user choices for creating/updating Pulses.
- [ ] `POST /api/pulse/test` — `post-api-pulse-test` — Test send an unsaved pulse.
- [ ] `GET /api/pulse/{id}` — `get-api-pulse-id` — Fetch `Pulse` with ID. If the user is a recipient of the Pulse but does not have read permissions for its collection, we still return it but with some sensit...
- [ ] `PUT /api/pulse/{id}` — `put-api-pulse-id` — Update a Pulse with `id`.
- [ ] `DELETE /api/pulse/{id}/subscription` — `delete-api-pulse-id-subscription` — For users to unsubscribe themselves from a pulse subscription.

### /api/pulse/unsubscribe (0/2 complete)

- [ ] `POST /api/pulse/unsubscribe` — `post-api-pulse-unsubscribe` — Allow non-users to unsubscribe from pulses/subscriptions, with the hash given through email.
- [ ] `POST /api/pulse/unsubscribe/undo` — `post-api-pulse-unsubscribe-undo` — Allow non-users to undo an unsubscribe from pulses/subscriptions, with the hash given through email.

### /api/revision (0/3 complete)

- [ ] `GET /api/revision` — `get-api-revision` — Get revisions of an object.
- [ ] `POST /api/revision/revert` — `post-api-revision-revert` — Revert an object to a prior revision.
- [ ] `GET /api/revision/{entity}/{id}` — `get-api-revision-entity-id` — Fetch `Revisions` for an object with ID.

### /api/search (0/5 complete)

- [ ] `GET /api/search` — `get-api-search` — Search for items in Metabase. For the list of supported models, check [[metabase.search.config/all-models]]. Filters: - `archived`: set to true to search arc...
- [ ] `POST /api/search/force-reindex` — `post-api-search-force-reindex` — This will trigger an immediate reindexing, if we are using search index.
- [ ] `POST /api/search/re-init` — `post-api-search-re-init` — This will blow away any search indexes, re-create, and re-populate them.
- [ ] `GET /api/search/weights` — `get-api-search-weights` — Return the current weights being used to rank the search results
- [ ] `PUT /api/search/weights` — `put-api-search-weights` — Update the current weights being used to rank the search results

### /api/segment (0/6 complete)

- [ ] `POST /api/segment` — `post-api-segment` — Create a new `Segment`.
- [ ] `GET /api/segment` — `get-api-segment` — Fetch *all* `Segments`.
- [ ] `GET /api/segment/{id}` — `get-api-segment-id` — Fetch `Segment` with ID.
- [ ] `PUT /api/segment/{id}` — `put-api-segment-id` — Update a `Segment` with ID.
- [ ] `DELETE /api/segment/{id}` — `delete-api-segment-id` — Archive a Segment. (DEPRECATED -- Just pass updated value of `:archived` to the `PUT` endpoint instead.)
- [ ] `GET /api/segment/{id}/related` — `get-api-segment-id-related` — Return related entities.

### /api/session (0/8 complete)

- [ ] `POST /api/session` — `post-api-session` — Login.
- [ ] `DELETE /api/session` — `delete-api-session` — Logout.
- [ ] `POST /api/session/forgot_password` — `post-api-session-forgot_password` — Send a reset email when user has forgotten their password.
- [ ] `POST /api/session/google_auth` — `post-api-session-google_auth` — Login with Google Auth.
- [ ] `POST /api/session/password-check` — `post-api-session-password-check` — Endpoint that checks if the supplied password meets the currently configured password complexity rules.
- [ ] `GET /api/session/password_reset_token_valid` — `get-api-session-password_reset_token_valid` — Check if a password reset token is valid and isn't expired.
- [ ] `GET /api/session/properties` — `get-api-session-properties` — Get all properties and their values. These are the specific `Settings` that are readable by the current user, or are public if no user is logged in.
- [ ] `POST /api/session/reset_password` — `post-api-session-reset_password` — Reset password with a reset token.

### /api/setting (0/4 complete)

- [ ] `GET /api/setting` — `get-api-setting` — Get all `Settings` and their values. You must be a superuser or have `setting` permission to do this. For non-superusers, a list of visible settings and valu...
- [ ] `PUT /api/setting` — `put-api-setting` — Update multiple `Settings` values. If called by a non-superuser, only user-local settings can be updated.
- [ ] `GET /api/setting/{key}` — `get-api-setting-key` — Fetch a single `Setting`.
- [ ] `PUT /api/setting/{key}` — `put-api-setting-key` — Create/update a `Setting`. If called by a non-admin, only user-local settings can be updated. This endpoint can also be used to delete Settings by passing `n...

### /api/setup (0/1 complete)

- [ ] `POST /api/setup` — `post-api-setup` — Special endpoint for creating the first user during setup. This endpoint both creates the user AND logs them in and returns a session ID. This endpoint can a...

### /api/slack (0/4 complete)

- [ ] `GET /api/slack/app-info` — `get-api-slack-app-info` — Returns the Slack app_id and team_id. Used by the frontend to construct direct links to the Slack app settings page.
- [ ] `POST /api/slack/bug-report` — `post-api-slack-bug-report` — Send diagnostic information to the configured Slack channels.
- [ ] `GET /api/slack/manifest` — `get-api-slack-manifest` — Returns the JSON manifest file that should be used to bootstrap new Slack apps
- [ ] `PUT /api/slack/settings` — `put-api-slack-settings` — Update Slack related settings. You must be a superuser to do this. Also updates the slack-cache. There are 3 cases where we alter the slack channel/user cach...

### /api/table (2/16 complete)

- [x] `GET /api/table` — `get-api-table` — Get all `Tables`. Optional filters: - `can-query=true` - filter to only tables the user can execute queries against - `can-write=true` - filter to only table...
- [ ] `PUT /api/table` — `put-api-table` — Update all `Table` in `ids`. Deprecated, should use PUT /table/edit from now on.
- [ ] `GET /api/table/card__:id/fks` — `get-api-table-card__:id-fks` — Return FK info for the 'virtual' table for a Card. This is always empty, so this endpoint serves mainly as a placeholder to avoid having to change anything o...
- [ ] `GET /api/table/card__:id/query_metadata` — `get-api-table-card__:id-query_metadata` — Return metadata for the 'virtual' table for a Card.
- [x] `GET /api/table/{id}` — `get-api-table-id` — Get `Table` with ID.
- [ ] `PUT /api/table/{id}` — `put-api-table-id` — Update `Table` with ID.
- [ ] `POST /api/table/{id}/append-csv` — `post-api-table-id-append-csv` — Inserts the rows of an uploaded CSV file into the table identified by `:id`. The table must have been created by uploading a CSV file.
- [ ] `POST /api/table/{id}/discard_values` — `post-api-table-id-discard_values` — Discard the FieldValues belonging to the Fields in this Table. Only applies to fields that have FieldValues. If this Table's Database is set up to automatica...
- [ ] `PUT /api/table/{id}/fields/order` — `put-api-table-id-fields-order` — Reorder fields
- [ ] `GET /api/table/{id}/fks` — `get-api-table-id-fks` — Get all foreign keys whose destination is a `Field` that belongs to this `Table`.
- [ ] `GET /api/table/{id}/query_metadata` — `get-api-table-id-query_metadata` — Get metadata about a `Table` useful for running queries. Returns DB, fields, field FKs, and field values. Passing `include_hidden_fields=true` will include a...
- [ ] `GET /api/table/{id}/related` — `get-api-table-id-related` — Return related entities.
- [ ] `POST /api/table/{id}/replace-csv` — `post-api-table-id-replace-csv` — Replaces the contents of the table identified by `:id` with the rows of an uploaded CSV file. The table must have been created by uploading a CSV file.
- [ ] `POST /api/table/{id}/rescan_values` — `post-api-table-id-rescan_values` — Manually trigger an update for the FieldValues for the Fields belonging to this Table. Only applies to Fields that are eligible for FieldValues.
- [ ] `POST /api/table/{id}/sync_schema` — `post-api-table-id-sync_schema` — Trigger a manual update of the schema metadata for this `Table`.
- [ ] `GET /api/table/{table-id}/data` — `get-api-table-table-id-data` — Get the data for the given table

### /api/task (0/7 complete)

- [ ] `GET /api/task` — `get-api-task` — Fetch a list of recent tasks stored as Task History
- [ ] `GET /api/task/info` — `get-api-task-info` — Return raw data about all scheduled tasks (i.e., Quartz Jobs and Triggers).
- [ ] `GET /api/task/runs` — `get-api-task-runs` — List task runs with optional filters. Returns runs with hydrated entity names and task counts.
- [ ] `GET /api/task/runs/entities` — `get-api-task-runs-entities` — Get distinct entities that have task runs for a given run type. Used for populating entity filter picker.
- [ ] `GET /api/task/runs/{id}` — `get-api-task-runs-id` — Get a single task run with all its child tasks.
- [ ] `GET /api/task/unique-tasks` — `get-api-task-unique-tasks` — Returns possibly empty vector of unique task names in alphabetical order. It is expected that number of unique tasks is small, hence no need for pagination....
- [ ] `GET /api/task/{id}` — `get-api-task-id` — Get `TaskHistory` entry with ID.

### /api/tiles (0/3 complete)

- [ ] `GET /api/tiles/{card-id}/{zoom}/{x}/{y}` — `get-api-tiles-card-id-zoom-x-y` — Generates a single tile image for a saved Card.
- [ ] `GET /api/tiles/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/{zoom}/{x}/{y}` — `get-api-tiles-dashboard-id-dashcard-dashcard-id-card-card-id-zoom-x-y` — Generates a single tile image for a dashcard.
- [ ] `GET /api/tiles/{zoom}/{x}/{y}` — `get-api-tiles-zoom-x-y` — Generates a single tile image for an ad-hoc query.

### /api/timeline (0/7 complete)

- [ ] `POST /api/timeline` — `post-api-timeline` — Create a new [[Timeline]].
- [ ] `GET /api/timeline` — `get-api-timeline` — Fetch a list of `Timeline`s. Can include `archived=true` to return archived timelines.
- [ ] `GET /api/timeline/collection/root` — `get-api-timeline-collection-root` — Fetch the root Collection's timelines.
- [ ] `GET /api/timeline/collection/{id}` — `get-api-timeline-collection-id` — Fetch a specific Collection's timelines.
- [ ] `GET /api/timeline/{id}` — `get-api-timeline-id` — Fetch the `Timeline` with `id`. Include `include=events` to unarchived events included on the timeline. Add `archived=true` to return all events on the timel...
- [ ] `PUT /api/timeline/{id}` — `put-api-timeline-id` — Update the [[Timeline]] with `id`. Returns the timeline without events. Archiving a timeline will archive all of the events in that timeline.
- [ ] `DELETE /api/timeline/{id}` — `delete-api-timeline-id` — Delete a [[Timeline]]. Will cascade delete its events as well.

### /api/timeline-event (0/4 complete)

- [ ] `POST /api/timeline-event` — `post-api-timeline-event` — Create a new [[TimelineEvent]].
- [ ] `GET /api/timeline-event/{id}` — `get-api-timeline-event-id` — Fetch the [[TimelineEvent]] with `id`.
- [ ] `PUT /api/timeline-event/{id}` — `put-api-timeline-event-id` — Update a [[TimelineEvent]].
- [ ] `DELETE /api/timeline-event/{id}` — `delete-api-timeline-event-id` — Delete a [[TimelineEvent]].

### /api/transform (0/12 complete)

- [ ] `GET /api/transform` — `get-api-transform` — Get a list of transforms.
- [ ] `POST /api/transform` — `post-api-transform` — Create a new transform.
- [ ] `GET /api/transform/run` — `get-api-transform-run` — Get transform runs based on a set of filter params.
- [ ] `GET /api/transform/run/{run-id}` — `get-api-transform-run-run-id` — Get a transform run by ID.
- [ ] `GET /api/transform/{id}` — `get-api-transform-id` — Get a specific transform.
- [ ] `PUT /api/transform/{id}` — `put-api-transform-id` — Update a transform.
- [ ] `DELETE /api/transform/{id}` — `delete-api-transform-id` — Delete a transform.
- [ ] `POST /api/transform/{id}/cancel` — `post-api-transform-id-cancel` — Cancel the current run for a given transform.
- [ ] `GET /api/transform/{id}/dependencies` — `get-api-transform-id-dependencies` — Get the dependencies of a specific transform.
- [ ] `POST /api/transform/{id}/reset-checkpoint` — `post-api-transform-id-reset-checkpoint` — Reset the stored checkpoint for an incremental transform.
- [ ] `POST /api/transform/{id}/run` — `post-api-transform-id-run` — Run a transform.
- [ ] `DELETE /api/transform/{id}/table` — `delete-api-transform-id-table` — Delete a transform's output table.

### /api/transform-job (0/7 complete)

- [ ] `POST /api/transform-job` — `post-api-transform-job` — Create a new transform job.
- [ ] `GET /api/transform-job` — `get-api-transform-job` — Get all transform jobs.
- [ ] `PUT /api/transform-job/{job-id}` — `put-api-transform-job-job-id` — Update a transform job.
- [ ] `DELETE /api/transform-job/{job-id}` — `delete-api-transform-job-job-id` — Delete a transform job.
- [ ] `GET /api/transform-job/{job-id}` — `get-api-transform-job-job-id` — Get a transform job by ID.
- [ ] `POST /api/transform-job/{job-id}/run` — `post-api-transform-job-job-id-run` — Run a transform job manually.
- [ ] `GET /api/transform-job/{job-id}/transforms` — `get-api-transform-job-job-id-transforms` — Get the transforms of job specified by the job's ID.

### /api/transform-tag (0/4 complete)

- [ ] `POST /api/transform-tag` — `post-api-transform-tag` — Create a new transform tag.
- [ ] `GET /api/transform-tag` — `get-api-transform-tag` — Get a list of all transform tags.
- [ ] `PUT /api/transform-tag/{tag-id}` — `put-api-transform-tag-tag-id` — Update a transform tag.
- [ ] `DELETE /api/transform-tag/{tag-id}` — `delete-api-transform-tag-tag-id` — Delete a transform tag. Removes it from all transforms and jobs.

### /api/upload (0/1 complete)

- [ ] `POST /api/upload/csv` — `post-api-upload-csv` — Create a table and model populated with the values from the attached CSV. Returns the model ID if successful.

### /api/user (3/11 complete)

- [x] `GET /api/user` — `get-api-user` — Fetch a list of `Users` for admins or group managers. By default returns only active users for admins/data-analysts and only active users within groups that...
- [ ] `POST /api/user` — `post-api-user` — Create a new `User`, return a 400 if the email address is already taken
- [x] `GET /api/user/current` — `get-api-user-current` — Fetch the current `User`.
- [ ] `GET /api/user/recipients` — `get-api-user-recipients` — Fetch a list of `Users`. Returns only active users. Meant for non-admins unlike GET /api/user. - If user-visibility is :all or the user is an admin, include...
- [x] `GET /api/user/{id}` — `get-api-user-id` — Fetch a `User`. You must be fetching yourself *or* be a superuser *or* a Group Manager.
- [ ] `PUT /api/user/{id}` — `put-api-user-id` — Update an existing, active `User`. Self or superusers can update user info and groups. Group Managers can only add/remove users from groups they are manager of.
- [ ] `DELETE /api/user/{id}` — `delete-api-user-id` — Disable a `User`. This does not remove the `User` from the DB, but instead disables their account.
- [ ] `PUT /api/user/{id}/modal/{modal}` — `put-api-user-id-modal-modal` — Indicate that a user has been informed about the vast intricacies of 'the' Query Builder.
- [ ] `PUT /api/user/{id}/password` — `put-api-user-id-password` — Update a user's password.
- [ ] `POST /api/user/{id}/password-reset-url` — `post-api-user-id-password-reset-url` — Generate a password reset URL for a user. Admins can share this URL directly with the user. The link expires in 48 hours.
- [ ] `PUT /api/user/{id}/reactivate` — `put-api-user-id-reactivate` — Reactivate user at `:id`

### /api/user-key-value (0/4 complete)

- [ ] `GET /api/user-key-value/namespace/{namespace}` — `get-api-user-key-value-namespace-namespace` — Returns all KV pairs in a given namespace for the current user
- [ ] `PUT /api/user-key-value/namespace/{namespace}/key/{key}` — `put-api-user-key-value-namespace-namespace-key-key` — Upsert a KV-pair for the user
- [ ] `GET /api/user-key-value/namespace/{namespace}/key/{key}` — `get-api-user-key-value-namespace-namespace-key-key` — Get a value for the user
- [ ] `DELETE /api/user-key-value/namespace/{namespace}/key/{key}` — `delete-api-user-key-value-namespace-namespace-key-key` — Deletes a KV-pair for the user

### /api/util (0/1 complete)

- [ ] `GET /api/util/random_token` — `get-api-util-random_token` — Return a cryptographically secure random 32-byte token, encoded as a hexadecimal string. Intended for use when creating a value for `embedding-secret-key`.
