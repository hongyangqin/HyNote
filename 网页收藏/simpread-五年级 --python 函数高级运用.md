> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 http://www.cnblogs.com/xiaobaiskill/p/8998714.html

### **一、装饰器**

#### 　　1.1 闭包函数用法

<pre># 需求:
# 执行一个函数前需要认证是否登录,如果登录则不需再登录.
# 只认证一次,后续操作无需认证
# 要求认证使用闭包函数用法
# 闭包函数 = 函数嵌套 + 命名空间作用域 + 函数对象</pre>

<pre>login_status = {
    'user':None,
    'status':None
}

def login(user:str,pwd:str):
    if user == 'jmz' and pwd =='123':
        return True
    else:
        return False

# 认证用户是否登录成功
def auth(func):
    def wrapper(*args,**kwargs):
        if login_status['user'] and login_status['status']:
            return func(*args,**kwargs)
        else:
            uname = input('username>>').strip()
            upwd = input('password>>').strip()
            res =login(uname,upwd)
            if res:
                return func(*args, **kwargs)
            else:
                print('认证失败')
    return wrapper

def index():
    print('from index')

index = auth(index)

def cat():
    print('form cat')

index()
cat()</pre>

实现

#### 　　1.2 什么是装饰器

<pre>#  什么是装饰器
    # 1、装饰即修饰，器指的就是工具
    # 2、装饰器本身可以是任意可调用的对象
    # 3、被装饰的对象也可以是任意可调用的对象</pre>

#### 　　1.3 为什么要使用装饰器

<pre>#  为什么要使用装饰器
    # 1、在不改变原有的调用方式,不改变原方法的前提下，如何实现对内容上的新增？？
    # 例如：
        # 今天公司cto要求对一些方法添加文件的日志记录（此时你是否需要对每一个方法添加日志的记录？）
        # 第二天CTO 突然改变主意说 原来的方法添加日志记录改为 mysql 记录（此时你是否又要修改每一个方法的日志记录？？）
        # 我知道你此时此刻一定会想，我可以写一个日志记录方法，让每一个方法内部调用这个方法（很不错的想法）
        # 第三天 你的公司cto 告诉你，我的日志一定要记录那些方法执行的开始和结束时间。（是不是有点懵X了？你该怎么办？？）</pre>

#### 　　1.4 怎么用装饰器

<pre>    # 是否是和上面的那个闭包函数很像呀（其实装饰器就是闭包函数的一种运用）
    # 装饰器语法糖：
    # 在被装饰对象的正上方一行写@装饰器的名字
    # @auth   ==> func = auth(func)</pre>

<pre>login_status = {
    'user':None,
    'status':None
}

def login(user:str,pwd:str):
    if user == 'jmz' and pwd =='123':
        login_status['user']=user
        login_status['status']=True
        return True
    else:
        return False

# 认证用户是否登录成功
def auth(func):
    def wrapper(*args,**kwargs):
        if login_status['user'] and login_status['status']:
            return func(*args,**kwargs)
        else:
            uname = input('username>>').strip()
            upwd = input('password>>').strip()
            res =login(uname,upwd)
            if res:
                return func(*args, **kwargs)
            else:
                print('认证失败')
    return wrapper

@auth
def index():
    print('from index')

@auth
def cat():
    print('form cat')

index()
cat()</pre>

怎么使用装饰器

#### 　　1.5 有参装饰器

<pre>    # 上面的装饰器只是使用了固定的用户jmz,登录，而且没有实现以哪种方式 验证（文件方式，还是mysql方式）
    # 如果我需要暂时以文件的方式验证，后期再改为使用mysql 方式验证该如何使用？？？ （尽量减少代码的修改）
    # 要求：
        # 1、验证的方式是不固定的
        # 2、使用的装饰器要兼顾至少两种以上的验证方式
        # 3、需要能够随时给方法添加验证或撤销验证</pre>

<pre>login_status = {
    'user':None,
    'status':None
}

def login(user:str,pwd:str,type='file'):
    if type == 'file':
        # 假设这就是文件认证
        if user == 'jmz' and pwd == '123':
            login_status['user'] = user
            login_status['status'] = True
            return True
        else:
            return False
    elif type =='mysql':
        # 假设这就是mysql认证
        if user == 'jmz' and pwd == '123':
            login_status['user'] = user
            login_status['status'] = True
            return True
        else:
            return False

# 认证用户是否登录成功
def auth(type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)
            else:
                uname = input('username>>').strip()
                upwd = input('password>>').strip()
                res =login(uname,upwd,type)
                if res:
                    return func(*args, **kwargs)
                else:
                    print('认证失败')
        return wrapper
    return auth2

@auth('file')
def index():
    print('from index')

@auth('file')
def cat():
    print('form cat')

index()
cat()</pre>

有参装饰器

### **二、迭代器**

#### 　　2.1 什么是迭代器？

　　　　迭代的工具:

　　　　　　迭代是一个重复的过程, 每一次的重复都是基于上一次的结果进行的　　　　　　

<pre># 这不是迭代
while True:
    print('....')</pre>

#### 　　2.2 为什么要使用迭代器？

　　　　找到一种不依赖于索引的迭代的方式?

<pre># 1、列表是自带索引的，那么如何迭代没有索引的呢？？？（禁止使用for）
l = ['a','b','c']
k = 0
while k<len(l):
    print(l[k])
    k+=1

# 2、如何循环取一个无限大的值？
#     如果使用上面的方法显然是不现实的，因为你的列表是存不下无限大的值的（列表的数据占着内存的空间）

# 那怎么办呢？</pre>

#### 　　2.3 怎么使用迭代器？

　　　　2.3.1　可迭代对象

　　　　　　　　python 中, 但凡内置__iter__方法的, 都是可迭代对象

<pre>a = 1
b = 1.1
# 以下都是可以使用__iter__ 方法
c = 'abcd'
#c.__iter__()
d = ['a','b','c']
# d.__iter__()
e = ('a','b','c')
# e.__iter__()
f = {'a':1,'b':2}
# f.__iter__()
g={'a','b','c'}
# g.__iter__()
h=open('a.txt','r')  # 本身就是一个迭代器对象</pre>

　　　　　2.3.2 迭代器对象　　　　　　　

<pre>#     可迭代对象：在python中但凡有内置方法__iter__的对象，都是可迭代对象
#     迭代器对象 ：
#         执行可迭代对象下__iter__方法后得到迭代器对象
#     迭代器对象的内置方法
#         __next__
#         __iter__方法,执行该方法得到仍然是迭代器本身，干什么用？？(等下解释)
# 有了迭代器我们就不需要依赖索引取值了
</pre>

<pre>#       注意：
#　　　　　　1、迭代器对象一定是对迭代对象
#　　　　　　2、可迭代对象不一定是迭代器对象</pre>

<pre>dic = {'a':1,'b':2,'c':3,'d':4}
iter_obj = dic.__iter__()
print(next(iter_obj))     # a
print(next(iter_obj))     # b

iter_obj1 = dic.__iter__()     # 重新 做了一次迭代器对象操作
print(next(iter_obj1))    # a。

iter_obj = iter_obj.__iter__()      # iter_obj.__iter__()  is iter_obj     #True
#iter_obj.__iter__() 无论执行多少次都是本身
print(next(iter_obj))     # c    # 会继续给予上一次的操作继续执行
print(next(iter_obj))     # d</pre>

__iter__ , 迭代器对象执行后任然是本身

<pre>#for循环的底层运行机制：for循环可以称之为迭代器循环
#1、先调用in后那个对象的__iter__方法，得到该对象的迭代器对象
#2、执行迭代器对象的__next__方法，将得到的返回值赋值in前面的变量名，然后执行一次循环体代码
#3、循环往复，直到取干净迭代器内所有的值，自动捕捉异常结束循环
dic = {'a':1,'b':2}

iter_obj = dic.__iter__()
while True:
    try :
        print(dic[iter_obj.__next__()])
    except StopIteration:
        break

for k in dic: #iter_obj=dic.__iter__()
    print(dic[k])</pre>

for 循环实现原理

#### 　　　2.4 总结

<pre># 优点：
#        1、不依赖于索引的迭代取值
#        2、节省内存，计算取值

# 缺点：
#        1、无法获取长度
#        2、只能next,不能向上取值，只能想下直至结束</pre>

迭代器的优缺点

### **三、生成器**

#### 　　3.1 什么是生成器　

<pre># 函数内部含有yield关键字，那么该函数（） 即为生成器。
# 自定义迭代器

def func():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3

f = func()
print(f) **#<generator object func at 0x0000000001DF0DB0>**</pre>

#### 　　3.2 生成器的使用方式

<pre># yield 返回值操作
# 生成器就是迭代器，所以用法与迭代器一样

# 仿range函数
def range(start:int,end:int,step=1):
    while start < end:
        yield start        # 当一次next 执行到这里时便会返回start,并停止，下一次操作会从本次停止的地方继续往下执行，
        start += step       # 直到再次遇到 yield 再停止，返回后面的值

num = range(1,6,2)
print(num.__next__())
print(num.__next__())
print(num.__next__())

# yield ： 具有停止本次操作，并return yield 后面的值，与return的返回值一样</pre>

生成器使用方式一

<pre># yield 传值操作
def doing(name):
    print('%s开始干活了'%name)
    thing_list = set()
    while True:
        do_thing = yield thing_list          # 返回thing_list
        print('%s 正在%s'%(name,do_thing))
        thing_list.add(do_thing)

xiaoming = doing('xiaoming')
next(xiaoming)                   # 第一次使用，需暂停到yield 那边
print(xiaoming.send('做饭'))    # 先给yield 传值， 之后再接受执行到下一个yield的返回值
print(xiaoming.send('吃饭'))
print(xiaoming.send('干活'))
print(xiaoming.send('睡觉'))
xiaoming.close()                 # 关闭生成器
xiaoming.send('起床时')         # 此时无法再传值执行，并且报错</pre>

生成器使用方式二

#### 　　3.3 总结

<pre># 1、可以像return 一样，返回值，但又可以多次返回
# 2、可以挂起/保存函数的当前状态，可以达到随用随启动的程度
# 3、可以多次传值操作</pre>

### **四、练习**

<pre># 作业一:写一个取基数的操作 (迭代器)
# 作业二:咖啡3元，糖0.5元 牛奶2元，平时咖啡单点的，活动需要，需加糖与牛奶捆绑销售(装饰器)
# 作业三:用户购买商品，以邮箱或短信的形式通知(装饰器)</pre>

<pre>#作业一
def jishu():
    num = 1
    while True:
        is_true = True
        if num > 1:
            count = 2
            while count < num - 1:
                if num%count==0:
                    is_true = False
                    break
                count +=1
        if is_true:
            yield num
        num +=1

num = jishu()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

#作业二
def sugar(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        res += 0.5
        return res
    return wrapper

def milk(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        res += 2.5
        return res
    return wrapper

@sugar
@milk
def coffee():
    return 3

print(coffee())

#作业三
def notice(type='email'):
    def shopping(func):
        def wrapper(*args,**kwargs):
            if type == 'email':
                print('邮箱通知成功')
            elif type == 'sms':
                print('短信通知成功')
            return func(*args,**kwargs)
        return wrapper
    return shopping

@notice('sms')
def shopping(good):
    print('成功购买了%s商品'%good)

shopping('电脑')</pre>

作业