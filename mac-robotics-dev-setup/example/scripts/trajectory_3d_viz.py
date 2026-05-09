"""trajectory_3d_viz.py

三维空间路径与轨迹可视化示例。

轨迹形状：三维 Lemniscate（∞ 字形）叠加垂直振荡，模拟机器人末端执行器的
Cartesian 规划路径。脚本会在路径上均匀采样位姿，以切线方向为 x 轴构造
SE(3) 变换，展示"路径 + 速度方向 + 末端位姿" 的完整可视化。

支持两种可视化后端（通过命令行切换）：
  Matplotlib —— 默认，弹出静态 3D 图窗口，不需要额外依赖
  Rerun      —— 交互式，可播放时间轴上的末端位姿动画

运行方式（从 mac-robotics-dev-setup 根目录）：
    python example/scripts/trajectory_3d_viz.py           # Matplotlib
    python example/scripts/trajectory_3d_viz.py --rerun   # Rerun 模式
"""

from __future__ import annotations

import argparse
import time

import numpy as np


# ─────────────────────────────────────────────────────────────────
# 轨迹生成
# ─────────────────────────────────────────────────────────────────

def generate_trajectory(n: int = 300) -> dict:
    """生成三维 Lemniscate 轨迹（∞ 字形 + 高度振荡）。

    Returns dict with keys:
        t, x, y, z        — 时间与位置
        vx, vy, vz        — 速度分量
        tx, ty, tz        — 单位切线向量（用于构造末端位姿）
    """
    t = np.linspace(0, 2 * np.pi, n)

    # Lemniscate of Bernoulli（参数形式）
    denom = 1.0 + np.sin(t) ** 2
    x = np.cos(t) / denom
    y = np.sin(t) * np.cos(t) / denom
    z = 0.28 * np.sin(2 * t)           # 垂直振荡，幅值 ±0.28 m

    # 数值微分得速度
    dt = t[1] - t[0]
    vx = np.gradient(x, dt)
    vy = np.gradient(y, dt)
    vz = np.gradient(z, dt)

    # 单位切线方向
    speed = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2) + 1e-9
    tx, ty, tz = vx / speed, vy / speed, vz / speed

    return dict(t=t, x=x, y=y, z=z, vx=vx, vy=vy, vz=vz, tx=tx, ty=ty, tz=tz)


def rotation_from_tangent(tangent: np.ndarray) -> np.ndarray:
    """以切线方向为 x 轴构造旋转矩阵 (3×3)，模拟末端执行器朝向。"""
    xaxis = tangent / (np.linalg.norm(tangent) + 1e-9)
    ref = np.array([0.0, 0.0, 1.0]) if abs(xaxis[2]) < 0.9 else np.array([0.0, 1.0, 0.0])
    yaxis = np.cross(ref, xaxis)
    yaxis /= np.linalg.norm(yaxis) + 1e-9
    zaxis = np.cross(xaxis, yaxis)
    return np.column_stack([xaxis, yaxis, zaxis])


# ─────────────────────────────────────────────────────────────────
# Matplotlib 可视化
# ─────────────────────────────────────────────────────────────────

def viz_matplotlib(traj: dict) -> None:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 — 注册 3D 投影

    t, x, y, z = traj["t"], traj["x"], traj["y"], traj["z"]
    vx, vy, vz = traj["vx"], traj["vy"], traj["vz"]
    speed = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

    fig = plt.figure(figsize=(15, 5))

    # ── 左：三维空间路径 ──────────────────────────────────────────
    ax3d = fig.add_subplot(131, projection="3d")
    ax3d.plot(x, y, z, linewidth=1.8, color="royalblue", label="path")
    ax3d.scatter(x[0], y[0], z[0], color="green", s=80, zorder=5, label="start")
    ax3d.scatter(x[-1], y[-1], z[-1], color="red", s=80, zorder=5, label="end")

    # 每隔约 1/12 个周期画一个速度方向箭头
    stride = max(1, len(t) // 12)
    scale = 0.10
    ax3d.quiver(
        x[::stride], y[::stride], z[::stride],
        vx[::stride] / (speed[::stride] + 1e-9) * scale,
        vy[::stride] / (speed[::stride] + 1e-9) * scale,
        vz[::stride] / (speed[::stride] + 1e-9) * scale,
        color="orange", linewidth=1.2, label="direction",
    )

    ax3d.set_title("3D Path  (Lemniscate + Z oscillation)")
    ax3d.set_xlabel("X (m)")
    ax3d.set_ylabel("Y (m)")
    ax3d.set_zlabel("Z (m)")
    ax3d.legend(fontsize=7)

    # ── 中：XYZ 位置时序 ─────────────────────────────────────────
    ax_pos = fig.add_subplot(132)
    ax_pos.plot(t, x, label="x(t)", linewidth=1.5)
    ax_pos.plot(t, y, label="y(t)", linewidth=1.5)
    ax_pos.plot(t, z, label="z(t)", linewidth=1.5)
    ax_pos.set_title("Position — time series")
    ax_pos.set_xlabel("t  (s)")
    ax_pos.set_ylabel("m")
    ax_pos.legend()
    ax_pos.grid(True, linestyle="--", alpha=0.4)

    # ── 右：速度时序 ──────────────────────────────────────────────
    ax_vel = fig.add_subplot(133)
    ax_vel.plot(t, vx, label="vx(t)", linewidth=1.5)
    ax_vel.plot(t, vy, label="vy(t)", linewidth=1.5)
    ax_vel.plot(t, vz, label="vz(t)", linewidth=1.5)
    ax_vel.plot(t, speed, "k--", label="|v|(t)", linewidth=1.2)
    ax_vel.set_title("Velocity — time series")
    ax_vel.set_xlabel("t  (s)")
    ax_vel.set_ylabel("m/s")
    ax_vel.legend()
    ax_vel.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────────────────────────
# Rerun 可视化
# ─────────────────────────────────────────────────────────────────

def viz_rerun(traj: dict) -> None:
    import rerun as rr

    rr.init("trajectory_3d", spawn=True)

    t, x, y, z = traj["t"], traj["x"], traj["y"], traj["z"]
    tx, ty, tz = traj["tx"], traj["ty"], traj["tz"]

    positions = np.column_stack([x, y, z]).astype(np.float32)

    # 整条路径一次性作为折线写入（不绑定时间轴）
    rr.log("world/path", rr.LineStrips3D([positions], colors=[[30, 120, 255]]))

    # 起点 / 终点标记
    rr.log("world/start", rr.Points3D([[x[0], y[0], z[0]]], colors=[[0, 210, 0]], radii=0.025))
    rr.log("world/end",   rr.Points3D([[x[-1], y[-1], z[-1]]], colors=[[220, 40, 0]], radii=0.025))

    # 沿轨迹逐帧记录末端位姿，绑定时间轴 → Rerun 可播放动画
    stride = max(1, len(t) // 100)
    for i in range(0, len(t), stride):
        rr.set_time_seconds("timeline", float(t[i]))

        rot = rotation_from_tangent(np.array([tx[i], ty[i], tz[i]]))
        pos = [float(x[i]), float(y[i]), float(z[i])]

        # 末端执行器坐标系
        rr.log(
            "world/end_effector",
            rr.Transform3D(translation=pos, mat3x3=rot.tolist()),
        )

        # 三轴箭头（红=切线 X，绿=副法线 Y，蓝=法线 Z）
        arrow_scale = 0.07
        rr.log(
            "world/end_effector/axes",
            rr.Arrows3D(
                origins=[[0, 0, 0]] * 3,
                vectors=[
                    (rot[:, 0] * arrow_scale).tolist(),
                    (rot[:, 1] * arrow_scale).tolist(),
                    (rot[:, 2] * arrow_scale).tolist(),
                ],
                colors=[[220, 40, 40], [40, 200, 40], [40, 80, 220]],
            ),
        )

    print("Rerun viewer launched.")
    print("拖动时间轴可播放末端位姿动画，按 Ctrl+C 退出。")
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nExit.")


# ─────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="三维轨迹可视化示例")
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="使用 Rerun 交互式可视化（默认使用 Matplotlib）",
    )
    args = parser.parse_args()

    traj = generate_trajectory(n=300)

    if args.rerun:
        viz_rerun(traj)
    else:
        viz_matplotlib(traj)


if __name__ == "__main__":
    main()
