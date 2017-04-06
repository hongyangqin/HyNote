<!--toc-->

- [2-3 Tree](#2-3-tree)
	- [疑问](#疑问)
	- [性质&定义](#性质定义)
	- [查找过程](#查找过程)
		- [时间复杂度：](#时间复杂度)
		- [代码](#代码)
	- [插入操作](#插入操作)
		- [代码实现思路](#代码实现思路)
		- [时间复杂度：](#时间复杂度-1)
		- [只有一个键值](#只有一个键值)
		- [两个键值](#两个键值)
	- [删除操作](#删除操作)
	- [部分代码（未整理）](#部分代码未整理)
	- [其他](#其他)
	- [参考](#参考)

<!-- tocstop -->

# 2-3 Tree
## 疑问
问：怎么判断一棵树是不是合法的 2-3 Tree?
答：
0. 空树是2-3 树
1. 子树的都是高度 2-3 Tree，
2. 满足 $L < key_1 <= M < key_2 <= R$

## 性质&定义
如图:
```{mermaid}
graph TD
18,33 --> 12
18,33 --> 23,30
18,33 --> 48

12 --> 10
12 --> 15

23,30 --> 20,21
23,30 --> 24
23,30 --> 31

48 --> 45,47
48 --> 50,52
```

1. 每个节点，有1-2个关键字
2. 每个中间节点，有2-3个子节点
3. 对于有三个孩子的节点：
		0. 有两个关键字:$key_1,key_2$
		1. $value(leftSon) < key_1$
		2. $key_1 <= valus(centerSon) < key_2$
		3. $key_2 <= valus(rightSon)$

4. 对于有二个孩子的节点：
		0. 只有一个关键字：$key_1$
		1. $value(leftSon) < key_1$
		2. $key_1 <= valus(rightSon)$
				注意，下面代码实现的时候，使用代表中间节点的指针，来存这个右子树的

5. 所有叶子都在一个高度
6. 所有的data都是有序的

## 查找过程
不断和关键字比较，知道找到，或者到达叶子
```
2-3 Search Tree
– If a 2 Node with value, m
	• Left subtree nodes are < node value
	• Right subtree nodes are > node value
– If a 3 Node with value, l and r
	• Left subtree nodes are < l
	• Middle subtree > l and < r
	• Right subtree nodes are > r
```

### 时间复杂度：
$\theta(\log n)$
最极端的情况，就是找到叶子位置

### 代码
1. 判断是否在当前节点 `hyRoot`
	1. 是否和 $key1$ 相等
		直接比较

	2. 是否和 $key2$ 相等
		要先判断 $key_2$ 是否存在
		通过 判断 右子树 是否为空（为空说明只有两个儿子）

2. 往左走
	$k < key_1$

3. 往中间走
	1. 只有2个儿子
	2. $key_1 <= k < key_2$

3. 往右走
	$key_2 <= k$（前提是当前节点有3个儿子）
	除了上面的情况就是它了...

```{cpp}
bool search(TTNode *hyRoot,Elem &e) {
	if (e == hyRoot->key1) {
		return true;
	}
	else if (hyRoot->rightSon != NULL && hyRoot->key2 == e) {
		return true;
	}

	if (e < hyRoot->key1) {
		return search(hyRoot->leftSon, e);
	}
	else if (hyRoot->rightSon == NULL || e < hyRoot->key2 ) {
		return search(hyRoot->centerSon, e);
	}else return search(hyRoot->rightSon, e);
}
```

## 插入操作
```
To insert a value,
– 1. walk the tree to a leaf using your search approach
– 2a. If the leaf is a 2-node (i.e.1 value), add the new value to that node
– 2b. Else break the 3-node into two 2-nodes with the smallest value as the left,
	biggest as the right, and median value promoted to the parent with smallest and
	biggest node added as children of the parent
– Repeat step 2(a or b) for the parent
```
直接往下查找合适的叶子节点
如果叶子节点有空位（只有一个键值），就直接放进去
如果叶子节点没有空位（有两个键值），就分裂叶子,把中间的值加入到父节点中，父节点如果也满了也重复上面前面的操作（向上生长）

>  Any time a node accumulates 3 values, split it into single valued nodes (i.e. 2-nodes) and promote the median

要点：一个节点积累到了3个值，就分裂这个节点成两个，并把中值传递到父节点。

### 代码实现思路
1. 在搜索的过程需要经过的所有路径，在后面往上生长的时候可能也会再次经过。
所以把寻找和生长两个过程合并到一起，递归函数，再递的过程中寻找，在归的过程中生长

2. 也许可以直接根据上面你的思路来写，寻找一个过程，生长也一个过程（待实现）

### 时间复杂度：
$\theta(\log n)$
找到叶子位置 $\theta(\log n)$，再向上生长（最极端的情况就是生长到树根）

### 只有一个键值
直接找到一个叶子节点是空的。比如上面的树中插入 14

### 两个键值
操作：把一个节点，分裂成两个节点，两个节点分别存放的是 3个数中的最值，中间值就插入到父亲节点中，父节点重复这个步骤

注意：如果父节点已经是树根了，那么就需要创建一个新的节点作为树根

比如，在下图中，插入19
```{mermaid}
graph TD
23 --> 20,21
23 --> 24
```
找到插入的位置，发现是满的
```{mermaid}
graph TD
23 --> 19,20,21
23 --> 24
```
分裂节点，取中间节点出来加入到父节点
```{mermaid}
graph TD
20,23 --> 19
20,23 --> 21
20,23 --> 24
```

## 删除操作
```
2-3 Tree Removal
* Key:  2-3 Trees must remain "full" (leaf nodes all at the same level)
* Remove
	1. Find data item to remove
	2. If data item is not in a leaf node, find in-order successor (which is in a leaf node) and swap values (it's safe to put successor in your location)
	3. Remove item from the leaf node
	4. If leaf node is nowempty,callfixTree(leafNode)

* fixTree(n)
	- If n is root, delete root and return – Let p be the parent of n
	- If a sibling of n has two items
	 	* Redistribute items between n, sibling, and p and move any appropriate child from sibling to n

	- Else
      * Choose a sibling, s, of n and bring an item from p into s redistributing any children of n to s
      * Remove node n
      * If parent is empty, fixTree(p)
```

> Want to get item to remove down to a leaf and then work up the tree.

1. 把需要删除的节点，和某个叶子节点的某个值交换（具体等搞清楚再写），
2. 然后删除这个值
3. 如果删除这个值之后，叶子节点变成空（即原来节点只有一个值），那么就需要从当前叶子节点开始调整树
4. 调整树的结构，只需要关心当前节点，当前节点的兄弟节点，当前节点的父亲 三者的调整即可
		至于 更高层的，只需要递归实现即可

## 部分代码（未整理）

```{cpp}
#include<iostream>
#include<sstream>
#include<string>
#include<queue>
using namespace std;
const int EMPTY = 0x3F3F3F3F;
struct TTNode {
	int lkey, rkey;
	TTNode * left, *center, *right;
	bool isTwoNode;
	TTNode() {
		//initiallize pointers
		left = center = right = NULL;
		lkey = rkey = EMPTY;
		isTwoNode = true;
	}
	bool isLeaf() {
		return left == NULL;
	}
};
struct TTTree {
	TTNode *root;
	TTTree() {
		root = NULL;
	}

	//insert value e to the TTTree
	void insert(int e) {

		//TTTree is empty , then just create a new node with value e as root;
		if (root == NULL) {
			root = new TTNode();
			root->lkey = e;
			return;
		}

		//Recursion according searching approach then insert the value e to the leafNode
		int hyRetValue;
		TTNode * hyRetPtr = NULL;
		insertHelp(root, e, hyRetValue, hyRetPtr);

		//if childNode promote the median,and now is already at the root, so we should create a new node as new root
		if (hyRetPtr != NULL) {
			TTNode * tmp = new TTNode();
			tmp->left = root;
			tmp->center = hyRetPtr;
			tmp->lkey = hyRetValue;
			root = tmp;
		}
	}

	void insertHelp(TTNode * hyRoot, int &e, int & retValue, TTNode *& retPtr) {
		int hyRetValue;
		TTNode * hyRetPtr = NULL;
		// out of tree
		if (hyRoot == NULL)	return;
		//recursion to the leafNode
		if (e < hyRoot->lkey) {
			insertHelp(hyRoot->left, e, hyRetValue, hyRetPtr);
		}
		else if (hyRoot->isTwoNode || e < hyRoot->rkey) {
			insertHelp(hyRoot->center, e, hyRetValue, hyRetPtr);
		}
		else {
			insertHelp(hyRoot->right, e, hyRetValue, hyRetPtr);
		}

		//when arrive the leafNode or get the median from the childNode ,we should add it to the key
		if (hyRoot->isLeaf()) {
			if (hyRoot->isTwoNode) {
				hyRoot->isTwoNode = false;
				if (e < hyRoot->lkey) {
					hyRoot->rkey = hyRoot->lkey;
					hyRoot->lkey = e;
				}
				else {
					hyRoot->rkey = e;
				}
			}
			else splitNode(hyRoot, e, NULL, retValue, retPtr);
		}
		else if (hyRetPtr != NULL) {
			if (hyRoot->isTwoNode) {
				hyRoot->isTwoNode = false;
				if (e < hyRoot->lkey) {
					hyRoot->rkey = hyRoot->lkey;
					hyRoot->lkey = hyRetValue;
					hyRoot->right = hyRoot->center;
					hyRoot->center = hyRetPtr;
				}
				else {
					hyRoot->rkey = hyRetValue;
					hyRoot->right = hyRetPtr;
				}
			}
			else splitNode(hyRoot, hyRetValue, hyRetPtr, retValue, retPtr);
		}
	}

	//split the node because of e and inPtr
	void splitNode(TTNode * hyRoot, int &e, TTNode *inPtr , int & retValue, TTNode *& retPtr) {
		retPtr = new TTNode();
		if (e < hyRoot->lkey) {
			retValue = hyRoot->lkey;			
			retPtr->lkey = hyRoot->rkey;
			hyRoot->lkey = e;

			retPtr->center = hyRoot->right;
			retPtr->left = hyRoot->center;

			hyRoot->center = inPtr;
		}
		else if (e < hyRoot->rkey) {
			retValue = e;
			retPtr->lkey = hyRoot->rkey;

			retPtr->center = hyRoot->right;
			retPtr->left = inPtr;

		}
		else {
			retValue = hyRoot->rkey;
			retPtr->lkey = e;

			retPtr->center = inPtr;
			retPtr->left = hyRoot->right;			
		}
		hyRoot->isTwoNode = true;
	}

	//search for value e ,if exist return the addres of the node
	TTNode * search(int e) {
		return searchHelp(root, e);
	}

	TTNode * searchHelp(TTNode * hyRoot, int & e) {
		if (hyRoot == NULL) return NULL;
		else if (e < hyRoot->lkey) {
			return searchHelp(hyRoot->left, e);
		}
		else if (e == hyRoot->lkey) {
			return hyRoot;
		}
		else if (hyRoot->isTwoNode || e < hyRoot->rkey) {
			return searchHelp(hyRoot->center, e);
		}
		else if (e == hyRoot->rkey) {
			return hyRoot;
		}else return searchHelp(hyRoot->right, e);
	}

	int ans[100000];
	void printByLevelBfs(TTNode * hyRoot = NULL) {
		if (hyRoot == NULL) hyRoot = root;
		queue<TTNode *> q;
		q.push(hyRoot);
		int cnt = 0;
		while (q.empty() == false) {
			TTNode * p = q.front(); q.pop();
			ans[cnt++] = p->lkey;
			if (p->isTwoNode == false)
				ans[cnt++] = p->rkey;

			if (p->isLeaf() == false) {
				q.push(p->left);
				q.push(p->center);
				if (p->isTwoNode == false)
					q.push(p->right);
			}			
		}

		for (int i = 0; i < cnt - 1; ++i) {
			cout << ans[i] << " ";
		}
		cout << ans[cnt - 1] << endl;
	}
	void clear() {
		clearHelp(root);
		root = NULL;
	}
	void clearHelp(TTNode * hyRoot) {
		if (hyRoot == NULL)	return;
		clearHelp(hyRoot->left);
		clearHelp(hyRoot->center);
		clearHelp(hyRoot->right);
		delete hyRoot;
	}
	~TTTree() {
		clear();
	}
};
int main() {
	int t,tmp;
	string str;
	cin >> t;
	getline(cin, str);
	while (t--) {
		getline(cin, str);
		stringstream ss(str);
		TTTree t;
		while (ss >> tmp){
			t.insert(tmp);
		}
		t.printByLevelBfs();
	}
	return 0;
}
```

## 其他
1. 2-3树叶子的高度都是一样，那么不管是删除，插入，当操作的地方是叶子的时候，不能往下操作，而是根据当前的情况，向上调整非叶子节点

## 参考
[维基百科](https://en.wikipedia.org/wiki/2%E2%80%933_tree)
[2–3 Tree In-depth description](http://www.aihorizon.com/essays/basiccs/trees/twothree.htm)
