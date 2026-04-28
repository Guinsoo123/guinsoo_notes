# modern-robotics-mechanics-planning

《Modern Robotics》中文术语化学习资料与网页渲染工程。

本文档面向 macOS，目标是让你从零开始完成：

1. 安装 Conda
2. 创建并激活文档环境
3. 启动本地渲染并正常阅读 Web 文档
4. 在 Cursor 中安装推荐扩展，提升编写与预览体验

---

## 1. 技术栈

- `MkDocs`
- `mkdocs-material`
- `pymdown-extensions`

项目核心配置文件：

- 文档配置：`mkdocs.yml`
- Python 依赖：`requirements-docs.txt`
- 本地预览脚本：`scripts/serve_docs.sh`
- 构建脚本：`scripts/build_docs.sh`

---

## 2. 在 macOS 安装 Conda（推荐 Miniforge）

> 如果你已经安装了 Conda，可跳到下一节。

### 2.1 下载并安装 Miniforge

访问官方发布页下载适配你芯片的安装包（Apple Silicon 选 `arm64`，Intel 选 `x86_64`）：

- [https://github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases)

下载后在终端执行（文件名按你的实际版本替换）：

```bash
bash ~/Downloads/Miniforge3-MacOSX-arm64.sh
```

安装过程中保持默认即可（推荐同意初始化 shell）。

### 2.2 让 Conda 在 zsh 生效

```bash
source ~/.zshrc
conda --version
```

看到版本号即表示安装成功。

---

## 3. 创建项目环境并安装依赖

先进入项目目录（按你的本地路径）：

```bash
cd ~/guinsoo_notes/modern-robotics-mechanics-planning
```

创建并激活专用环境（推荐 Python 3.11）：

```bash
conda create -n mr-docs python=3.11 -y
conda activate mr-docs
```

安装渲染依赖：

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-docs.txt
```

快速验证：

```bash
mkdocs --version
```

---

## 4. 启动本地渲染并阅读 Web 文档

在激活 `mr-docs` 环境后运行：

```bash
./scripts/serve_docs.sh
```

默认监听地址：

- [http://127.0.0.1:8000](http://127.0.0.1:8000)

打开浏览器访问该地址即可阅读。修改 `doc/` 下的 Markdown 后，页面会自动热更新。

停止服务：`Ctrl + C`

---

## 5. 生成静态站点（可选）

```bash
./scripts/build_docs.sh
```

构建输出目录为：`site/`

---

## 6. Cursor 推荐扩展

为了更顺畅地写作和预览，建议在 Cursor 安装以下扩展：

1. `yzhang.markdown-all-in-one`  
   常用 Markdown 快捷键、目录生成、列表操作。
2. `shd101wyy.markdown-preview-enhanced`  
   增强本地 Markdown 预览能力（数学公式、流程图等）。
3. `DavidAnson.vscode-markdownlint`  
   Markdown 规范检查，减少格式问题。
4. `esbenp.prettier-vscode`  
   统一 Markdown/JSON/YAML 的格式风格。
5. `streetsidesoftware.code-spell-checker`  
   英文术语拼写检查，适合技术文档维护。

> 安装方式：在 Cursor 的 Extensions 面板搜索上述扩展 ID 并安装。

---

## 7. 常见问题排查

### 7.1 `conda: command not found`

执行：

```bash
source ~/.zshrc
```

仍不行就重新执行安装脚本，并确认安装时选择了 shell 初始化。

### 7.2 `mkdocs: command not found`

通常是环境未激活：

```bash
conda activate mr-docs
```

或依赖未安装完整，重新执行：

```bash
python -m pip install -r requirements-docs.txt
```

### 7.3 8000 端口被占用

可以改端口运行：

```bash
mkdocs serve -a 127.0.0.1:8001
```

然后访问 [http://127.0.0.1:8001](http://127.0.0.1:8001)。

---

## 8. 推荐使用流程

每次开始写作前：

```bash
cd ~/guinsoo_notes/modern-robotics-mechanics-planning
conda activate mr-docs
./scripts/serve_docs.sh
```

这样可以保持环境隔离、预览稳定、维护成本低。
