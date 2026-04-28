# 第8章-03 Newton-Euler逆动力学

## 核心术语

- `recursive algorithm`
- `inverse dynamics`
- `joint torque`

## 一句话定义

- `recursive algorithm`：沿机构链前后递推的高效计算结构。
- `inverse dynamics`：由运动求驱动力矩的问题。
- `joint torque`：关节驱动器输出的力矩。

## 关键关系/公式（记忆版）

- M(q)q_ddot + C(q,q_dot)q_dot + g(q)=tau。
- 逆动力学：已知(q,q_dot,q_ddot)求tau。

## 易错点

- 混淆坐标系表达与物理对象本身。
- 未检查公式适用条件（小角度、无约束、线性化等）。

## 与前后章节的连接

- 递归算法实现高效力矩计算。
- 该节概念通常在后续算法章节中作为输入模型被重复调用。

## 30 秒复习清单

- 我能说出本节每个术语的中文含义吗？
- 我能写出本节至少一个核心关系式吗？
- 我知道本节结论会在后续哪类问题里使用吗？
