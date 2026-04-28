# 第5章 Velocity Kinematics and Statics（速度运动学与静力学）

## 本章核心问题

- 本章回答：速度运动学与静力学在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 空间雅可比](./section-01-jacobian-space.md)
- [02. 本体雅可比](./section-02-jacobian-body.md)
- [03. 开链机构静力学](./section-03-statics.md)
- [04. 奇异性分析](./section-04-singularity.md)
- [05. 可操作度](./section-05-manipulability.md)

## 本章最重要 5 个术语

- `Jacobian`：关节速度到末端速度的线性映射。
- `singularity`：雅可比降秩导致运动/受力能力退化的状态。
- `manipulability`：末端速度或力可实现能力的几何度量。
- `null space`：线性映射输出为零的输入子空间。
- `wrench mapping`：末端受力映射到关节力矩的关系。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
