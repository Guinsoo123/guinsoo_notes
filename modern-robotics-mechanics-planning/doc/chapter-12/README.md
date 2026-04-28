# 第12章 Grasping and Manipulation（抓取与操作）

## 本章核心问题

- 本章回答：抓取与操作在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 接触运动学](./section-01-contact-kinematics.md)
- [02. 接触力与摩擦](./section-02-contact-force-friction.md)
- [03. 操作策略](./section-03-manipulation.md)

## 本章最重要 5 个术语

- `contact`：本章关键概念。
- `form closure`：纯几何约束实现全向运动封闭。
- `force closure`：通过接触力可平衡任意外载荷。
- `friction cone`：摩擦力允许方向形成的锥集。
- `wrench space`：所有可实现广义力构成的空间。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
