sync.Once为什么使用LoadUint32/StoreUint32而不是普通的赋值?

https://golang.org/ref/mem#tmp_3
https://stackoverflow.com/questions/15115589/is-the-two-atomic-style-code-in-sync-atomic-once-go-necessary
https://stackoverflow.com/questions/65935091/why-is-atomic-storeuint32-preferred-over-a-normal-assignment-in-sync-once


```
func (o *Once) Do(f func()) {
    // Note: Here is an incorrect implementation of Do:
    //
    //    if atomic.CompareAndSwapUint32(&o.done, 0, 1) {
    //        f()
    //    }
    //
    // Do guarantees that when it returns, f has finished.
    // This implementation would not implement that guarantee:
    // given two simultaneous calls, the winner of the cas would
    // call f, and the second would return immediately, without
    // waiting for the first's call to f to complete.
    // This is why the slow path falls back to a mutex, and why
    // the atomic.StoreUint32 must be delayed until after f returns.

    if atomic.LoadUint32(&o.done) == 0 {	//为什么不是o.done == 0?
        // Outlined slow-path to allow inlining of the fast-path.
        o.doSlow(f)
    }
}

func (o *Once) doSlow(f func()) {
    o.m.Lock()
    defer o.m.Unlock()
    if o.done == 0 {							//为什么不是atomic.LoadUint32(&o.done) == 0?
        defer atomic.StoreUint32(&o.done, 1)	//为什么不是o.done = 1?
        f()
    }
}
```

```
atomic.StoreUint32(&o.done, 1) can make sure a:=1 is coherent in all cpus' caches before o.done is 1
```

1. atomic保证写操作的结果对后续所有的访问都是可见的, 避免同一块内存被多次写入, 如果不用atomic则不保证所有cpu的cache 都更新
2. 但是即使不用atomic, 由于有所的锁的存在, 也可以保证代码只执行一次
3. 不能使用CompareAndSwapUint32, 因为第二个do的返回不保证f已经执行完毕, 即使执行完毕, 也无法保证f的操作对所有的cpu都可见
