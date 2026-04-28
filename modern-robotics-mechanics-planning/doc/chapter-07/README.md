# 第7章 Kinematics of Closed Chains（闭链机构运动学）

## 本章核心问题

- 本章回答：闭链机构运动学在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 并联机构正逆运动学](./section-01-parallel-ik-fk.md)
- [02. 微分运动学](./section-02-differential-kinematics.md)
- [03. 闭链奇异性](./section-03-singularity.md)

## 本章最重要 5 个术语

- `closed chain`：存在回路约束的机构拓扑。
- `parallel mechanism`：多个支链并联支撑同一动平台的机构。
- `constraint Jacobian`：约束方程对速度变量的一阶线性化。
- `Stewart platform`：典型6自由度并联平台机构。
- `singularity`：雅可比降秩导致运动/受力能力退化的状态。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
