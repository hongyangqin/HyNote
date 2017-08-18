<!--toc-->

- [kmp 算法](#kmp-算法)
	- [实现](#实现)
	- [参考代码](#参考代码)
	- [模式匹配](#模式匹配)
		- [可在已匹配成功的地方继续匹配](#可在已匹配成功的地方继续匹配)
		- [匹配成功后从下一位从头开始匹配](#匹配成功后从下一位从头开始匹配)

<!-- tocstop -->
# kmp 算法
问题：在原串s中查找 模式串p，问是否能找到

简单的想法就是从s的每一个点作为起点，不断和p进行比较
时间复杂度是 $O(mn)$，n为s长度，m为p长度

举个例子，
1. ![1]
2. ![2]
3. ![3]
4. ![4]
5. ![5]

可以看出到了第五步的时候，才匹配错误的位置才到到原来匹配错误的位置。实际上，第2，3，4步 没必要和原串匹配就能知道一定不会匹配成功，可以看成是自己和自己比较。如图：
![6]
到了蓝色部分才匹配失败，那么我们可以知道，第2，3，4步不需要和原字符串比较就能判断得到的，到了第5步开始才需要和原字符串进行比较。

所以，当匹配到某一个位置（比如蓝色位置）出现失败的时候，如果我们预先知道后面移动几次是一定失败的，那么就可以直接跳过这几步。（即跳过第2，3，4捕，直接进行第5步）。

kmp就是预处理出需要跳过的步数（对于这题的意义而言），然后匹配失的时候 就直接跳过那些必然失败的地方。

## 实现
实现的时候是用 NEXT 数组
NEXT[i] 表示 第i+1位匹配失败的时候，下一下应该比较的地方。
比如 上面的例子，模式串和原串在第6个位置匹配失败的时候，下一次 和 原串当前的位置进行比较的位置应该是 2 (NEXT\[6 - 1\])
![7]

## 参考代码
```{cpp}
//这份代码只是演示了指针i，j的移动，并没有对数据进行判断和统计。如果要进行判断是否已经匹配成功之类，需要添加代码
const int maxn = 1E4 + 10;
int NEXT[maxn];
void makeNext(char p[], int n) {
	memset(NEXT, 0, sizeof(NEXT));
	int i = 1, j = 0;
	while (i < n) {
		if (p[i] == p[j])	NEXT[i++] = ++j;
		else if (j > 0)	j = NEXT[j - 1];
		else ++i;
	}
}

void kmp(char str[], char p[]) {
	int n = strlen(str);
	int m = strlen(p);
	makeNext(p, m);
	int i = 0, j = 0;
	while(i < n){
		if (str[i] == p[j]) {
			++i; ++j;
		}
		else if(j > 0)	j = NEXT[j - 1];
		else ++i;
	}
}
```

## 模式匹配
### 可在已匹配成功的地方继续匹配
![8]
```{cpp}
//返回 str 中 p的数目
int hyStrstr(char str[], char p[]) {
	int n = strlen(str);
	int m = strlen(p);
	makeNext(p, m);
	int i = 0, j = 0,cnt = 0;
	while(i < n){
		if (str[i] == p[j]) {
			++i; ++j;
			if (j == m) {
				j = NEXT[j - 1];
				++cnt;
			}
		}
		else if(j > 0)	j = NEXT[j - 1];
		else ++i;
	}
	return cnt;
}
```

### 匹配成功后从下一位从头开始匹配
```{cpp}
//返回 str 中 p的数目
int hyStrstr(char str[], char p[]) {
	int n = strlen(str);
	int m = strlen(p);
	makeNext(p, m);
	int i = 0, j = 0,cnt = 0;
	while(i < n){
		if (str[i] == p[j]) {
			++i; ++j;
			if (j == m) {
				j = 0;
				++cnt;
			}
		}
		else if(j > 0)	j = NEXT[j - 1];
		else ++i;
	}
	return cnt;
}
```



[1]:assets/kmp-97d54.png
[2]:assets/kmp-71fd9.png
[3]:assets/kmp-a7905.png
[4]:assets/kmp-97340.png
[5]:assets/kmp-5b29b.png
[6]:assets/kmp-069e2.png
[7]:assets/kmp-2b4c6.png
[8]:assets/kmp-f392f.png
