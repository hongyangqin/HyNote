
<!--toc-->

- [基础数据结构之List](#基础数据结构之list)
	- [list的约定&ADT](#list的约定adt)
	- [fence](#fence)
	- [Array-based list](#array-based-list)
		- [优缺点](#优缺点)
		- [数组空间不足怎么办](#数组空间不足怎么办)
		- [参考代码](#参考代码)
		- [时间复杂度](#时间复杂度)
	- [Linked list](#linked-list)
		- [优点](#优点)
		- [缺点](#缺点)
		- [参考代码](#参考代码-1)
			- [为什么fence定义的时候，一般指向前面的元素，而不是后面的元素？](#为什么fence定义的时候一般指向前面的元素而不是后面的元素)
			- [为什么 定义 head为第一个节点而不是空指针，且不存放任何数据](#为什么-定义-head为第一个节点而不是空指针且不存放任何数据)
		- [时间复杂度](#时间复杂度-1)
			- [Linked list d的插入操作一定 比 Array-based list 慢吗？](#linked-list-d的插入操作一定-比-array-based-list-慢吗)
	- [小结：Array-based list 和 linked list 的对比](#小结array-based-list-和-linked-list-的对比)
	- [freeList 优化](#freelist-优化)
		- [优化的原因](#优化的原因)
		- [解决办法](#解决办法)
		- [参考代码](#参考代码-2)
	- [Double-linked list 双向列表](#double-linked-list-双向列表)
		- [优化的原因](#优化的原因-1)
		- [优化的方法](#优化的方法)

<!-- tocstop -->
# 基础数据结构之List
List：数据的集合，列表（比如，菜单，歌单等）
Notation（符号） of list：$a_0,a_1,...,a_{n-1}$
Length（长度）of list：数组的元素数目
分类1：$\begin{cases}
sorted &,\text{有序的}\\
unsorted &,\text{无序的}
\end{cases}$

分类2：$\begin{cases}
Array-based-list&，数组实现的list\\
Linked-list &，链表实现的list
\end{cases}$

## list的约定&ADT
成员属性$\begin{cases}
head &，list 的头部\\
tail &，list的尾部\\
fence &，list的当前栅栏的位置，这里约定函数操作的都是fence后面的元素\\
listSize &，list的大小(length)
\end{cases}$

函数operations$\begin{cases}
insert/remove &，在 fence处 插入/删除  \\
search &，查找 \\
next &，fence后移 \\
previous &，fence前移\\
repalce &，替换当前fence后面的元素\\
setFence &，设置fencen的位置\\
getSzie &，获得列表大小\\
clear &，清空列表\\
\end{cases}$

## fence
fence：栅栏，当前操作的位置
$<1,2|3,4,5>$

## Array-based list
Array-based list：数组实现的list，连续存放

### 优缺点
$\begin{cases}
优点：读取快 \\
缺点：插入删除慢
\end{cases}$

### 数组空间不足怎么办
1. 申请更大的内存空间，把数据拷贝过去
2. 使用链表实现

### 参考代码
```{cpp}
class ArrayList {
public:
	//列表的容量，数据，当前数目，当前操作的位置(操作第一个元素的位置是 -1)
	int maxSize, *arr, cnt, fence;
	ArrayList(int _maxSize = 100) :maxSize(_maxSize), cnt(0), fence(-1) { arr = new int[maxSize]; }
	~ArrayList() { delete[] arr; }

	//在 fence 指向的元素后面插入元素 e,完成之后，fence指向插入的元素
	bool insert(int e) {
		//列表满
		if (cnt >= maxSize)	return false;

		//把fence后面的数据 往后挪一位
		for (int i = cnt - 1; i > fence; --i) {
			arr[i + 1] = arr[i];
		}

		//加入元素e 到fence后面
		arr[++fence] = e;

		//数量更新
		++cnt;
		return true;
	}

	//设置fence的位置，返回是否成功
	bool setPos(int pos) {
		//判断pos 是否合法
		if (pos < -1 || pos >= maxSize)	return false;
		fence = pos;
		return true;
	}

	//获取当前fence 的位置
	int getPos() { return fence; }

	//删除fence后面的元素，成功返回true，e存放被删除的元素，失败（fence后面没有元素）返回false
	bool remove(int & e) {
		if (fence == cnt - 1)	return false;
		e = arr[fence + 1];
		for (int i = fence + 1; i < cnt; ++i) {
			arr[i] = arr[i + 1];
		}
		--cnt;
		return true;
	}

	//删除在 列表中 值为 e的元素一次，不存在返回false
	bool removeItemOnce(int e) {
		int i;
		//寻找元素
		for (i = 0; i < cnt && arr[i] != e; ++i);

		//不存在
		if (i == cnt)	return false;

		//存在把后面的元素往前挪动
		for (; i < cnt; ++i) {
			arr[i] = arr[i + 1];
		}

		//更新 cnt 和 fence
		if (fence == cnt - 1)	--fence;
		--cnt;
		return true;
	}

	//查找元素 e 是否存在于 列表中
	bool find(int e) {
		for (int i = 0; i < cnt; ++i) {
			if (arr[i] == e)	return true;
		}
		return false;
	}

	//返回 fence 后面元素的值，fence后面没有元素返回false
	bool getValue(int & e) {
		if (fence == cnt - 1)	return false;
		e = arr[fence + 1];
		return true;
	}

};
```

### 时间复杂度
插入:$O(n)$
删除:$O(n)$
查找:$O(n)$(非有序，Array-based-sorted list 为 $\log n$)

## Linked list
原理：
![1]
使用指针存放下一个存储单元的地址

### 优点
Array-based list 的缺点,存满之后，需要重新分配内存空间，但是 Linked-List 能动态分配空间

### 缺点
如果频繁 插入/删除(**new** / **delete**)操作，代价会很大。

### 参考代码
```{cpp}

class Node {
public :
	int v;
	Node * hyNext;
	Node(int _v = 0, Node * _hyNext = NULL) :v(_v), hyNext(_hyNext) {}
};

class LinkedList {
public:
	//列表的 头部，当前位置，尾部
	//head是一个非空节点，但不存放任何元素，fence，tail都不会指向空，便于代码的编写
	Node *head,*fence,*tail;

	//当前数目
	int cnt;
	LinkedList() {init();}
	~LinkedList() {clear();}

	void init() {fence = tail = head = new Node();cnt = 0;}

	void clear() {
		//fence 充当临时变量
		while (head) {
			fence = head;
			head = head->hyNext;
			delete fence;
		}		
		fence = tail = head = NULL;
	}

	//在 fence 指向的元素后面插入元素 e,完成之后，fence指向保持不变，同时更新大小，和尾巴
	void insert(int e) {
		fence->hyNext = new Node(e, fence->hyNext);

		//更新tail
		if (fence == tail)	tail = fence->hyNext;
		++cnt;
	}

	//设置fence的位置，返回是否成功,pos == 0表示链表最前面。在这个位置插入元素就直接加入到头部
	bool setPos(int pos) {
		if (pos < 0 || pos > cnt)	return false;
		fence = head;
		while (pos) {
			fence = fence->hyNext;
			--pos;
		}
	}

	//获取当前fence 的位置
	Node * getPos() { return fence; }

	//删除fence后面的元素，成功返回true，e存放被删除的元素，失败（fence后面没有元素）返回false
	bool remove(int & e) {
		if (fence == tail)	return false;
		Node * target = fence->hyNext;
		e = target->v;
		fence->hyNext = target->hyNext;
		if (target == tail)	tail = fence;
		delete target;		
		--cnt;
		return true;
	}

	//删除在 列表中 值为 e的元素一次，不存在返回false
	bool removeItemOnce(int e) {
		Node * tmp = head->hyNext,*pre = head;
		while (tmp) {
			if (tmp->v == e) {
				pre->hyNext = tmp->hyNext;
				if (tmp == tail) tail = pre;					
				if (tmp == fence) fence = pre;
				delete tmp;
				--cnt;
				return true;
			}
			pre = pre->hyNext;
			tmp = tmp->hyNext;
		}
		return false;
	}

	//查找元素 e 是否存在于 列表中
	bool find(int e) {
		Node * tmp = head->hyNext;
		while (tmp) {
			if (tmp->v == e) {
				return true;
			}
			tmp = tmp->hyNext;
		}
		return false;
	}

	//返回 fence 后面元素的值，fence后面没有元素返回false
	bool getValue(int & e) {
		if (fence == tail)	return false;
		e = fence->hyNext->v;
		return true;
	}

};
```

#### 为什么fence定义的时候，一般指向前面的元素，而不是后面的元素？
指向前者的时候，操作更快。指向后者的话，在插入操作的时候，需要花费$\Theta(n)$的时间来查找前面的元素

#### 为什么 定义 head为第一个节点而不是空指针，且不存放任何数据
这样可以使得head tail fence 这3个指针永远不会指向空，在后面代码的编写过程中，可以简化条件的判断

### 时间复杂度
![2]

#### Linked list d的插入操作一定 比 Array-based list 慢吗？
不一定，在有序列表中，插入的速度两者是一样的

## 小结：Array-based list 和 linked list 的对比
![3]

## freeList 优化
FreeList：解决new和delete的代价问题

### 优化的原因
new/delete 对 操作系统 来说 实际上 是一个 很复杂 的操作,如果 频繁 new/delete 代价会很大

### 解决办法
思路：建立一个回收站FreeList用来存放被删除的对象,而不是直接delete

建立 一个 freelist  用来 存放 空闲的结点 ,即 一个结点 delete 之后 放入 freelist 而不 释放内存。在 new 之前,先看 freelist 有没 结点。
(就像 图书馆借书,每次不用 就还书很麻烦,不如先放一边 不 还,等到 需要 再拿过来用)

### 参考代码
建立 一个 freelist,重载 new/delete 运算符 (在 重载函数 内部 调用 全局 **::new** 来 实现 普通的new操作)，其他代码不需要改变(嗯，析构的时候连freeList 也要一起清理了)

freelist 是一个 简单的 链表 ,只需要 一个 指针指向链表头 即可 ,
每次操作 链表头,(即不需要 fence,head,tail等其他元素)

注意：这里是对 `Node` 的 `new` 和 `delete` 进行重写，而不是 `List` 的

```{cpp}
struct Node {
	int v;
	Node * hyNext;
	Node(int _v = 0, Node * _hyNext = NULL) :v(_v), hyNext(_hyNext) {}

	void* operator new(size_t) {
		if (freeList == NULL)	return ::new Node();
		Node * tmp = freeList;
		freeList = freeList->hyNext;
		return tmp;
	}
	void operator delete (void * ptr) {
		((Node *)ptr)->hyNext = freeList;
		freeList = (Node *)ptr;
	}
	static Node * freeList;
};
Node * Node::freeList = NULL;
```

## Double-linked list 双向列表

### 优化的原因
1. 加速 prev() 操作(如果 需要 频繁 prev ,next 操作)
2. 从 任意点 任意方向 都可以 访问 整个链表(双向循环列表)

### 优化的方法
增加 一个 指向 上一个 元素 的 指针
注 : 增加 结点 的 时候 连边 的 顺序 ,先 连 新节点 的边 ,在 连 旧结点上 的边

[1]:assets/list-46e43.png
[2]:assets/list-f61e9.png
[3]:assets/list-d020c.png
