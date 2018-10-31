# C++

## C++ 不允许重载的运算符是？

不能重载的运算符只有5个：
.  (成员访问运算符)
.*  (成员指针访问运算符)
::  (域运算符)
sizeof  (长度运算符)
?:  (条件运算符）

前两个运算符不能重载是为了保证访问成员的功能不能被改变，域运算符和sizeof 运算符的运算对象是类型而不是变量或一般表达式，不具备重载的特征。

## C++继承: 公有, 私有, 保护

|       |public   |protected|private|
|-------|---------|---------|------|
|公有继承|public   |protected|不可见|
|私有继承|private  |private  |不可见|
|保护继承|protected|protected|不可见|

即: 派生类继承父类的成员之后, 这些成员在派生类中的访问权限

通过 `using` 和 `typedef` 可以修改派生类中基类成员的访问权限

- [C++继承：公有，私有，保护 - csqlwy - 博客园](https://www.cnblogs.com/qlwy/archive/2011/08/25/2153584.html)
- [C++继承权限和继承方式_C语言中文网](http://c.biancheng.net/cpp/biancheng/view/2984.html)
- [派生类 - cppreference.com](https://zh.cppreference.com/w/cpp/language/derived_class)
- [访问指定符 - cppreference.com](https://zh.cppreference.com/w/cpp/language/access)
