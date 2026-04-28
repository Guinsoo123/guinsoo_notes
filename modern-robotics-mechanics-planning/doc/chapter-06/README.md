# 第6章 Inverse Kinematics（逆运动学）

## 本章核心问题

- 本章回答：逆运动学在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 解析逆解](./section-01-analytic-ik.md)
- [02. 数值逆解](./section-02-numerical-ik.md)
- [03. 逆速度运动学](./section-03-inverse-velocity.md)
- [04. 闭环机构逆解注记](./section-04-closed-loop-note.md)

## 本章最重要 5 个术语

- `inverse kinematics（逆运动学）`：本章关键概念。
- `analytic IK（解析逆运动学）`：通过代数消元得到闭式逆解的方法。
- `iterative IK（迭代逆运动学）`：通过迭代逐步逼近目标位姿的逆解法。
- `pseudoinverse（伪逆）`：对非方阵或奇异矩阵求最小二乘逆的算子。
- `redundancy（冗余）`：自由度高于任务维度导致解不唯一。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
