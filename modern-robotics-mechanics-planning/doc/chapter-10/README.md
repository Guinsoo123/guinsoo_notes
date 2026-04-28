# 第10章 Motion Planning（运动规划）

## 本章核心问题

- 本章回答：运动规划在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 运动规划总览](./section-01-overview.md)
- [02. 规划基础](./section-02-foundations.md)
- [03. 完备方法与栅格方法](./section-03-complete-grid.md)
- [04. 采样规划](./section-04-sampling.md)
- [05. 势场与优化](./section-05-potential-optimization.md)
- [06. 轨迹平滑](./section-06-smoothing.md)

## 本章最重要 5 个术语

- `motion planning`：在障碍和约束下寻找无碰路径。
- `collision detection`：判断构型或路径是否与障碍相交。
- `RRT`：快速随机树，偏探索性强。
- `PRM`：先采样建图后查询的概率路图法。
- `potential field`：通过势能梯度生成导航方向。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
