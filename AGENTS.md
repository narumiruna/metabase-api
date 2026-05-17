- metabaseapi.cli 的 CLI 入口點，提供命令列工具。
- api.json 包含 OpenAPI 規格的 API 定義，供測試和參考使用。

## Requeriments

- api.json 中的 description 必須要對應到 CLI 命令的說明
- api.json 中的 endpoints 必須要對應到 CLI 命令的實作
- 使用者可以透過 $ uv run metabaseapi --help 來查看所有可用的命令和選項
