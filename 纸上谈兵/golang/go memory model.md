go内存模型

https://golang.org/ref/mem#tmp_3

1 For example, if one goroutine executes a = 1; b = 2;, another might observe the updated value of b before the updated value of a.
2 为保证线程时间的执行顺序(生效), 需要使用sync/atomic包里边的函数保证, 比如once等


疑问: go底层是怎么保证Once执行的f()一定会生效? 
1. atomic保证o.done的写对所有线程可见
2. lock/unlock保证f()的结果对所有线程可见

**疑问**: golang底层是如何保证lock/unlock/channel等同步语句的执行结果的同步, 是有对应的缓存刷新指令还是有其他的可分解知识点需要进一步学习?