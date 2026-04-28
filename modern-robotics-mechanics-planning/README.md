# modern-robotics-mechanics-planning

《Modern Robotics》中文术语化学习资料与网页渲染配置。

## 技术栈

- MkDocs
- mkdocs-material
- pymdown-extensions

与 `guinsoo_notes/curobot` 使用同一渲染技术栈，便于统一环境维护。

## 本地预览

```bash
cd /home/qj00433/guinsoo_notes/modern-robotics-mechanics-planning
python3 -m pip install -r requirements-docs.txt
./scripts/serve_docs.sh
```

浏览器访问：`http://127.0.0.1:8000`

## 站点构建

```bash
cd /home/qj00433/guinsoo_notes/modern-robotics-mechanics-planning
./scripts/check_doc_links.py
./scripts/build_docs.sh
```
