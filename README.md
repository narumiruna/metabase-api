# Metabase API

A small async-first Python client and Typer CLI for the Metabase API.

此專案用手寫、明確的 client/CLI surface 支援 Metabase endpoints。`docs/TODO.md` 是依據最新 Metabase API 文件整理的靜態實作清單；只有具備手寫 client method、request/response `BaseModel`、以及 CLI 命令的 endpoint 才能被打勾。

## 安裝

```bash
uv sync
```

## 環境變數

- `METABASE_URL`：Metabase 服務網址（預設 `http://localhost:3000`）
- `METABASE_API_KEY`：Metabase API 金鑰（API Key authentication）
- `METABASE_TIMEOUT_SECONDS`：請求逾時秒數（預設 `30.0`）
- `METABASE_VERIFY_SSL`：是否驗證 TLS 憑證（預設 `true`）

## 使用方式

```bash
export METABASE_URL=https://your-metabase.example
export METABASE_API_KEY=your-api-key
```

### 手寫 CLI 命令

CLI 不提供 raw `request` / `invoke`。新增 API 能力時，請同時新增手寫 client method、request/response `BaseModel`、CLI 命令與測試。

```bash
metabaseapi current-user
metabaseapi list-databases
metabaseapi create-database my_db postgres --details '{"host":"localhost","port":5432}'
metabaseapi get-database 1
metabaseapi list-cards
metabaseapi create-question Orders '{"database":1,"type":"query","query":{"source-table":2}}'
metabaseapi create-card Orders '{"database":1,"type":"query","query":{"source-table":2}}' --type question
metabaseapi get-card 2
metabaseapi list-dashboards
metabaseapi get-dashboard 1
metabaseapi list-users
metabaseapi get-user 4
metabaseapi list-collections
metabaseapi get-collection root
metabaseapi list-tables
metabaseapi get-table 8
metabaseapi get-field 9
```

所有輸出都會以可讀 JSON（縮排、排序）輸出，便於 AI / 腳本處理。

## API coverage

- `docs/TODO.md` 追蹤官方 Metabase API 文件中的 600 個 operations。
- 只有具備手寫 client method、request/response `BaseModel`、CLI 命令與測試的 endpoint 會被標記為完成。
- CLI 不提供 raw `request` / `invoke`；未完成的 endpoint 必須先補齊手寫 surface。
- typed endpoint models 維持手寫，不從 `api.json` 產生 runtime registry 或 generated endpoint modules。

## Live test

`.env` 設好 `METABASE_URL` 與 `METABASE_API_KEY` 後，可以執行低風險唯讀 live checks：

```bash
just live-test
```

此命令只檢查 current-user 的 convenience 與 typed 路徑，輸出欄位名稱與狀態，不輸出 API key。
