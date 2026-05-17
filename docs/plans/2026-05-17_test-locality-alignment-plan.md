## Goal
提升新重構方向的測試 locality：依資源對應的 client/CLI/metabase model 測試分群，讓單一 domain 改動只改一組測試而不影響整體。

## Context
目前測試已拆為 `tests/test_cli.py`、`tests/test_cli_core.py`、`tests/test_cli_misc.py`，但仍以執行面向分類為主。

## Plan
- [x] 建立 `tests/metabase/` 與 `tests/client/` 或 `tests/cli/` 子目錄；規劃 domain 對應測試檔（`test_client_actions.py`, `test_client_cards.py`, `test_client_collections.py`, ...）； verify with: 目錄建立與命名。
- [x] 依 endpoint domain 將 `tests/test_client.py`、`tests/test_cli*.py`、`tests/test_endpoints.py`、`tests/test_metabase_models.py` 中可切分案例逐步分離； verify with: 每個新測試檔有明確 endpoint 群組。
- [x] 在每個 domain 測試模組加入 import smoke（例如 `from metabaseapi.metabase import CreateCardRequest`）確保聚合入口穩定； verify with: `python -m compileall tests`。
- [x] 增加 `pytest` markers 或簡易目錄命令，例如 `pytest tests/client -q`、`pytest tests/cli -q`； verify: 兩命令皆可執行並返回非零錯誤。
- [x] 保持現有總測試命令通過作為回歸保證； verify with: `uv run pytest -q`。

## Risks
- 過度拆分造成 import 循環或 fixture 重複定義導致維護成本上升。
- 測試資料/輔助 client 重複定義導致維護成本上升。

## Completion Checklist
- [x] 測試資料與 helper 以 domain 為主分組且可定位性提升（新目錄存在，且有單元測試對應）； verify with 目錄與檔名清單。
- [x] `uv run pytest -q` 維持 `171 passed`（或更新為新總數但無功能回歸）； verify with 回歸輸出。
- [x] CLI/endpoint/typed/transport 相關修改均可由 domain 測試範圍快速定位； verify by code review。
