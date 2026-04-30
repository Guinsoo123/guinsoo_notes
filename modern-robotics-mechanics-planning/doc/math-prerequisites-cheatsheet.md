# 数学先修速查（考前 5 分钟版）

> 用途：考试/推导前快速激活记忆。  
> 原则：只放“高频定义 + 高频公式 + 高频坑点”。  
> 详细解释见：[数学先修指南（完整版）](./math-prerequisites.md)。

---

## 0. 一眼先看这 10 条

1. 维度规则：\(A_{m\times n}B_{n\times p}=C_{m\times p}\)。
2. 乘法顺序：\(AB\) 表示先 \(B\) 后 \(A\)。
3. 一般不交换：\(AB\neq BA\)。
4. 结合律成立：\((AB)C=A(BC)\)。
5. 旋转矩阵：\(R^TR=I,\ \det(R)=1,\ R^{-1}=R^T\)。
6. 齐次变换：\(T=\begin{bmatrix}R&p\\0&1\end{bmatrix}\in SE(3)\)。
7. 齐次逆：\(T^{-1}=\begin{bmatrix}R^T&-R^Tp\\0&1\end{bmatrix}\)。
8. hat 映射：\(\omega^\wedge v=\omega\times v\)。
9. 姿态微分：\(\dot R=R[\omega]_b=[\omega]_sR\)（取决于坐标约定）。
10. 速度雅可比：\(V=J(q)\dot q,\ \tau=J^TF\)。

---

## 1. 高频定义（最小记忆）

### \(SO(3)\)：旋转群

$$
SO(3)=\{R\in\mathbb{R}^{3\times3}\mid R^TR=I,\det(R)=1\},\quad \dim=3
$$

### \(SE(3)\)：刚体位姿群

$$
SE(3)=\left\{
\begin{bmatrix}R&p\\0&1\end{bmatrix}
\middle|
R\in SO(3),p\in\mathbb{R}^3
\right\},\quad \dim=6
$$

### \(\mathfrak{so}(3)\)、\(\mathfrak{se}(3)\)：李代数

- \(\mathfrak{so}(3)\)：3x3 反对称矩阵空间。
- \(\mathfrak{se}(3)\)：刚体瞬时运动（twist）的矩阵表示空间。

---

## 2. 高频公式（必会手写）

### 矩阵乘法元素式

$$
(AB)_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}
$$

### Rodrigues 公式（\(\omega\in\mathbb{R}^3,\ \theta=\|\omega\|\)）

$$
\exp(\omega^\wedge)=I+\frac{\sin\theta}{\theta}\omega^\wedge+\frac{1-\cos\theta}{\theta^2}(\omega^\wedge)^2
$$

### \(SE(3)\) 复合与逆

$$
\begin{bmatrix}R_1&p_1\\0&1\end{bmatrix}
\begin{bmatrix}R_2&p_2\\0&1\end{bmatrix}
=
\begin{bmatrix}R_1R_2&R_1p_2+p_1\\0&1\end{bmatrix}
$$

$$
\begin{bmatrix}R&p\\0&1\end{bmatrix}^{-1}
=
\begin{bmatrix}R^T&-R^Tp\\0&1\end{bmatrix}
$$

### 速度映射

$$
V=J(q)\dot q,\qquad \tau=J^TF
$$

---

## 3. 坐标系速判（space/body 不混）

- **空间速度 \(V_s\)**：在基坐标系表达。
- **本体速度 \(V_b\)**：在末端坐标系表达。
- 同一运动在不同系的表达通过伴随 \(\mathrm{Ad}_T\) 互换。
- 写公式前先写清：变量“属于哪个坐标系”。

---

## 4. 五个最常见扣分点

1. 把矩阵乘法写成逐元素乘法。
2. 变换链顺序写反（把“先右后左”写错）。
3. 忘记检查维度是否可乘。
4. 把 \(R^{-1}\) 写错（应为 \(R^T\)）。
5. space/body 变量混用，导致雅可比或动力学式整体错位。

---

## 5. 考前 5 分钟复习流程

1. 先背 10 条总览（第 0 节）。
2. 手写 4 个核心式：矩阵乘法元素式、Rodrigues、\(T^{-1}\)、\(V=J\dot q\)。
3. 口头检查一次：\(SO(3)\) 与 \(SE(3)\) 的定义和维数。
4. 最后提醒自己：先约定坐标系，再推导。

---

## 6. 一页跳转

- 完整版（定义+直觉+学习路线）：[数学先修指南（刚体运动与现代机器人）](./math-prerequisites.md)
- 实战章节入口：[chapter-03 刚体运动](./chapter-03/README.md)
