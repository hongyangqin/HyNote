<!--toc-->

- [二叉搜索树 BST](#二叉搜索树-bst)
	- [注意](#注意)
	- [参考代码](#参考代码)
		- [查找](#查找)
		- [BST的插入](#bst的插入)
		- [BST的删除](#bst的删除)
	- [BST使用的时机](#bst使用的时机)
	- [时间复杂度](#时间复杂度)
	- [为什么平衡树的高度 是 $log_2 n$](#为什么平衡树的高度-是-log_2-n)
	- [如果出现多个变量 的 查询，插入，删除操作怎么办？](#如果出现多个变量-的-查询插入删除操作怎么办)
	- [数据特别大的时候，内存不够用怎么办？](#数据特别大的时候内存不够用怎么办)
	- [参考代码](#参考代码-1)

<!-- tocstop -->
#  二叉搜索树 BST
左子树所有节点的值小于树根，所有右子树的值大于等于树根

## 注意
1. 相同一组值的BST 不是唯一的（树根不同）
2. BST 有可能退化成 线性表

## 参考代码
### 查找
```{cpp}
void search(root,val){
    if(root == NULL)    return ;
    if(val < lc)    search(lc,val)
    else    if(val > lc)    
        search(rc,val);
    else {    
        find!
     }
}
```

### BST的插入
```{cpp}
    Node* addNodeHelp(Node* hyRoot,Elem item){
        if(hyRoot == NULL){
            return new Node(item);
        }
        if(hyRoot->key() > item){
            hyRoot->setLeft(addNodeHelp(hyRoot->left(),item));
        }else{
            hyRoot->setRight(addNodeHelp(hyRoot->right(),item));
        }
        return hyRoot;
    }
```

### BST的删除
1. 先查找
2. 找不到 直接返回NULL
3. 找到之后，
    1. 只有 左/右 子树，那么，直接把节点替换即可
    2. 找到的点，左，右 子树都有，为了保证BST，需要在右子树中找最大（小），或者左子树中找最小（大）来作为根节点
```{cpp}
    void removeNodeOnce(const Elem &e,Node * &t){
        root = removeHelp(root,e,t);
    }    
   Node * deleteMax(Node *hyRoot, Node * &hyMax) {
        if (!hyRoot->hasRight()) {
            hyMax = hyRoot;
            return NULL;
        }
        else {
            hyRoot->setRight(deleteMax(hyRoot->right(), hyMax));
        }
        return hyRoot;
    }
    Node * removeHelp(Node * hyRoot, const Elem &e, Node * &t) {
        if (hyRoot == NULL) {
            return t = NULL;
        }
        else if (e < hyRoot->key()) {
            hyRoot->setLeft(removeHelp(hyRoot->left(), e, t));
        }
        else if (e > hyRoot->key()) {
            hyRoot->setRight(removeHelp(hyRoot->right(), e, t));
        }
        else {
            if (hyRoot->hasLeft() && !hyRoot->hasRight()) {
                t = hyRoot;
                return hyRoot->left();
            }
            else if (!hyRoot->hasLeft() && hyRoot->hasRight()) {
                t = hyRoot;
                return hyRoot->right();
            }
            else if (hyRoot->isLeaf()) {
                t = hyRoot;
                return NULL;
            }
            else {
                hyRoot->setLeft(deleteMax(hyRoot->left(), t));
                Elem tmp = t->key();
                t->setKey(hyRoot->key());
                hyRoot->setKey(tmp);
            }
        }
        return hyRoot;
    }
```

## BST使用的时机
输入 数据乱序
输入 数据有序的话，整个BST就 退化成 线性表

## 时间复杂度
时间复杂度分析：
最严重的情况，找到最深的叶子：$O(h)$
最好的情况：$O(1)$

平衡树的情况
树的高度：$h = log_2 n$

## 为什么平衡树的高度 是 $log_2 n$
$n = 2^0 + 2^1 + ... + 2^h = 2^h - 1$，则 $h = log_2 (n + 1)$

## 如果出现多个变量 的 查询，插入，删除操作怎么办？
建立索引，每个变量建立一个 BST树

## 数据特别大的时候，内存不够用怎么办？
1. 索引才读入内存，数据不读入
2. 只载入部分树到内存，其他存入磁盘
3. 把常用的 数据 放入缓冲区 cache（避免频繁读写慢的问题）
4. 建立索引数组的时候，删除数据不一定要真的删除，可以建立一个 freelist类似的东西

注：
1. 实际上，数据库不用BST，因为BST是二叉，当数据特别多的时候，树特别高
2. 数据库 用的是 B+树，（多叉的BST，通过区分不同区间来分叉）

## 参考代码
```{cpp}
typedef int Elem;
class Node {
private:
	Elem item;
	Node * leftTree;
	Node * rightTree;
public:
	Node(Elem _item, Node * _leftTree = NULL, Node * _rightTree = NULL) :
		item(_item), leftTree(_leftTree), rightTree(_rightTree) {}
	void setLeft(Node *_leftTree) {
		leftTree = _leftTree;
	}
	void setRight(Node *_rightTree) {
		rightTree = _rightTree;
	}
	Elem key() {
		return item;
	}
	void setKey(Elem item) {
		this->item = item;
	}
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
	bool isLeaf() {
		return !hasLeft() && !hasRight();
	}
};

class BST {
private:
	Node * root;
	Node* addNodeHelp(Node* hyRoot, Elem item) {
		if (hyRoot == NULL) {
			return new Node(item);
		}
		if (hyRoot->key() > item) {
			hyRoot->setLeft(addNodeHelp(hyRoot->left(), item));
		}
		else {
			hyRoot->setRight(addNodeHelp(hyRoot->right(), item));
		}
		return hyRoot;
	}
	int heightHelp(Node *hyRoot) {
		if (hyRoot == NULL)	return 0;
		return max(heightHelp(hyRoot->left()), heightHelp(hyRoot->right())) + 1;
	}
	void clearHelp(Node * hyRoot) {
		if (hyRoot == NULL)	return;
		clearHelp(hyRoot->left());
		clearHelp(hyRoot->right());
		delete hyRoot;
	}
	Node * deleteMax(Node *hyRoot, Node * &hyMax) {
		if (!hyRoot->hasRight()) {
			hyMax = hyRoot;
			return NULL;
		}
		else {
			hyRoot->setRight(deleteMax(hyRoot->right(), hyMax));
		}
		return hyRoot;
	}
	Node * removeHelp(Node * hyRoot, const Elem &e, Node * &t) {
		if (hyRoot == NULL) {
			return t = NULL;
		}
		else if (e < hyRoot->key()) {
			hyRoot->setLeft(removeHelp(hyRoot->left(), e, t));
		}
		else if (e > hyRoot->key()) {
			hyRoot->setRight(removeHelp(hyRoot->right(), e, t));
		}
		else {
			if (hyRoot->hasLeft() && !hyRoot->hasRight()) {
				t = hyRoot;
				return hyRoot->left();
			}
			else if (!hyRoot->hasLeft() && hyRoot->hasRight()) {
				t = hyRoot;
				return hyRoot->right();
			}
			else if (hyRoot->isLeaf()) {
				t = hyRoot;
				return NULL;
			}
			else {
				hyRoot->setLeft(deleteMax(hyRoot->left(), t));
				Elem tmp = t->key();
				t->setKey(hyRoot->key());
				hyRoot->setKey(tmp);
			}
		}
		return hyRoot;
	}
public:
	~BST() {
		clear();
	}
	BST() :root(NULL) {}
	void addNode(Elem item) {
		root = addNodeHelp(root, item);
	}
	int height() {
		return heightHelp(root);
	}
	void clear() {
		clearHelp(root);
	}
	void removeNodeOnce(const Elem &e, Node * &t) {
		root = removeHelp(root, e, t);
	}
};
```
