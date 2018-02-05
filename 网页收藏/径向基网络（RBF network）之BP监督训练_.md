#  [径向基网络（RBF network）之BP监督训练](http://blog.csdn.net/zouxy09/article/details/13297881)

**径向基网络（RBF network）之BP监督训练**

 之前看了流行学习的时候，感觉它很神奇，可以将一个4096维的人脸图像降到3维。然后又看到了可以用径向基网络来将这3维的图像重构到4096维。看到效果的时候，我和小伙伴们都惊呆了（呵呵，原谅我的孤陋寡闻）。见下图，第1和3行是原图像，维度是64x64=4096维，第2和第4行是将4096维的原图像用流行学习算法降到3维后，再用RBF网络重构回来的图像（代码是参考一篇论文写的）。虽然在重构领域，这效果不一定是好的，但对于无知的我，其中的奥妙勾引了我，使我忍不住又去瞻仰了一番。

![](http://img.blog.csdn.net/20131028181020843?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

推荐大家先看看这个博主的这篇博文：

<http://www.cnblogs.com/zhangchaoyang/articles/2591663.html>

**一、径向基函数**

       在说径向基网络之前，先聊下径向基函数（Radical Basis Function，RBF）。径向基函数（Radical
Basis
Function，RBF）方法是Powell在1985年提出的。所谓径向基函数，其实就是某种沿径向对称的标量函数。通常定义为空间中任一点x到某一中心c之间欧氏距离的单调函数，可记作k(||x-c||)，其作用往往是局部的，即当x远离c时函数取值很小。例如高斯径向基函数：

![](http://img.blog.csdn.net/20131028181106343?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 当年径向基函数的诞生主要是为了解决多变量插值的问题。可以看下面的图。具体的话是先在每个样本上面放一个基函数，图中每个蓝色的点是一个样本，然后中间那个图中绿色虚线对应的，就表示的是每个训练样本对应一个高斯函数（高斯函数中心就是样本点）。然后假设真实的拟合这些训练数据的曲线是蓝色的那根（最右边的图），如果我们有一个新的数据x1，我们想知道它对应的f(x1)是多少，也就是a点的纵坐标是多少。那么由图可以看到，a点的纵坐标等于b点的纵坐标加上c点的纵坐标。而b的纵坐标是第一个样本点的高斯函数的值乘以一个大点权值得到的，c的纵坐标是第二个样本点的高斯函数的值乘以另一个小点的权值得到。而其他样本点的权值全是0，因为我们要插值的点x1在第一和第二个样本点之间，远离其他的样本点，那么插值影响最大的就是离得近的点，离的远的就没什么贡献了。所以x1点的函数值由附近的b和c两个点就可以确定了。拓展到任意的新的x，这些红色的高斯函数乘以一个权值后再在对应的x地方加起来，就可以完美的拟合真实的函数曲线了。

![](http://img.blog.csdn.net/20131028181129406?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**二、径向基网络**

       到了1988年， Moody和
Darken提出了一种神经网络结构，即RBF神经网络，属于前向神经网络类型，它能够以任意精度逼近任意连续函数，特别适合于解决分类问题。

![](http://img.blog.csdn.net/20131028181156281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


 RBF网络的结构与多层前向网络类似，它是一种三层前向网络。输入层由信号源结点组成；第二层为隐含层，隐单元数视所描述问题的需要而定，隐单元的变换函数是RBF径向基函数，它是对中心点径向对称且衰减的非负非线性函数；第三层为输出层，它对输入模式的作用作出响应。从输人空间到隐含层空间的变换是非线性的，而从隐含层空间到输出层空间变换是线性的。

![](http://img.blog.csdn.net/20131028181209859?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


 RBF网络的基本思想是：用RBF作为隐单元的“基”构成隐含层空间，这样就可将输入矢量直接（即不需要通过权连接）映射到隐空间。根据Cover定理，低维空间不可分的数据到了高维空间会更有可能变得可分。换句话来说，RBF网络的隐层的功能就是将低维空间的输入通过非线性函数映射到一个高维空间。然后再在这个高维空间进行曲线的拟合。它等价于在一个隐含的高维空间寻找一个能最佳拟合训练数据的表面。这点与普通的多层感知机MLP是不同的。


 当RBF的中心点确定以后，这种映射关系也就确定了。而隐含层空间到输出空间的映射是线性的，即网络的输出是隐单元输出的线性加权和，此处的权即为网络可调参数。由此可见，从总体上看，网络由输人到输出的映射是非线性的，而网络输出对可调参数而言却又是线性的。这样网络的权就可由线性方程组直接解出，从而大大加快学习速度并避免局部极小问题。


 从另一个方面也可以这样理解，多层感知器（包括BP神经网络）的隐节点基函数采用线性函数，激活函数则采用Sigmoid函数或硬极限函数。而RBF网络的隐节点的基函数采用距离函数（如欧氏距离），并使用径向基函数（如Gaussian函数）作为激活函数。径向基函数关于n维空间的一个中心点具有径向对称性，而且神经元的输入离该中心点越远，神经元的激活程度就越低。隐节点的这一特性常被称为“局部特性”。



**三、RBF网络的设计与求解**


 RBF的设计主要包括两个方面，一个是结构设计，也就是说隐藏层含有几个节点合适。另一个就是参数设计，也就是对网络各参数进行求解。由上面的输入到输出的网络映射函数公式可以看到，网络的参数主要包括三种：
径向基函数的中心、方差和隐含层到输出层的权值。到目前为止，出现了很多求解这三种参数的方法，主要可以分为以下两大类：

**1、方法一：**


 通过非监督方法得到径向基函数的中心和方差，通过监督方法（最小均方误差）得到隐含层到输出层的权值。具体如下：

（1）在训练样本集中随机选择h个样本作为h个径向基函数的中心。更好的方法是通过聚类，例如K-means聚类得到h个聚类中心，将这些聚类中心当成径向基函数的h个中心。

（2）RBF神经网络的基函数为高斯函数时，方差可由下式求解：

![](http://img.blog.csdn.net/20131028181248906?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

       式中c <sub>max</sub>
为所选取中心之间的最大距离，h是隐层节点的个数。扩展常数这么计算是为了避免径向基函数太尖或太平。

（3）隐含层至输出层之间神经元的连接权值可以用最小均方误差LMS直接计算得到，计算公式如下：（计算伪逆）（d是我们期待的输出值）

![](http://img.blog.csdn.net/20131028181303625?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



**2、方法二：**


采用监督学习算法对网络所有的参数（径向基函数的中心、方差和隐含层到输出层的权值）进行训练。主要是对代价函数（均方误差）进行梯度下降，然后修正每个参数。具体如下：

（1）随机初始化径向基函数的中心、方差和隐含层到输出层的权值。当然了，也可以选用方法一中的（1）来初始化径向基函数的中心。

（2）通过梯度下降来对网络中的三种参数都进行监督训练优化。代价函数是网络输出和期望输出的均方误差：

![](http://img.blog.csdn.net/20131028181325703?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

然后每次迭代，在误差梯度的负方向已一定的学习率调整参数。

![](http://img.blog.csdn.net/20131028181351718?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



**四、代码实现：**

**1、第一种方法**

       第一种方法在
[zhangchaoyang的博客](http://www.cnblogs.com/zhangchaoyang/articles/2591663.html)上面有C++的实现，只是上面针对的是标量的数据（输入和输出都是一维的）。而在Matlab中也提供了第一种方法的改进版（呵呵，个人觉得，大家可以在Matlab中运行open
newrb查看下源代码）。


 Matlab提供的一个函数是newrb()。它有个技能就是可以自动增加网络的隐层神经元数目直到均方差满足我们要求的精度或者神经元数数目达到最大（也就是我们提供的样本数目，当神经元数目和我们的样本数目一致时，rbf网络此时的均方误差为0）为止。它使用方法也能简单：

rbf = newrb(train\_x, train\_y);

output = rbf(test\_x);

      直接把训练样本给它就可以得到一个rbf网络了。然后我们把输入给它就可以得到网络的输出了。



**2、第二种方法**

       第二种方法在
[zhangchaoyang的博客](http://www.cnblogs.com/zhangchaoyang/articles/2591663.html)上面也有C++的实现，只是上面针对的还是标量的数据（输入和输出都是一维的）。但我是做图像的，网络需要接受高维的输入，而且在Matlab中，向量的运算要比for训练的运算要快很多。所以我就自己写了个可以接受向量输入和向量输出的通过BP算法监督训练的版本。BP算法可以参考这里：
[BackpropagationAlgorithm](http://deeplearning.stanford.edu/wiki/index.php/Backpropagation_Algorithm)，主要是计算每层每个节点的残差就可以了。另外，我的代码是可以通过梯度检查的，但在某些训练集上面，代价函数值却会随着迭代次数上升，这就很奇怪了，然后降低了学习率还是一样。但在某些简单点的训练集上面还是可以工作的，虽然训练误差也挺大的（没有完全拟合训练样本）。所以大家如果发现代码里面有错误的部分，还望大家告知下。

       主要代码见下面：

learnRBF.m

``` cpp
%// This is a RBF network trained by BP algorithm
%// Author : zouxy
%// Date   : 2013-10-28
%// HomePage : http://blog.csdn.net/zouxy09
%// Email  : zouxy09@qq.com

close all; clear; clc;

%%% ************************************************
%%% ************ step 0: load data ****************
display('step 0: load data...');
% train_x = [1 2 3 4 5 6 7 8]; % each sample arranged as a column of train_x
% train_y = 2 * train_x;
train_x = rand(5, 10);
train_y = 2 * train_x;
test_x = train_x;
test_y = train_y;

%% from matlab
% rbf = newrb(train_x, train_y);
% output = rbf(test_x);


%%% ************************************************
%%% ******** step 1: initialize parameters ********
display('step 1: initialize parameters...');
numSamples = size(train_x, 2);
rbf.inputSize = size(train_x, 1);
rbf.hiddenSize = numSamples;        % num of Radial Basis function
rbf.outputSize = size(train_y, 1);
rbf.alpha = 0.1;  % learning rate (should not be large!)

%% centre of RBF
for i = 1 : rbf.hiddenSize
    % randomly pick up some samples to initialize centres of RBF
    index = randi([1, numSamples]);
    rbf.center(:, i) =  train_x(:, index);
end

%% delta of RBF
rbf.delta = rand(1, rbf.hiddenSize);

%% weight of RBF
r = 1.0; % random number between [-r, r]
rbf.weight = rand(rbf.outputSize, rbf.hiddenSize) * 2 * r - r;


%%% ************************************************
%%% ************ step 2: start training ************
display('step 2: start training...');
maxIter = 400;
preCost = 0;
for i = 1 : maxIter
    fprintf(1, 'Iteration %d ,', i);
    rbf = trainRBF(rbf, train_x, train_y);
    fprintf(1, 'the cost is %d \n', rbf.cost);

    curCost = rbf.cost;
    if abs(curCost - preCost) < 1e-8
        disp('Reached iteration termination condition and Termination now!');
        break;
    end
    preCost = curCost;
end


%%% ************************************************
%%% ************ step 3: start testing ************
display('step 3: start testing...');
Green = zeros(rbf.hiddenSize, 1);
for i = 1 : size(test_x, 2)
    for j = 1 : rbf.hiddenSize
        Green(j, 1) = green(test_x(:, i), rbf.center(:, j), rbf.delta(j));
    end
    output(:, i) = rbf.weight * Green;
end
disp(test_y);
disp(output);
```



trainRBF.m

``` cpp
function [rbf] = trainRBF(rbf, train_x, train_y)
    %%% step 1: calculate gradient
    numSamples = size(train_x, 2);
    Green = zeros(rbf.hiddenSize, 1);
    output = zeros(rbf.outputSize, 1);
    delta_weight = zeros(rbf.outputSize, rbf.hiddenSize);
    delta_center = zeros(rbf.inputSize, rbf.hiddenSize);
    delta_delta =  zeros(1, rbf.hiddenSize);
    rbf.cost = 0;
    for i = 1 : numSamples
        %% Feed forward
        for j = 1 : rbf.hiddenSize
            Green(j, 1) = green(train_x(:, i), rbf.center(:, j), rbf.delta(j));
        end
        output = rbf.weight * Green;

        %% Back propagation
        delta3 = -(train_y(:, i) - output);
        rbf.cost = rbf.cost + sum(delta3.^2);
        delta_weight = delta_weight + delta3 * Green';
        delta2 = rbf.weight' * delta3 .* Green;
        for j = 1 : rbf.hiddenSize
            delta_center(:, j) = delta_center(:, j) + delta2(j) .* (train_x(:, i) - rbf.center(:, j)) ./ rbf.delta(j)^2;
            delta_delta(j) = delta_delta(j)+ delta2(j) * sum((train_x(:, i) - rbf.center(:, j)).^2) ./ rbf.delta(j)^3;
        end
    end

    %%% step 2: update parameters
    rbf.cost = 0.5 * rbf.cost ./ numSamples;
    rbf.weight = rbf.weight - rbf.alpha .* delta_weight ./ numSamples;
    rbf.center = rbf.center - rbf.alpha .* delta_center ./ numSamples;
    rbf.delta = rbf.delta - rbf.alpha .* delta_delta ./ numSamples;
end
```



green.m

``` plain
function greenValue = green(x, c, delta)
    greenValue = exp(-1.0 * sum((x - c).^2) / (2 * delta^2));
end
```

**五、代码测试**

      首先，我测试了一维的输入，需要拟合的函数很简单，就是y=2x。

train\_x = \[1 2 3 4 5 6 7 8\];

train\_y = 2 \* train\_x;

     所以期待的输出就是：

2    4     6     8   10    12    14   16

     我代码训练迭代200次后的网络输出是：

2.0042   4.0239    5.9250    8.0214  10.0692   11.9351  14.0179  15.9958

      Matlab的newrb的输出是：

2.0000   4.0000    6.0000    8.0000  10.0000   12.0000  14.0000  16.0000

      可以看到，Matlab的是完美拟合啊。我的那个还是均方误差还是挺大的。

      然后，我测试了高维的输入，训练样本是通过Matlab的rand(5, 10)来得到的，它生成的是5行10列\[0
1\]之间的随机数。也就是说我们的样本是10个，每个样本的维度是5维。我们测试的也是很简单的函数y=2x。结果如下：


![](http://img.blog.csdn.net/20131028181619796?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvem91eHkwOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

      关于这个结果，我也不说什么了。期待大家发现代码里面错误的地方，然后告知下，非常感谢。