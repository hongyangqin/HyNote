# Effective C++

## const 成员函数

1. 当对象为const时，调用const版本的成员函数
    除此之外，const成员函数还通过返回值为const来限制返回结果的操作
    ```cpp
    const char & operator[](std::size_t pos) const {
        return text[pos];
    }
    ```
2. `mutable`关键字
    当一个成员变量声明的时候，含有`mutable`关键字，表示该成员变量总是可能被更改的，即使在const成员函数内

    场景：`length()`函数，当当前保存的距离是有效时，就直接输出该值，当该量无效时，就重新计算长度，并保存。而`length`是const函数，无法更改用于缓存长度的变量，此时需要声明该变量为`mutable`

    ```cpp
    mutable int a;
    ```

3. 常量性转移 casting away constness
    1. `static_cast<const Text>`转型成const对象，然后调用const的[]操作
    2. `const_cast`将返回的const常量性消除
    ```cpp
    class Text {
        char * pText;
    public:
        const char & operator[](size_t pos)const{
            return pText[pos];
        }
        char & operator[](size_t pos){
            return const_cast<char &>(static_cast<const Text>(*this)[pos]);
        }
    };
    ```


## 构造/析构/赋值

1. 当想要default构造一个成员变量，值需要成员初值列指定空即可
    ```cpp
    A::A():val(){}
    //根据val里面的参数决定调用val的那个构造函数
    //无参数则调用默认构造函数（如果有）或无参的构造函数
    ```

2. 不同单元的non-local static对象的初始化并无明确定义。
    ```cpp
    //a.cpp
    A a;
    //b.cpp
    B b;
    ```
    若`B`构造函数内使用了`a`对象，当初始化`b`对象时，可能存在`a`对象尚未构件而出错

    解决办法：未每个non-local static对象搬到自己的专属函数内（该对象在此函数内被声明为static），这些函数返回一个reference指向它所含的对象。

    ```cpp
    A& a(){
        static A a;
        return a;
    }
    ```
    优点：
    1. 解决上述问题：当调用`a()`时，函数内的`a`一定会被初始化
    2. 如果从未调用`a()`，不会引发构造和析构成本

3. C++ 默默编写哪些调用函数
    特点：
    1. 当这些函数被调用的时候，它们才会被创建出来
    2. 当手动创建对应的函数，那么就不会有对应的默认创建操作。

    默认：
    1. 复制构造函数
    2. 赋值操作符
        当含有const成员或父类的赋值操作无法调用，则不会有该默认操作。
    3. 析构函数
    4. 默认构造函数

4. 可以把成员函数声明成`private`阻止别人调用
    但，这些函数还是可以被成员函数或者友元函数调用

    解决：可以只声明而不定义它，当这些函数被调用的时候，连接器就会产生错误。（因为没调用过，即使没定义也可以成功编译，因为连接时没用到。）

5. virtual 函数
    特点：
    1. 任何class只要带有virtual函数，几乎确定应该也有一个virtual的析构函数
    2. class不包含virtual函数，通常表示它不意图被用做一个base class
    3. 在base class构造期间，virtual函数不是virtual函数
        因此，不要在构造和析构过程中调用virtual函数
        原理：（derived 对象初始化时）在base class构造的期间，对象的类型是base class而不是derived class。

    实现：
    欲实现virtual函数，对象必须携带某些信息，主要用来在运行期决定哪个virtual函数该被调用，这份信息通常由一个vptr(virtual table pointer)指针指出。
    vptr指向一个由函数指针构成的数组，称为vtbl(virtual table)
    每一个带有virtual函数的class都有对应的vtbl
    当一个对象调用virtual函数，实际被调用的函数取决于该对象的vptr所指向的vtbl，**编译器** 在其中寻找适当的函数指针。

## 资源管理

1. `explicit` 修饰的构造函数
    显示构造，表示不允许经过构造函数进行隐式构造

2. 智能指针`auto_ptr`
    特点：
    1. `explicit`构造函数
    2. 析构函数自动调用其所指对象的 `delete`
        不会调用`delete[]`，因此对动态数组不能使用智能指针，因为 `vector` 和 `string` 几乎可以取代动态分配而得的数组。
    3. 复制构造或赋值操作后，原来的指针会指向 `null` ，而复制所得的指针将取得资源的唯一拥有权
        1. 避免多个智能指针指向同一对象而造成多次调用 `delete` （但多次同一个地址构造还是会存在问题呢）
        2. 想要保留原来的指针指向，用`std::tr1::shared_ptr`，引用计数型智慧指针，记录有多少个对象指向某资源，并在无人指向它时自动删除该资源。
