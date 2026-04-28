# 第8章 Dynamics of Open Chains（开链动力学）

## 本章核心问题

- 本章回答：开链动力学在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 拉格朗日建模](./section-01-lagrangian.md)
- [02. 单刚体动力学](./section-02-single-body-dynamics.md)
- [03. Newton-Euler逆动力学](./section-03-ne-inverse-dynamics.md)
- [04. 闭式动力学方程](./section-04-closed-form-dynamics.md)
- [05. 正动力学](./section-05-forward-dynamics.md)
- [06. 任务空间动力学](./section-06-task-space-dynamics.md)
- [07. 受约束动力学](./section-07-constrained-dynamics.md)
- [08. 执行器与摩擦](./section-08-actuation-friction.md)

## 本章最重要 5 个术语

- `mass matrix（质量矩阵）`：描述关节惯性耦合的对称正定矩阵。
- `inverse dynamics（逆动力学）`：由运动求驱动力矩的问题。
- `forward dynamics（正动力学）`：由力矩求加速度的问题。
- `Coriolis（科里奥利项）`：速度耦合引起的惯性项总称。
- `friction model（摩擦模型）`：描述粘滞、库伦等摩擦效应的模型。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
