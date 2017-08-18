<!--toc-->

- [stack](#stack)
	- [ADT](#adt)
	- [参考代码 Array-based Stack](#参考代码-array-based-stack)
	- [Linked Stack](#linked-stack)
	- [应用](#应用)

<!-- tocstop -->

# stack
栈，类似一个盒子，先入后出，FILO

## ADT
```{cpp}
class stack{
	virtual void push(int e) = 0;
	virtual void pop() = 0;
	virtual int top() = 0;
	virtual int size() = 0;
	virtual bool empty() = 0;
};
```

## 参考代码 Array-based Stack
使用数组实现比较简单，只需要一个指向栈顶的'指针'，对这个'指针'进行操作即可，再注意一下边界问题就可以了。

```{cpp}
class stack{
public:
	int maxSize,cnt;
	int *arr;
	stack(int _maxSize) :maxSize(_maxSize), cnt(0) { arr = new int[maxSize]; }
	~stack() { delete[] arr; }

	bool push(int e) {
		if (cnt >= maxSize)	return false;
		arr[cnt++] = e;
	}

	int top() {
		if (cnt <= 0)	return -0x3F3F3F3F;
		return arr[cnt - 1];
	}

	bool pop(){
		if (cnt <= 0)	return false;
		--cnt;
		return true;
	}

	bool empty() {
		return cnt == 0;
	}

	int size() {
		return cnt;
	}
};
```

## Linked Stack
使用列表实现栈，实际上就是对链表的一个修改而已，具体代码和链表类似。
和链表相比，栈的操作更加简单。

## 应用
1. [括号匹配](http://222.201.146.216/JudgeOnline/problem.php?cid=1381&pid=1)
		括号字符串匹配 : 给定 一个括号 字符串 ,判断 是否 合法
		每遇到 一个 "(" 入栈 ,每遇到 一个 ")" 就出栈 ,处理完之和 ,栈是空的则合法
		优化 : 不需要 入栈 ,只需要 记录 已经 入栈 的 数目 即可


2. [四则运算](http://222.201.146.216/JudgeOnline/problem.php?cid=1445&pid=2)
		在系统调用函数的过程中,会 把函数调用处 下一行代码的地方 压入栈 ,


3. 使用循环模拟函数调用过程
		递归 = 循环语句 + 栈		
		有时候 可以 通过 把 递归 改写 成循环 语句 (借用栈的辅助),来加快效率
		见 树的非递归式遍历
