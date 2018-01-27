# [RNN的神奇之处（The Unreasonable Effectiveness of Recurrent Neural Networks）](http://blog.csdn.net/menc15/article/details/78775010) 

本文译自
<http://karpathy.github.io/2015/05/21/rnn-effectiveness/>。结合个人背景知识，忠于原文翻译，如有不明欢迎讨论。
以下正文。

-----

RNN有很多神奇的地方。我仍然记得为Image
Captioning训练的第一个RNN。我随便设定了超参数，在训练了几十分钟后这个小模型开始产生看起来非常不错、几乎有意义的描述。有些时候，模型的简单程度与结果超出预期的程度对比十分悬殊——我的第一个RNN就是这些时候之一。当时这个结果让我大吃一惊的原因是一个共识，即RNN是很难训练的（事实上相比于支持这一共识，我的经历里大多数都是反对这一共识的）。快进到一年后：我一直在训练RNN，许多次都见证了这个模型的能力(power)和健壮(robustness)，仍然会有些神奇的输出让我在某些方面感到好玩。这篇博客就是为了与你分享那些神奇之处。

> 我们将会训练一个逐字产生文本的RNN，同时思考这一问题“这怎么可能发生呢？”

本文用一个多层LSTM训练了一个character-level的语言模型，
[代码](https://github.com/karpathy/char-rnn)在Github上。你可以用这些代码来复现我的实验。但是现在先让我们来想想：究竟什么是RNN？

### 1 RNN

**序列（Sequence）**。什么使得RNN如此特殊？Vanilla
RNN的一个明显的局限是它的API的局限性太强：输入必须是固定长度的向量（如图像），产生的输出也是固定长度的向量（如不同类别的概率）。除此之外，模型是通过固定数量的计算步骤（如模型中的网络层数）来完成这一映射的。RNN如此神奇的一个核心原因就是它允许我们操作
**向量的序列**。输入可以是序列，输出也可以是序列，或者在大多数情况下，输入输出都是序列。下面是一些更具体形象的例子：
![](http://img.blog.csdn.net/20171211171937608?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

上图中矩形代表向量，箭头代表函数。输入向量是红色，输出向量是蓝色，绿色向量是RNN的状态。从左到右依次为：(1) Vanilla
mode，从固定大小的输入到固定大小的输出，如图像分类问题。(2) 输出是序列，如Image Captioning。(3)
输入是序列，如情感分析，输入是一个句子，输出是对句子情感极性的判定（积极或消极）。(4)输入是序列，输出也是序列，如机器翻译。(5)
输入与输出是序列且同步，如一种视频分类任务：对视频中的每一帧打标签。注意，对于序列长度是没有任何限制的，因为图中的递归变换（绿色矩形）可以被应用任意次。

正如你所期待的那样，这种序列化的操作机制相比于固定大小的网络更为强大，因为后者在最开始就确定要计算多少步注定了模型的厄运，而且前者对于追求更加智能的系统的我们来说也更有吸引力。另外，在之后的部分中我们将会看到，RNN将输入向量和状态向量用一个固定的（但是是学习过的）函数结合起来产生了一个新的状态向量。在编程语言中，这可以被写成一个固定的程序，这段程序有固定的输入和一些内部变量。从这个角度说，RNN本质上是在描述程序（program）。事实上，从RNN可以模拟任意程序的角度来说，RNN是图灵完备的（Turing-complete）。但是与神经网络的通用逼近定理一样，你不应理解太多。忘掉我刚刚说的吧。

> 如果说训练一个Vanilla是在优化函数，那么训练RNN就是在优化程序。

**没有序列时的序列化处理**。你可能认为输入或输出为序列的情况比较少见，但是你必须意识到的重要的一点是：即便你的输入或输出是固定的向量，你也可以用这种强大的机制序列化的处理它。例如，下面两张图展示了DeepMind的两个很棒的工作。左图展示的是一个递归网络策略的算法，它引导注意力遍历整幅图片，学习从左到右读出门牌号（
[Ba et
al.](https://arxiv.org/abs/1412.7755)）。右图是一个通过学习按顺序向canvas添加颜色来产生数字图片的递归网络（
[Gregor et
al.](https://arxiv.org/abs/1502.04623)）。

![读门牌号](http://img.blog.csdn.net/20171211185249642?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![生成门牌号](http://img.blog.csdn.net/20171211185318514?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这一段及例子想要告诉你的是：即便你的数据不是序列的形式，你也可以把它变成序列的形式，然后学习一个很强的模型序列化的处理它。学习的是一个有状态的、能够处理固定大小数据的程序。

**RNN的计算**。所以这些事情如何工作呢？核心部分，RNN有一个欺骗性的简单的API，接受输入向量 `x`和输出向量
`y`。然而，关键是输出向量的内容不仅受你给定的输入的影响，也受到你在过去给定的全部历史输入的影响。如果写成一个类，RNN的API可以由一个简单的
`step`函数组成：

``` prettyprint
rnn = RNN()
y = rnn.step(x) # x is an input vector, y is the RNN's output vector.12
```

这个RNN类有一些在每次调用step时会更新的内部状态。在最简单的情况下，这个状态只是一个隐向量 `h`。下面是在Vanilla RNN中
`step`函数的一个实现：

``` prettyprint
class RNN:
  def step(self, x):
    # update the hidden state
    self.h = np.tanh(np.dot(self.W_hh, self.h) + np.dot(self.W_xh, x))
    # compute the output vector
    y = np.dot(self.W_hy, self.h)
    return y1234567
```

上面的程序说明了Vanilla RNN的前向传递过程。这个RNN的参数是三个矩阵： `W_hh, W_xh, W_hy`。隐藏状态
`self.h`被初始化为零向量。函数 `np.tanh`实现了一个激活单元非线性的压缩到
`[-1,1]`。注意一下这是如何工作的：在tanh的输入中包含两项，一项基于过去的隐藏状态，一项基于当前的输入。在numpy中
`np.dot`是矩阵乘法函数。两项中间变量想加后传入tanh函数被压缩，结果成为新的状态变量，数学形式是          h    t   
 = t a n h (    W        h h          h      t − 1       +    W        x
h          x    t     )       

，公式中tanh函数被应用到向量中的每个元素上。

我们对RNN中的矩阵进行随机初始化，在训练过程中的大部分都在寻找可以是目标行为上升的矩阵，通常用某种损失函数来度量。损失函数表达了在给定输入序列
`x`下，你更像见到哪种
`y`作为响应。

**变“深”**。RNN是神经网络，如果你戴上深度学习的帽子，开始把模型像煎饼一样堆起来，每部分也能工作的很好。例如，我们可以像下面这样建立一个2层的递归网络：

``` prettyprint
y1 = rnn1.step(x)
y = rnn2.step(y1)12
```

换句话说我们有两个单独的RNN：一个RNN接收输入向量，第二个RNN接收第一个RNN的输出作为输入。除了其中的任一个RNN知道或在意——其实输入和输出的都只是向量，在反向传播过程中梯度会在每个模块中传递。

**加点想象力**。我想简单提一下，在实际应用中我们采用一种LSTM的网络结构，与我上面描述的有一点不同。LSTM是RNN的一种，在实际应用中效果更好，因为它的更新方程更有效以及一些更动人的反向传播特性。我不会具体介绍，但是上面我说的关于RNN的描述都是一样的，只有更新隐藏状态的数学表达式(
`self.h=...`那一行)变得更复杂了一点。从这里开始我将交替使用”RNN”和”LSTM”这两个名词，但是这篇博文里的实验都使用了LSTM。

### 2 Character-level的语言模型

好啦，现在我们对RNN是什么，为什么让人激动，以及是如何工作的有了一些了解。现在我们来通过一个有趣的应用来落实它：我们将训练一个RNN
character-level language
model。意思是，我们喂给RNN大量的文本然后让它依据已有的字符序列来对下一个字符的概率分布建模。这回让我们每一次为新文本产生一个字符。

举一个可以手工操作的例子，假设我们现在有一个词典，只包含四个可能的字母，  
“h,e,l,o”，想训练一个RNN，训练序列是”hello”。这个训练序列事实上产生了四个训练实例：1.给定上文”h”，”e”的概率应该比较大；2.给定上文”he”，”l”的概率应该比较大；3.给定上文”hel”，”l”的概率应该比较大；4.给定上文”hell”，”o”的概率应该比较大。

更具体地，我们使用1-k编码（i.e.只有字符在词典中对应的下标的位置为1，其余位置都为0）将每个字符编码成一个向量，然后将它喂进RNN，每次用
`step`函数喂进一个字符。我们将会观察到一个4维输出向量（一个字符一维），我们可以把这个向量理解成RNN当前分配给每个字符将要在序列中下一位置出现的“信心”。

![这里写图片描述](http://img.blog.csdn.net/20171211202352432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

上图是一个4维输入的及4维输出的RNN，隐藏层有3个单元。图中描述的是以”hell”为输入时RNN的前向传播过程。输出层的向量是RNN分配给下一个字符的“信心”；我们希望绿色的数值高，红色的数值低。

*（跳过半段对上图的具体描述）*  
由于RNN全部由可导计算组成，我们可以应用反向传播来找出我们应该想哪一个方向来调整权重向量使得希望的字符的分数变高。参数更新就是将每一个权重向量向梯度方向移动一个极小的量。如果我们在参数更新后喂进同样的输入，我们会发现正确的字符的分数会略微变高，错误的字符的分数会略微降低。我们可以重复许多次直到网络收敛，即它的输出最后和训练数据一致——总是能正确的预测下一个字符。

一个更技术流的解释是，我们可以对每个输出向量同时用Softmax分类器（也经常被称为交叉熵损失函数）。RNN采用mini-bach随机梯度下降法训练，我喜欢用
[RMSProp](https://arxiv.org/abs/1502.04390)或Adam（每个参数的学习率自适应）的方法来稳定更新。

注意第一次字符”l”输入时，期望目标是”l”；但第二次时期望目标是”o”。因此RNN不能只依赖于输入，必须利用递归关系来跟踪记忆上文来完成这个任务。

在测试时，我们给RNN一个字符，然后得到字符可能在下一个位置出现的概率分布。我们从这个分布采样，将采样得到的结果当做下一个字符喂进RNN。重复这个过程你就是在对文本采样！下面让我们在不同的数据集上训练RNN然后看看发生了什么。

为了更清楚一点，我也写了一个不到100行的总结 [minimal character-level RNN language model in
Python/numpy](https://gist.github.com/karpathy/d4dee566867f8291f086)。下面我们将具体分析一些由更有效的Lua/Torch代码产生的结果。

### 3 RNN的有趣之处

译者注：本部分是对在不同数据集上结果的描述，在翻译过程中有所删减，只保留以下内容：数据集简介，模型结构，训练方式，效果评估。

#### 3.1 保罗·格雷厄姆发生器

我们先用一个小的英文数据集做一个检查。我最喜欢的趣味数据集是(保罗·格雷厄姆Paul Graham的文章集锦\](
[http://www.paulgraham.com/articles.html\]](http://www.paulgraham.com/articles.html%5D)。  
数据集：将PG近五年的文章合成一个约1MB大的文本文件，包含了大约100万个字符。  
模型：2层LSTM隐藏层，每层512个节点，大约350万个参数，每层dropout设为0.5。  
训练：每个batch包含100条样本，反向传播进行100个timestep就截断。在TITAN Z
GPU上，每个batch号是0.46秒。如果将BPTT限制在50，效果差不多但是耗时可以减半。  
效果评估：一段节选如下：

> “The surprised in investors weren’t going to raise money. I’m not
> the  
> company with the time there are all interesting quickly, don’t have
> to  
> get off the same programmers. There’s a super-angel round
> fundraising,  
> why do you can do. If you have a different physical investment are  
> become in people who reduced in a startup with the way to argument
> the  
> acquirer could see them just that you’re also the founders will part  
> of users’ affords that and an alternation to the idea. \[2\] Don’t
> work  
> at first member to see the way kids will seem in advance of a bad  
> successful startup. And if you have to act the big company
too.”

不幸的是，这个RNN模型完全不能取代PG，但是记得这是RNN完全从0开始学英语得到的，而且是在一个比较小的数据集上（包含了逗号，省略号，空格）。而且看起来它学会了支撑自己的观点（e.g.\[2\]）。而且某些地方能提供一丝灵感，如”a
company is a meeting to think to investors”。如果你感兴趣，可以看看这个
[5万字符的结果](http://cs.stanford.edu/people/karpathy/char-rnn/pg.txt)。

**温度参数**。我们可以调整采样过程中Softmax函数的temperature参数。把T从1降低会使RNN更加自信，这意味着结果会更加保守，更“像”训练样本。相反，更高的T会提高多样性，作为代价错误会更多（如拼写错误等）。特殊的，将T设为接近0的值会产生最像PG说的话，如

> “is that they were all the same thing that was a startup is that
> they  
> were all the same thing that was a startup is that they were all the  
> same thing that was a startup is that they were all the
same”

译者注：温度参数是Softmax函数中的一个参数，默认为1。当T很大时，即趋于正无穷时，所有的激活值对应的激活概率趋近于相同（激活概率差异性较小）；而当T很低时，即趋于0时，不同的激活值对应的激活概率差异也就越大。Hinton在2015年的一篇文章中阐释了
[如何根据温度参数来soften神经网络的输出，提出了distillation的方法](https://www.cs.toronto.edu/~hinton/absps/distillation.pdf)。

#### 3.2 莎士比亚

看起来RNN能学会拼写英语单词。那么当数据中有更多的结构(structure)和题材(style)时它能否学会呢？为了检验这一点我下载了莎士比亚的所有作品来实验。  
数据集：4.4MB的文本文件  
模型：3层的LSTM隐藏层，每层512个节点  
训练：几小时  
效果评估：

> PANDARUS:  
> Alas, I think he shall be come approached and the day When little  
> srain would be attain’d into being never fed, And who is but a chain  
> and subjects of his death, I should not sleep.
> 
> Second Senator: They are away this miseries, produced upon my soul,  
> Breaking and strongly should be buried, when I perish The earth and  
> thoughts of many states.
> 
> DUKE VINCENTIO: Well, your wit is in the care of side and that.
> 
> Second Lord: They would be ruled after this chamber, and my fair
> nues  
> begun out of the fact, to be conveyed, Whose noble souls I’ll have
> the  
> heart of the wars.
> 
> Clown: Come, sir, I will make did behold your worship.
> 
> VIOLA: I’ll drink it.

尽管RNN只知道字符，但是它同时学会了说话者的名字和内容。有时还会产生更长的独白，例如：

> VIOLA: Why, Salisbury must find his flesh and thought That which I
> am  
> not aps, not a man and in fire, To show the reining of the raven and  
> the wars To grace my hand reproach within, and not a fair are hand,  
> That Caesar and my goodly father’s world; When I was heaven of  
> presence and our fleets, We spare with hours, but cut thy council I
> am  
> great, Murdered and by thy master’s ready there My power to give
> thee  
> but so much as hell: Some service in the noble bondman here, Would  
> show him to her wine.
> 
> KING LEAR: O, if you were a feeble sight, the courtesy of your law,  
> Your sight and several breath, will wear the gods With his heads,
> and  
> my hands are wonder’d at the deeds, So drop upon your lordship’s
> head,  
> and your opinion Shall be against your honour.

#### 3.3 维基百科

我们已经看到LSTM可以学会拼写单词以及特定的语法结构。下面让我们来提高难度，在有结构的markdown文本上训练。  
数据集： [Hutter
Prize 100MB数据](http://prize.hutter1.net/)。其中96MB用来训练，其他用来测试。  
训练：一夜(overnight)  
效果评估：

> Naturalism and decision for the majority of Arab countries’
> capitalide  
> was grounded by the Irish language by \[\[John Clair\]\], \[\[An
> Imperial  
> Japanese Revolt\]\], associated with Guangzham’s sovereignty. His  
> generals were the powerful ruler of the Portugal in the
> \[\[Protestant  
> Immineners\]\], which could be said to be directly in Cantonese  
> Communication, which followed a ceremony and set inspired prison,  
> training. The emperor travelled back to \[\[Antioch, Perth, October  
> 25|21\]\] to note, the Kingdom of Costa Rica, unsuccessful fashioned
> the  
> \[\[Thrales\]\], \[\[Cynth’s Dajoard\]\], known in western
> \[\[Scotland\]\], near  
> Italy to the conquest of India with the conflict. Copyright was the  
> succession of independence in the slop of Syrian influence that was
> a  
> famous German movement based on a more popular servicious,  
> non-doctrinal and sexual power post. Many governments recognize the  
> military housing of the \[\[Civil Liberalization and Infantry
> Resolution  
> 265 National Party in Hungary\]\], that is sympathetic to be to the  
> [\[Punjab  
> Resolution\]](PJS)\[
> <http://www.humah.yahoo.com/guardian.cfm/7754800786d17551963s89.htm>  
> Official economics Adjoint for the Nazism, Montgomery was swear to  
> advance to the resources for those Socialism’s rule, was starting to  
> signing a major tripad of aid exile.\]\]

上面的雅虎网址并不存在。值得注意的是，模型学会了正确的使用括号。模型也学会了正确使用一些复杂的markdown结构，如标题，列表等，像下面这样：

> { { cite journal | id=Cerling Nonforest  
> Department|format=Newlymeslated|none } } ”www.e-complete”.
> 
> ”’See also”’: \[\[List of ethical consent processing\]\]
> 
> \== See also ==  
> \*\[\[Iender dome of the ED\]\]  
> \*\[\[Anti-autism\]\]
> 
> \===\[\[Religion|Religion\]\]===  
> \*\[\[French Writings\]\]  
> \*\[\[Maria\]\]  
> \*\[\[Revelation\]\]  
> \*\[\[Mount Agamul\]\]
> 
> \== External links==  
> \* \[ <http://www.biblegateway.nih.gov/entrepre/> Website of the World
> Festival. The labour of India-county defeats at the Ripper of  
> California Road.\]
> 
> \==External links==  
> \* \[ <http://www.romanology.com/> Constitution of the Netherlands and
> Hispanic Competition for Bilabial and Commonwealth Industry  
> (Republican Constitution of the Extent of the Netherlands)\]

有时模型还会产生随机的但是合法的XML，像下面这样：

``` prettyprint
<page>   <title>Antichrist</title>   <id>865</id>   <revision>
    <id>15900676</id>
    <timestamp>2002-08-03T18:14:12Z</timestamp>
    <contributor>
      <username>Paris</username>
      <id>23</id>
    </contributor>
    <minor />
    <comment>Automated conversion</comment>
    <text xml:space="preserve">#REDIRECT [[Christianity]]</text>   </revision> </page>12345678910
```

在上面这段XML中，时间戳、id等标签的内容都是合法的。标签也按照正确的顺序关闭了。

#### 3.4 代数几何(LaTeX)

前面三个例子的结果说明模型在学习复杂的语法结构上确实表现不错，这给我和同事 [Justin
Johnson](http://cs.stanford.edu/people/jcjohns/)留下了深刻印象，于是我们决定在结构化的领域进行更深入的尝试并拿到了一本代数几何方面的书。我们下载了LaTeX源文件(大小为16MB的一个文件)并训练了一个多层LSTM。令人惊喜的是，sample生成的LaTeX源码几乎可以编译。我们手工调整了几个问题然后你就可以看到下面这样的“假数学”，太惊喜了！

![这里写图片描述](http://img.blog.csdn.net/20171212103806055?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
![这里写图片描述](http://img.blog.csdn.net/20171212103902362?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在上面的图中你可以看到，模型还试图产生LaTeX示意图，虽然并没有真的解决它。我还喜欢它选择跳过证明的那部分（第二张图左上角）。当然，你要记得LaTeX其实是一种相对复杂的结构化语法格式，我自己甚至还没有完全掌握。

下面是一段模型产生的原始文本：

``` prettyprint
\begin{proof} We may assume that $\mathcal{I}$ is an abelian sheaf on $\mathcal{C}$. \item Given a morphism $\Delta : \mathcal{F} \to \mathcal{I}$ is an injective and let $\mathfrak q$ be an abelian sheaf on $X$. Let $\mathcal{F}$ be a fibered complex. Let $\mathcal{F}$ be a category. \begin{enumerate} \item \hyperref[setain-construction-phantom]{Lemma} \label{lemma-characterize-quasi-finite} Let $\mathcal{F}$ be an abelian quasi-coherent sheaf on $\mathcal{C}$. Let $\mathcal{F}$ be a coherent $\mathcal{O}_X$-module. Then $\mathcal{F}$ is an abelian catenary over $\mathcal{C}$. \item The following are equivalent \begin{enumerate} \item $\mathcal{F}$ is an $\mathcal{O}_X$-module. \end{lemma}1
```

这段样本是一个相对好的模型得到的，但仍然有一些错误。比如，由 `\begin{proof}`开始但是却以
`\end{lemma}`来结尾。这个是我们需要手工调整的问题的一个例子，很有可能是由于依赖过于长期而导致的——当模型结束证明的时候它已经忘记了它是在做一个证明还是一个引理。相似地，它开始了一个
`\begin{enumerate}`但是忘了结束它。当我们使用更大或更好的模型时，这类问题会少一些，但是仍然存在。

#### 3.5 Linux源码

我想探索一下结构化数据表现上的极限，因此最后的挑战我决定使用代码。我把
[Github上的Linux代码库](https://github.com/torvalds/linux)中的全部代码和头文件合成了一个巨大的文件（474MB的C代码）。然后我花了几天时间训练了几个达到了我的GPU计算极限的3层LSTM模型。这些模型大概有一千万个参数，对于RNN模型来讲仍然算比较少的。结果十分有趣：

``` prettyprint
/*
 * Increment the size file of the new incorrect UI_FILTER group information
 * of the size generatively.
 */
static int indicate_policy(void)
{
  int error;
  if (fd == MARN_EPT) {
    /*
     * The kernel blank will coeld it to userspace.
     */
    if (ss->segment < mem_total)
      unblock_graph_and_set_blocked();
    else
      ret = 1;
    goto bail;
  }
  segaddr = in_SB(in.addr);
  selector = seg / 16;
  setup_works = true;
  for (i = 0; i < blocks; i++) {
    seq = buf[i++];
    bpf = bd->bd.next + i * search;
    if (fd) {
      current = blocked;
    }
  }
  rw->name = "Getjbbregs";
  bprm_self_clearl(&iv->version);
  regs->new = blocks[(BPF_STATS << info->historidac)] | PFMR_CLOBATHINC_SECONDS << 12;
  return segtable;
}1234567891011121314151617181920212223242526272829303132
```

代码整体看起来不错。当然，我不认为它能编译但是当你快速浏览时看起来很像是一个巨大的C代码库。注意RNN时不时的在代码中加入一些注释作调剂，而且很少有语法错误。比如，它正确使用了字符串、指针等，也学会了匹配括号和缩进代码。一个比较普遍的问题是它失去了对变量名的追踪，经常会使用未定义的变量，声明从未使用的变量或者是返回一个不存在的变量。

还有很多有趣的地方，如果你感兴趣可以看看这个
[1MB的Linux代码样本](http://cs.stanford.edu/people/karpathy/char-rnn/linux.txt)。

#### 3.6 生成婴儿名字

让我们试一个有意思的。给RNN一个包含8000婴儿名的大文件，每行是一个名字，然后它可以生成新名字！我挑选了一些在训练数据中没有出现过的新名字（90%没有出现过）列在下面：

> Rudi Levette Berice Lussa Hany Mareanne Chrestina Carissy Marylen  
> Hammine Janye Marlise Jacacrie Hendred Romand Charienna Nenotto Ette  
> Dorane Wallen Marly Darine Salina Elvyn Ersia Maralena Minoria Ellia  
> Charmin Antley Nerille Chelon Walmor Evena Jeryly Stachon Charisa  
> Allisa Anatha Cathanie Geetra Alexie Jerin Cassen Herbett Cossie
> Velen  
> Daurenge Robester Shermond Terisa Licia Roselen Ferine Jayn Lusine  
> Charyanne Sales Sanny Resa Wallon Martine Merus Jelen Candica Wallin  
> Tel Rachene Tarine Ozila Ketia Shanne Arnande Karella Roselina
> Alessia  
> Chasty Deland Berther Geamar Jackein Mellisand Sagdy Nenc Lessie  
> Rasemy Guen Gavi Milea Anneda Margoris Janin Rodelin Zeanna Elyne  
> Janah Ferzina Susta Pey Castina

更多名字可以去
[这里](http://cs.stanford.edu/people/karpathy/namesGenUnique.txt)看。我最喜欢的几个是”Baby”,
“Killie”, “Char”, “R”, “More”, “Mars”, “Hi”, “Saddie”, “With”和
“Ahbort”。在写小说时或者是在给创业公司起名字时这能提供一些有用的灵感。

### 4 理解在发生的事情

我们看到在训练后的结果会让人印象深刻，但是这是如何工作的呢？下面让我们做两个快速实验来简单的揭开面纱。

#### 4.1 训练时样本(sample)的演变

*(译者注：这里的样本原文是sample，指的是模型生成的文本。)*  
在模型训练时观察样本是如何演变的非常有趣。我用列夫·托尔斯泰的《战争与和平》训练了一个LSTM并且在每100次迭代后生成样本。在第一个100次迭代后，模型生成的像是随机的、杂乱的一堆东西：

> tyntd-iafhatawiaoihrdemot lytdws e ,tfti, astai f ogoh eoase  
> rrranbyne ‘nhthnee e plia tklrgd t o idoe ns,smtt h ne etie  
> h,hregtrs nigtike,aoaenns
lng

然而，注意它至少开始有了单词是被空格分隔的这样的概念，除了有时会用两个空格。他还不知道逗号后面总是跟着一个空格。在300次迭代后我们可以看到模型开始学会了引号和句号：

> “Tmont thithey” fomesscerliund Keushey. Thom here sheulke,
> anmerenith  
> ol sivh I lalterthend Bleipile shuwy fil on aseterlome coaniogennc
> Phe  
> lism thond hon at. MeiDimorotion in ther thize.”

在500次迭代后：

> we counter. He stutn co des. His stanted out one ofler that  
> concossions and was to gearang reay Jotrets and with fre colt otf  
> paitt thin wall. Which das stimn

可以看到模型学会了拼写最简单、常见的单词，比如”we”, “He”, “His”, “Which”,
“and”等。在700次迭代后，我们开始看到更多的类英语文本出现：

> Aftair fall unsuch that the hall for Prince Velzonski’s that me of
> her  
> hearly, and behs to so arwage fiving were to it beloge, pavu say  
> falling misfort how, and Gogition is so overelical and ofter.

在1200次迭代后我们开始看到引语的使用以及问号、感叹号，长句子也被掌握了：

> “Kite vouch\!” he repeated by her door. “But I would be done and  
> quarts, feeling, then, son is people….”

直到最后，在大约2000次迭代后，模型开始正确拼写单词，引语，名字等等：

> “Why do what that day,” replied Natasha, and wishing to himself the  
> fact the princess, Princess Mary was easier, fed in had oftened him.  
> Pierre aking his soul came to the packs and drove up his
> father-in-law  
> women.

所以演变的大致路径是：模型先发现了普遍的词语-空格结构，然后开始快速学习单词；从短单词开始知道最后学会长单词；跨过多个单词的主题/话题（以及比较长期的依赖关系）在这之后很久才出现。

#### 4.2 可视化预测结果以及RNN的“神经元”激发

一个有趣的可视化是观察预测结果中个字符的分布。我们给一个Wikipedia
RNN模型输入验证集中的字符数据（第一行，用蓝色或绿色标注的），然后从对下一字符的预测中选择信心最高（即概率最高）的5个。猜测字符的颜色与概率正相关（所以深红色代表很有可能，白色代表不太可能）。例如，注意到有几串字符中模型对下一个字母极端自信。

我们随机从隐藏层中选择了一个神经元，用它的激发程度来给输入字母序列染色。就是说，绿色代表这个神经元非常兴奋，蓝色代表这个神经元不太兴奋（如果你熟悉LSTM的细节的话，其实兴奋程度是隐藏状态向量中\[-1,1\]区间内的一个值，是经过gate和tanh后的LSTM单元状态）。直观上将，这是在对RNN大脑读入输入序列时的某个神经元的激发状态进行可视化。不同的神经元可能在关注不同的模式，下面我们列举了我认为有趣或者可解释的4个不同的神经元（很多并不有趣或可解释）：  
![这里写图片描述](http://img.blog.csdn.net/20171213150205823?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
上图中的神经元似乎对URL很兴奋，在URL外部转为抑制状态。LSTM很可能是用这个神经元来记住是不是在URL内。

![这里写图片描述](http://img.blog.csdn.net/20171213150226441?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
上图展示的神经元在\[\[\]\]的markdown环境内很兴奋，在外部则转为抑制状态。有趣的是，神经元并不能在看到字符”\[“后立刻激发，他必须等到第二个”\[“才会激发。对当前遇到一个”\[“还是两个”\[“来计数的任务很有可能是由另一个神经元完成的。

![这里写图片描述](http://img.blog.csdn.net/20171213150239398?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
上图展示的神经元在\[\[\]\]环境中几乎是线性变化。换句话说，它的兴奋状态可以给RNN提供一个跨越\[\[\]\]范围的时间相对坐标系统。RNN可能是在以来它在\[\[\]\]范围内出现的早晚来判断不同字符出现可能性的高低。

![这里写图片描述](http://img.blog.csdn.net/20171213150253517?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
上面的神经元有非常短期的行为特性：它一直保持相对的平静但是会在www序列的第一个w出现后突然抑制。RNN可能用这个神经元来计算在www序列中走了多远，这样它能知道是否应该产生另一个w，或是直接开始URL。

当然，上面的大部分结论都是基于感觉的，缺乏逻辑或理论证明，因为RNN的隐藏状态是一个巨大的、高维的、分散的表达。这些可视化是用传统的HTML/CSS/Javascript来生成的，如果你想做出类似的可视化可以看看
[这份代码](http://cs.stanford.edu/people/karpathy/viscode.zip)。

我们把上面的可视化压缩，去掉所有可能的预测，只展示文本，并用颜色来表示一个神经元的激活状态。我们可以看到尽管绝大多数神经元做的事情并不可解释，大概5%显示出他们确实学到了一些有趣的、可解释的算法：  
![这里写图片描述](http://img.blog.csdn.net/20171213152654862?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWVuYzE1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

再说一遍，这个方法优美的地方是你不必对任何对可能有用的东西（例如是否正处于引号内）进行硬编码就可以预测下一个可能的字符。我们仅仅是用原始数据训练LSTM，它来决定什么是有必要跟踪的。换句话说，RNN的神经元中的一个在训练中逐渐的对自己进行调整来变成一个引号检测单元，因为这可能会直接帮助模型在任务中表现的更好。这是深度学习模型（和大多数端到端训练）能力来源的一个最简洁且有吸引力的一个例子之一。

### 5 源代码

我希望我已经说服了你：训练字符级别的语言模型是一个非常有趣的练习。你可以用这份我在Github上发布的
[char-rnn代码](https://github.com/karpathy/char-rnn)训练你自己的模型。训练一个可以生成样本的字符级别的模型需要一个大文本文件。另外，GPU对此有所帮助，因为用CPU训练速度会慢10倍。无论如何，如果你完成了在某些数据上的训练并得到了有趣的结果，请让我知道！如果你对Torch/Lua不太了解记得还有一个
[100行的python版本](https://gist.github.com/karpathy/d4dee566867f8291f086)。

*(译者注：在这里有一段对Torch的推荐，不翻译了，原文如下：)*  
Brief digression. The code is written in Torch 7, which has recently
become my favorite deep learning framework. I’ve only started working
with Torch/LUA over the last few months and it hasn’t been easy (I spent
a good amount of time digging through the raw Torch code on Github and
asking questions on their gitter to get things done), but once you get a
hang of things it offers a lot of flexibility and speed. I’ve also
worked with Caffe and Theano in the past and I believe Torch, while not
perfect, gets its levels of abstraction and philosophy right better than
others. In my view the desirable features of an effective framework are:

  - CPU/GPU transparent Tensor library with a lot of functionality
    (slicing, array/matrix operations, etc. )
  - An entirely separate code base in a scripting language (ideally
    Python) that operates over Tensors and implements all Deep Learning
    stuff (forward/backward, computation graphs, etc)
  - It should be possible to easily share pretrained models (Caffe does
    this well, others don’t), and crucially
  - NO compilation step (or at least not as currently done in Theano).
    The trend in Deep Learning is towards larger, more complex networks
    that are are time-unrolled in complex graphs. It is critical that
    these do not compile for a long time or development time greatly
    suffers. Second, by compiling one gives up interpretability and the
    ability to log/debug effectively. If there is an option to compile
    the graph once it has been developed for efficiency in prod that’s
    fine.

### 扩展阅读

在这篇博文结束前我想在一个更大的背景下定位RNN，并概述当前研究方向。RNN最近开始开始在深度学习领域赢得口碑，让人兴奋。与卷积神经网络相似，RNN也已经存在了几十年但是似乎知道最近它的全部潜力才被广泛认识到，很大程度上得益于计算资源的增长。下面是对一些近期工作的概述：

在
**NLP和语音领域**，RNN可以把语音转录成文本，实现机器翻译、生成手写文本，当然，也被用做强大的语言模型(同时在字符级别和单词级别)。目前看起来单词级别的模型比字符级别的模型更好，但是这当然是暂时的。

**计算机视觉**。同样，RNN在计算机视觉领域也快速普及。例如，我们可以看到RNN在帧级别的视频分类，图像标注，视频标注，图像问答。我最喜欢的CV领域RNN工作是
[Recurrent Models of Visual Attention](https://arxiv.org/abs/1406.6247)。

（更新中，TBA）