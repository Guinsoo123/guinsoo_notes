# 第2章 Configuration Space（构型空间）

## 本章核心问题

- 本章回答：构型空间在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 刚体自由度](./section-01-rigid-body-dof.md)
- [02. 机器人自由度与关节](./section-02-robot-dof.md)
- [03. 构型空间拓扑与表示](./section-03-topology-representation.md)
- [04. 构型与速度约束](./section-04-constraints.md)
- [05. 任务空间与工作空间](./section-05-task-workspace.md)

## 本章最重要 5 个术语

- `configuration space（构型空间）`：机器人全部可能构型构成的空间。
- `holonomic（完整约束）`：可积分为位置约束的约束类型。
- `nonholonomic（非完整约束）`：仅体现为速度约束且一般不可积分为位置约束。
- `workspace（工作空间）`：末端在物理空间可达的区域。
- `task space（任务空间）`：任务变量所在空间，如末端位姿空间。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
