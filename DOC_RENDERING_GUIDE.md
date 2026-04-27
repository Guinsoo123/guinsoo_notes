# 07 — 文档渲染与更新维护指南（跨平台，多项目通用）

本文是 `guinsoo_notes` 根目录的公共规范，适用于仓库下所有项目笔记（例如 `curobot` 以及后续新增项目）。

## 目标与范围

- 目标：在 macOS / Ubuntu 上稳定渲染 Markdown（表格、公式、图表），并形成统一更新流程。
- 范围：仓库内各项目的 `doc/`、`docs/` 或 `notes/` 目录。

## 语法基线

- 基础语法（必须）：CommonMark / GFM（标题、列表、表格、围栏代码块、相对链接）。
- 扩展语法（可选）：
  - 数学公式：`\( ... \)`、`\[ ... \]`
  - 图表：`plantuml` fenced code

结论：基础语法各平台几乎都兼容；公式与 PlantUML 需要额外渲染支持。

## 跨平台工具栈建议

### 编辑器

- `Cursor / VS Code`（首选）
- `Obsidian`（知识管理友好）
- `Typora / MarkText`（轻量写作）

### Cursor / VS Code 插件建议

- `Markdown All in One`
- `Markdownlint`
- `Markdown Preview Enhanced`
- `PlantUML`

### 依赖

- Java（PlantUML 必需）
- Graphviz（PlantUML 某些图类型需要）

## 浏览器建议

- Chrome / Edge：渲染稳定，调试强
- Firefox：阅读体验好
- Safari（macOS）：系统集成好

## 网页化渲染（MkDocs）

### 1) 环境准备

```bash
conda create -n guinsoo_notes python=3.11 -y
conda activate guinsoo_notes
pip install -r <project>/requirements-docs.txt
```

### 2) 本地预览

```bash
cd ./curobot
mkdocs serve
```

访问：`http://127.0.0.1:8000`

### 3) 构建

```bash
mkdocs build --strict
```

## 文档更新标准流程

1. 编辑：按模板写作（见 `README_08`）。
2. 本地检查：
   - Markdown 预览（表格、公式、PlantUML）
   - 链接检查（相对路径 + 外链）
3. 构建验证：`mkdocs build --strict`
4. 提交：

```bash
git add .
git commit -m "docs: update notes and keep docs checks green"
git push
```

## CI 最小检查项

- markdownlint
- 链接检查脚本（如 `scripts/check_doc_links.py`）
- `mkdocs build --strict`

## 维护注意点

- 不要写本机绝对路径（如 `/home/...`）到可点击链接中。
- 项目内文档用相对路径；跨项目/上游源码优先绝对 URL。
- 重要图表建议保留源码（如 `.puml`）并可选导出 `svg`。

## 术语速查

| 术语 | 含义 |
|------|------|
| CommonMark | Markdown 通用规范基线。 |
| GFM | GitHub Flavored Markdown（含表格等扩展）。 |
| MathJax / KaTeX | 网页公式渲染引擎。 |
| PlantUML | 文本驱动 UML/流程图工具。 |
| MkDocs | Markdown 静态文档站生成器。 |
| CI | 持续集成自动检查流水线。 |
