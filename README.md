# guinsoo_notes

多项目学习笔记仓库（Markdown + Git）。

## 仓库定位

- `guinsoo_notes` 是你的总笔记仓，面向多个项目长期维护。
- `curobot` 只是其中一个项目子目录，后续可并行增加更多项目笔记。
- 公共规范（渲染、更新、目录模板）统一放在仓库根目录，避免每个项目重复维护一套。

## 推荐目录结构（多项目版）

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
│  ├─ mkdocs.yml
│  ├─ requirements-docs.txt
│  └─ ...
└─ <future_project_1>/
   └─ ...
```

## 入口文档

- 渲染与维护指南：[`DOC_RENDERING_GUIDE.md`](DOC_RENDERING_GUIDE.md)
- 目录规范与模板：[`NOTES_REPO_STRUCTURE.md`](NOTES_REPO_STRUCTURE.md)

## 使用建议

1. 新项目进入仓库时，先按 `NOTES_REPO_STRUCTURE.md` 建立其 `doc/`、`assets/`、`templates/`。
2. 每个项目保留自己的技术索引（如 `curobot/doc/CH00_INDEX.md`）。
3. 渲染工具、CI 和更新流程尽量复用根目录规范，减少分叉。
