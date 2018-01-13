<!--toc-->

- [queue](#queue)
	- [ADT](#adt)
	- [参考代码](#参考代码)
	- [为什么需要队列](#为什么需要队列)
	- [环形队列 Circular queue](#环形队列-circular-queue)
		- [下标](#下标)
		- [队列的长度](#队列的长度)
		- [empty 和 full 两个状态 ,front 和 rear 的位置关系是一样的,怎么区分两个状态?](#empty-和-full-两个状态-front-和-rear-的位置关系是一样的怎么区分两个状态)
		- [参考代码](#参考代码-1)
	- [优先队列](#优先队列)
	- [应用](#应用)

<!-- tocstop -->
# queue
队列，先进先出，FIFO

## ADT
```{cpp}
class queue {
	virtual void push(int e);
	virtual int front();
	virtual void pop();
	virtual bool empty();
	virtual int size();
};
```

## 参考代码
使用链表实现，注意 `pop` 的时候要修正 `tail`
数组实现见 [环形队列](#环形队列-circular-queue)
```{cpp id:"iw7syihc"}
struct Node {
	int v;
	Node * hyNext;
	Node(int _v = 0, Node * _hyNext = NULL) :v(_v), hyNext(_hyNext) {}
};
class queue {
public:
	Node * head, * tail;
	int cnt;
	queue():cnt(0) {
		head = tail = new Node();
	}
	~queue() {
		while (head) {
			tail = head;
			head = head->hyNext;
			delete tail;
		}
		head = tail = NULL;
	}

	void push(int e) {
		tail->hyNext = new Node(e);
		tail = tail->hyNext;
		++cnt;
	}
	int front() {
		if (cnt == 0)	return -0x3F3F3F3F;
		return head->hyNext->v;
	}

	void pop() {
		if (cnt == 0)	return;
		Node * tmp = head->hyNext;
		if (tmp == tail) tail = head;
		head->hyNext = tmp->hyNext;
		delete tmp;
		--cnt;
	}

	bool empty(){
		return cnt == 0;
	}

	int size() {
		return cnt;
	}
};
```

## 为什么需要队列
因为 服务 的 资源有限 ,不可能 同时 处理 全部 数据

## 环形队列 Circular queue
![1]
使用数组实现

通过模运算来控制下标的循环

### 下标
```{cpp}
i + 1 % size
```
### 队列的长度
```{cpp}
length = (rear - front + size + 1 ) % size
```

### empty 和 full 两个状态 ,front 和 rear 的位置关系是一样的,怎么区分两个状态?
![2] ![3]

1. 作标记
		1. 设置一个空状态的值
		2. 设置一个变量用来表示是否已经满了（或者直接计数）

2. 剩下 一个 元素 的时候 ,把 front 和 rear 设置 成一个 特殊的数字 (比如 size )
3. 申请多一个空间, 使得 full/空 两个状态 不 一样
		即只存放了 'n - 1' 个元素，就认为队列 '满' 了
		![4]

### 参考代码
对于上面的问题，使用第三种策略。
```{cpp}
class queue {
public:
	int maxSize;
	int frontPos;
	int rear;
	int *arr;
	queue(int _maxSize = 50) { maxSize = _maxSize; frontPos = 0; rear = maxSize - 1; arr = new int[maxSize + 1]; }
	~queue() { delete[] arr; }
	bool push(int e) {
		//full
		if (((rear + 2) % maxSize) == frontPos)	return false;

		rear = (rear + 1) % maxSize;
		arr[rear] = e;
		return true;
	}

	int front() {
		if (size() == 0) return -0x3F3F3F3F;
		return arr[frontPos];
	}

	bool pop() {
		if (size() == 0) return false;  // Empty
		frontPos = (frontPos + 1) % maxSize; // Circular increment
		return true;
	}

	bool empty() {
		return size() == 0;
	}

	int size() {
		return (rear + maxSize - frontPos + 1) % maxSize;
	}
};
```


## 优先队列
使用堆实现，具体见 **优先队列**

## 应用
1. Buffer 缓冲区
2. 消息队列 (优先队列)
3. 模拟
		比如 : 随机 到来 客人, 每个 客人 随机 的 服务时间 ,求 模拟 这个过程
		解 : 可以 使用 离散 事件 队列 : 新客人到来 ,服务 某个 客人 等 , 通过消息循环 不断 触发 和 处理 事件(而不是 使用一个 等待 客人 的列表)

[1]:assets/queue-76293.png
[2]:assets/queue-d833c.png
[3]:assets/queue-d5b9c.png
[4]:assets/queue-d0b0d.png
