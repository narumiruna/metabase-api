## Goal
明確化 CLI 與 HTTP transport 的錯誤/輸出 seam，避免 `_run_and_print` 兼任 too much 責任，建立可測試的 `cli/output` 與 `cli/error_adapter` 介面，提高變更 locality。

## Architecture
- **Module**：`src/metabaseapi/cli/__init__.py`, `src/metabaseapi/errors.py`, `src/metabaseapi/client/http.py`。
- **Interface**：CLI 只負責格式化輸出 payload；transport 專注 HTTP 與錯誤映射到 `MetabaseError`。
- **Adapter**：`format_payload(error, success)` 與 `run_call(call)` 分離。

## Plan
- [x] 新增 `src/metabaseapi/cli/output.py`：集中 `json` 格式化與 `null` 顯示； verify with: `python -m py_compile src/metabaseapi/cli/output.py`。
- [x] 新增 `src/metabaseapi/cli/error_adapter.py`：將 `MetabaseError`、`ValueError` 轉為可一致輸出的 JSON 錯誤 payload（保留原訊息）； verify with: payload 轉換函式有單元測試。
- [x] 將 `cli/__init__.py` 的 `_parse_json_body`、`_run_and_print`、`_run_client_call` 等 helper 重定向至新 module； verify with: `ruff check src/metabaseapi/cli/*.py`。
- [x] 增加/調整 `tests/test_cli_misc.py` 或新 test，覆蓋錯誤型態 payload 的一致格式（含 401/JSONDecode/Network）； verify with: 相關測試用例新增且 pass。
- [x] 以回歸方式執行 CLI 測試並核對既有錯誤輸出訊息行為（`tests/test_cli_misc.py::test_error_response_is_reported_as_json`）； verify with: 該測試用例通過。

## Completion Checklist
- [x] `tests/test_cli_misc.py::test_error_response_is_reported_as_json` 仍通過，錯誤 JSON format 未退化； verify with `uv run pytest tests/test_cli_misc.py -q`。
- [x] `uv run pytest tests/test_cli*.py -q` 全通； verify with test output。
- [x] CLI 成功/失敗輸出邏輯集中在新增 adapter/output module，`cli.py` 主要維持命令組裝/設定； verify with: code review。
