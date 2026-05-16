## Goal

以 Metabase OpenAPI 作為來源，參考 WISE API 的設計方式（`BaseModel` + `do_sync`/`do`）為 Metabase API 的 request/response 實作一組可維護的型別模型，並納入現有 `metabaseapi` 架構中。

## Context

目前專案已完成「每個 OpenAPI endpoint 對應 request/response 容器 model」的動態對應（`src/metabaseapi/models.py`）。本次目標改為補齊「可實際描述欄位與行為」的 metabase domain model，讓型別更精準，且仍保留通用請求能力，避免對外部 API 有硬依賴的測試設計。

## Architecture

- 保留 `src/metabaseapi/models.py` 的 `APIRequestModel`、`APIResponseModel` 作為動態 fallback 與基礎。
- 新增 `src/metabaseapi/metabase/models.py`（或既有 models 模組）定義實務上會使用的 Metabase typed model。
- 每個 model 不直接包住 httpx client，仍使用 client 發起請求；在 model 層只負責 schema + 轉換。
- 以方法如 `UserCurrentResponse`, `Database`, `Card`, `Dashboard` 這類實際 endpoint 的回應模型為主；可由使用者自行新增更多 endpoint 的 `XXXRequest`/`XXXResponse`。

## Assumptions

- 參考 WISE 的 `RateRequest`/`field_validator` 模式（即「型別驗證 + 簡潔 client 方法」）作為風格。
- 先聚焦少量高價值 endpoint：
  - `GET /api/user/current`
  - `GET /api/database`
  - `POST /api/card/{id}` 或 `GET /api/card/{id}` 等常用讀取 endpoint
- 這些 endpoint 的回應 JSON 結構可由目前 `tests/fixtures/api.json` 與測試 fixture 驗證與修正。

## Plan

- [x] 在 `src/metabaseapi/metabase/models.py` 新增 Metabase typed base 與 domain model：
  - 實作 `_MetabaseResponseBase` 共用時間欄位轉換，並定義 `CurrentUserResponse`、`Database`、`Card`、`Dashboard`、`ListDatabasesResponse`。
  - 驗證：`uv run ruff check src/metabaseapi`、`uv run ty check`。
- [x] 針對 `GET /api/user/current` 設計對應模型：
  - 建立 `CurrentUserRequest` 與 `CurrentUserResponse`。
  - `MetabaseClient.current_user_typed()` 透過 `CurrentUserRequest.do` 回傳 `CurrentUserResponse.model_validate()`。
  - 測試與驗證：`tests/test_metabase_models.py` 已覆蓋。
- [x] 針對 `GET /api/database` 與 `POST /api/database` 設計 typed 模型：
  - 建立 `ListDatabasesRequest/Response`、`CreateDatabaseRequest`。
  - 驗證：mock `httpx` 回傳 sample JSON，測試 request payload 與 response 模型解析。
- [x] 針對卡片與儀表板讀取 endpoint 建立模型：
  - 建立 `GetCardRequest`、`GetDashboardRequest`，並對應 `Card`、`Dashboard` response。
  - 驗證：離線測試 assert `model_validate` 成功與欄位型別、路徑參數。
- [x] 為 metabase 風格方法補上 `do_sync`/`do` 輕量封裝：
  - 所有 metabase request model 均支援 `do` 與 `do_sync`。
  - 驗證：`tests/test_metabase_models.py` 包含 `do()`/`do_sync()` 對 stub client 的測試。
- [x] 將 `MetabaseClient` 與 CLI 對齊：
  - 新增 `current_user_typed`、`list_databases_typed`、`get_card_typed`、`get_dashboard_typed`、`create_database_typed`。
  - 驗證：執行既有 `tests/test_endpoints.py` 保持 600 endpoints 可呼叫與通過；新 model 測試通過。

## Risks

- 以 OpenAPI fixture 推斷欄位時可能與實際執行環境回傳略有差異，需要以 fixture 或實際樣本資料持續修正。
- 部分 endpoint 回傳非 JSON（例如檔案下載）需要 `APIResponseModel` fallback，不宜硬性型別化。

## Rollback / Recovery

- 若某 typed response 與實際不一致：先退回較彈性的 `dict[str, Any]` 欄位並加 `Any` 容錯，避免阻塞開發。
- 若某 endpoint 行為與 OpenAPI 偏離大：將其排除於 typed scope，保留通用 `get_response_model` fallback。

## Completion Checklist

- [x] 已新增/更新 `src/metabaseapi/metabase/models.py` 並定義 Metabase 對應模型（已覆蓋 `user/current`、`database`、`card/dashboard` 相關 request/response）。
- [x] 這些模型的欄位有 `BaseModel` 驗證與必要的 `field_validator`（含時間欄位轉 UTC）。
- [x] `MetabaseClient` 可對應使用新模型（`tests/test_metabase_models.py` 有直接驗證證據）。
- [x] 新增並通過離線單元測試，涵蓋 request 建模、response 型別回傳、`do_sync` 行為。
- [x] 全域檢查通過：`uv run ruff check src/metabaseapi tests`、`uv run ty check`、`uv run pytest -q`、`just`。
