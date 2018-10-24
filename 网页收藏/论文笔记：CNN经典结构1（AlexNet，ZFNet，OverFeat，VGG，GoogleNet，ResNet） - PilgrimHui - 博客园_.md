# [论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）](https://www.cnblogs.com/liaohuiqiang/p/9606901.html)

### AlexNet

1.  **贡献**：ILSVRC2012冠军，展现出了深度CNN在图像任务上的惊人表现，掀起CNN研究的热潮，是如今深度学习和AI迅猛发展的重要原因。ImageNet比赛为一直研究神经网络的Hinton提供了施展平台，AlexNet就是由hinton和他的两位学生发表的，在AlexNet之前，深度学习已经沉寂了很久。
2.  **网络结构**：如下图所示，8层网络，参数大约有60 million，使用了relu函数，头两个全连接层使用了0.5的dropout。使用了LRN和重叠的池化，现在LRN都不用了，一般用BN作Normalization。当时使用了多GPU训练。
3.  **预处理**：先down-sample成最短边为256的图像，然后剪出中间的256x256图像，再减均值做归一化（over training set）。
    **训练时**，做数据增强，对每张图像，随机提取出227x227以及水平镜像版本的图像。除了数据增强，还使用了PCA对RGB像素降维的方式来缓和过拟合问题。
4.  **预测**：对每张图像提取出5张（四个角落以及中间）以及水平镜像版本，总共10张，平均10个预测作为最终预测。
5.  **超参数**：SGD，学习率0.01，batch size是128，momentum为0.9，weight decay为0.0005（论文有个权重更新公式），每当validation
    error不再下降时，学习率除以10。权重初始化用（0，0.01）的高斯分布，二四五卷积层和全连接层的bias初始化为1（给relu提供正值利于加速前期训练），其余bias初始化为0。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20171124090206484-877449439.png)

### ZFNet

1.  **贡献**：ILSVRC2013分类任务的冠军，使用反卷积对CNN的中间特征图进行可视化分析，通过分析特征行为找到提升模型的办法，微调Alexnet提升了表现。ZFNet的Z和F指的是Zeiler和Fergus，曾是hinton的学生，后在纽约大学读博的Zeiler，联手纽约大学研究神经网络的Fergus提出了ZFNet。
2.  **冠军？**：严格意义上来说当时分类冠军是Clarifai，但是我们通常讨论的ILSVRC2013冠军（winner）指的是ZFNet。ZF中的Zeiler是Clarifai的创建者和CEO。
3.  **网络结构**：如下图所示，和AlexNet一样，头两个全连接层后面加0.5的dropout。相比于AlexNet，主要区别是使用了更小的卷积核和步长，11x11的卷积核变成7x7的卷积核，stride从4变成了2。另外，通过可视化发现第一层的卷积核影响大，于是对第一层的卷积核做了规范化，如果RMS（Root Mean Square）超过0.1，就把卷积核的均方根normalize为固定0.1。
4.  **其它数据集**：ZFNet还在Caltech-101，Caltech-256，Pascal AOC-2012上做了迁移学习的实验。
5.  **预处理和超参数**：和AlexNet基本一致。权重初始化不同，权重初始化为0.01，bias初始化为0。
6.  **更多**：具体内容我在另一篇[论文笔记：可视化CNN](https://www.cnblogs.com/liaohuiqiang/p/9356753.html)中有所提及。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200007680-685219468.png)

### OverFeat

1.  **贡献**：ILSVRC2013定位任务的冠军，用一个CNN集成了分类，定位和检测三个任务，提出了多尺度的方法。OverFeat是由Yann Lecun团队提出，Lecun提出的LeNet可以说是CNN的开端，提出来并没有火起来，因为当时机器性能不高而且SVM也能达到类似的效果甚至超过。
2.  **网络结构**：相比于AlexNet，不再使用LRN；使用非重叠的池化；使用更小的步长，大的步长可以提高速度但是损害了精度。和AlexNet一样，头两个全连接层后面加0.5的dropout。
3.  **预处理和超参数**：和AlexNet基本一致。权重初始化不同，全部用（0，0.01）的高斯分布初始化。momentum为0.6，学习率为0.005。在（30，50，60，70，80）epoch学习率减半（decreased a factor by 0.5）。
4.  **预测**：在测试阶段，不再使用AlexNet的10 views法（4 corners and center, with horizontal flip），探索了多尺度来进行平均预测的方法，直接从原图rescale成多个尺度的图像输入网络进行多尺度预测。
5.  **多尺度（和全卷积）**：如下图所示，把全连接层改成全卷积（5x5卷积），在网络最后配合全局最大池化，可以输入多尺度的图像，举例来说，输入14x14的图像，最后得到的是1x1个分类特征，输入16x16的图像最后会得到2x2个分类特征，但是通过全局最大池化就可以转为1x1个分类特征，对于多尺度输入，输出是一致的。而且从下图中的蓝色色块可以看出，在16x16上卷积可以看作用14x14的窗口在上面滑动2步的4次卷积结果。
6.  **更多**：具体内容我在另一篇[论文笔记：OverFeat](https://www.cnblogs.com/liaohuiqiang/p/9348276.html)中有所提及。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180721220438599-1957099965.png)

### VGG

1.  **贡献**：ILSVRC2014定位任务的冠军（Winner），分类任务的亚军（runner-up）。该网络的特点在于结构规整，通过反复堆叠3x3的卷积，卷积核数量逐渐加倍来加深网络，后续的很多CNN结构都采用了这种3x3卷积思想，这是一个很大的影响。ZFNet和OverFeat都使用了更小的卷积核，更小的步长来提升AlexNet的表现，相比之下，VGG则是探索CNN的深度，通过固定其它参数，然后稳定地叠加深度。
2.  **网络结构**
    - 如下图所示，VGG-16，16层，参数大约有138 million。实验发现LRN的加入没有提升反而更差，舍弃使用。实验发现1x1效果更差，于是没有使用，1x1卷积在Network in Network（颜水成）中提出推广，是很重要的思想，在GoogleNet和ResNet都有用到。
    - 使用小卷积核3x3可以捕捉左右上下的信息，而且利于堆叠深度（保证参数不要过大）。步长为1。same卷积。
    - 两个3x3卷积可以和5x5卷积达到一样的感受野。三个3x3卷积可以和7x7卷积达到一样的感受野。使用三个3x3的好处在于使用了3个非线性变换，同时后减小了参数，假设输入输出通道数一样，那么有
    \[3(3^{2}C^{2}) = 27C^{2} < 7^{2}C^{2} = 49C^{2}\]
    - 和AlexNet一样，头两个全连接层后面加0.5的dropout。

1.  **超参数**：和AlexNet基本一致。batch size是256。初始化也是用（0，0.01）的高斯分布，只不过VGG先训练一个浅层的网络，然后把浅层网络的部分参数来初始化深层网络部分参数，其它参数还是用高斯分布。值得注意的是论文提交后VGG发现使用glorot的初始化方法可以不用预训练。
2.  **预处理**：和AlexNet不同，在下采样的时候不是变成256，变成一个S，S有两种方法来设定。第一个方法是固定的S（single-scale），固定为256或384。为了加速384的网络，用256预训练的模型进行权重初始化。另外学习率调小为0.001。第二个方法从[256, 512]中随机采样S（multi-scale，注意这里的是multi-scale training，和overfeat中的multi-scale test含义不一样），这可以看成用尺寸抖动（scale jittering）对训练集进行增强。为了加速，使用384预训练的模型进行权重初始化。
3.  **预测**：采用了AlexNet的10 views法（VGG论文中把它称作multi-crop评估）和overfeat的多尺度预测方法（VGG论文中把它称作dense评估）相结合。在OverFeat已经提到了multi-crop是有缺点的，存在冗余的卷积计算，所以使用了dense评估，但是Inceptionv1的论文中提到multi-crop使用大量crops能提高准确率因为它的采样更精细。而VGG认为实作上准确率的提升不足以弥补速度，但是为了参考起见，还是跑了multi-scrop的方法。在实验中，两者结合优于multi-crop优于dense，好那么一点点，差别不大。
4.  **集成**：实验的最后融合了多个模型（集成），最好的模型是融合了VGG-16和VGG-19，训练使用multi-scale training，测试使用multi-crop和dense评估相结合。在AlexNet，ZFNet和OverFeat最后的实验都会使用集成，最好的模型一般都是集成的结果。
5.  **定位**：VGG的定位任务的模型是在OverFeat的基础上做了一些修改。对于bounding box的预测有两种，SCR（single-class regression）是所有类共享一个框，这时最后输出是4维向量。PCR（per-class regression）是每个类一个框，这样最后输出就是4x1000，其中1000表示1000类。
6.  **泛化**：和ZFNet一样，VGG也做了迁移学习，用ILSVRC的数据预训练，然后迁移到其它数据集VOC-2007，VOC-2012，Caltech-101，Caltech-256。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20171124090234406-155051052.png)

### GoogleNet（Inceptionv1）

1.  **贡献**：ILSVRC2014分类任务的冠军。该网络设计了Inception块代替人工来选择卷积类型，然后堆叠Inception块（增加深度）形成Inception网络。去除了全连接层（占据了网络的大部分参数），使用了全局均值池化（思想来自Network in Network），大大减小了参数量。这两个思想在GoogleNet后面的一些论文中都有体现，一个是Inception块的自动选择网络结构（Google后面发表了一些自动选择网络超参，网络优化器，网络激活函数的论文），另一个是减小模型参数和计算资源（Google的mobileNet，类似工作还有face++的shuffleNet）。
2.  **网络结构**：如下图所示为Inception块。网络总共有22层，图太大，这里就给个表格。可以看到虽然把全连接替换成了全局均值池化（这后面还是使用了0.4的dropout），但是网络图中最后还是有一个全连接层，这是为了便于把网络fine tune到其它数据集。
3.  **参数**：为了提升模型表现，典型的办法是增大模型（增加深度或宽度），但是这样会带来过大的参数，然后导致计算资源增大而且需要的数据更多（而高质量数据往往是昂贵的），所以要考虑降低参数。Inceptionv1虽然有22层的参数却只有5 million，是同期VGG16（138 million）的1/27，是AlexNet（60 million）的1/12而准确率却远胜AlexNet。
4.  **1x1卷积好处**：减小了参数，允许增加深度； 可以降维，构建瓶颈层来减小计算成本，Inception块中就是通过在3x3和5x5后面加入1x1来减小计算；增强了网络的表达能力（可以根据自己的意愿，或压缩或增加或保持通道数）。还有配合全局均值池化来代替全连接层，这个就是为了能大大减小模型的参数。1x1的思想也来自Network in Network。
5.  **超参数和预处理**：因为比赛的过程做了很多变动，包括采样方法和各种超参，所以很难定义一个有效的指导去训练这个网络。只给出了几个超参数，固定学习率，每8epoch下降4%，momentum是0.9。
6.  **预测**：先下降样出256，288，320和352大小，分别从左中右三个方位裁（如果是人画像则从上中下三个方位裁），然后从4 corners和center剪出224x224再加上把正方形缩放到224，以及它们的水平镜像。这样就可以得到4x3x6x2也就是144个crops，最后对crops取平均。
7.  **集成**：和之前的网络一样，最后也使用了集成，训练了7个版本的网络进行集成，使用Polyak averaging进行平均，7个网络使用一样的初始化和学习率设置，不同之处在于数据采样的方法和顺序。
8.  **目标检测**：Inceptionv1的目标检测使用了类似R-CNN的方法来完成。
9.  **辅助输出**：Inceptionv1中有两个辅助输出，说是因为太深的网络的梯度回传能力有限（梯度消失），于是在中间层接另两条分支来利用中间层的特征，可以增加梯度回传，还有附加的正则化作用。然后在v3的论文中又提到说利用中间层特征的想法可能是错的，因为去掉低层的辅助（第一个辅助输出）对最终结果并没有什么影响，但是还是强调了辅助输出的正则化效果，因为在辅助输出中加入BN和dropout可以提升主输出表现。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20171124151010078-1933005968.png)

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200119341-1914878683.png)

### GoogleNet（Inceptionv2）

1.  **贡献**：学习VGG，使用两个3x3卷积代替5x5的大卷积（保持感受野的同时又可以减小参数量），还使用了众所周知的BN。值得注意的是Inception-BN在v4的论文中把这个网络被称为v2，而在v3的论文中有另外一个v2（v3的一个低配版）。这两篇论文中提到的v2不是同一个v2，通常说的v2指的是这个Inception-BN。
2.  **网络结构**：如下图所示，主要改变有，用两个3x3代替5x5，28x28的Inception块从2个变成了3个，pooling时有些是avg有些是max，在Incetpion块之间不再有额外的max-pool而是直接把卷积和池化的stride设置为2。BN被用在每一个输入层后面（先BN再激活）。batch size为32。网络使用DistBelief（Tensorflow前身）训练
3.  **其它变动**：增大学习率并加快学习率衰减（适用BN后的数据），移除dropout并减小L2权重衰减（BN有一定的正则效果），去除LRN（发现用了BN后不需要LRN了），更彻底对训练样本进行shuffle，减小数据增强时对数据的光学畸变（因为BN训练更快，每个样本被训练次数变少，模型需要注重更真实的样本）。
4.  **集成**：最好的结果当然还是要集成了（之前的BN笔记中没有提及）。集成了6个网络，都是基于BNx30，6个版本分别在卷积层增加初始化权重；使用dropout 5%；使用dropout 10%；在Inceptionv1适用dropout 40%；不使用卷积；先激活再BN。集成方式还有multi-crop的使用和Inceptionv1一样。
5.  **更多**：关于BN（包括我在上一条提到的BNx30）我在另一篇论文[论文笔记：BN](https://www.cnblogs.com/liaohuiqiang/p/9250469.html)中有所提及，这篇论文也是讲述Inception-BN的论文

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200056784-115226972.png)

### GoogleNet（Inceptionv3）

1.  **贡献**：通过一系列的卷积分解和正则化手段来提升模型。这篇论文称为v3论文，里面有一个低配版v3称为v2，这里的v2只是v3这篇论文的v2，这一节提到的v2都是指这个v2。平常说的v2指的是BN那篇论文的v2。
2.  **训练配置**：使用tensorflow训练，学习率为0.045，以0.94的指数率每两轮衰减一次。梯度裁剪阈值为2。
3.  **v2网络结构**：共42层，网络图就不放了，主要改动有如下。图有点多，这里就不放图了，各个改动模块图可以参考后面v4的结构图。
    - 修改部分Inception块，使5x5分解成2个3x3卷积（可参考下面v4的InceptionA）。
    - 修改部分Inception块，分解成非对称卷积（把nxn分解成1xn和nx1卷积，这里n=7。注意原始结构并没有7x7卷积）（可参考下面v4的InceptionB）。
    - 修改部分Inception块，扩大卷积核数量（汇聚的分支数量）（可参考下面v4的InceptionC）
    - 修改部分Inception块，减小特征图大小（使用并行的stride为2的卷积和池化）（可参考下面v4的Reduction）

1.  **v3网络结构**：在以上基础上，加入如下改动

    - 用RMSProp训练，decay为0.9，\(\epsilon\) 为1.0
    - 使用Label smoothing进行模型正则
    - 开头第一层7x7分解成3个3x3卷积
    - 加入带BN的辅助分类器

### GoogleNet（Inceptionv4，Inception-ResNet）

1.  **贡献**：基于v3的基础，引入残差结构，提出了Inception-ResNet-v1和Inception-ResNet-v2。同时修改了Inception提出了Inceptionv4，发现Inceptionv4能达到Incetpion-ResNet-v2类似的结果，认为残差结构对于训练深度网络不是必须的（之前看过一篇分形网络的论文也提出了”残差块并不是训练深度网络的必要组件”的观点，我在[论文笔记：分形网络](https://www.cnblogs.com/liaohuiqiang/p/9218445.html)有所提及）。
2.  **v4网络结构**：如下第一个图是v4。
3.  **Inception-ResNet**：探索了多种Inception-ResNet，论文只阐述了两个。其中Inceptin-ResNet-v1和Inceptinv3计算代价差不多，Inceptin-ResNet-v2和Inceptionv4计算代价差不多，然而实作上Inceptionv4慢很多可能是因为层数太多。在带有ResNet的Inception中，还有一个和纯Inception的不同点是只在传统层上使用BN，不在BN层上使用，这样可以减小计算从而堆叠更多Inceptin块。
4.  **Inception-ResNet-v2结构**：如下第二个图是Inception-ResNet-v2（输出的shape是Inception-ResNet-v1的）。
5.  **训练配置**：tensorflow，RMSProp，decay为0.9，\(\epsilon\) 为1.0，学习率为0.045，以0.94的指数率每两轮衰减一次。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200134678-337474579.jpg)
![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200151496-793846978.jpg)

### ResNet

1.  **贡献**：ILSVRC2015冠军（分类，检测，定位），由MSRA的何铠明等人提出，通过使用残差块训练了152层的网络，降低了错误率。解决了退化问题（plain网络随着网络加深，错误率升高），而使用残差后，随着网络加深，错误率还是能下降。
2.  **网络加深**：对于网络加深，会出现梯度消失或梯度爆炸，这个问题可以通过正则初始化（何凯明初始化等等）和BN来解决。
3.  **退化问题**：然而深层网络到了一定深度，准确率趋近饱和，而且继续加深的话会降低准确率，这称为退化问题（degradation），而且这个问题并不是过拟合导致的（过拟合在训练集应该更好），也不是梯度消失造成的（论文检查了梯度）。
4.  **残差块**：为了解决退化问题，提出了残差学习，如下图所示为残差块，假设本来是要学习H(x)，加了一条恒等映射之后我们要学习的就是F(x) = H(x) - x，（假设）学习F(x)会比学习H(x)更容易，最极端的情况就是假设我们要学习的映射是x，那么让F(x)为0，比学习到H(x)为恒等映射要容易。这种做法的motivation是，如果增加的层能被构建成恒等映射层，那么一个更深的网络的准确率至少不会低于浅层网络。
5.  **残差块的相加**：当残差块的输入和输出不是相同维度时，有两种方法来保证维度一致，一个是补0，另一个是乘以W矩阵做映射（使用1x1卷积）。在这两种方法实行时，残差块会使用stride为2的卷积。
6.  **训练配置**：预处理时像VGG一样随机采样[256, 480]的scale，然后像AlexNet一样crop出224x224的图像以及水平翻转，然后做mean substracted。预测时候使用AlexNet的10-crop测试法，最好的结果是跟从VGG中的全卷积后的multi-scale评估，scale为{224, 256, 384, 480, 640}。在每个卷积的激活前使用BN，不使用dropout。何凯明初始化。SGD，batch size为256，学习率从0.1开始每次错误率平缓时就除以10，模型训练了60万个iteration，权重衰减为0.0001，momentum为0.9。
7.  **Identity和projection**：对于残差块的相加，有三种配置，A配置是捷径用identity，同时需要增加维度时补0。B配置是捷径用identity，但是增加维度时使用映射。C配置是捷径和增加维度都使用映射。表现是C\>B\>A，但是三者差异不大，实作上不会使用C，因为C增加了参数和计算。
8.  **网络结构**：论文阐述了ResNet-18-34-50-101-152。其中ResNet-18/34使用配置A，ResNet-50/101/152使用配置B，此外使用了bottleneck结构，如下第一个图的右图所示。
9.  **其它实验**：除了在ImageNet上，还在CIFAR-10上做了实验。还在Pascal和MS COCO上做了目标检测的实验。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200228255-969637706.png)

### ResNetv2

1.  **贡献**：在v1的基础上做了修改，提升了表现。
2.  **分析**：ResNetv1的公式如下，论文分析了h函数和f函数的选取，即shortcut路径的函数选取，以及addition后的操作选取。在ResNetv1中，h函数为恒等映射，f函数为relu函数，如下图(a)所示。
\[y_{l} = h(x_{l}) + F(x_{l},W_{l}), x_{l + 1} = f(y_{l})\]
3.  **h函数的选取**：论文分析了h函数选取为恒等映射，做常数scale，异或，1x1卷积，dropout时的表现，发现恒等映射的表现最好，主要是通过实验来分析。
4.  **f函数的选取**：由于h函数使用恒等映射表现最好，下图的分析中h函数都使用的**恒等映射**。下图(a)表示f函数为Relu，这是ResNetv1的做法。下图(b)表示f函数为BN+Relu。下图(c)表示f函数为恒等映射（Relu放到addition前）。下图d表示f函数为恒等映射，但是把最后一个Relu放在下一个残差块的F-path中。下图e和图d类似，只不过把BN也放在addition后的下一个残差块的F-path，ResNetv2使用的就是图e的结构，通过实验发现这个结构表现最好。
5.  **f和h函数都为恒等映射**：ResNetv2采取图e的结构，此时f和h函数都为恒等映射，那么上式可以写成下式，可以看到这样的式子有几个特点，首先，不管L和l差多少层，\(x_{L}\)和\(x_{l}\) 总是相差一个残差函数；其次，普通网络输入和输出的关系是很多个Wx相乘（忽略激活和BN的话），而这里是各个残差函数相加；另外，从求导式看，1+后面那一项不会总是为-1（对一个mini-batch的样本来说），所以梯度很难为0。
    \[x_{l + 1} = x_{l} + F(x_{l},W_{l})\]
    \[x_{L} = x_{l} + \sum\limits_{i = l}^{L - 1}{F(x_{i},W_{i})}\]\[\frac{\partial\varepsilon}{\partial x_{l}} = \frac{\partial\varepsilon}{\partial x_{L}}\frac{\partial x_{L}}{\partial x_{l}} = \frac{\partial\varepsilon}{\partial x_{L}}(1 + \frac{\partial x_{L}}{\partial x_{l}}\sum\limits_{i = l}^{L - 1}{F(x_{i},W_{i})})\]

    **训练配置**：和ResNetv1基本一致。对于CIFAR的实验前400个iteration用0.01（warming up），之后恢复0.1，尽管观察到这对于残差块没有必要。对于ImageNet实验，学习率为0.1（no warming up），在30轮和60轮除以10。在ResNet的开头第一个残差块和最后一个残差块是特殊case，第一个残差块的激活会放在后面的“单独卷积”之后和分成两路之前，最后一个残差块的激活放在它的addition之后。

![](./assets/论文笔记：CNN经典结构1（AlexNet，ZFNet，OverFeat，VGG，GoogleNet，ResNet）%20-%20PilgrimHui%20-%20博客园_files/1160281-20180907200245189-889919810.png)

### 参考文献

1.  AlexNet（2012 NIPS）：[ImageNet Classification with Deep Convolutional Neural Networks](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
2.  ZFNet（2014 ECCV）：[Visualizing and Understanding Convolutional Networks](https://arxiv.org/pdf/1311.2901v3)
3.  OverFeat（2014 ICLR）：[OverFeat: Integrated Recognition, Localization and Detection using Convolutional Networks](https://arxiv.org/pdf/1312.6229v4)
4.  VGG（2015 ICLR）：[Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556v6)
5.  Inception-V1（2015 CVPR）：[Going Deeper with Convolutions](https://arxiv.org/pdf/1409.4842v1)
6.  Inception-V2（2015 ICML）：[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167v3)
7.  Inception-V3（2016 CVPR）：[Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/pdf/1512.00567v3.pdf)
8.  Inception-V4（2016 ICLR）：[Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/pdf/1602.07261v2)
9.  ResNetv1（2016 CVPR）：[Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385v1)
10. ResNetv2（2016 ECCV）：[Identity Mappings in Deep Residual Networks](https://arxiv.org/pdf/1603.05027v3)