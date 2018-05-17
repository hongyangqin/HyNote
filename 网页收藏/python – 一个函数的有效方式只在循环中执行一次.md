# [python – 一个函数的有效方式只在循环中执行一次](https://codeday.me/bug/20170901/65228.html)

时间：2017-09-01

标签： [python](https://codeday.me/tag/python)

目前，我正在做类似下面的事情，这变得乏味：

``` python
run_once = 0
while 1:
    if run_once == 0:
        myFunction()
        run_once = 1:
```

我猜有更多的接受的方式来处理这个东西？

我正在寻找的是一个函数执行一次，按需。例如，在按下某个按钮时。它是一个交互式应用程序，它有很多用户控制的开关。对于每个开关都有一个垃圾变量，只是为了跟踪它是否已经运行，似乎是低效的。

我将使用一个装饰器上的函数来处理跟踪它运行了多少次。

``` python
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def my_function(foo, bar):
    return foo+bar
```

现在my\_function只会运行一次。其他调用将返回None。只是添加一个else子句if如果你想要返回别的东西。从你的例子，它不需要返回任何东西。

如果你不控制函数的创建，或者函数需要在其他上下文中正常使用，你也可以手动应用装饰器。

``` python
action = run_once(my_function)
while 1:
    if predicate:
        action()
```

这将使my\_function可用于其他用途。

最后，如果你只需要运行一次两次，那么你可以做

``` python
action = run_once(my_function)
action() # run once the first time

action.has_run = False
action() # run once the second time
```

> 原文翻译自： http://stackoverflow.com/questions/4103773/efficient-way-of-having-a-function-only-execute-once-in-a-loop

本站文章除注明转载外，均为本站原创或编译
转载请明显位置注明出处： [python – 一个函数的有效方式只在循环中执行一次](https://codeday.me/bug/20170901/65228.html)