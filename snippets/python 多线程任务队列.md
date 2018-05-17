# python 多线程任务队列

```python
import threading
import queue

class TaskQueue(queue.Queue):
    def __init__(self, num_workers=1):
        queue.Queue.__init__(self)
        self.num_workers = num_workers
        self.started = False

    def start_workers(self):
        if self.started:
            return
        self.threads = []
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads.append(t)
        self.started = True

    def stop_workers(self):
        if not self.started:
            return
        self.join()
        for i in range(self.num_workers):
            self.put(None)
        for t in self.threads:
            t.join()
        self.threads = []
        self.started = False

    def add_task(self, task, *args, **kwargs):
        if not self.started:
            return
        for i in range(self.num_workers):
            args = args or ()
            kwargs = kwargs or {}
            self.put((task, args, kwargs))

    def worker(self):
        while True:
            item = self.get()
            if item is None:
                break
            item, args, kwargs = item
            item(*args, **kwargs)
            self.task_done()
```

## 参考

[Python 30 行代码实现小型多线程任务队列 - Python - 伯乐在线](http://python.jobbole.com/84327/)
[17.7. queue — A synchronized queue class — Python 3.6.5 documentation](https://docs.python.org/3.6/library/queue.html)