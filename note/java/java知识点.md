<!--toc-->

- [java 语言的特点](#java-语言的特点)
- [面向对象的3个特性](#面向对象的3个特性)
- [转义字符](#转义字符)
	- [八进制转义符](#八进制转义符)
	- [十六进制转义符](#十六进制转义符)
- [常量](#常量)
	- [正数常量](#正数常量)
		- [八进制整数](#八进制整数)
		- [二进制整数](#二进制整数)
- [final 关键字](#final-关键字)
	- [作用](#作用)
- [static 关键字](#static-关键字)
	- [作用](#作用-1)
	- [访问方法](#访问方法)
	- [其他](#其他)
- [this 关键字](#this-关键字)
	- [this方法](#this方法)
	- [this 引用](#this-引用)
- [初始化的顺序](#初始化的顺序)
- [super 关键字](#super-关键字)
	- [super方法](#super方法)
- [访问控制](#访问控制)
	- [public](#public)
	- [protected](#protected)
	- [package/default](#packagedefault)
		- [修饰类](#修饰类)
	- [private](#private)
		- [修饰构造器](#修饰构造器)
- [import](#import)
- [extends 关键字](#extends-关键字)
- [构造器](#构造器)
- [向上转型](#向上转型)
- [输入输出](#输入输出)
- [abstract](#abstract)
	- [修饰类](#修饰类-1)
	- [修饰方法](#修饰方法)
- [interface](#interface)
- [comparable 接口](#comparable-接口)
- [throw 关键字](#throw-关键字)
	- [抛出异常](#抛出异常)
	- [捕获异常](#捕获异常)
	- [自定义异常](#自定义异常)
- [内部类](#内部类)
- [局部内部类](#局部内部类)
- [匿名类](#匿名类)
- [instanceof 关键字](#instanceof-关键字)
- [string 类](#string-类)
	- [不可变性](#不可变性)
	- [valueOf(Object Obj)方法](#valueofobject-obj方法)
	- [String [] split(String regex) 方法](#string-splitstring-regex-方法)
- [StringBuffer 类](#stringbuffer-类)
- ['==' 与 equals方法](#与-equals方法)
- [foreach 语句](#foreach-语句)
- [map](#map)

<!-- tocstop -->

# java 语言的特点
1. 平台无关性
2. 面向对象
3. 简单性
4. 安全性
5. 分布性
6. 健壮性
7. 解释性
8. 多线程

# 面向对象的3个特性
1. 封装
2. 继承
3. 多态

# 转义字符
## 八进制转义符
`xxx` 是八进制数，位数可以是1位，2位，3位。
当位数是 3 位时，首位只能是0~3
```{java}
\xxx
```

## 十六进制转义符
`xxxx` 是十六进制数
```{java}
\uxxxx
```

# 常量

## 正数常量

### 八进制整数
首字符是 `0`
```
int a = 012;//a 表示八进制的12
```

### 二进制整数
以 `0b` 或者 `0B` 开头
```{java}
0b101
```

# final 关键字
## 作用
1. final 修饰的成员变量为常量，不能被修改
2. final 修饰成员方法，表示不能被当前类的子类重写
3. final 修饰类，表示这个类不能再被继承

# static 关键字
## 作用
1. static 修饰变量，即类变量，只有一个实例
2. static 修饰方法，即类方法，只可以访问类变量
3. static 块
    在第一次访问类成员的时候，会先运行 **static块** 内的代码

## 访问方法
1. objectName.value;
2. ClassName.value;
3. objectName.func();
4. ClassName.func();

## 其他
1. static 方法是 前期绑定，非static 方法是后期绑定

# this 关键字

## this方法
必须为构造器第一句代码，调用其他构造器。

## this 引用
引用当前方法所在的对象。可以用来处理局部变量和数据成员名字冲突的情况。

# 初始化的顺序
1. 先初始化父类(调用父类的构造器)
2. 对于每个类内部，先初始化静态成员变量，再初始化非静态成员变量
3. 调用自己类的构造器
4. 对于静态成员，先初始化父类的，再初始化自己的
5. 对于静态成员和静态块，谁先出现谁先运行。

父类静态块/成员->子类静态块/成员->父类成员->父类构造器->子类成员->子类构造器


# super 关键字
当前对象的父类的引用(类比this，this为自己的引用)

## super方法
调用父类的构造器

# 访问控制
成员变量 默认为 package 权限

-|本类|本包|不同包中的子类|不同包中的所有类
-|----|------------------|------------|---------------
public|$\surd$|$\surd$   |$\surd$     |$\surd$
protected|$\surd$|$\surd$|$\surd$     ||
package/default|$\surd$|$\surd$|||
private|$\surd$||||

## public
表示任何程序包内的类都可以访问

## protected
表示类自己，子类，相同包的类都可以访问

## package/default
表示同一个包内能访问，但是不同包的子类不能访问。（注：同包内的子类是可以访问的。）

### 修饰类
表示把类放入某个包内

```{java}
package com.qhy.cat
```

## private
表示只有类自己能访问

### 修饰构造器
表示在类的外部不能new，只能通过类内部的静态方法来实例化（应用：单例）

# import
导入当前包内的所有类

注意：只能导入当前目录下的类，不能导入其子目录下的类
```{java}
import com.qhy.*
```

# extends 关键字
继承类的关键字
```{java}
class Student extends Person{}
```

注意：
1. `extends` 后面有个 `s`
2. `interface` 在 `extends` 后面可以接多个父类接口

# 构造器
构造器是一种特殊的方法，这个方法名字和类名一样，在对象实例化的时候，会调用这个方法进行初始化

默认构造器是一个无参构造器

当构造器存在的时候，不会自动生成默认构造器

构造器内可以调用其他构造器，区别于C++，java 是通过 this方法来调用其他构造器的，并且只能在构造器首行代码中调用，且仅有一次。

子类的构造器，如果在父类中没有无参构造器（包括默认构造器在内），那么在子类的构造器内必须要显示地调用一次父类的构造器，否则出错。

# 向上转型
类似C++的虚函数

向上转型的本质 实际上就是 父类重名方法的重写。

所以，如果父类和子类有相同的名字的成员变量，使用父类引用子类时，访问这个成员变量，访问的是父类的那个。

好处：可以通过定义父类的对象，来控制不同的子类对象。

1. 只有 非 静态 方法能被重写，静态方法不被重写，因为静态方法是与类关联，而不是与对象关联

2. 只有 非final ，非private 方法才能被重写，否则两个就是完全不同的方法

3. 在 被重写的方法中，访问的成员都是 子类内的成员
		如果方法被重写，那么这个方法访问了父类和子类的一个同名变量，那么这个方法访问的是子类的。
		如果方法没被重写，如果这个方法也访问了子类和父类的一个同名变量，那么它访问的是父类的。

# 输入输出
字节流：8bit
字符流：16bit

# abstract

## 修饰类
声明：只需要在`class`前使用 `abstract` 关键字即可

抽象类一定不能实例化。

抽象类内不一定要有抽象方法。

继承抽象类的子类必须实现抽象类中的抽象方法

## 修饰方法
方法的定义就不需要写了，类似C++的纯虚函数

# interface
接口：只有方法的特殊的抽象类。

interface的方法，默认都是 `abstract` ,`public` 的

interface内域是静态的，所以 在interface 内声明的变量是final public ,static的

作用：
1. 用于实现多继承
2. 可以用作形参
3. 接口可以继承多个父类结构

# comparable 接口
比较两个类对象

# throw 关键字
## 抛出异常
```{java}
public void func()throws SomeException {
//声明该方法可能出现的异常,在小括号和 花括号之间加 上面那句语句
        if(someCondition()){
            //构造并抛出异常对象
            throw new SomeException("错误原因");
        }
}
```

## 捕获异常
注意：RuntimeException可以不捕获，但是其他异常必须处理。
```{java}
try{
    //可能导致一场的语句
} catch( 异常类型 t ){
    //处理异常
    t.printStackTrace();//输出异常的信息
}catch ...
```

## 自定义异常
```{java}
//从某个异常类中继承
class MyException extends Exception{
    MyException(){}
}
```
# 内部类
在类内部定义的类

可以有4种权限（普通类只有两种public package）

内部类对象是以来外围类对象而存在的，因此在类外面声明一个内部类对象，需要一个外围类对象。
```{java}
外围类.内部类 = 外围类对象.new
```

内部类构造器,即 除了除了静态类，在创建内部类对象的时候，必须确保 外围类对象的存在

内部类对象可以访问外围类的数据成员，包括private数据成员。

获取内部类所在的外围类对象的引用
```
外围类类名.this
```

# 局部内部类
在方法内的类
只有两种权限，不能有 public ,private ，因为局部内部类的作用域已经确定在方法的花括号内。

# 匿名类
语法:
```{java}
类名{
	定义
}
```

含义：创建一个父类是 `类名` 的子类
生成一个子类，并且向上转型，即类名是父类的名字，不是这个类的名字（这个生成的子类匿名了）

# instanceof 关键字
判断这个对象是否属于某个类 或者 这个类的子类
```{java}
if(obj instanceof Person)
```

# string 类
**不可改变** 的字符序列

## 不可变性
不是引用不可变， 而是引用的对象不可变
```{java}
String s1 = "hello ",s2 = "World ";
s1 += s2;
//合法，不过会创建要给新的对象（值是s1+s2），并把s1的引用改成是这个对象，
```

## valueOf(Object Obj)方法
把其他类型转换成字符串（调用 OJB的 toString 方法）

## String [] split(String regex) 方法
用特定字符串 regex 把 String 分成几个字符串，

# StringBuffer 类
可变 的字符序列

# '==' 与 equals方法
1. (自己定义的类)没有重写equals 方法，调用equals 方法默认是 '==' 的结果??
2. 重写 equals 也要重写 hashcode 方法，反之亦然

# foreach 语句
1. 对于数组，不能知道下标
2. 对于集合，不能使用remove方法
```{java}
Collect c = new ArrayList();
for(Sbject obj:c){
    //do something with obj;
}
```

# map
map 不允许键重复，但允许值重复。
