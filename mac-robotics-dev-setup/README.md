# Mac 机器人运控开发环境（安装 + 示例运行）

本文档用于统一说明：

1. 在 macOS 上完成机器人运控开发环境安装
2. 在同一目录直接运行示例脚本做环境验收
3. 了解各工具的概念定位与机器人运控开发中的具体作用

---

## 1. 工作目录

后续所有命令默认在这里执行：

```bash
cd /Users/guinsoo/guinsoo_notes/mac-robotics-dev-setup
```

目录结构：

- `README.md`：主指南（本文件）
- `example/data/`：示例点云与轨迹数据
- `example/scripts/`：示例脚本

---

## 2. 工具概念定位与运控开发中的作用

### 基础环境

#### Homebrew

macOS 上最主要的包管理器。运控开发中几乎所有系统级工具（编译工具链、依赖库、可视化软件）都通过它安装，是后续一切工具的安装入口。

#### Miniforge（Conda）

Python 环境管理器。运控项目经常需要同时维护多组 Python 版本与依赖组合（比如在线控制器 vs 仿真器有不同的依赖），Conda 负责把它们隔离开来，避免版本冲突。相比 venv，它对 C 扩展库（如 Open3D、Pinocchio）的二进制安装支持更好。

#### Cursor / VSCode

工程开发主界面。运控算法通常跨文件、跨模块，IDE 负责代码补全、跳转定义、断点调试、Git 集成。SSH Remote 扩展还能直接连接远端 GPU 服务器开发，而本机界面不变。

#### JupyterLab

Notebook 环境。适合以下运控场景：调参时边改边看曲线结果、推导运动学公式并即时验证、记录实验过程（代码 + 图 + 分析文字在一起）。与纯脚本相比，它能逐格执行，方便逐步定位问题。

---

### 点云与三维可视化

#### Open3D

最常用的点云处理库。在机器人感知流程中，激光雷达或深度相机产出的原始点云需要经过下采样（降低计算量）、离群点去除（去掉噪声）、法向量估计（为后续配准或建图提供方向信息）、ICP 配准（把不同帧的点云对齐到同一坐标系）等操作。Open3D 提供了这一整套流程，同时内置交互式窗口可以边开发边看中间结果。

#### Rerun

多模态时序可视化框架。运控调试时，问题往往是「某一时刻点云、图像、位姿同时出了问题」，需要把这些数据对齐到同一时间轴上看。Rerun 支持把点云、RGB 图、位姿变换、包围框等打上时间戳同步录制，开发时实时流式查看，也可以录制为 `.rrd` 文件事后回放分析，定位是感知还是控制的问题。

#### Viser

基于 WebGL 的浏览器实时 3D 可视化服务。适合在 Python 脚本里直接推送机器人的关节姿态、坐标系变换树、碰撞体等，在浏览器里实时看效果。常用于：在线调试逆运动学结果是否合理、验证规划出来的轨迹在空间中的形状、展示多传感器坐标系关系。无需安装 ROS 或任何外部 GUI 框架。

#### MeshCat

轻量级浏览器 3D 可视化。功能上比 Viser 更精简，设计上与 Pinocchio、PyDrake 深度集成。典型用途：用 Pinocchio 跑正运动学后，把每个链杆的 mesh 推到 MeshCat 看姿态是否正确；播放关节空间轨迹的动画验证。

#### CloudCompare

桌面端点云 GUI 工具。适合离线场景：拿到一批 `.pcd`/`.las` 文件需要人工检查建图质量、做点到面距离评估、切截面对比，不需要写代码，直接拖文件进窗口操作即可。常用于现场采集后的数据质检和精度报告生成。

---

### 机器人算法与仿真

#### Pinocchio

刚体运动学与动力学计算库。运控算法中最核心的计算工作之一就是：给定关节角度，计算末端位姿（正运动学）；给定末端目标，求解关节角度（逆运动学）；计算质量矩阵、科氏力、重力项（逆动力学）；计算雅可比矩阵（速度/力映射）。Pinocchio 支持从 URDF 文件加载机器人，实现上述计算，性能高、精度好，是学术界和工业界的标准选择。

#### PyBullet

轻量物理仿真引擎。无需 GPU，Mac 直接跑。适合早期原型验证：把运控算法写好后先接入 PyBullet 仿真，验证力矩控制回路、关节轨迹跟踪、碰撞检测逻辑是否正确，再去接真机或高保真仿真器。

#### MuJoCo

高精度刚体物理仿真引擎（DeepMind 出品，现已开源）。Mac 原生支持 Apple Silicon Metal 渲染，性能好。相比 PyBullet，接触力建模更精确，适合强化学习训练（并行仿真）、精密操作任务仿真（夹持、装配）、MPC 控制器的仿真验证。运控工程里通常的分工是：PyBullet 做快速概念验证，MuJoCo 做精细验证，再到真机。

#### CasADi

非线性优化与自动微分框架。在模型预测控制（MPC）中，每个控制周期都需要求解一个带约束的非线性优化问题（最优化未来 N 步的控制序列）。CasADi 负责建立这个问题的数学模型（目标函数 + 动力学约束 + 关节限位约束），调用 IPOPT 等求解器求解，并通过自动微分高效计算梯度。运控里的轨迹优化、在线 MPC 都经常用它。

#### python-control

经典控制工具箱。用于设计和分析 PID、LQR、状态空间等控制器：画 Bode 图看系统频率特性、设计 LQR 增益矩阵、验证系统稳定裕度。在把算法部署到实机之前，先用它做理论层面的稳定性分析和增益调试是标准流程。

---

### 数据调试

#### Foxglove Studio

类似 RViz 的桌面可视化工具，消费 MCAP 或 ROS2 bag 格式的时序数据。适合：查看真机运行时记录下来的传感器数据（激光扫描、关节状态、IMU、相机），用时序 Panel 对比控制指令与实际响应的误差，用 3D Panel 可视化 TF 坐标系变换树和点云。无需启动 ROS 进程，直接打开录制文件就能交互分析。

#### PlotJuggler

轻量级信号时序曲线工具。Mac 从 GitHub Releases 下载 `.dmg` 安装（[下载页](https://github.com/facontidavide/PlotJuggler/releases)，Apple Silicon 选 `arm64`，Intel 选 `x64`）。适合把多条关节角速度、力矩、控制误差、速度指令曲线叠加对比，支持缩放同步、导入 CSV/MCAP，定位震荡、延迟、饱和等控制问题，比 matplotlib 交互性强得多。

---

## 3. 环境安装

### 3.1 Homebrew（已安装可跳过）

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
brew --version
```

> Intel Mac 路径是 `/usr/local`，其余步骤一致。

### 3.2 Miniforge（已安装可跳过）

- 下载页：[https://github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases)
- Apple Silicon 选 `arm64` 安装包，Intel 选 `x86_64`

```bash
bash ~/Downloads/Miniforge3-MacOSX-arm64.sh
source ~/.zshrc
conda --version
```

### 3.3 创建环境

```bash
conda create -n robot-dev python=3.11 -y
conda activate robot-dev
```

### 3.4 安装 Python 依赖

```bash
python -m pip install --upgrade pip
python -m pip install numpy scipy sympy matplotlib seaborn
python -m pip install open3d rerun-sdk viser meshcat
python -m pip install yourdfpy pybullet mujoco
python -m pip install casadi control jupyterlab
```

### 3.5 安装系统工具（可选）

```bash
brew install --cask cloudcompare
brew install git gh
```

- Foxglove Studio: [https://foxglove.dev/download](https://foxglove.dev/download)
- PlotJuggler: [https://github.com/facontidavide/PlotJuggler/releases](https://github.com/facontidavide/PlotJuggler/releases)
  - Apple Silicon 选 `arm64.dmg`，Intel 选 `x64.dmg`

### 3.6 安装 Pinocchio

```bash
conda install pinocchio -c conda-forge -y
```

---

## 4. 运行示例（环境验收）

以下命令都在 `mac-robotics-dev-setup` 根目录执行：

### open3d_quickstart.py

```bash
python example/scripts/open3d_quickstart.py
```

读取 `example/data/cube_points.pcd`（一个 1×1×1 立方体的均匀采样点云），将其着色为蓝色，在 Open3D 交互窗口里展示。可以用鼠标旋转、缩放。这一步验证 Open3D 的 GUI 渲染链路是否正常。

---

### open3d_processing_icp_demo.py

```bash
python example/scripts/open3d_processing_icp_demo.py
```

读取 `example/data/two_clusters.pcd`（两个稀疏点群），演示完整的点云处理流程：

1. 体素下采样：降低点云密度，减少计算量
2. 统计离群点去除：剔除偏离均值过远的噪声点
3. 构造人工偏移的目标点云（模拟未对齐的两帧数据）
4. 运行 ICP 精配准，输出配准质量指标（fitness、inlier_rmse）和估计的变换矩阵

弹出两个窗口，分别展示 ICP 前后的对齐效果。这是感知模块中「点云帧对帧配准」的最小实现。

---

### rerun_pointcloud_demo.py

```bash
python example/scripts/rerun_pointcloud_demo.py
```

使用 Rerun 记录两类数据：

- `world/pcd`：来自 `two_clusters.pcd` 的点云
- `world/robot_pose`：一个固定的 SE(3) 位姿，加上一条方向箭头

Rerun Viewer 会自动打开，在浏览器或桌面窗口里同时显示点云与坐标系，模拟「传感器点云 + 机器人位姿」的多模态可视化场景，这是运控调试里最常用的组合。

---

### viser_pointcloud_demo.py

```bash
python example/scripts/viser_pointcloud_demo.py
```

启动 Viser HTTP 服务（默认端口 8080），将 `cube_points.pcd` 以蓝色点云推到浏览器中展示，同时添加一个世界坐标系轴。用浏览器打开 `http://localhost:8080` 即可交互查看。这演示了不借助任何 ROS 环境，直接在 Python 脚本里把 3D 数据推到浏览器的流程——常用于调试坐标系变换和规划结果。

---

### meshcat_pointcloud_demo.py

```bash
python example/scripts/meshcat_pointcloud_demo.py
```

打开 MeshCat 浏览器窗口，展示两样东西：

- `world/points`：来自 `two_clusters.pcd` 的绿色点云
- `world/ref_box`：一个参考盒子（位移偏置），模拟障碍物或工具

这演示了 MeshCat 混合展示点云与几何体的能力，常配合 Pinocchio 把机器人链杆 mesh 和环境障碍物一起展示。

---

### trajectory_plot_demo.py

```bash
python example/scripts/trajectory_plot_demo.py
```

读取 `example/data/trajectory_xy.csv`（一段二维轨迹时序数据），绘制两张图：

- 左：XY 平面轨迹图（空间路径）
- 右：x(t)、y(t) 时序曲线（各轴随时间的变化）

模拟运控开发中最基本的结果可视化需求：验证规划出来的路径是否合理、对比指令轨迹与实际轨迹的误差分布。

---

### trajectory_3d_viz.py

```bash
# Matplotlib 静态可视化（默认）
python example/scripts/trajectory_3d_viz.py

# Rerun 交互式可视化（可播放时间轴）
python example/scripts/trajectory_3d_viz.py --rerun
```

在三维空间中生成一段 **Lemniscate（∞ 字形）叠加垂直振荡**的参数化轨迹，模拟机器人末端执行器的 Cartesian 规划路径，并在两种后端中可视化：

**Matplotlib 模式**（默认）弹出三张子图：

- 左：三维空间路径 + 起点/终点标记 + 速度方向箭头（橙色），直观展示路径形状和运动方向
- 中：x(t)、y(t)、z(t) 位置时序曲线，对应轨迹跟踪中的参考信号
- 右：vx(t)、vy(t)、vz(t) 速度时序曲线及合速度 |v|(t)，用于检查速度连续性和峰值

**Rerun 模式**（`--rerun`）在交互式 Viewer 中展示：

- `world/path`：整条路径折线
- `world/end_effector`：随时间轴变化的 SE(3) 末端位姿（红/绿/蓝三轴箭头代表局部坐标系三个轴方向）

拖动时间轴可播放末端执行器沿轨迹移动的动画，完整模拟「规划轨迹 + 末端位姿」在运控调试中的可视化需求。

---

## 5. 常见问题

### `ModuleNotFoundError: No module named 'rerun'`

`rerun` 的 pip 包名是 `rerun-sdk`（导入时用 `import rerun`，安装时包名不同）：

```bash
conda activate robot-dev
python -m pip install rerun-sdk
python -c "import rerun; print(rerun.__version__)"
```

### `python: can't open file ... scripts/xxx.py`

从根目录执行时路径要带 `example/`：

```bash
python example/scripts/open3d_quickstart.py
```

### Open3D 没有弹窗

确认在本机图形界面终端（不是纯 SSH）运行，或尝试升级：

```bash
python -m pip install --upgrade open3d
```

### Viser / MeshCat 端口占用

```bash
lsof -i :8080
lsof -i :7000
kill -9 <PID>
```
