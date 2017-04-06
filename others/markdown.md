<!--toc-->

- [在编号下加入代码](#在编号下加入代码)
- [代码块指定编程语言](#代码块指定编程语言)
- [画图](#画图)
- [atom 星号问题，下划线问题](#atom-星号问题下划线问题)
	- [问题描述](#问题描述)
	- [解决办法](#解决办法)
	- [参考](#参考)
- [language-pfm 代码块的着色一直蔓延到下一个代码块？](#language-pfm-代码块的着色一直蔓延到下一个代码块)
	- [解决办法](#解决办法-1)
	- [另一个问题](#另一个问题)
	- [最终解决](#最终解决)
- [渲染一个代码块之后，后面的渲染基本上都不对，乱七八糟的](#渲染一个代码块之后后面的渲染基本上都不对乱七八糟的)
	- [原因&解决办法](#原因解决办法)
- [折叠展开代码](#折叠展开代码)
- [求和符号](#求和符号)

<!-- tocstop -->

# 在编号下加入代码
  把编号内的所有内容都增加一个缩进，这样，这些内容都是在 编号下的
  注意，代码块里面的代码也要增加一个缩进
  ![1]


# 代码块指定编程语言
在 **```** 后面加方括号，括号内写语言
```
> ```{cpp}
> ```
```
![2]

# 画图
```{mermaid}
graph LR
A --> B
B --> C
C -- 线上文字 --> A
```

# atom 星号问题，下划线问题

## 问题描述
Wrong syntax highlighting when one line contains a single `*` or `_`

atom 在markdown文件进行编辑的时候，在大部分地方输入 星号 是 用转移字符`\*`
但是在代码块内输入星号，显然是不需要使用转义字符的，但是编辑器对代码块内的星号，还是会执行 紫色加亮，如图![3]

## 解决办法
1. 在代码块后面添加星号，使得这个紫色强调结束
    使用html的注释，可以使得这个星号不会出现的最终的渲染界面上
    ```
    <!--*-->
    ```
    ![4]

2. 使用 其他人 对 language-gfm 的优化插件
    使用 其他插件 替换 language-gfm 就可以了
    1. 安装 其他插件
    2. 禁用 language-gfm

## 参考
[atom的官方讨论](https://github.com/atom/language-gfm/issues/44)
[另一个讨论](https://github.com/leipert/language-pfm/issues/5)
[language-pfm](https://github.com/leipert/language-pfm)
[language-gfm-enhanced](https://github.com/shd101wyy/language-gfm-enhanced)

# language-pfm 代码块的着色一直蔓延到下一个代码块？
如图:![5]
## 解决办法
产生的原因是因为代码块内的括号没有匹配（为什么会这样就不知道了）
所以匹配好括号就ok了

## 另一个问题
但是 匹配之后，后面依旧不是markdown的高亮

## 最终解决
根本原因：代码块内的代码不符合指定语言类型的语法要求
代码块如果指定了语言，那么里面的语句必须要符合这个语言的语法

# 渲染一个代码块之后，后面的渲染基本上都不对，乱七八糟的
渲染第一个代码块之后，后面的代码块有时候对，有时候会把外面的文字也包括进去了
## 原因&解决办法
那个因为第一个代码块 **```** 后面有3空格


# 折叠展开代码
1. 添加脚本
	```
	<script>
	function ishidden(odiv){
	  var vdiv = document.getElementById(odiv);
	  vdiv.style.display = (vdiv.style.display == 'none')?'block':'none';
	}
	</script>
	```

2. 添加以下语句
	```
	<div onclick="ishidden('X')">有东西藏起来了!</div>
	<div id="X" style="display:none;">啊，被发现了</div>
	```

# 求和符号
$\displaystyle{\sum_{i=1}^{n}}$

[参考](http://nyhtn.leanote.com/post/ea9dee43df01)

[1]:assets/markdown-c92d7.png
[2]:assets/markdown-e700d.png
[3]:assets/markdown-126de.png
[4]:assets/markdown-1ef56.png
[5]:assets/markdown-2538c.png
