# 04. 经典教程与 30 天学习计划

## 1. 经典教程（按用途）

### 线性代数

- MIT OCW 18.06 Linear Algebra  
  <https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/>
- MIT 18.06 主页  
  <https://web.mit.edu/18.06/www/>
- 3Blue1Brown 直觉系列  
  <https://www.3blue1brown.com/essence-of-linear-algebra>

### 多元微积分

- MIT OCW 18.02  
  <https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/>
- MIT OCW 18.02SC  
  <https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/>

### 常微分方程

- MIT OCW 18.03  
  <https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/>
- MIT OCW 18.03SC  
  <https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/>

### 李群（机器人向）

- Modern Robotics 官网  
  <http://www.modernrobotics.org/>
- Modern Robotics 预印本（v2）  
  <https://hades.mech.northwestern.edu/images/2/25/MR-v2.pdf>
- Ethan Eade Lie Groups  
  <https://www.ethaneade.com/lie.pdf>
- Solà: A micro Lie theory  
  <https://arxiv.org/abs/1812.01537>

---

## 2. 30 天计划（最小可执行）

### 第 1 周：线代重置

- 输入：矩阵乘法、正交、行列式、特征值。
- 输出：能独立解释 \(R^{-1}=R^T\) 与 \(\det(R)=1\)。

### 第 2 周：微积分与雅可比

- 输入：偏导、链式法则、线性化。
- 输出：能从 \(x(q)\) 推到 \(\dot x=J(q)\dot q\)。

### 第 3 周：\(SO(3)\) 与指数映射

- 输入：hat/vee、Rodrigues、\(\log(R)\) 直觉。
- 输出：能完成角速度到姿态的离散更新。

### 第 4 周：\(SE(3)\)、twist、Adjoint

- 输入：齐次变换逆、PoE、伴随。
- 输出：能解释空间/本体速度转换并手写核心式。

---

## 3. 使用策略（避免“看过但不会用”）

1. 主线课只选 1 门，直觉课选 1 门。
2. 每学一个定义，立刻做一个机器人映射例子。
3. 每周两次“闭卷复写”：
   - Rodrigues；
   - \(T^{-1}\)；
   - \(V=J\dot q\)；
   - \(\mathrm{Ad}_T\) 形式。
