# 08 — 笔记仓目录规范与模板（多项目总规范）

本文定义 `guinsoo_notes` 的全局目录规范，解决“一个仓库维护多个项目笔记”的可扩展性问题。

## 设计目标

- 让每个项目有独立笔记空间，互不干扰。
- 公共规范只维护一份（根目录），减少重复。
- 支持后续新增项目时快速复制骨架。

## 总目录建议

```text
guinsoo_notes/
├─ README.md
├─ DOC_RENDERING_GUIDE.md
├─ NOTES_REPO_STRUCTURE.md
├─ templates/
│  ├─ chapter_template.md
│  └─ note_template.md
├─ scripts/
│  └─ check_doc_links.py
├─ curobot/
│  ├─ doc/
│  │  ├─ CH00_INDEX.md
│  │  ├─ CH01_algorithm_design.md / CH02_software_design.md / ...
│  │  ├─ assets/images/
│  │  ├─ diagrams/
│  │  └─ templates/
│  ├─ mkdocs.yml
│  └─ requirements-docs.txt
└─ <new_project>/
   ├─ doc/
   ├─ mkdocs.yml
   └─ requirements-docs.txt
```

## 规范分层

### 根目录（全局层）

- 放通用规范：渲染、更新流程、目录模板。
- 放通用模板：`templates/`
- 放通用脚本：`scripts/`

### 项目目录（项目层）

- 每个项目维护自己的 `doc/CH00_INDEX.md`
- 每个项目可以有独立 `mkdocs.yml` 与依赖
- 项目内技术细节只写在项目目录，不写到根目录

## 命名规范

- 章节文档：`README_XX_topic_name.md`（两位编号）
- 模板文件：`*_template.md`
- 图源文件：`*.puml`
- 图片文件：`topic-keyword-001.svg/png`

## 链接策略（关键）

1. 项目内部文档：相对路径（稳定）。
2. 上游仓库源码/文档：绝对 URL（避免本地目录依赖）。
3. 禁止将 `/home/...` 作为可点击链接写入文档。

## 新项目接入流程

1. 在根目录新增 `<new_project>/`。
2. 建立 `doc/` + `CH00_INDEX.md`。
3. 从根 `templates/` 拷贝模板到该项目文档目录。
4. 配置该项目的 `mkdocs.yml` 与 `requirements-docs.txt`。
5. 将项目索引链接补充到根 `README.md`。

## 模板说明

- `templates/chapter_template.md`：章节型长文（适合技术专题）
- `templates/note_template.md`：短笔记（问题、结论、证据、下一步）

## 最小更新流程

```bash
# 项目目录内执行
python3 scripts/check_doc_links.py
mkdocs build --strict
git add .
git commit -m "docs: update project notes"
git push
```

## 术语速查

| 术语 | 含义 |
|------|------|
| 全局层 | 根目录公共规范与工具层。 |
| 项目层 | 某个具体项目的独立笔记空间。 |
| 可移植路径 | 不依赖本机目录结构的链接写法。 |
| 模板化写作 | 用固定结构降低维护成本。 |
