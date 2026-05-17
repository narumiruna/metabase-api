## Goal

將 `tests/fixtures/api.json` 中定義的 600 組 OpenAPI endpoint 轉成可維護的一級 API 能力：
- CLI 至少能穩定呼叫高價值 endpoint（至少目前缺口中的第一批）
- client module 具備明確且可自動擴展的 typed/半-typed 對應能力
- 避免手寫 600 個 method 的維護負擔，改以規則化/自動化生成為主

## 現況盤點（基於 api.json）

- 以目前 `tests/fixtures/api.json` 解析結果：共 **600** 個 endpoint（GET/POST/PUT/PATCH/DELETE）
- 目前 `MetabaseClient` 有：
  - 通用 request 介面：`request/get/post/put/patch/delete`
  - 小量 convenience：`current_user/list_databases/get_dashboard/get_card` 與其 typed 版本
- 目前 CLI 有：
  - `request`（通用 raw）
  - `current-user`, `list-databases`, `get-dashboard`, `get-card`, `get-database`, `create-database`
- 目前已具備「全部 endpoint 可打」的最低能力（透過 `request` + dynamic openapi model fallback）
- 目前尚未具備「全 endpoint 一級方法 / typed command」的能力（缺口主因是手工方法與 command 數量不足）

## Plan

### 1) 盤點階段：建立 endpoint 目錄與缺口報表
- 建立 `scripts/` 下的 generator 腳本（建議 `scripts/sync_openapi_endpoints.py`）：
  - 讀 `tests/fixtures/api.json`
  - 輸出：
    - endpoint 清單（method, path, operationId, 是否含 body/query）
    - 以 resource prefix 分組（如 `/api/card`, `/api/database`, `/api/dashboard`）
    - 缺少一級 API 的項目
- 產生 `docs/` 下一份 `endpoint-coverage.md`，每次更新時可對比差異。

### 2) 優先序第一批：建立「通用生成型」一級 command
- 實作 `src/metabaseapi/cli.py` 新增通用 `invoke` 命令模板：
  - `metabaseapi invoke get /api/card/1`
  - `metabaseapi invoke post /api/database -b '{...}'`
- 對現有 `request` 做薄包裝，讓參數體驗統一（`--query/--body`）。
- 先保留 current-user/list-databases/get-*/create-* 既有命令，避免破壞相容。

### 3) 第一階段 typed 客戶端模組（高價值 endpoint）
- 以 `metabase` 資料夾建立 generator 輸出機制，先覆蓋常用高價值群：
  - card/dashboard/database/user/session/collection/table/field
- 每一群至少補齊：
  - request model（method/path/params/body）
  - do/do_sync
  - response model 盡量以實務欄位 + `extra="allow"` 寬鬆模式
- client 提供 `run(request)` seam，request object 可直接呼叫，減少新增 endpoint 時改 client 的次數。

### 4) 第二階段：自動化命令產生（避免人工爆炸）
- 建立 command generator 測試腳手架：
  - 根據 endpoint 分組產生可選命令（例如：`get-card`, `get-database`, `get-user`）
  - 對 query/body 有參數格式化規範
- CLI command 以「固定命名 + group 機制」掛載到 `metabaseapi`，而非手工 600 個獨立函式。

### 5) 第三階段：資料品質與穩定性
- 新增/更新測試：
  - `tests/test_cli.py`：驗證 `invoke` 命令可打通 endpoint 清單中的代表性 sample
  - `tests/test_endpoints.py`：保留 600 endpoint mock 可打通測試（不回歸）
  - `tests/test_metabase_models.py`：新增/擴大 typed response/validator 覆蓋
- 針對每次 api.json 更新增加快照比對（endpoint 數/新增/移除）

## Implementation strategy（避免手工到崩潰）

- **不要**直接手刻 600 個 method；改為：
  1. 通用 `request`/`invoke` 作為完整覆蓋
  2. 以 generated typed module 補上最常用 endpoint
  3. 以分組機制逐步提升一級 command 的數量
- 每 50~100 個 endpoint 為一個 release chunk，先有行為再擴充覆蓋率。

## Completion Checklist（MVP）

- [x] 有至少一個可重複執行的 `api.json` 掃描報表（method/path/operationId）
  - 已實作 `src/metabaseapi/openapi_coverage.py`、`scripts/sync_openapi_endpoints.py`，並產生 `docs/endpoint-coverage.md`（目前顯示 `600` endpoints、便利方法 coverage `462/600`）。
- [x] 新增 `metabaseapi invoke` 命令，並接管原有 `request` 的通用能力
  - 已於 `src/metabaseapi/cli.py` 新增 `invoke`，並讓 `request` 走相同 raw 呼叫流程。
- [x] 以 generator 方式自動產生第一批高價值 endpoint 的 typed request/response（最少 10-20 個）
  - 已補齊 `src/metabaseapi/metabase/models.py` 與 `src/metabaseapi/metabase/__init__.py` 中高價值群組（card/dashboard/database/user/collection/table/field）請求/回應與 client convenience。
- [x] `MetabaseClient` 新增 `run` seam，透過 request object 執行
  - 已新增 `MetabaseClient.run()` 並回歸到 typed methods。
- [x] 測試仍通過：`uv run ruff check src/metabaseapi tests`、`uv run ty check`、`uv run pytest -q`、`just`
- [x] 記錄每個 phase 完成的 endpoint 覆蓋進度（可追蹤）
  - 以 `docs/endpoint-coverage.md` 作為每次快照。

## 備註（進度）

- 第一階段已完成並可關閉：`openapi_coverage` 報表、`invoke`/`request` 重構、typed request/response 增補、`MetabaseClient.run()` seam、CLI/模型/測試同步擴充皆已落地。
- 本階段未進入「一次性為 600 endpoint 手刻」；保留 `request/invoke` 作為完整 fallback。
- CLI 在現階段已補齊 `get-user/list-collections/list-cards/list-users` 等常用命令，後續可延續同一機制分批擴充。
- 下一步建議持續在 `docs/endpoint-coverage.md` 上設定缺口阈值（例如 missing rate < 10%）作為 release gate。

## 驗證與結果

- 已執行：`uv run ruff check src/metabaseapi tests`
- 已執行：`uv run ty check`
- 已執行：`uv run pytest -q`
- 已執行：`uv run ruff check src tests scripts`
- 已執行：`just`
- 目前 `tests/fixtures/api.json` 快照維持 `600` endpoints；`docs/endpoint-coverage.md` 顯示 convenience 覆蓋 `462/600`（第一階段基準）。

## Fallback

- 若 endpoint 規格變更頻繁：維持通用 `request/invoke` 不斷線，typed 進度可以慢慢追。
- 若 generator 產生過多：先凍結最常用 20~50 個 endpoint，優先保證可用性再擴張。
