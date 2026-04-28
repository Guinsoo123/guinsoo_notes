# 第3章 Rigid-Body Motions（刚体运动）

## 本章核心问题

- 本章回答：刚体运动在机器人建模/规划/控制链路中的作用是什么。
- 重点把术语与可计算关系对应起来，而不是死记公式。

## 小节导航

- [01. 平面刚体运动](./section-01-planar-motions.md)
- [02. 旋转与角速度](./section-02-rotations-angular-vel.md)
- [03. 齐次变换与Twist](./section-03-homogeneous-twists.md)
- [04. 指数坐标表示](./section-04-exponential-coordinates.md)
- [05. Wrench 与力学表示](./section-05-wrenches.md)

## 本章最重要 5 个术语

- `SE(3)（三维特殊欧式群）`：空间刚体位姿群，含三个旋转和三个平移自由度。
- `SO(3)（三维旋转群）`：三维旋转矩阵构成的李群。
- `twist（速度旋量）`：刚体瞬时速度的6维表示。
- `wrench（力旋量）`：力与力矩组成的6维广义力。
- `Adjoint（伴随变换）`：用于变换twist和wrench的伴随矩阵。

## 本章易错点

- 只记术语名字，不理解变量与坐标系语义。
- 忽略“适用条件”，把局部结论错误外推。
