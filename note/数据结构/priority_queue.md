# 优先队列 priority_queue
队列中的元素，除了按先后顺序排队，还按一定的优先级排队。（即优先级高的元素始终排在优先级低的前面）

## 参考代码
实际上就是用堆来实现
```{cpp}
class priority_queue{
public:
	int *heapArr, heapSize,maxSize;
	priority_queue(int _maxSize):heapSize(0){
		maxSize = _maxSize;
		heapArr = new int[maxSize];
	}

	~priority_queue() {
		delete[] heapArr;
		heapArr = NULL;
		heapSize = maxSize = 0;
	}

	bool isLeaf(int pos) {
		return  pos >= heapSize / 2 && pos < heapSize;
	}

	int leftChild(int pos) {
		return (pos << 1) + 1;
	}

	int rightChild(int pos) {
		return (pos << 1) + 2;
	}

	int parent(int pos) {
		return (pos - 1)>> 1;
	}

	//把元素e插入到堆中(加入到堆的最后，然后往上和父节点比较调整位置)
	bool push(const int e) {
		if (heapSize >= maxSize)    return false;
		int cur = heapSize++;
		heapArr[cur] = e;
		while ((cur != 0) && heapArr[cur] > heapArr[parent(cur)]) {
			swap(heapArr[cur], heapArr[parent(cur)]);
			cur = parent(cur);
		}
		return true;
	}

	//把pos位置的元素，往下筛落到正确的位置
	void heapSiftDown(int pos) {
		int cur = pos;
		while (!isLeaf(cur)) {
			int larger = leftChild(cur);
			int rson = rightChild(cur);
			if (rson < heapSize && heapArr[larger] < heapArr[rson]) {
				larger = rson;
			}
			if (heapArr[cur] >= heapArr[larger])	return;
			swap(heapArr[cur], heapArr[larger]);
			cur = larger;
		}
	}

	//移除队首元素
	void pop() {
		swap(heapArr[0], heapArr[--heapSize]);
		if (heapSize != 0)	heapSiftDown(0);
	}

	//返回队首元素
	int top() {
		if (heapSize == 0)	return 0x3F3F3F3F;
		return heapArr[0];
	}

	bool empty() {
		return heapSize == 0;
	}

};
```
