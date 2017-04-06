<!--toc-->

- [堆](#堆)
	- [插入操作](#插入操作)
	- [建树](#建树)
		- [问：如何调整？](#问如何调整)
		- [复杂度分析](#复杂度分析)
	- [删除操作](#删除操作)
	- [参考代码](#参考代码)
	- [堆的应用](#堆的应用)

<!-- tocstop -->
# 堆
堆：完全二叉树，树根 是 树的最值（子树也满足这个特性）
实现：由于是完全二叉树，所以用数组实现

父节点:`(pos - 1)>> 1`
左儿子:`(pos << 1) + 1;`
右儿子:`(pos << 1) + 2`
判断是否是叶子:`pos >= heapSize / 2 && pos < heapSize`


## 插入操作
插入操作：插入到数组最后，然后不断和父节点比较来调整位置
```{cpp}
void insert(const Elem& it){
    if(n >= maxSize)    return;
    int cur = n++;
    Heap[cur] = it;
    while((cur != 0) && Heap[cur] > heap[parent(cur)]){
       swap(Heap,cur,parent(cur));
      cur = parent(cur);
   }
}
```

## 建树
有两个方法
1. 逐个插入 $\theta (n\log n)$
2. 一次性存入数据，在进行调整 $\theta (n)$

### 问：如何调整？
答：每个树根 和 子树 取较大值作为树根（树根 和 子树最大值交换），（分治？）
然后这里的最小的子树的树根，是 n/2，一直往前，所以直接for语句，而不用递归

```{cpp}
void sifedown(int pos){
    while(!isLeaf(pos)){
        int j = leftchild(pos);
        int rc = rightChild(pos);
        if( (rc<n) &&Heap[rc] > Heap[j] ){
            j = rc;
       }
        if(Heap[pos] >= Heap[j])    return;
				swap(heap[pos],heap[j]);
        pos = j;
   }
}
void build(){
    for(int i = n/2 - 1; i >= 0;--i){
       siftdown(i);
   }
}
```

### 复杂度分析
建树方法：先都存进去数组，然后从后往前，对于每个中间节点都使用一次 siftdown
$T(n) = 0 \times \frac{n}{2} + 1 \times \frac{n}{4} + ... = \sum (i - 1)\frac{n}{2^i} = n$

## 删除操作
把最后一个结点替换成树根，再对树根 siftdown
```{cpp}
void removeMax() {
	swap(heapArr[0], heapArr[--heapSize]);
	if (heapSize != 0)	heapSiftDown(0);
}
```

## 参考代码
```{cpp}
class Heap{
public:
	int *heapArr, heapSize,maxSize;
	Heap(int _maxSize):heapSize(0){
		maxSize = _maxSize;
		heapArr = new int[maxSize];
	}

	~Heap(){
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
	bool insert(const int e) {
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

	//根据长度为 n 数列 arr 进行建树，如果长度大于 堆的容量则失败
	bool build(int arr[], int n) {
		if (n > maxSize || n < 0)	return false;
		memcpy(heapArr, arr, sizeof(arr[0])*n);
		heapSize = n;
		for (int i = heapSize / 2 - 1; i >= 0; --i) {
			heapSiftDown(i);
		}
	}

	//移除并返回最大的元素（树根）
	int removeMax() {
		swap(heapArr[0], heapArr[--heapSize]);
		if (heapSize != 0)	heapSiftDown(0);
		return heapArr[heapSize];
	}

	bool empty() {
		return heapSize == 0;
	}
};
```

## 堆的应用
1. 堆排序算法
2. 优先队列
3. 哈夫曼编码
    贪心算法，使用优先队列建树
