# git 优雅回退操作

- 问题描述
    从
    ```
    A -> B -> C -> D (HEAD)
    \
    E --------> F
    ```
    变成
    ```
    A -> B -> C -> D -> G -> H (HEAD)
    \                      /
    E ----------------> F
    ```
    而不是
    ```
    A
    \
    E ----------------> F
    ```

- 解决方法
    * `git revert` 撤销某个commit，添加新的commit撤销该commit的改动，历史记录依旧存在
    * `git merge` 合并

    第三种情况的做法是：
    * `git reset` + `git push -f`


- 参考
    - [跪求不要 git push -f - 简书](https://www.jianshu.com/p/41cef45ef6ce?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)