# 第13章 Wheeled Mobile Robots（轮式移动机器人）

## 本章核心问题

- 本章回答：轮式移动机器人在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 轮式机器人类型](./section-01-types.md)
- [02. 全向轮机器人](./section-02-omni.md)
- [03. 非完整约束移动机器人](./section-03-nonholonomic.md)
- [04. 里程计](./section-04-odometry.md)
- [05. 移动操作](./section-05-mobile-manipulation.md)

## 本章最重要 5 个术语

- `WMR（轮式移动机器人）`：wheeled mobile robot，轮式移动机器人。
- `nonholonomic（非完整约束）`：仅体现为速度约束且一般不可积分为位置约束。
- `controllability（可控性）`：系统是否可由输入到达目标状态。
- `odometry（里程计）`：由轮编码器积分估计位姿的方法。
- `mobile manipulation（移动操作）`：移动底盘与机械臂协同操作。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
