# 第11章 Robot Control（机器人控制）

## 本章核心问题

- 本章回答：机器人控制在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 控制系统概览](./section-01-control-overview.md)
- [02. 误差动力学](./section-02-error-dynamics.md)
- [03. 速度输入控制](./section-03-velocity-input-control.md)
- [04. 力矩输入控制](./section-04-torque-input-control.md)
- [05. 力控制/混合控制/阻抗控制](./section-05-force-hybrid-impedance.md)
- [06. 底层控制与其他主题](./section-06-low-level-other.md)

## 本章最重要 5 个术语

- `feedback`：利用测量误差实时修正控制输入。
- `error dynamics`：误差随时间演化的动力学方程。
- `computed torque`：用动力学前馈补偿的轨迹跟踪控制。
- `hybrid control`：受约束方向力控、自由方向位控的组合。
- `impedance control`：设定力-位移动态关系的交互控制。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
