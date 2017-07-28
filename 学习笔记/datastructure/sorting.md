[toc]
# 排序

## 分类

### stable 排序
排序之后，值相同的节点，先后顺序不发生改变，则称为稳定排序

### unstable 排序
排序之后，值相同的节点，先后顺序发生改变，则称为不稳定排序

一般地，如果出现跨区间交换（不是相邻的交换），那么就有 不稳定 的风险
比如希尔排序，选择排序

### internal 排序
在内存中排序

### external 排序
在外部设备 disk 中排序

## 插入排序 insertion_sort
排序过程：和已经排好序的值进行比较，把当前值插入到合适的位置

### 优化
1. 在不断和 前面的有序列进行比较的时候，当出现不是逆序的情况，后续的比较就不需要继续进行了，直接进入下一轮，因为前面的数字肯定是更小的。

2. 先预处理使得数组近似排序，再对全部进行插入排序 见 [希尔排序](#希尔排序)

### 参考代码
```{cpp id:"chj4pnkl02"}
void hyInsertionSort(int arr[],int n) {
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = i; j > 0 && arr[j] < arr[j - 1]; --j) {
				swap(arr[j], arr[j - 1]);		
		}
	}
}
```

### 时间复杂度
Best Case :$\theta(n)$
Worst Case:$\theta(n^2)$
Average Case:$\theta(n^2)$

### 优点
对于近似有序的数组，能够很快地就完成排序

## 冒泡排序 bubble sort
从后面往前两两比较相邻的元素，交换逆序的两个元素
（从效果来看，小的元素会不断的往前冒，并且每一轮都会把当前的最小值冒泡到最前面）

### 区别：插入排序
插入排序是 选定一个值 不断往前插入
冒泡排序是 把当前遇到的最小值不断往前冒

### 优化
1. 第一次冒泡之后，第一个元素为最小值，那么第二次冒泡遇到的值一定比第一个元素要大，所以，第 **i** 次冒泡只需要冒泡到 **i-1** 的位置即可

2. 对于有序的情况，那么后序的冒泡其实是毫无意义的。
所以，只要有一轮冒泡过程中没有出现交换的，那么就说明数组已经有序了，就没必要进行后续的冒泡

### 参考代码
```{cpp id:"chj4pnkl04"}
void hyBubbleSort(int arr[], int n) {
	for (int i = 0; i < n - 1; ++i) {
		bool flg = true;
		for (int j = n - 1; j > i; --j) {
			if (arr[j] < arr[j - 1]) {
				swap(arr[j], arr[j - 1]);
				flg = false;
			}
		}
		if (flg)	return;
	}
}
```

### 时间复杂度
Best Case（未优化2）:$\theta(n^2)$
Best Case（优化了2）: $\theta(n)$
Worst Case:$\theta(n^2)$
Average Case:$\theta(n^2)$

## 选择排序 selection sort
选择当前 未排序的序列中的 最小值 ，加入到 当前已排序的序列 后面（因为有序列的值，是每一轮中选出的最小值，所以下一轮的选出的值一定比上一轮的大，所以直接加入到后面）

### 参考代码
```{cpp id:"chj4pnkl06"}
void hySelectionSort(int arr[], int n) {
	for (int i = 0; i < n - 1; ++i) {
		int hyMin = i;
		for (int j = i + 1; j < n; ++j) {
			if (arr[j] < arr[hyMin]) {
				hyMin = j;
			}
		}
		swap(arr[hyMin], arr[i]);
	}
}
```

### 时间复杂度
Best Case :$\theta(n^2)$
Worst Case:$\theta(n^2)$
Average Case:$\theta(n^2)$

## 希尔排序
插入排序的改良

对于排序算法，数组的长度越短，那么排序的速度就越快
对于插入排序算法，数组的越接近有序，那么它的排序速度越快

基于上面两点，利用分治的思想，对数组进行划分，分别对每个子序列进行插入排序，最后再对整个数组进行一个插入排序（也就是把参与排序的数组划分的更小，利用了上面的第一点）

但是，如果是均匀分割 数组，那么即使每一个子序列是有序的，但是对于整个数组来说，它未必就是近似有序的，出现这种情况，前面所做的就变成了无用功

什么时候这样的预处理是有效的？
当然是 对每个子序列进行插入排序之后，整个序列 有近似有效

显然均匀分割 是 不一定能保证整个序列是近似有序的，希尔排序是这么分割的
取一定间隔的数字作为一个序列，
比如，`1，2，3，4，5，6，7，8，9` 中，取间隔为2的作为一个序列
那么子序列 就是 `1，3，5，7，9` 和 `2，4，6，8`

当然，实现的时候，是在原序列上进行 子序列的排序的，
那么 预处理 结束 之后，前2个数字 ，就总是比后2个数字 小（对于上面的例子来说）

分治的思想还可以多次使用，比如第一个次取的间隔为8，那么第二次可以取成4，第三次2，最后才 1

### 时间复杂度
希尔排序的关键，是对整个序列的划分，取决于每次每个子序列的长度

当 间隔取值为 $\Delta [K] = 2^{t - k + 1} - 1$ 的时候，时间复杂度为$\theta(n^{\frac{3}{2}})$

比如 长度为24的数组，第一次的间隔取为 15(即$2^4 - 1$)，第二次为 7，第三次为3，最后为 1

### 参考代码
```{cpp id:"chj4pnkl07"}
void hyInertionSort2(int arr[], int n,int s,int incr) {
	for (int i = s; i < n; i += incr) {
		for (int j = i; j > s && arr[j] < arr[j - incr]; j -= incr) {
			swap(arr[j], arr[j - incr]);
		}
	}
}

void hyShellSort(int arr[],int n) {
	for (int i = (n >> 1); i > 0; i >>= 1) {
		for (int j = 0; j < i; ++j) {
			hyInertionSort2(arr, n, j, i);
		}
	}
}
```


## Quick Sort 快排
选择一个参考点，根据参考点，把数组分成两组，一边小于参考点，另一边大于等于参考点。
分出的两个区间重复此操作，直到区间不能再分割。

### 怎么根据参考点把数组分成两个部分？
$O(n)$的方法：
利用双指针，分别指向数组头部和数组尾部（为了方便，首先把参考点交换到最后面）
如果左边指针指向的值小于参考点，右边指针指向的值大于参考点，那么两个指针就不断往中间移动，
当两个指针都无法移动的时候，（这时候左边指针指向的值大于参考点，右边指针指向的值小于参考点），就交换两个指针指向的值（使得指针得以继续往中间移动）
循环上面的操作，直到两个指针相遇。

在相遇的地方，交换参考点和当前指向的值（因为要使得参考点处于正确的位置）

### 参考代码
```{cpp id:"chj4pnkl09"}
int getPivot(int i, int j) {
	return (i + j) / 2;
}
/*
int partition(int arr[], int i, int j,int &p) {
	int l = i, r = j;
	do {		
		//一定有 arr[j] = p ，所以这里不需要判断边界
		while (arr[l] < p)
			++l;
		//这里可能越界，所以需要判断边界
		while (r && arr[r] >= p)
			--r;
		//两边都不能移动了，就交换值
		swap(arr[l], arr[r]);
	} while (l < r);

	//当上面的循环结束之后，会有 l = r + 1
	//因为结束前,最后那个交换一定会发生，因为此时，l指向了大于p的一端，r指向了小于p的一端，所以需要修正
	swap(arr[l], arr[r]);
	//l越界，指向了大于p的一端，所以返回l，而不是返回r
	return l;

	//注意也有可能出现 l == r 的情况，但这个时候上面的代码并没有影响
}
*/
int partition(int arr[], int i, int j,int &p) {
	int l = i, r = j;
	do{
		while (arr[l] < p)
			++l;
		while (l < r && arr[r] >= p)
			--r;
		swap(arr[l], arr[r]);
	} while (l < r);
	return l;
}
//对下标为区间 [i,j] 范围内的数组进行排序
void hyQuickSort(int arr[], int i, int j) {
	if (j <= i)	return;
	int pivot = getPivot(i, j);
	swap(arr[j], arr[pivot]);
	int k = partition(arr, i, j,arr[j]);
	swap(arr[k], arr[j]);
	hyQuickSort(arr,i, k - 1);
	hyQuickSort(arr, k + 1, j);
}
```
### 优化

#### Better Pivot
快排的效率很大程度上依赖 pivot 的值，所以值的选择很重要，但是这个过程也不能太过复杂。

1. 最简单的话，一般选择数组中间的值，因为如果是近似有序的数组（或者近似逆序），中间的值一般也属于中间大小，较大概率均匀的把数组分割成两部分，如果是随机的数列，那么选不选中间都无所谓。

2. 也可以选择在数列中随机抽样几个出来，然后取中间值作为参考点
比如抽取 第一个，中间，最后一个 这三个元素

#### Better Algorithm for smalll sub-arrays
对于快排来说，如果考虑常数操作的时间，那么当数列的长度比较短的时候，快排的时间是不如其他排序的，比如插入排序，所以这里可以优化，当子数列的长度较短的时候，插入排序。

##### 为什么选择插入排序？
因为插入排序比冒泡，选择排序好啊。

#### Eliminate recursion
实际上是优化常数时间，对于整个算法的复杂度是没有影响的。

实现上，使用递归实现代码的编写很方便，但是同时会产生系统调用函数的一个较大的常数时间，因此如果把递归改成循环形式，效率显然更高。

### 优化后代码
```{cpp id:"chj4pnkl0b"}
int getPivot(int arr[],int i, int j) {
	int mid = (i + j) / 2;
	if(arr[i] <= arr[mid] && arr[mid] <= arr[j]){
		return mid;
	}else if(arr[mid] <= arr[i] && arr[i] <= arr[j]){
		return i;
	}else return j;
}
int partition(int arr[], int i, int j,int &p) {
	int l = i, r = j;
	do{
		while (arr[l] < p)
			++l;
		while (l < r && arr[r] >= p)
			--r;
		swap(arr[l], arr[r]);
	}while (l < r);
	return l;
}
void hyQuickSort(int arr[], int i, int j) {
	if (j - i < 7)	{
		insertion_sort(arr + i,j - i + 1);
		return ;
	}
	int pivot = getPivot(arr,i, j);
	swap(arr[j], arr[pivot]);
	int k = partition(arr, i, j,arr[j]);
	swap(arr[k], arr[j]);
	hyQuickSort(arr,i, k - 1);
	hyQuickSort(arr, k + 1, j);
}
```
### 非递归实现
```{cpp id:"chj4pnkl0c"}
inline void hyInsertionSort(int arr[], int n) {
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = i; j > 0 && arr[j] < arr[j - 1]; --j) {
			swap(arr[j], arr[j - 1]);
		}
	}
}
inline int getPivot(int arr[], int i, int j) {
	int mid = (i + j) / 2;
	if (arr[i] <= arr[mid] && arr[mid] <= arr[j]) {
		return mid;
	}
	else if (arr[mid] <= arr[i] && arr[i] <= arr[j]) {
		return i;
	}
	else return j;
}
inline int partition(int arr[], int i, int j, int &p) {
	int l = i, r = j;
	do {
		while (arr[l] < p)
			++l;
		while (l < r && arr[r] >= p)
			--r;
		swap(arr[l], arr[r]);
	} while (l < r);
	return l;
}
void hyQuickSort(int arr[], int n) {
	int i = 0, j = n - 1, k, pivot,cnt = 1;
	int *sj = new int[n + 1], *sk = new int[n + 1];
	while (cnt) {
		if (j - i < 7) {
			hyInsertionSort(arr + i, j - i + 1);
			i = sk[cnt - 1] + 1;
			j = sj[cnt - 1];
			--cnt;
		}
		else {
			pivot = getPivot(arr, i, j);
			swap(arr[j], arr[pivot]);
			k = partition(arr, i, j, arr[j]);
			swap(arr[k], arr[j]);
			sk[cnt] = k;
			sj[cnt++] = j;
			j = k - 1;
		}
	}
	delete[]sj;
	delete[]sk;
}
```

### 时间复杂度
最好的情况，每次子数列都被均匀分割，所以至少被分割$\log_2 n$ 次
最坏的情况，每次子数列的支点都选择到了极值，最多分割了 $n$ 次s
每次分割，需要 $n$ 的时间

BsetCase:$\theta(n\log_2n)$
worstCase:$n^2$
averageCase:$n\log_2n$

## Heap Sort 堆排序
把数组一次加入堆中，堆不断地调用 **removeMax** 函数，这样结束之后，数组的元素就是排好序的。（因为每次remove都会把最大值移动到数组当前的最后面）

### 参考代码
```{cpp id:"chj4pnkl0e"}
int *heapArr, heapSize;
bool isLeaf(int pos) {
	return  pos >= heapSize / 2 && pos < heapSize;
}
int leftChild(int pos) {
	return (pos << 1) + 1;
}

int rightChild(int pos) {
	return (pos << 1) + 2;
}
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

void build(int arr[], int n) {
	heapArr = arr;
	heapSize = n;
	for (int i = heapSize / 2 - 1; i >= 0; --i) {
		heapSiftDown(i);
	}
}

void removeMax() {
	swap(heapArr[0], heapArr[--heapSize]);
	if (heapSize != 0)	heapSiftDown(0);
}

void hyHeapSort(int arr[], int n) {
	build(arr, n);
	for (int i = 0; i < n; ++i) {
		removeMax();
	}
}
```

## Merge Sort 归并排序
利用分治的思想，把数组分割成两块，每一块分别排序，排好序的两块依次从头往另一个数组写入输入，每次写入当前的最小值。（每一块也重复这样的操作，直到不能分割为止）

实际上就是两个过程，归和并
归：不断地把数列平均分割
并：把排好序的两个子序列合并到一个序列中

### 和 quick Sort 比较
快排分割依赖 支点的值，所以分割得到的树的高度（递归的深度）是 变化的，介于$\log_2n$ 和 $n$ 之间

归并排序则每次都是平均分割，所以递归的深度始终都是 $\log_2n$

### 参考代码
```{cpp id:"chj4pnkl0g"}
void hyMergeSortHelp(int arr[], int tmp[], int l, int r) {
	if (l >= r)	return;
	int mid = (l + r) / 2;
	hyMergeSortHelp(arr, tmp, l, mid);
	hyMergeSortHelp(arr, tmp, mid + 1, r);

	for (int i = l; i <= r; ++i) {
		tmp[i] = arr[i];
	}

	int l1 = l , l2 = mid + 1;
	for (int i = l; i <= r; ++i) {
		if (l1 <= mid && (l2 > r || tmp[l1] <= tmp[l2]))
			arr[i] = tmp[l1++];		
		else	arr[i] = tmp[l2++];
	}
}

void hyMergeSort(int arr[], int n) {
	int *tmp = new int[n];
	hyMergeSortHelp(arr, tmp, 0, n - 1);
	delete[] tmp;
}
```

### 优化
#### 去边界探测
合并的时候，每次循环都要进行边界的探测，但是探测成功的次数是少数的，所以考虑能不能把探测去掉。

方法：把右边的子序列逆序，那么就两个指针就变成了 从两端向中间靠拢，这样就不用关心边界的问题

#### better algorithm for small sub-arrays
见[快排-Better Algorithm for smalll sub-arrays](#better-algorithm-for-smalll-sub-arrays)

#### Eliminate recursion
见 [Eliminate recursion](#eliminate-recursion)

### 优化后代码
```{cpp id:"chj4pnkl0h"}
void hyMergeSortHelp(int arr[], int tmp[], int l, int r) {
	if (r - l < 6){
		insertion_sort(arr + l,r - l + 1);
		return ;
	}
	int mid = (l + r) / 2;
	hyMergeSortHelp(arr, tmp, l, mid);
	hyMergeSortHelp(arr, tmp, mid + 1, r);

	for (int i = l; i <= mid; ++i) {
		tmp[i] = arr[i];
	}

	for (int i = 0; i < r - mid; ++i) {
			tmp[r - i] = arr[mid + i + 1];
	}

	int i = l,j = r;
	for(int cur = l ; cur <= r; ++cur){
		if(tmp[i] < tmp[j])	arr[cur] = tmp[i++];
		else arr[cur] = tmp[j--];
	}
}

void hyMergeSort(int arr[], int n) {
	int *tmp = new int[n];
	hyMergeSortHelp(arr, tmp, 0, n - 1);
	delete[] tmp;
}
```

### 非递归实现
实际上就是逆过程，每两个进行合并，然后每4个，一直合并出整个数组
```{cpp id:"chj4pnkl0i"}
inline void merge(int arr[], int tmp[], int l, int r,int mid) {
	for (int i = l; i <= mid; ++i) {
		tmp[i] = arr[i];
	}

	for (int i = 0; i < r - mid; ++i) {
		tmp[r - i] = arr[mid + i + 1];
	}

	int i = l, j = r;
	for (int cur = l; cur <= r; ++cur) {
		if (tmp[i] < tmp[j]) arr[cur] = tmp[i++];
		else arr[cur] = tmp[j--];
	}
}

inline void hyMergeSort(int arr[], int n) {
	int *tmp = new int[n];
	int i,j;
	for (i = 2; i < n; i *= 2) {
		for(j = 0 ; j + i < n ; j += i){
			merge(arr, tmp, j, j + i - 1, j + i / 2 - 1);
		}
		if(n - j > i / 2)
			merge(arr, tmp, j, n - 1,j + i / 2 - 1);
	}
	merge(arr, tmp, 0, n - 1, i / 2 - 1);
	delete[]tmp;
}
```

## bin排序 箱排序
箱排序，类似哈希表
```{mermaid id:"chj4pnkl0j"}
graph LR
data --> dispatch
dispatch --> clooect
clooect --> sorted-array
```
主要是两个步骤，
1. 把数据依照对应的key放入对应的箱子中
2. 数据全部放完之后，扫描所有的箱子，以此取出

### 重复元素冲突处理
类似 开放式哈希的处理方式，使用一个链表存放

## radix排序 基数排序
基数排序，是箱排序的一个优化。
很显然，要使用箱排序，那么就要求空间足够大，至少要比数据最大值要大。
radix排序就是对箱排序的优化，减少空间的消耗。

### 优化的思路
把一个数据分解成多个key，然后分别按每个 key进行排序。这样分解出来的key值比较小，那么进行箱排序的空间消耗就少了很多。

以整数为例，就是先按个位进行箱排序，再按十位进行排序，一直到最高位。因为  箱排序是稳定的，那么对十位进行箱排序的时候，不会对个位的大小进行破坏。所以这种排序策略是可行的。

### 分析
0. 如果整数的话，箱子数目的多少，就取决于基数的大小
1. 这里的按key以此进行箱排序，而不是指排序的是，先按key1比较，再按key2比较。

## 基于关键字比较的排序算法的理论下界
基于关键字比较的算法，都可以展开成一个 二叉决策树，每种排序策略，都对应一种二叉决策树，而树的高度最少为 $n\log n$，因此排序最快只能是 $n\log n$
