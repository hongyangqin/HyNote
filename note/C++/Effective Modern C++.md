# Effective Modern C++

<<Effective Modern C++: 42招独家技巧助你改善C++11和C++14的高效用法>> 的阅读笔记

## 型别推导

> C++98 仅有一套型别推导规则, 用于函数模板
> C++11对这套规则进行了一些改动
> , 并增加了两套规则, 一套用于 `auto`, 一套用于 `decltype`
> C++14又扩展了能够运用 `auto` 和 `decltype` 的语境

### 型别推导理解

函数模板基本形式:

```cpp
template<typename T>
void f(ParamType param);
```

一次调用形式为:

```cpp
f(expr);
```

后续用到的变量定义:

```cpp
int x = 27;
const int cx = x;
const int & rx = x;
const int *px = &x;
const char * const ptr = "Fun with pointers";
const char name[] = "J. P. Briggs"; //name的型别是 cosnt char[13]
const char *ptrToName = name;       //数组退化成指针
```

直觉上, `x` 的型别是 `int`, `T`的型别也推导成 `int`, 这一点并不总是成立的. `T`的型别推导结果, 不仅仅依赖 `expr` 的型别, 还依赖 `ParamType` 的形式

1. 在模板型别 `T` 推导的过程中, 具有引用型别的实参 `expr` 会被当成非引用型别来处理, 即引用性会被忽略.
    ```cpp
    template<typename T>
    void f(T& param);

    f(x);   //T的型别是 int, param的型别是int &
    f(cx);  //T的型别是 const int, param的型别是const int &
    f(rx);  //T的型别是 const int, param的型别是const int &
    ```
    在`f(rx)`中, `rx`的型别是 `const int &`, 而 `T`的型别却是 `const int`, 引用性 `&` 被忽略了.

2. 对万能引用形参进行推导时, 左值实参会进行特殊处理.
    > 左值指的是字面值或者常量值?
    > `ParamType` 是个万能引用, 此类形参的声明方式类似右值引用(即在函数模板中持有型别形参`T`时, 万能引用的声明写别写作`T&&`)

    当遇到万能引用时, 型别推导规则会区分实参是左值还是右值, 而非万能引用时从来不会作这样的区分的

    ```cpp
    template<typename T>
    void f(T&& parm);

    f(x);       // x 是个左值, T的型别是 int&, param的型别是 int&
    f(cx);      //cx 是个左值, T的型别是 const int&, param的型别是 const int&
    f(rx);      //rx 是个左值, T的型别是 const int&, param的型别是 const int&
    f(27);      //27 是个右值, T的型别是 int, param的型别是 int&&
    ```

    当遇到万能引用时

3. 对按值传递的形参进行推导时, 若实参的 `const` 和 `volatile` 性会被忽略.
    ```cpp
    template<typename T>
    void f(T param);

    f(x);   //T 和 param 的型别都是 int
    f(cx);  //T 和 param 的型别还都是 int
    f(rx);  //T 和 parma 的型别仍都是 int
    ```
    `cx` 和 `rx` 都是 `const`, 而 `T` 的型别是 `int`, `const`被忽略了. `volatile` 同理.
    这是合理的, 因为 `param` 是个完全独立于 `cx` 和 `rx` 存在的对象, 是它们的副本, 从而 `rx` 和 `cx` 的不可修改性并不是说明 `param`是否可以修改.

    注: `const` 和 `volatile` 仅会在 **按值** 形参处被忽略.
    ```cpp
    f(ptr);  //T和param的型别是 const char *
    ```
    传递性质为 `const char* const` 的形参 `ptr`, 而 `param` 被推导为 `const char *`, 其自身的常量性会在以复制方式创建新的指针 `param` 的过程中被忽略. 而指针指向的内容的常量性会被保留.

4. 若 `ParamType` 包含实参 `expr` 型别的部分, 那么 `T`的推导结果就不需要包含该部分
    - `param` 具有 `const` 引用型别, 那么 `T` 的型别推导结果就不需要包含 `const`
        ```cpp
        template<typename T>
        void f(const T param);

        f(x);   // T 的型别是 int, param 的型别是 const int
        f(cx);  // T 的型别是 int, param 的型别是 const int
        f(rx);  // T 的型别是 int, param 的型别是 const int
        ```
        `cx` 型别为 `const int`, 而 `T`的型别是 `int`, 其 `const` 出现在 `const T` 这里.
    - `param` 是指针而非引用, 也同理
        ```cpp
        template<typename T>
        void f(T* param);

        f(&x);   // T 的型别是 int, param 的型别是 int *
        f(px);   // T 的型别是 const int, param 的型别是 const int *
        ```
        `px` 型别为 `const int *`, 而 `T`的型别是 `const int`, 其 `*` 出现在 `T*` 这里.

    综合二者:
    ```cpp
    template<typename T>
    void f(const T* param);

    f(&x);   // T 的型别是 int, param 的型别是 const int *
    f(px);   // T 的型别是 int, param 的型别是 const int *
    ```

5. 在模板型别推导过程中, 数组或函数型别的实参会退化成对应的指针.
    ```cpp
    template<typename t>
    void f(T param);

    f(name);    //T和param的型别是 const char *
    ```
    `name` 的型别是 `const char[13]`, `T` 被推导成 `const char *`

    在引用方式传递实参, 则可以保留 `[13]`
    ```cpp
    template<typename param>
    void f(T& param);

    f(name); //T 的型别是 const char[13], param的型别是 const char (&)[13]
    ```

    可以利用声明数组引用这一能力创造出一个模板, 用来推导出数据含有的元素个数:
    ```cpp
    template<typename T, std::size_t N>
    constexpr std::size_t arraySize(T (&)[N]) noexcept {
        return N;
    }
    ```
    > 该函数声明为 `constexpr`, 能够使得其返回值在编译期间就可用.

    函数型别也同样会退化函数指针, 和数组类似.
