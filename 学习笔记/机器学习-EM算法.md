<!--toc-->

- [EM算法](#em算法)
	- [从极大似然法说起-一个简单的例子](#从极大似然法说起-一个简单的例子)
	- [从极大似然法说起-一个稍微复杂点的例子-三硬币模型](#从极大似然法说起-一个稍微复杂点的例子-三硬币模型)
	- [EM算法的具体步骤 和 隐变量](#em算法的具体步骤-和-隐变量)
	- [EM算法的证明](#em算法的证明)
	- [其他](#其他)
	- [EM算法的应用-高斯混合聚类](#em算法的应用-高斯混合聚类)

<!-- tocstop -->
# EM算法
EM算法(期望最大化算法,Expectation Maximization Algorithm)是一种迭代算法,用于隐变量(hidden variable)的概率模型参数的极大似然估计,或极大后延概率估计。


在存在隐变量的情况,由于隐变量未知,以下为似然函数
$LL(X|\theta) = \displaystyle{\sum_{i = 1}^m} \ln \displaystyle{\sum_z} P(X,z|\theta)$
令其导数为0,由于$\ln$ 后面的 $\Sigma$ 和 $P$ 本身的复杂性,导致解析解难以求出。

而在完全数据的情况下,我们能很轻易地计算出解析解。
$LL(X,Z|\theta) = \displaystyle{\sum_{i = 1}^m} \ln P(X,Z|\theta) = \displaystyle{\sum_{i = 1}^m} \ln P(Z)P(X|\theta,Z)$

EM算法的核心思想是:使用$z_i$的期望(或者使用所用的$z_i$,不同的$z_i$赋予不同的权重)来代替缺失的$Z$隐变量的数据,这样就能使用完全数据的计算方法来计算。
(这么近似处理之后,表达式就变成了似然函数关于$Z$的后验概率的期望)

EM算法有几个要点:
1. 是上面提到的,通过构造$z_i$,把计算方法转换到完全数据上来
2. 使用$Z$的后验概率,而不是其他
3. 迭代求解

EM算法主要分两个步骤:
1. E步
		这一步实际上就是求似然函数在新的参数下的表达式,具体就是求隐变量$Z$的后验概率

2. M步
		最大化似然函数的期望,具体方法就是令似然函数(或其拉格朗日形式)的导数为0

EM算法对初始值敏感,不同的初始值可能会得到不同的结果。
常用的做法是,使用多几组初始值进行迭代
(对于高斯混合模型)使用$k-means$算法进行预处理,其结果作为EM算法的初始值

k-means算法可以看成是高斯混合聚类在混合成分 方差均等、且每个样本仅指派给一个混合成分的特例加。

EM算法证明示意图:
![2]

疑问:关于PRML上的关于奇异点的描述没看明白。

## 从极大似然法说起-一个简单的例子
假设有一枚硬币,抛出硬币,其为正面的概率为p,已知m次试验的结果$\{x_1,x_2,...,x_m\}$,使用极大似然法估计参数p

一次试验的概率为:$P(x) = p^x\times(1-p)^{1-x}$

似然函数为:
$L(x_1,x_2,\ldots,x_m;p) = \displaystyle{\prod_{i = 1}^m} P(x_i) = p^{\displaystyle{\sum_{i = 1}^m} x_i}\cdot(1-p)^{m - \displaystyle{\sum_{i = 1}^m} x_i}$

则令$\frac{\partial L(x_1,x_2,\ldots,x_m;p)}{\partial p} = 0$
得:$p = \frac{ \displaystyle {\sum_{i = 1}^m} x_i}{m}$

## 从极大似然法说起-一个稍微复杂点的例子-三硬币模型
假设要有3枚硬币,分别记作A,B,C。这些硬币正面出现的概率分别为$\pi,p,q$。进行如下试验:
先抛出硬币A,根据其结果选出硬币B或C,正面选B,反面选C
然后抛出选中的硬币,如果出现正面,记作1,反面记作0

现有m次试验的结果$(Z,Y) = \{(z_1,y_1),(z_2,y_2),\ldots,(z_m,y_m)\}$,
$z_i$表示第i次试验中,抛出硬币A的结果,$y_i$表示第i次试验抛出第二枚硬币的结果,结果正面为1,反面为0
使用极大似然法估计参数$\theta = (\pi, p,q)^T$

一次试验的概率为:$P(y,z|\theta) = \pi^zp^{zy}(1-p)^{z(1-y)} \times (1-\pi)^{1-z}q^{(1-z)y}(1-q)^{(1-z)(1-y)}$

似然函数为:
$\begin{align}L(\theta|Y,Z) &= \displaystyle{\prod_{i = 1}^m} P(y_i,z_i|\theta) \\
&=  \pi^{\displaystyle {\sum_{i = 1}^m} z_i}p^{\displaystyle {\sum_{i = 1}^m}z_iy_i}(1-p)^{\displaystyle {\sum_{i = 1}^m}z_i(1-y_i)}
\\&\quad\times (1-\pi)^{\displaystyle {\sum_{i = 1}^m}(1-z_i)}q^{\displaystyle {\sum_{i = 1}^m}(1-z_i)y_i}(1-q)^{\displaystyle {\sum_{i = 1}^m}(1-z_i)(1-y_i)}\end{align}$

为简化运算,取对数形式:
$\begin{align}LL(\theta|Y,Z) &= \displaystyle{\sum_{i = 1}^m} \ln P(y_i,z_i|\theta) \\
&= \bigg (\displaystyle {\sum_{i = 1}^m} z_i\bigg ) \ln \pi +
\bigg (\displaystyle {\sum_{i = 1}^m}z_iy_i\bigg ) \ln p +
\bigg (\displaystyle {\sum_{i = 1}^m}z_i(1-y_i)\bigg ) \ln (1-p) \\
&\quad +
\bigg (\displaystyle {\sum_{i = 1}^m}(1-z_i)\bigg ) \ln (1-\pi) +
\bigg (\displaystyle {\sum_{i = 1}^m}(1-z_i)y_i\bigg ) \ln q +
\bigg (\displaystyle {\sum_{i = 1}^m}(1-z_i)(1-y_i)\bigg ) \ln (1-q)\end{align}$

$\begin{align}
\frac{\partial LL(\theta|Y,Z)}{\partial \theta} &= \begin{bmatrix}
\frac{\partial LL(\theta|Y,Z)}{\partial \pi}  \\
\frac{\partial LL(\theta|Y,Z)}{\partial p}  \\
\frac{\partial LL(\theta|Y,Z)}{\partial q}
\end{bmatrix} \\
&= \begin{bmatrix}
\frac{\displaystyle {\sum_{i = 1}^m} z_i}{\pi} - \frac{\displaystyle{\sum_{i = 1}^m} (1 - z_i)}{1 - \pi}  \\
\frac{\displaystyle {\sum_{i = 1}^m}z_iy_i}{p} - \frac{\displaystyle {\sum_{i = 1}^m}z_i(1-y_i)}{1-p}\\
\frac{\displaystyle {\sum_{i = 1}^m}z_iy_i}{q} - \frac{\displaystyle {\sum_{i = 1}^m}z_i(1-y_i)}{1-q}
\end{bmatrix}
\end{align}$

令$\frac{\partial LL(\theta|Y,Z)}{\partial \theta}=0$
得:
$\pi = \frac{ \displaystyle {\sum_{i = 1}^m} z_i}{m}$
$p = \frac{ \displaystyle {\sum_{i = 1}^m} z_iy_i}{\displaystyle {\sum_{i = 1}^m} z_i}$
$q = \frac{ \displaystyle {\sum_{i = 1}^m}  (1-z_i)y_i}{\displaystyle {\sum_{i = 1}^m} (1-z_i)}$

## EM算法的具体步骤 和 隐变量
原log似然函数:$LL(\theta|Y,Z) = \displaystyle{\sum_{i = 1}^m} \ln P(y_i,z_i|\theta)$
上面的例子中,隐变量或者说中间变量$z_i$是已知的, 但$z_i$如果是未知的,那么我们要怎么进行参数的估计?

按照上面的过程,极大似然法无法进行下去,因为我们并不知道输出的结果$y_i$到底是由B硬币生成的,还是C硬币生成的。

使用极大似然法,在完整数据求似然函数的时候,需要知道$y_i$和$z_i$(即样本的生成过程信息),但我们不知道$z_i$到底是多少,所以极大似然法无法进行下去。

在不完全数据下的计算过程:
似然函数为:$LL(X|\theta) = \displaystyle{\sum_{i = 1}^m} \ln \displaystyle{\sum_z} P(X,z|\theta)$
令这个似然函数的导数为0,并不能得到一个解析解。(PRML说的,但至少足够难运算)

那么有什么方法,既可以避开$z_i$真实值的问题,而又能使得极大似然法得以进行下去?
一个简单地想法就是使用$z_i$的期望,或者是$z_i$的概率取值来代替真实值。
这样我们就能近似得到$Z$的值,使得可以使用完全数据下的似然函数的方法来计算下去。

注意是$P(X,Z) = \displaystyle{\sum_z} q(z)P(X,z)$
或者是$P(X,Z) = P(X,E(Z))$
而不是指 $P(X) = \displaystyle{\sum_z} P(z)P(X|z)$

那么$z_i$怎么取?
这里我们采用第一种策略,并且取$z_i$的概率分布为其后验概率。(后面会证明只能是后验概率。)

如果我们知道$\theta$的值,那么我们可以轻易地得到$z_i$的分布,如果我们知道$z_i$的值,那么也可以使用极大似然法直接得到$\theta$的参数估计。

EM算法就是使用通过迭代上面提到的两个步骤来实现参数的估计的。

也就是说EM算法取当前$\theta^{(t)}$下$z_i$的后验概率作为$z_i$的概率分布。(具体表示见后面的表达式。)
然后在$z_i$的后验概率下,计算$\theta^{(t+1)}$

~~EM算法的想法就是使用隐变量$z_i$的概率取值来代替$z_i$的真实值(每个取值,以其后验概率作为权重),并且使用 **似然函数的期望** 来代替 **似然函数**~~
~~具体表现为:使用$z_i$的后验概率$P(z_i|y_i,\theta)$,来猜测$z_i$,这样就避开的$z_i$的实际取值为多少。~~
~~具体含义见期望的表达式(关于期望见后面的详细信息)。~~
~~这样就避开的z的真实取值。~~

基于上面规避$z_i$的方法,
我们得到:
$\begin{align}\theta^{(i+1)} &= \begin{matrix}
argmax \\
\theta
\end{matrix} LL(\theta|Y,Z) \\
&=
\begin{matrix}
argmax \\
\theta
\end{matrix} \displaystyle{\sum_{i = 1}^m} \ln P(y_i,z_i|\theta) &(1)\\
&\dot{=} \begin{matrix}
argmax \\
\theta
\end{matrix} \displaystyle{\sum_{i = 1}^m} \displaystyle{\sum_{z=0}^1} q(z) \ln P(y_i,z|\theta) &(2)\\
&=\begin{matrix}
argmax \\
\theta
\end{matrix} \displaystyle{\sum_{z=0}^1}\displaystyle{\sum_{i = 1}^m}  q(z) \ln P(y_i,z|\theta)&(3)\\
&=\begin{matrix}
argmax \\
\theta
\end{matrix} \displaystyle{\sum_{z=0}^1} P(z|y_i,\theta^{(t)})\bigg(\displaystyle{\sum_{i = 1}^m}   \ln P(y_i,z|\theta)\bigg)&(4)\\
&=\begin{matrix}
argmax \\
\theta
\end{matrix} E_{Z|Y,\theta^{(t)}}\bigg(LL(\theta|Y,Z)\bigg) &(5)
\end{align}$

(1):完整数据下的似然函数
(2):使用z的概率取值来近似
(3):调整一下两个求和符号的位置
(4):$q(Z)$取值为$Z$的后验概率
(5):上面的形式,可以理解成似然函数的期望
>期望:$E\bigg(\ln\big(g(x)\big)\bigg) = \displaystyle{\sum_z}P(z)\ln\big(g(x)\big)$

即从$\theta^{(i+1)} =
\begin{matrix}
argmax \\
\theta
\end{matrix} LL(\theta|Y)$
变成了
$\theta^{(i+1)} =
\begin{matrix}
argmax \\
\theta
\end{matrix} E_{Z|Y,\theta^{(t)}}\bigg(LL(\theta|Y,Z)\bigg)$

后面证明两者是等价的,我们先看EM算法的具体过程:
$\begin{align}
E_{Z|Y,\theta^{(t)}}\bigg(LL(\theta|Y,Z)\bigg)
& = E_{Z|Y,\theta^{(t)}}\bigg( \displaystyle{\sum_{i = 1}^m} \ln P(y_i,z_i|\theta)\bigg)
\\
&= \displaystyle{\sum_{i = 1}^m}  \displaystyle{\sum_{z = 0}^1}
P(z|y_i,\theta^{(t)})
\ln P(y_i,z|\theta)
\\
&= \displaystyle{\sum_{i = 1}^m}  \displaystyle{\sum_{z = 0}^1}
P(z|y_i,\theta^{(t)})
\bigg(
z \ln \pi +
zy_i \ln p +
z(1-y_i) \ln (1-p) +
(1-z) \ln (1-\pi) +
(1-z)y_i \ln q +
(1-z)(1-y_i) \ln (1-q) \bigg)
\end{align}$



因为我们不知道$z_i$到底是多少,因此我们从概率的角度来考虑,我们列举了$z_i$的所有可能值,使用后验概率作为其权重。

~~注意:在EM算法中,$p(z|y_i,\theta^{(t)})$和参数$\theta$有关,但是把$p(z|y_i,\theta^{(t)})$这个量当作一个常量,具体原因见后面EM算法迭代的过程及其证明。我们先继续沿着极大似然法这个思路算下去。~~

为方便,记$P(z|y_i,\theta^{(t)}) = \lambda_{zi}$

令$\frac{\partial E_{Z|Y,\theta^{(t)}}\big(LL(\theta|Y,Z)\big)}{\partial \theta} = 0$(有约束条件,则使用其拉格朗日形式)
得:
$\pi = \frac{ \displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} z\lambda_{zi}}{\displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} \lambda_{zi}}$

$p = \frac{ \displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} zy_i\lambda_{zi}}{\displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} z\lambda_{zi}}$

$q = \frac{ \displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} (1-z)y_i\lambda_{zi}}{\displaystyle{\sum_{i = 1}^m}\displaystyle{\sum_{z = 0}^1} (1-z)\lambda_{zi}}$

$\lambda_{zi} = P(z|y_i,\theta^{(t)}) = \frac{P(y_i,z|\theta^{(t)})}{ P(y_i|\theta^{(t)})} = \frac{P(y_i,z|\theta^{(t)})}{\displaystyle{\sum_{z_j = 0}^1} P(y_i,z_j|\theta^{(t)})}$
> $P(X) = \displaystyle{\sum_z} P(z)P(X|z) = \displaystyle{\sum_z} P(X,z)$

EM算法是一个迭代算法
$\lambda_{zi}$为当前参数$\theta^{(t)}$下$z$的后验概率
上面$\pi,p,q$的等式,则是$\theta^{(t+1)} = \begin{matrix}
argmax\\
\theta
\end{matrix} E_{Z|Y,\theta^{(t)}}\big( LL(\theta|Y,Z) \big)$的解
~~迭代的过程,使用了上一次迭代的结果$\lambda_{zi}$
这也解释了为什么把$\lambda_{zi}$看作常量,因为这个量来自于上一次迭代输出的参数,而和这一次迭代的需要更新的参数无关。~~



我们整理一下这题EM算法的具体过程:
0. 随机取参数$\theta$ (或者 取k-means的结果作为初始参数)
		采用k-means的时候,
		均值作为初始化的均值,
		协方差矩阵初始化为各类的样本的协方差
		混合系数初始化为对应类别中的数据点所占的比例

1. E步:求似然函数期望的表达式
		即 计算$z_i$的后验概率 $p(z_i|y_i,\theta^{(t)})$(也就是$\lambda_{zi}$)

2. M步:更新参数$\theta$
		即 $\theta^{(t + 1)} = \begin{matrix} argmax \\ \theta\end{matrix} E_{Z|Y,\theta^{(t)}}\big( LL(\theta|Y,Z) \big)$

3. 重复2,3步骤,直到达到停止条件
		停止条件可以是达到最大轮迭代数,期望变化,参数变化达到阈值
		$|\theta^{(t+1)} - \theta^{(t)}| < \epsilon_1$ 或$\bigg|E_{Z|Y,\theta^{(t)}}\big( LL(\theta^{(t+1)}|Y,Z) \big) - E_{Z|Y,\theta^{(t)}}\big( LL(\theta^{(t)}|Y,Z) \big)\bigg|< \epsilon_2$

疑问:采用上述$z_i$真实值的规避策略,可以有:
$L(\theta|Y,Z) = \displaystyle{\prod_{i = 1}^m} P(y_i,z_i|\theta) = \displaystyle{\prod_{i = 1}^m}  \displaystyle{\sum_{z = 0}^1}
p(z|y_i,\theta^{(t)})P(y_i,z)$
和
$L(\theta|Y,Z) = \displaystyle{\prod_{i = 1}^m} P(y_i,z_i|\theta) = \displaystyle{\sum_{z = 0}^1}
p(z|y_i,\theta^{(t)})\displaystyle{\prod_{i = 1}^m}  P(y_i,z)$
两种选择,为什么采用后者?

前者取对数之后为:$\displaystyle{\sum_{i = 1}^m} \ln \displaystyle{\sum_{z = 0}^1}
p(z|y_i,\theta^{(t)})P(y_i,z)$

后者取对数之后为::$  \displaystyle{\sum_{z = 0}^1}
p(z|y_i,\theta^{(t)})
\bigg(\displaystyle{\sum_{i = 1}^m}\ln P(y_i,z)\bigg)$

无论是没取对数(有连乘),还是前者取了对数(有$\ln \sum$),其求导运算都不好算,而后者取对数之后,则把$\ln$放在了$\sum$的里面,显然运算更加简单。

## EM算法的证明
为什么EM算法这样迭代是有效的?
$\begin{align}LL(\theta|Y) = \ln P(Y|\theta) &= \ln\frac{ P(Y,Z|\theta)}{P(Z|Y,\theta)} &,贝叶斯定理\\\\
&= \ln P(Y,Z|\theta) - \ln P(Z|,Y,\theta) \\\\
\displaystyle{\sum_z}P(Z|Y,\theta^{(t)}) ln P(Y|\theta)&= \displaystyle{\sum_z}P(Z|Y,\theta^{(t)})\ln P(Y,Z|\theta) - \displaystyle{\sum_z}P(Z|Y,\theta^{(t)})\ln P(Z|,Y,\theta)
& ,(1)\\\\
ln P(Y|\theta)&= Q(\theta|\theta^{t}) +  H(\theta|\theta^{t})&,(2)
\end{align}$

(1):等号两边乘上一个系数,这个系数值为1,即$\displaystyle{\sum_z}P(Z|Y,\theta^{(t)}) = 1$
(2):为方便,定义两个符号

令$\theta = \theta^{(t)}$
有$\ln P(Y|\theta^{(t)}) = Q(\theta^{(t)}|\theta^{(t)}) +  H(\theta^{(t)}|\theta^{(t)})$

$Q(\theta^{(t)}|\theta^{(t)})$就是$E_{Z|Y,\theta^{(t)}}\big( LL(\theta|Y,Z) \big)$

则上面两个方程式相减有:
$\begin{align}\ln P(Y|\theta) - \ln P(Y|\theta^{(t))}) &= \bigg (Q(\theta|\theta^{t})  - Q(\theta^{t}|\theta^{t}) \bigg) + \bigg(H(\theta|\theta^{t})  - H(\theta^{t}|\theta^{t})\bigg) \\
&\geq \bigg(H(\theta|\theta^{t})  - H(\theta^{t}|\theta^{t})\bigg) \\
&\geq 0
\end{align}$

也就是说,EM算法迭代之后,Q的值要么增大,要么不变(不变则说明迭代结束),所以EM算法是有效的。

证明:$Q(\theta|\theta^{t})  - Q(\theta^{t}|\theta^{t}) \geq 0$
$\theta^{(t+1)} =
\begin{matrix}
argmax \\
\theta
\end{matrix} Q(\theta|\theta^{t})$
也就是说$Q(\theta^{(t+1)}|\theta^{t}) = \max_\theta(Q(\theta|\theta^{t})) \geq Q(\theta^{t}|\theta^{t})$

证明:$H(\theta|\theta^{t})  - H(\theta^{t}|\theta^{t}) \geq 0$
$H(\theta|\theta^{t}) = - \displaystyle{\sum_z}P(Z|Y,\theta^{(t)})\ln P(Z|,Y,\theta)$
由吉布斯不等式(**gibbs' inequality**),$\bigg(H(\theta|\theta^{t})  - H(\theta^{t}|\theta^{t})\bigg) \geq 0$,

>吉布斯不等式(**gibbs' inequality**)
若$\displaystyle{\sum_i} p_i = \displaystyle{\sum_i} q_i = 1,且p_i,q_i \in (0,1],则 -\displaystyle{\sum_i} p_i\ln p_i \leq -\displaystyle{\sum_i} p_i \ln q_i $,当且仅当$p_i = q_i$时等式成立

这里要求$p_i = q_i$,否则无法比较$H(\theta|\theta^{t})$和$H(\theta^{t}|\theta^{t})$的大小,这也解释了为什么选择z的后验概率,而不是其他。

从整体上来看,只有$\theta = \theta{(t)}$的时候,整个式子才能取等号。
因此随着迭代,似然函数的值不断变大(除非参数不再变化,收敛)

图示理解:
![1]

PRML上的证明类似,只不过构造的函数形式不太一样。

- [ ] : PRML上的证明

## 其他
EM算法可能走到鞍点,故需要多次进行,
也就是说EM算法对初始值敏感,常用的做法是使用k-means的结果作为初始值。

EM算法实际上有两种:
1. soft EM
		也就是前面我们用的,枚举所有的z,以其后验概率作为每个z的权重,综合考虑

2. hard EM
		$z_i$未知,则取$z_i$的期望作为真实值的近似。(对于离散型不可用,因为期望这个值不一定在可选范围内,比如前面的例子,可选择的值只有0和1,而期望则不是0或者1)

em算法有3个关键的地方:
1. 使用Z的概率取值(或者期望)来代替Z的真实值,这样就避免了Z真实值的需求
		注意是$P(X,Z) = \displaystyle{\sum_z} q(z)P(X,z)$
		或者是$P(X,Z) = P(X,E(Z))$
		而不是 $P(X) = \displaystyle{\sum_z} q(z)P(X|z)$

3. 使用z的后验概率而不是其他
3. 迭代求解

## EM算法的应用-高斯混合聚类
高斯分布的定义:
对n维样本空间X中的随机向量x，若x服从高斯分布，其概率密度函数为：
$p(\boldsymbol x) = \frac{1}{(2\pi)^\frac{n}{2}|\Sigma|^\frac{1}{2}} e^{ -\frac{1}{2}(\boldsymbol x - \boldsymbol \mu)^T\Sigma^{-1}(\boldsymbol x - \boldsymbol \mu) }$
其中$\boldsymbol \mu,\boldsymbol x$为n维均值向量，$\Sigma$是$n\times n$的协方差矩阵,$|\Sigma|$为$\Sigma$的行列式
为明确显示高斯分布与相应参数的依赖关系，将概率密度函数记为$p(\boldsymbol x | \boldsymbol \mu,\Sigma) = p(\boldsymbol x)$

高斯混合分布的定义:
高斯混合分布：$p_{\mathcal{M}}(x) = \displaystyle{\sum_{i - 1}^k} \alpha_i \cdot p(\boldsymbol x | \boldsymbol \mu_i,\Sigma_i)$
该分布由k个混合成分组成，每个混合成分对应一个高斯分布。其中$\mu_i$和$\Sigma_i$为第i个高斯混合成分的参数，而$\alpha_i>0$为相应的 **混合系数(mixture coefficient)** ,且$\displaystyle{\sum_{i - 1}^k} \alpha_i = 1$

高斯混合分布样本的生成过程:
首先,根据$\alpha_1,\alpha_2,\ldots,\alpha_k$定义的先验分布选择高斯混合成分,其中$\alpha_i$为第i个混合成分的概率;
然后,根据被选择的混合成分的概率密度进行采样,从而生成相应的样本。

定义:
样本:$X = \{x_1,x_2,\ldots,x_m\}$,$x_i$表示第i个样本的值
隐变量:$Z = \{z_1,z_2,\ldots,z_m\}$,$z_i$表示第i个样本真实来自的混合高斯成分。
参数:$\theta_i = (\alpha_i,\mu_i,\Sigma_i)$:表示第i个高斯混合成分的参数。

使用下标 **M** 以区别高斯混合模型和高斯混合成分

在已知$X$和$Z$的情况,其概率为:$P_\mathcal{M}(x,z|\theta) = \alpha_zP(x|\theta) = \alpha_zP(x|\mu,\Sigma)$
其似然函数为:$LL(\theta|X,Z) = \displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(x_j,z_j|\theta_j)$

$ \displaystyle{\sum_{j = 1}^m} \displaystyle{\sum_{l = 1}^k} p_{\mathcal{M}}(z_j = l|x_j,\theta^{(t)}) \ln P_{\mathcal{M}}(x_j.z_j = l|\theta_l)$

 期望为:$\begin{align}E_{Z|X,\theta^{(i)}}\big(LL(\theta|X,Z)\big) &=  \displaystyle{\sum_{j = 1}^m}  P_{\mathcal{M}}(x_j,z_j|\theta_j) &(1)\\
&= \displaystyle{\sum_{j = 1}^m} \displaystyle{\sum_{l = 1}^k} p_{\mathcal{M}}(z_j = l|x_j,\theta^{(t)}) \ln P_{\mathcal{M}}(x_j,z_j = l|\theta_l) &(2)
\end{align}$
(1)是定义
(2)是使用期望的公式展开隐变量,使用后验概率作为每个隐变量取值的权重

隐变量z的后验概率为:$\begin{align}
p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)}) &= \frac{ p_{\mathcal{M}}(z_j = i,x_j|\theta^{(t)})}{p_{\mathcal{M}}(x_j|\theta^{(t)})} &(1) \\
&= \frac{ p_{\mathcal{M}}(z_j = i,x_j|\theta^{(t)})}{\displaystyle{\sum_{l = 1}^k}p_{\mathcal{M}}(x_j,z_j = l|\theta^{(t)})} &(2)\\
&= \frac{ p_{\mathcal{M}}(z_j = i,x_j|\theta^{(t)})}{\displaystyle{\sum_{l = 1}^k} \alpha_lP(x_j|\mu_l,\Sigma_l)}
\end{align}$
(1)贝叶斯公式
(2)隐变量z使用其概率分布展开

则$\begin{align}
\frac{\partial LL(\theta|X,Z)}{\partial \mu_i}
&= \displaystyle{\sum_{j = 1}^m} \displaystyle{\sum_{l = 1}^k}  p_{\mathcal{M}}(z_j = l|x_j,\theta^{(t)})
\frac{\alpha_l}{P_{\mathcal{M}}(x_j,z_j = l|\theta_l)} \cdot
\frac{\partial P(x_j|\mu_l,\Sigma_l) }{\partial \mu_i} &(1)
\\
&= \displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})
\frac{\alpha_i}{P_{\mathcal{M}}(x_j,z_j = i|\theta_i)} \cdot
\frac{\partial P(x_j|\mu_i,\Sigma_i) }{\partial \mu_i} &(2)\\
&= \displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})
\frac{\alpha_i}{P_{\mathcal{M}}(x_j,z_j = i|\theta_i)} \cdot P(x_j|\mu_i,\Sigma_i)\Sigma_{-1}(x_j-\mu_i) &(3) \\
&= \displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)}) \cdot
\Sigma_{-1}(x_j-\mu_i) &(4)\\
&= 0
\end{align}$

得:$\mu_i = \frac{\displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})x_j }{\displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)}) }$


$\begin{align}
\frac{\partial LL(\theta|X,Z)}{\partial \Sigma_i}
&= \displaystyle{\sum_{j = 1}^m} \displaystyle{\sum_{l = 1}^k}  p_{\mathcal{M}}(z_j = l|x_j,\theta^{(t)})
\frac{\alpha_l}{P_{\mathcal{M}}(x_j,z_j = l|\theta_l)} \cdot
\frac{\partial P(x_j|\mu_l,\Sigma_l) }{\partial \Sigma_i} &(1)\\
&= \displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})
\frac{\alpha_i}{P_{\mathcal{M}}(x_j,z_j = i|\theta_i)} \cdot
\frac{\partial P(x_j|\mu_i,\Sigma_i) }{\partial \Sigma_i} &(2)\\
&= \displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})
\frac{\alpha_i}{P_{\mathcal{M}}(x_j,z_j = i|\theta_i)} \cdot
(\frac{1}{2})[(\Sigma_i^{-1})^T - (x_j - \mu_i)(x_j - \mu_i)^T\Sigma_i^{-2}] &(3)\\
& = 0
\end{align}$

$\begin{align}
\frac{\partial p(x_j|\mu_i,\Sigma_i)}{\partial \Sigma_i}
&= \frac{\partial \frac{1}{t}e^p}{\partial Sigma_i} &(1)\\
&= e^p\frac{\partial \frac{1}{t}}{\partial Sigma_i} + \frac{1}{t}\frac{\partial e^p}{\partial Sigma_i} &(2)\\
&=e^p\frac{1}{(2\pi)^{\frac{\pi}{2}}} (-\frac{1}{2})|\Sigma_i|^{-\frac{3}{2}}\frac{\partial |Sigma_i|}{\partial \Sigma_i} + e^p (-\frac{1}{2})\frac{\partial (x_j - \mu_i)^T\Sigma_i^{-1}(X_j - \mu_i)} {\partial \Sigma_i}
&(3)\\
&= p(x_j|\mu_i,\Sigma_i)((E^{-1})^T - (x_j - \mu_i)(x_j - \mu_i)^T\Sigma_i^{-2})&(4)\\
\end{align}$


$\frac{\partial |\Sigma_i|}{\partial \Sigma_i} = |\Sigma_i|(\Sigma_i^{-1})^T$


$\begin{align}
\frac{\partial( x_j - \mu_i)^T\Sigma_i^{-1}(x_j - \mu_i)}{ \partial}
&= \frac{\partial (x_j - \mu_i)^T\Sigma_i^{-1}(x_j - \mu_i)}{\partial \Sigma_i^{-1}(x_j - \mu_i)}
\frac{\partial \Sigma_i^{-1}(x_j - \mu_i)}{\partial \Sigma_i^{-1}}
\frac{\partial \Sigma_i^{-1}}{\partial \Sigma_i} &(1)\\
&=(x_j - \mu_i)\frac{\partial \Sigma_i^{-1}(x_j - \mu_i)}{\partial \Sigma_i^{-1}}
\frac{\partial \Sigma_i^({-1}}{\partial \Sigma_i} &(2)\\
&=(x_j - \mu_i)(x_j-\mu_i)^T\frac{\partial \Sigma_i^({-1}}{\partial \Sigma_i} &(3)\\
&=(x_j - \mu_i)(x_j-\mu_i)^T(-1)\Sigma_i^{-2}
\end{align}$


得:
$\begin{align}
(\Sigma_i^{-1})^T\Sigma_i^2 &= \Sigma_i &(1)\\
&=\frac{\displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)})(x_j - \mu_i)(x_j - \mu_i)^T }{\displaystyle{\sum_{j = 1}^m}  p_{\mathcal{M}}(z_j = i|x_j,\theta^{(t)}) }&(2)
\end{align}$

(1):$\Sigma_i$是对称矩阵($A^T = A$),并且$(A^{-1})^T = (A^T)^{-1}$
(2):参数$\mu_i$是更新之后的值,而不是原来的值。

$\begin{align}
\frac{\partial \bigg(LL(\theta|X,Z) + \lambda(\displaystyle{\sum_{i = 1}^k} \alpha_i - 1)\bigg)}{\partial \alpha_i}
&= \displaystyle{\sum_{j = 1}^m} \displaystyle{\sum_{l = 1}^k} P_\mathcal{M}(z_j = l | x_j,\theta^{(t)}) \frac{p(x_j|\mu_i,\Sigma_i)}{P_\mathcal{M}(x_j,z_j = l |\theta\_l)}\frac{\partial \alpha_l}{\partial \alpha_i} + \lambda &(1)\\
&=\displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(z_j = i | x_j,\theta^{(t)}) \frac{p(x_j|\mu_i,\Sigma_i)}{P_\mathcal{M}(x_j,z_j = i |\theta\_i)} + \lambda &(2)\\
&= 0
\end{align}$

等号两边同乘$\alpha_i$,得:$\displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(z_j = i | x_j,\theta^{(t)}) + \lambda \alpha_i = 0$

全部k个表达式求和:得到
$\begin{align}
\displaystyle{\sum_{i = 1}^k} \displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(z_j = i | x_j,\theta^{(t)}) + \displaystyle{\sum_{i = 1}^k} \lambda \alpha_i &= 0\\
\displaystyle{\sum_{i = 1}^k} \displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(z_j = i | x_j,\theta^{(t)}) +  \lambda &= 0\\
m + \lambda &= 0 \\
\lambda &= -m
\end{align}$

则$\alpha_i = \frac{1}{m}\displaystyle{\sum_{j = 1}^m} P_\mathcal{M}(z_j = i | x_j,\theta^{(t)})$

至此,关于高斯混合聚类模型参数的推导完成。

下面只需要进行迭代即可。

EM算法的结果对初始值敏感,对于高斯混合模型,一般先采用k-means算法的结果作为其初始值

如果有k个混合成分,那么就应该有$k!$个等价的解,为什么EM算法只会得到其中一个?
根据参数初始值,一开始就决定了最终会导向哪一个形式的解。

[1]:assets/机器学习-EM算法-e8373.png
[2]:assets/机器学习-EM算法-96f58.png
