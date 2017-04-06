<!--toc-->

- [树](#树)
	- [树的特点](#树的特点)
	- [例子](#例子)
	- [中间节点](#中间节点)
	- [叶子节点](#叶子节点)
	- [路径](#路径)
	- [层次/节点的深度](#层次节点的深度)
	- [高度](#高度)
	- [二叉树](#二叉树)
		- [满二叉树](#满二叉树)
			- [定理 : 叶子 个数 = 中间 节点 数 + 1](#定理-叶子-个数-中间-节点-数-1)
		- [完全二叉树](#完全二叉树)
		- [ADT](#adt)
		- [Link-Based Tree](#link-based-tree)
		- [Array-Based Tree](#array-based-tree)
			- [优缺点](#优缺点)
	- [树的遍历](#树的遍历)
		- [前序遍历](#前序遍历)
			- [递归实现](#递归实现)
			- [非递归实现](#非递归实现)
			- [已知中序遍历 ,后序遍历的结果 ,求树的形状](#已知中序遍历-后序遍历的结果-求树的形状)
				- [参考代码](#参考代码)
			- [已知中序遍历，后序遍历，求树的高度](#已知中序遍历后序遍历求树的高度)
		- [逐层遍历](#逐层遍历)
	- [节点的数目](#节点的数目)
	- [树的高度](#树的高度)
	- [清空树](#清空树)
	- [树的序列化](#树的序列化)
		- [解决办法](#解决办法)
		- [参考代码](#参考代码-1)

<!-- tocstop -->

# 树
## 树的特点
1. 一对多连边
2. 节点分层次
3. 无环

## 例子
1. 目录树
2. 族谱

## 中间节点
除了叶子节点 (树根也是中间节点)

## 叶子节点
最下面的节点


## 路径
必须满足 前一个节点 是 后一个节点的 父亲 ,才是 路径

比如 下图 : AC是路径 ,BAC不是路径
![1]


## 层次/节点的深度
从 树根 到 当前节点 路径的长度

## 高度
路径的最大值 + 1
比如 上例 中的树 ,高度是 2


## 二叉树
每个节点 不超过 两个分支 的树

二叉树 的嵌套结构: $\begin{cases}
左子树 \\
树根 \\
右子树
\end{cases}$

### 满二叉树
每个中间节点 都 有 2个 孩子的二叉树

#### 定理 : 叶子 个数 = 中间 节点 数 + 1
证明 : $\begin{cases}
点 : x + y = n \\
边 : 2x = n - 1
\end{cases}$
x是中间节点的个数 ,y是叶子节点的个数 ,n是总节点数 ,
2x 表示 每个分支节点都能分出两条边 ,表示总边数
n - 1,表示 除了 树根 ,每个节点 和 父节点 都有一条边

### 完全二叉树
叶子的深度都一样

### ADT
```{cpp}
template<class Elem>
class BinNode{
    virtual void setVal(const Elem &) = 0;
    virtual BinNode * left()const = 0;
    virtual void setLeft(BinNode *) = 0;
    virtual BinNode * right()const = 0;
    virtual void setRight(BinNode *) = 0;
    virtual bool isLeaf() = 0;
};

template<class Elem>
class BinTree{
    virtual BinNode<Elem> * getRoot() = 0;
    virtual void preOrder(BinNode<Elem> * subRoot,void (*pfunc)) = 0;
    virtual void inOrder(BinNode<Elem> * subRoot,void (*pfunc)) = 0;
    virtual void posOrder(BinNode<Elem> * subRoot,void (*pfunc)) = 0;
};
```

### Link-Based Tree
实现见 **BST**
1. 空间消耗 : (2p + d)n,p表示指针消耗的空间,d表示数据消耗的空间
2. 空指针占用的空间 : (n + 1)p,n表示节点数目,p表示一个指针消耗的空间
		所以 ,叶子节点上 ,空指针占用的空间也可能比较大, 可以根据需要 利用这部分空间 ,比如 把叶子节点 连接起来

### Array-Based Tree
实现见 **heap**
完全二叉树 : 从上往下,从左往右 ,依次往数组中 存入 数据
那么 ,父子节点的关系:$\begin{cases}
parent(r) = \frac{r - 1}{2} ,r > 0 && r < n \\
left(r) = 2r + 1, 2r + 1 < n \\
right(r) = 2r + 2, 2r + 2 < n
\end{cases}$

#### 优缺点
优点  : 如果 树 是 完全二叉树 ,用数组 实现会特别高效
缺点 : 如果树 不是二叉树 ,普通树 比较 稀疏,那么 数组的空间利用率不高,
所以 ,在考虑数组实现之前 ,先考虑树 是否是完全二叉树

注意 : 如果 存数据的时候 ,不是从 下标0的位置开始存,而是从下标为2的位置开始存,那么,任意节点的下标 异或 1,就可以得到 兄弟节点的位置
比如下图,3^1 = 4,4^1 = 3 ,不论哪个节点 ,异或一次 1就能得到兄弟节点
![2]

## 树的遍历
### 前序遍历
先序遍历 : 先访问 树根, 再访问左子树 ,最后访问 右子树

注：后序遍历的结果 反转 过来 ,可以看成是 ,先访问树根,再访问右子树 ,最后访问左子树

#### 递归实现
```{cpp}
void preOrder(BinNode<Elem> *root){
    if(root == NULL)    return;
    visit(root);
    preOrder(root->left());
    preOrder(root->right());
}
```
#### 非递归实现
非递归方式：手写栈栈， 模拟调用的过程

为什么需要非递归的方式？
1. 递归也需要时间
2. 可能出现爆栈

```{cpp}
void preOrder(BinNode<Elem> * root){
    stack<BinNode<Elem> *> s;
    BinNode<Elem> *p = root;
    while(!s.empty() || p){
       if(p!=NULL){
            visit(p);
            push(p);
            p = p -> left();
       }else {
            p = s.pop();
            p = p->right();
       }
   }
}
```

#### 已知中序遍历 ,后序遍历的结果 ,求树的形状
由后序遍历确定 树根 ,再由中序遍历 确定 左子树 和右子树 ,递归上面过程
后序遍历 : DECBHGFA
中序遍历 : BDCEAFHG
![3]

##### 参考代码
[HDU-1710](http://acm.hdu.edu.cn/showproblem.php?pid=1710)
[UVA-548](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=489)
```{cpp}
// 给出 中序遍历，前序遍历，输出后序遍历
int inorder[maxn], preorder[maxn],n,postorder[maxn]；
void recur(int l1, int r1, int l2, int r2) {
	if (l1 == r1) {
		postorder[cnt++] = inorder[l1];
	}
	if (l1 >= r1)	return;

	int root = l1;
	while (inorder[root] != preorder[l2]) {
		++root;
	}

	recur(l1, root - 1, l2 + 1, l2 + 1 + (root - 1 - l1));
	recur(root + 1, r1, l2 + 1 + (root - 1 - l1) + 1, r2);
	postorder[cnt++] = inorder[root];
}

recur(0, n - 1, 0, n - 1);
```
#### 已知中序遍历，后序遍历，求树的高度
```{cpp}
const int maxn = 1E6;
char inorder[maxn], postorder[maxn];
int recur(int l1, int r1, int l2, int r2) {
	if (l1 == r1) {
		return 0;
	}
	if (l1 >= r1)   return 0;

	int root = l1;
	while (inorder[root] != postorder[r2]) {
		++root;
	}
	int h1 = recur(l1, root - 1, l2, l2 + (root - l1 - 1));
	int h2 = recur(root + 1, r1, l2 + (root - l1 ), r2 - 1);
	return max(h1,h2) + 1;
}
```
### 逐层遍历
实际上就是 `bfs(广度优先搜索)`
```{cpp}
#include<queue>
int visitByLevelBFS(){
	queue<BinNode<Elem>*> q;
	q.push(root);
	while(!q.empty()){
		BinNode<Elem>* p = q.front();q.pop();
		visis(p);
		if(p->left())	q.push(p->left());
		if(p->right()) q.push(p->right());
	}
}
```

## 节点的数目
```{cpp}
int count(BinNode<Elem> *subRoot){
    if(subRoot == NULL)    return 0;
    return count(subRoot->left()) + count(subRoot->right()) + 1;
}
```

## 树的高度
```{cpp}
int height(BinNode<Elem> * subRoot){
     if(subRoot == NULL)    return 0;
    return max(height(subRoot->left),height(subRoot->right)) + 1;
}
```

## 清空树
```{cpp}
void clearTree(Node *root){
    if(root == NULL)    return ;
    clearTree(root -> lc);
    clearTree(root -> rc);
    delete root;
}
```

## 树的序列化
就是把树转换成一序列的数
但是 只知道 先/中/后序遍历 是无法还原出树的结构的。

### 解决办法
实际上，不能还原出树结构的原因就是，递归分割的时候，无法确定风分割的终点

设置边界，即在先序遍历 的序列中，设置标记，表示已经到达了叶子节
比如:`qxABzCgRQ` 大写字母表示叶子节点（实现下面见[参考代码](#参考代码-1)）
### 参考代码
```{cpp}
//根据先序遍历建树 qxABzCgRQ 大写字幕表示叶子节点
typedef char Elem;
class Node {
private:
	Elem item;
	Node * leftTree;
	Node * rightTree;
public:
	Node(Elem _item, Node *_leftTree = NULL, Node * _rightTree = NULL) :
		item(_item), leftTree(_leftTree), rightTree(_rightTree) {}
	Node * left() {
		return leftTree;
	}
	Node * right() {
		return rightTree;
	}
	bool hasLeft() {
		return leftTree != NULL;
	}
	bool hasRight() {
		return rightTree != NULL;
	}
	void setLeft(Node * _leftTree) {
		leftTree = _leftTree;
	}
	void setRight(Node * _rightTree) {
		rightTree = _rightTree;
	}
	Elem key() {
		return item;
	}

};
class Tree {
private:
	Node * root;
	string str;
	int sz;
	Node* builtHelp(int &pos, Node * hyRoot) {
		if (pos >= sz)	return NULL;
		if (isupper(str[pos])) {
			return new Node(str[pos]);
		}
		Node * tmp = new Node(str[pos]);
		if (++pos < sz)
			tmp->setLeft(builtHelp(pos, tmp));
		if (++pos < sz)
			tmp->setRight(builtHelp(pos, tmp));
		return tmp;
	}
	void clearHelp(Node * hyRoot) {
		if (hyRoot == NULL)	return;
		clearHelp(hyRoot->left());
		clearHelp(hyRoot->right());
		delete hyRoot;
	}
public:
	Tree() :root(NULL), sz(0) {}
	~Tree() {
		clear();
	}
	void clear() {
		clearHelp(root);
	}
	void built(string _str) {
		str = _str;
		sz = str.length();
		int pos = 0;
		root = builtHelp(pos, root);
	}
};
```


[1]:assets/binaryTree-47558.png
[2]:assets/binaryTree-4410b.png
[3]:assets/binaryTree-2fc00.png
