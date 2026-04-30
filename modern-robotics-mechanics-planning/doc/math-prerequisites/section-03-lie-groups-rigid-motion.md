# 03. 李群与刚体运动卡片（SO(3)/SE(3)/twist）

## 1. \(SO(3)\)：三维旋转群

### 定义

$$
SO(3)=\{R\in\mathbb{R}^{3\times3}\mid R^TR=I,\det(R)=1\},\quad \dim=3.
$$

### 直觉

\(SO(3)\) 收集了所有“三维纯旋转”。它不是线性空间，但能做群运算（乘法与逆）。

### 机器人语境

- 末端姿态；
- IMU 姿态传播；
- 相机外参旋转块。

---

## 2. \(SE(3)\)：三维刚体位姿群

### 定义

$$
T=
\begin{bmatrix}
R & p\\
0 & 1
\end{bmatrix},
\quad R\in SO(3),\ p\in\mathbb{R}^3,\ \dim=6.
$$

### 群运算

$$
T_1T_2=
\begin{bmatrix}
R_1R_2 & R_1p_2+p_1\\
0 & 1
\end{bmatrix}.
$$

$$
T^{-1}=
\begin{bmatrix}
R^T & -R^Tp\\
0 & 1
\end{bmatrix}.
$$

### 直觉

把“旋转 + 平移”绑定成单个对象，便于链式复合。

### 机器人语境

- 连杆坐标变换；
- 手眼标定；
- 里程计位姿拼接。

---

## 3. 李代数 \(\mathfrak{so}(3)\)、\(\mathfrak{se}(3)\)

### \(\mathfrak{so}(3)\)

由 3x3 反对称矩阵组成：
$$
\omega^\wedge=
\begin{bmatrix}
0 & -\omega_3 & \omega_2\\
\omega_3 & 0 & -\omega_1\\
-\omega_2 & \omega_1 & 0
\end{bmatrix}.
$$

满足
$$
\omega^\wedge v=\omega\times v.
$$

### \(\mathfrak{se}(3)\)

twist \(\xi=[v;\omega]\) 的矩阵表示：
$$
\xi^\wedge=
\begin{bmatrix}
\omega^\wedge & v\\
0 & 0
\end{bmatrix}.
$$

### 直觉

李代数是群在单位元附近的“局部线性化坐标”。

### 机器人语境

- 小量增量更新；
- 非线性优化中的误差状态参数化；
- 姿态/位姿对数映射。

---

## 4. 指数映射与 Rodrigues

### 定义

指数映射把代数元素映射到群元素：
$$
\exp:\mathfrak{so}(3)\to SO(3),\quad
\exp:\mathfrak{se}(3)\to SE(3).
$$

### Rodrigues（\(\theta=\|\omega\|\)）

$$
\exp(\omega^\wedge)=
I+\frac{\sin\theta}{\theta}\omega^\wedge
+\frac{1-\cos\theta}{\theta^2}(\omega^\wedge)^2.
$$

### 直觉

“沿瞬时角速度方向积分一小段时间”得到有限旋转。

### 机器人语境

- IMU 积分；
- 姿态插值；
- PoE 公式中的关节指数积。

---

## 5. twist、空间/本体速度与雅可比

### 定义

- 空间速度 \(V_s\)：以世界坐标表示；
- 本体速度 \(V_b\)：以末端坐标表示。

### 直觉

同一运动可在不同观察坐标系下表达，分量不同但几何运动一致。

### 机器人语境

- 空间雅可比 \(J_s\) 与本体雅可比 \(J_b\) 对应不同控制/建模习惯；
- 推导前必须先固定约定，否则后续全错。

---

## 6. Adjoint（伴随）

### 定义

对 \(T=\begin{bmatrix}R&p\\0&1\end{bmatrix}\in SE(3)\)，
$$
\mathrm{Ad}_T=
\begin{bmatrix}
R & 0\\
p^\wedge R & R
\end{bmatrix}.
$$

### 作用

- twist 换系：\(V_s=\mathrm{Ad}_T V_b\)（具体符号依约定可能有逆）；
- wrench 换系：对偶形式与 \(\mathrm{Ad}\) 相关。

### 直觉

它是“同一几何速度在不同坐标系下的换算器”。

### 机器人语境

- 空间/本体雅可比转换；
- 力与速度在多坐标系耦合时的统一表达。

---

## 7. 李括号与 BCH（先会用结论）

### 李括号

$$
[X,Y]=XY-YX.
$$

反映“先做 \(X\) 再做 \(Y\)”与“先做 \(Y\) 再做 \(X\)”的差异。

### BCH（叙述级）

$$
\log(\exp(X)\exp(Y))
=
X+Y+\frac12[X,Y]+\cdots
$$

用于处理小量复合和误差传播近似。

### 机器人语境

- 误差状态滤波；
- 李群优化迭代中的增量合成。
