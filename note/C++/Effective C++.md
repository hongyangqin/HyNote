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

3. 以独立的语句将 newed 对象存储于智能指针内，因为
    ```cpp
    process(std::tr1::shared_ptr<A>(new A), prority());
    ```
    上述语句中，C++的参数运算的顺序是不确定的（编译器相关）
    可能是
    ```cpp
    new A
    prority
    shared_ptr<A>
    ```
    当`prority`异常时，那么前面`new A`返回的指针将会遗失，引发资源泄露。
    因此，建议
    ```cpp
    std::tr1::shared_ptr<A> pw(new A);
    process(pw, prority());
    ```

## 设计与声明

1. 将成员变量声明为 `private`

    1. `public`接口内声明的东西都是函数，用户就不需要再打算访问类成员时迷惑地试着记住是否使用小括号
    2. 封装
        如果通过函数访问成员变量，日后可改某个计算替换在这个成员变量，而类客户一点也不知道类的内部实现已经改变。
        否则，当 `public` 或者 `protected` 的成员改变时， 所有使用它们的客户代码(`public`)，子类成员(`protected`)均受到影响。

2. 命名空间的作用
    1. 封装
        有序组织同类或相关代码
    2. 跨文件，使用时只包含所需，只与使用部分形成编译依赖
    3. 易于扩展，同命名空间下新建头文件即可

3. 全特化 `swap`

    ```cpp
    namespace std{
        template<>
        void swap<ClassA>(ClassA &a, ClassA &b){
            a.swap(b);
        }
    }
    ```
    - 当 `std:swap` 对自定义的类型效率不高时，提供一个 `swap` 成员函数，并确定这个函数不抛出异常

## 实现

1. 新式转型
    - `const_cats<T>( expression )`
        通常被用来将对象的 **常量性转除**
    - `dynamic_cast<T>( expression )`
        主要用来执行 **安全向下转型** , 用来决定某对象是否归属继承体系中的某个类型.
        它是唯一无法由旧式语法执行的动作, 也是唯一可能消耗重大运行成本的转型动作.
    - `reinterpret_cast<T>( expression )`
        意图执行低级转型, 实际动作可能取决于编译器, 这也就表示它不可移植.

    - `static_cast<T>( expression )`
        强制隐式转换

2. 单一对象可能拥有一个以上的地址
    比如: 以 `Base*` 指向它时的地址 和 以 `Derived*` 指向它时的地址
    一个情况: 使用多重继承
    因此, 应该避免做出 "对象在 C++ 中如何分布" 的假设

3. `inline`: 对函数的每一个调用 都以函数本体替换之
    特点:
    - 过度的 `inlining` 会导致程序体积太大
        即使有虚拟内存, `inline` 造成的打码膨胀亦会导致额外的幻夜行为, 降低告诉缓存装置的命中率, 以及伴随这些而来的效率损失
    - 换个角度, 如果 `inline` 函数的本体很小, 编译器将针对 "函数本体" 所阐述的码可能比针对 "函数调用" 所产生的码更小
        若如此, 将函数 `inlining` 确实可能导致较小的目标码和较高的指令高速缓存装置命中率
    - 所有 `virtual` 函数的调用都会使得 `inlining`落空
        `virtual` 意味着 等待, 直到运行期才确定调用那个函数
        `inline` 意味着 执行前, 先将调用动作替换为被调用函数的本体

    分类:
    - 隐喻 `inline`: 将函数定义于 `class` 内 ( 成员函数 或 友元函数 )
        注: 在类内声明, 而定义在类外的, 不是 `inline`
    - 显式 `inline`: 在函数 **定义式** 前加上 `inline` 关键字

    例子:
    ```cpp
    class Base{
    public:
        ...
    private:
        std::string bm1, bm2;
    };

    class Derived: public Base{
    public:
        Derived(){}         //Derived 构造函数虽然看起来是空的, 并不一定是空的
    private:
        std::string dm1, dm2;
    }
    ```
    `Derived` 构造函数虽然看起来是空的, 并不一定是空的, 析构函数同理
    原因: 程序中一定有某些代码让某些事情发生(构造), 这些代码由编译器于编译期间代为产生并安插到程序中的代码, 肯定存在于某个地方, 有时候就放在构造函数和析构函数中
    ```cpp
    //`Derived`  构造函数可能产生的代码
    Derived::Derived(){
        Base::Base();                   //构造 Base 成分
        try{
            dm1.std::string::string();  //构造 dm1
        }catch(...){
            Base::~Base();              //销毁 Base 成分
            throw;
        }
        try{
            dm2.std::string::string();
        }catch(...){
            dm1.std::string::~string(); //销毁dm1
            Base::~Base();
            throw;
        }
    }
    ```


    使用 `inline` 需要考虑的问题:
    - `inline` 函数无法随着程序库的升级而升级
        如果 函数 `f` 是 `inline` 函数, 一旦程序设计者改变 `f`, 所有用到 `f` 的客户端程序都必须重新编译
        若 `f` 是 `non-inline` 函数, 一旦它有任何修改, 客户端只需要重新连接就好, 远比重新编译的负担少很多, 如果程序采用动态连接, 升级版函数甚至可以不知不觉地被应用程序吸纳

    - 大部分调试器对 `inline` 束手无策, 仅仅只能 在调试版程序中 **禁止发生** `inlining`

4. 将文件间的编译依存关系降至最低
    原因: 如果一个头文件有任何改变, 或头文件所依赖的其他头文件有任何改变, 那么每个包含该头文件的文件就得需要重新编译
    解决: 接口与实现分离
    具体实现:
    - `handle` class: 使用一个 `实现类` 作为 该类的成员函数
        ```cpp
        //Person.h
        class Person{
        public:
        ...
            std::string name() const;
        private:
            std::tr1::shared_ptr<PersonImpl> pImpl; //指针, 指向实现物
        }
        //Person.cpp
        std::string Person::name() const{
            return pImpl->name();   //调用具体实现
        }
        ```
        每一次访问会增加一层间接访问, 而每个对象消耗的内存数量必须增加

    - `interface` class: 使用抽象类
        ```cpp
        //Person.h
        class Person{
        public:
        ...
            virtual std::string name() const = 0;
        }
        ```
        除非 `interface class` 的接口被修改, 否则其客户不需要重新编译
        必须为每次函数调用付出一个间接跳跃成本(`virtual`)

## 继承与面向对象设计

1. `public` 继承
    表示 `is-a` 的关系, 基类能做的事情, 子类都能够做到

2. 避免遮掩继承而来的名称
    当子类存在一个和父类相同名字函数, 就会遮掩父类的所有同名的函数(包括函数的重载形式)

    想要使用继承来的名字, 在子类中使用 `using` 关键字, 告诉编译器要使用父类的函数
    ```cpp
    class Derived: public Base{
    public:
        using Base::mf1;    //当Base的mf1在Derived中可见, 且都为public
    }
    ```
    - `Base::mf1` 在子类中都可见
        若不想继承弗雷德所有函数, 应该采用 `private` 继承
    - `Base::mf1` 的访问权限被指定为 `public`
    - 当子类的 `mf1` 和父类的有相同的参数, 调用的是子类的 `mf1`

3. 区分接口继承与实现继承
    采用实现继承(为非纯 虚函数指定函数声明和函数缺省行为), 可能存在 子类未明白说出"继承"的情况下, 就继承了父类(接口)的缺省行为实现.

    一个解决的办法是: 以不同的函数分别提供接口和缺省实现(这不是最好的, 比较好的是为纯虚函数提供定义), 但这可能因过度雷同的名称而引起类命名空间污染问题
    ```cpp
    class Airplane{
    public:
        virtual void fly(...) = 0;
    protected:
        void defaultFly(...);
    };
    void Airplane::defaultFly(...){
        ...
    }
    ```

    更好的解决办法是: 为纯虚函数提供定义, 这个定义不会被继承, 只能通过指定类名的方式访问
    ```cpp
    Airplane::fly(...)
    ```
    前一个例子调用 `defaultFly` 的地方都替换成 `Airplane::fly`, 避免类命名空间污染的问题

4. 考虑 `virtual` 函数意外的其他选择
    1. non-virtual interface (NVI)手法 (模板设计模式)
        令客户通过 `public non-virtual` 成员函数间接调用 `private virtual` 函数, 允许子类重新定义 `virtual` 函数, 从而赋予它们 **如何实现机能** 的控制能力, 但基类保留诉说 **函数何时被调用** 的权利.

    2. 策略(Strategy)模式
        NVI手法对于所有的子类对象, 都只能同样的行为, 但如果希望(同一个子类)不同的对象, 有不同的行为呢?
        解决办法: 策略模式, 由某个变量确定某个行为

        1. 由 函数指针 实现
            使用一个函数指针, 指明需要的行为
            该办法还可以在 `运行期` 进行行为的变更

            运用函数指针替代 `virtual` 函数, 其优点是否足以弥补缺点, 需要根据每个设计情况的不同而抉择.

        2. 由 `tr1::function` 实现 策略模式
            使用函数指针还是有一定的约束的, 比如必须是函数, 而不能是函数对象(实现 `operator()`), 也不能是成员函数, 也不能是可以隐式转换成对应返回值的函数(比如返回值是 `int` 的话, 返回值是 `double`也是不被允许的).

            这些问题, 采用 `tr1::function` 对象 替换 函数指针即可解决.
            `tr1::function`接收任何可调用(`callable`)对象
            > 注: 从`C++11`起, 为`std::function`, 在`<functional>`有文件里

            声明:
            ```cpp
            #include<functional>
            typedef std::function<int(const int &a)> Func;
            ```

        3. 古典 策略模式
            将虚函数替换成另一个继承体系内的虚函数
            即创建一个策略基类, 派生不同的策略子类

5. 绝不冲定义继承而来的缺省参数值
    子类重写的时候, 虽然可以继续写成相同的缺省参数值, 但是, 这却导致了代码的重复, 代码重复又带来的相依性

    解决办法: 可采用 `NVI` 手法, 在 `public non-virtual` 函数里面指定缺省参数, 来调用 不带缺省参数的 `private virutal`函数

    虚函数是动态绑定的，但缺省参数是静态绑定的。所以当父类指针指向子类对象，调用虚函数时，虚函数的默认参数由父类的定义决定。
    ```cpp
    #include<iostream>
    using namespace std;

    class Base {
    public:
        virtual void func1(int num = 1) {
            cout <<"Base:func1:"<< num << endl;
        }

        void func2() {
            cout << "Base:func2" << endl;
        }
    };

    class Derive : public Base{
    public:
        void func1(int num = 2) {
            cout << "Derive:func1:" << num << endl;
        }

        void func2() {
            cout << "Derive:func2" << endl;
        }
    };
    int main() {
        Base * pbase = (Base*)new Derive();
        Derive * pderive = (Derive *)pbase;
        pbase->func1();     //Derive:func1:1, 子类的函数, 但参数值来自父类
        pderive->func1();   //Derive:func1:2
        pbase->func2();     //Base:func2
        pderive->func2();   //Derive:func2
        return 0;
    }
    ```

6. `private` 继承
    - 特点
        如果类之间的继承关系是 `private`, 编译器不会自动将一个子类对象转换成基类对象

        因为子类对象继承来的所有成员, 在子类中都会变成 `private`, 因此, 能访问父类共有成员(函数)的方法, 却不能访问子类.

        具体而言: 当参数是父类, 如果子类是 `private` 继承, 那么不能传入子类对象作为参数

        `private` 继承纯粹只是实现技术, 在软件设计层面没有意义. 即子类采用父类的某个实现.

    - 与 `复合` 的关系(类的成员为 "前文`private`继承的父类" 的对象)
        两者都能实现相同的功能(利用父类/复合对象的实现, 去实现类的功能)

        取舍: 尽可能使用 `复合`, 当涉及 `protected`成员或 `虚函数`, 或 对 **空间要求** 十分激进时, 才使用 `private` 继承

        1. 涉及 `protected`成员 或 `虚函数`
            需要重写某个虚函数, 如果只是定义为成员变量, 并不能改变这个成员变量的函数的定义, 因此采用继承, 然后重写

            或需要访问 该类的`protected`成员, 类外无法访问, 需要继承才能访问

            但此方法, 也可以使用 "派生一个重写虚函数/重定义成员为public后的类" 定义为成员变量 的方法代替

        2. 涉及 `空间`, `private` 继承占更少的空间
            C++ 裁定凡是独立(非附属)对象都必须有非零大小
            因此, 对于一个空类的对象, 其大小不为0, 即使它什么都不包含

            先看复合的情况: 定义一个空类, 和一个只有 `int`成员的类
            ```cpp
            class Empty {};
            class HoldsAnInt {
            private:
                int x;
                Empty e;
            };
            ```
            看各个类的大小:
            ```cpp
            cout << sizeof(HoldsAnInt) << endl;	//8
            cout << sizeof(int) << endl;		//4
            cout << sizeof(Empty) << endl;		//1
            ```
            1. `sizeof(HoldsAnInt) != sizeof(int)` 和 `sizeof(Empty)`
                这个现象, 说明了 `Empty` 类即使没有任何成员变量, 也是占空间的
            2. `sizeof(HoldsAnInt) - sizeof(int) != sizeof(Empty)`
                这个现象说明了, 编译器会对位对齐进行优化

            在看 `private` 继承的情况:
            ```cpp
            class HoldsAnInt : private Empty{
            private:
                int x;
            };
            ```
            大小为:
            ```cpp
            cout << sizeof(HoldsAnInt) << endl;	//4
            cout << sizeof(int) << endl;		//4
            cout << sizeof(Empty) << endl;		//1
            ```
            可以看出, `private` 继承下, `Empty`类不占任何空间, 称 `EBO`(empty base optimization: 空白基类最优化)

            (用处)问:`Empty` 类什么都没有, 要来有什么用呢?
            `Empty`并不是`empty`, 它从未拥有 `non-static` 成员, 却可以含有 `typedefs`, `enums`, `static`成员变量 或 `non-virtual`函数.
            这样的继承很少增加子类的大小, 也就是说, 继承了遗产, 却不占空间.

7. 谨慎使用多重继承
    1. 当多个父类出现多个同名函数(参数相同)是怎么办?
        明确指数使用哪个基类的函数
        ```
        a.BaseOne::func();
        ```

    2. 虚继承(钻石型多重继承)
        当出现父类们的父类相同的情况, C++默认情况下, 执行赋值操作, 即有多个父类的父类的成分, 即使这个类相同

        如果希望只有一个这样的成分(共享同一个父类的父类), 则父类们需声明为 `虚继承`

        ```cpp
        class File{...};
        class InputFile: virtual public File{...};
        class OutputFile: virtual public File{...};
        class IOFile: public InputFile, public OutputFile{...};
        ```

        但是, 为了避免继承得来的成员变量重复, 即使用虚继承的类所产生的对象, 往往比 非虚-继承的大, 访问虚基类的成员变量时, 也比访问 非虚基类的成员变量慢

## 模板与泛型编程

1. 模板板元编程: template metaprogramming
    在C++编译器内执行并于编译完成时停止执行 的程序

2. 隐式接口 与 编译期多态
    隐式接口: 当使用模板时, 模板 `T` 所用过的操作, 为 `T` 必须满足的条件, 这些条件就是 隐式接口

    编译期多态: 以不同的模板参数具现化, 会导致调用不同的函数, 这就是编译期多态

3. `typename` 和 `class`
    在 **声明模板参数** 时, 不论使用关键字 `typename` 还是`class`意义完全相同
    ```cpp
    template<class T> class A;
    template<typename T> class A;
    ```

    使用 `typename`的时机:
    缺省情况下, 嵌套从属名称(`::`)不是类型, 如果指的是类型, 则必须在它前面放上关键字 `typename`(有2个例外情况, 在基类列表和初值列表前不需要加 `typename`)

    给定以下代码:
    ```cpp
    template<typename C>
    void print2nd(const C& container){
        C::const_iterator* x;
        ...
    }
    ```
    此处, `C::const_iterator`默认不是类型, 而是变量, 因此, 上式的含义是 `C::const_iterator` 乘(`*`)上 `x`.

    如果需要指明 `C::const_iterator` 是类型 而不是变量, 则
    ```cpp
    typename C::const_iterator* x;
    ```

    例外情况: 基类列表和初值列表
    ```cpp
    template<typename T>:
        public Base<T>::Nested{ //不需要 typename
            explicit Derived(int x):
                Base<T>::Nested(x){} //不需要 typename
    }
    ```

4. 处理基类模板内的名称
    基类模板可能会被特化, 而特化的版本可能并不提供与基类模板相同的接口, 因此, 编译器不会再基类模板内寻找继承而来的名称(即, 派生类里面不能使用基类的方法)

    解决办法: 告诉编译器, 假设方法会被继承
    1. 在基类函数调用动作之前加 `this->`
        即在 子类中调用父类的方法的形式如下:
        ```cpp
        this->baseFunc(); //假设baseFunc将被继承
        ```

    2. 使用 `using` 声明式
        ```cpp
        using Bast<T>::baseFunc;    //告诉编译器, baseFunc位于Base里
        ```

    3. 指明被调用函数在基类内
        ```cpp
        Base<T>::baseFunc();    //调用基类的方法与实现
        ```
        此方式会关闭 `virtual` 的绑定行为, 使用调用父类的实现

5. 将与参数无关的代码抽离 `templates`
    使用 `templates` 可能会导致代码膨胀, 其二进制码带着重复(几乎重复)的代码或数据.

    比如:
    1. 接收非类型参数
    ```cpp
    template<typename T, std::size_t n> ...
    ```

    2. `int` 和 `long` 虽然在某些平台有相同的二进制表述, 但可能导致代码膨胀, 即
    ```cpp
    template<T> class A;
    ```
    "`A<int>`和`A<long>`" 或 类似 "`A<vector<int>>`和`A<vector<long>>`" 都各自产生一份底层实现, 即使它们是一样的

6. 运用成员函数模板接收所有兼容类型
    同一个 `template`的不同具现体之间并不存在任何与生俱来的关系,如果我们希望他们之间有相互转换的能力, 需要明确地编写出来(比如不同类型的指针之间的转换).

    ```cpp
    template<typename T>
    class SmartPtr{
    public:
        template<typename U>
        SmartPtr(const SmartPtr<U>& pther):heldPtr(other.get()){...}
        T* get() const{ return heldPtr };
        ...
    private:
        T* heldPtr;
    }
    ```
    上面代码中, 初始化列表的含义是, 只有当 "存在某个隐式转换可将一个`U*`转换成一个`T*`指针" 时才能通过编译.

7. 需要类型转换时, 请为模板定义非成员函数
    template实参推导的过程中, 从不将隐式类型转换函数纳入考虑.
    即
    ```cpp
    template<typename T>
    const Rational<T> operator*(
        const Rational<T> lhs,
        const Rational<T> rhs
        ) {
        return Rational<T>(lhs.getnumerator() * lhs.getdenominator(), rhs.getnumerator()*rhs.getdenominator());
    }
    ```
    上述模板, 仅当`a * b`且`a`和`b`都是同一类`Rational<T>`对象时才会具现出具体的代码.
    `a*2`, 或者 `2*a` 都会导致编译错误(没有定义`*`运算符)
    即:
    ```cpp
    Rational<int> onehalf(1, 2);
    Rational<int> result = onehalf * 2;//编译错误
    ```

    解决此问题的办法是, 把`const Rational<T> operator*`作为友元函数放入类模板内:
    ```cpp
    class Rational {
    public:
        friend const Rational<T> operator*(
                const Rational<T> lhs,
                const Rational<T> rhs
            );	//只是声明是不行的
        ...
    };
    ```
    如此, 当对象`onehalf`被具现出来, 而作为过程的一部分, 友元函数`operator*`也被自动声明出来.

    **然而**, 这份代码虽然编译不会出错, 但是却无法连接, 因为函数被声明在`Rational<int>`, 却并没有被定义出来. 我们意图令类外的`operator*`模板提供定义式, 但是行不通.

    因此, 需要把定义也放入类内, 为减少inline所带来的影响(体积,代码重复), 调用一个外部函数, 代码如下:
    ```cpp
    template<typename T>
    class Rational {
    public:
        friend const Rational<T> operator*(
            const Rational<T> lhs, const Rational<T> rhs) {
            return domulti(lhs, rhs);   //友元定义, 调用外部函数
        }
        Rational(const T& _numerator = 0, const T& _denominator = 1):
            numerator(_numerator), denominator(_denominator){};
        const T getnumerator() const;
        const T getdenominator() const;
    private:
        T numerator;
        T denominator;
    };

    template<typename T>
    const Rational<T> domulti(
        const Rational<T> lhs, const Rational<T> rhs) {
        return Rational<T>(lhs.getnumerator() * lhs.getdenominator()
            , rhs.getnumerator()*rhs.getdenominator());
    }

    template<typename T>
    const T Rational<T>::getnumerator() const {
        return numerator;
    }

    template<typename T>
    const T Rational<T>::getdenominator() const {
        return denominator;
    }

    Rational<int> onehalf(1, 2);
    Rational<int> result = onehalf * 2;
    ```

8. 使用 `traits classes` 表现类型信息
    1. 原理
        模板具现出的不同类型, 在模板内均通过 `typedef` 定义出同名字的新类型 `type`, 如此, 均可以通过 `类型::type` 来获取类型信息
        比如: `list` 和 `vector` 均可以通过 `iterator_category` 判断迭代器类型

        比如:
        ```cpp
        template <typename T>
        class A {
        public:
            typedef T type;
        };

        template <typename T>
        class B {
        public:
            typedef T type;
        };
        ```
        这里仅判断具现模板时用的T相同, 就归为同类, 即`A<int>`与`B<int>`同类, 而和 `A<char>` 不同类

        使用 `typeid` 验证:
        ```cpp
        typeid(A<int>) == typeid(B<int>)   //0

        typeid(typename A<int>::type) ==
            typeid(typename B<int>::type)  //1

        typeid(typename A<int>::type) ==
            typeid(typename A<char>::type) //0

        typeid(typename A<int>::type) ==
            typeid(typename A<long>::type) //0

        typedef int newInt;
        typeid(typename A<int>::type) ==
            typeid(typename A<newInt>::type)) //1
        ```
        `A<int>`和`A<long>`不同而和`typedef`得到的`A<newInt>`相同, 也验证了前面的说法, "虽然 `int` 和 `long` 的底层实现可能一样, 但编译器把他们看做不同的类型"

    2. 原理实现
        1. 模板封装 `typeid`
            由于知道变量名而不知道其变量名, 因此, 需要使用函数模板封装, 通过函数调用的方式获取到变量类型

            例子1:
            ```cpp
            template<typename T, typename U>
            bool isSameType(T &a, U& b) {
                return std::type_index(typeid(typename T::type))
                    == std::type_index(typeid(typename U::type));
            }
            ```

            例子2:
            使用:
            ```cpp
            template<typename T>
            void doFunc(T &a) {
                if (std::type_index(typeid(typename T::type))
                    == std::type_index(typeid(int))) {
                    cout << "Int" << endl;
                }
                else cout << "Not Int" << endl;
            }

            A<int> typeInt1;
            B<int> typeInt2;
            A<char> typeChar;
            doFunc(typeInt1);//Int
            doFunc(typeInt2);//Int
            doFunc(typeChar);//Not Int
            ```

            但还是建议使用重载方式, 原因如下:
            1. 实际上, `T::type` 和 `U::type` 在编译的时候已经确定了, 为什么要在运行期才做这件事呢? 不仅浪费时间, 也造成可执行文件膨胀.
                > 为什么可执行文件会膨胀?
                > 验证结果如下, 的确如此
                > |类型|文件大小|占用空间|
                > |---|---------------|-------|
                > |typeid|11,776 Bytes|12,288 Bytes|
                > |重载|11,264 Bytes|12,288 Bytes|

            2. 其次, 上面代码中 `cout << "Int" << endl;` 对`int`和`char`而言都是一样的, 因此编译成功.
            但如果这一句代码是非`int`不能执行(不考虑类型转换), 那么就会导致错误, 因为类型`T`并没有 `if` 成立下所要求的隐式接口

        2. 利用重载
            通过传入 `type` 的变量, 来利用重载
            ```cpp
            template<typename T, typename U>
            void doFunc(T &a, U b) {
                cout << "Not Int" << endl;
            }

            template<typename T>
            void doFunc(T &a, int b) {
                cout << "Int" << endl;
            }

            template<typename T>
            void doFunc(T &a) {
                doFunc(a, T::type());
            }
            ```
            注意, 此处, `T::type()` 被定义成 `int`, 而实际我们并不关心它的值, 值关心它的类型, 因此, 如果不是 `int` 而是其他类, 若是值的占空间大就造成浪费.
            一般, 声明若干个空白类来定义`type`而不是采用`int`这些, 从而减少空间消耗.
            可以通过空白类的继承, 实现隐式转换, 比如 `Derived` 类可以调用所有参数类型为 `Base`的类

    3. `traits` 实现
        要求: 对内置类型和用户自定义类型的表现一样好, 即 `traits` 能施于内置指针上

        运作方式: 针对每一个类型`A`, 在 `traits<A>` 内声明某个 `typedef` 名为 `category`, 这个 `typedef` 来确认 `A` 的分类.

        > 疑问: 利用上面的特性已经可以实现类型信息的查看了, 为什么还需要整理成一个 `traits` 类模板? 这样可以使得获取类型信息就像调用函数一样?

        步骤:
        1. 若干个空白类, 空白类的继承关系, 表示实际类的继承关系
            ```cpp
            struct random_tag {};
            struct sequential_tag {};
            ```
        2. 为特定的类 `typedef` 类型
            ```cpp
            template <typename T>
            class List {
            public:
                typedef sequential_tag access_tag;
            };

            template <typename T>
            class Array {
            public:
                typedef random_tag access_tag;
            };
            ```
        3. 声明 `traits` 模板类整合所有类型
            ```cpp
            template<typename T>
            struct traits {
                typedef typename T::access_tag access_tag;
            };
            ```
        4. 指针类型下, 特例化 `traits` 模板
            因为指针的 `typedef` 不能嵌套, 这里直接把指针认定为 `random_tag`
            ```
            template<typename T>
            struct traits<T*> {
                typedef random_tag access_tag;
            };
            ```
        5. 使用:
            ```cpp
            template<typename T>
            void doFunc(T&a) {
                doFunc(a, traits<T>::access_tag());
            }

            template<typename T>
            void doFunc(T&a, random_tag) {	//省略第二个参数的变量名
                cout << "random access" << endl;
            }

            template<typename T>
            void doFunc(T&a, sequential_tag) {
                cout << "sequential access" << endl;
            }

            List<int> list;
            Array<double> arr;
            doFunc(list);		//sequential access
            doFunc(arr);		//random access
            ```

    4. STL中的 `traits`
        `is_fundamental<T>`, `is_array<T>`, `is_base_of<T1, T2>`

9. `template` 元编程(TMP: Template metaprograms)

好处:
1. 它让某些事情变得更加容易, 如果没有它,那些事情将是困难的, 甚至不可能的
2. 由于TMP执行与C++编译期, 因此可将工作从运行期转移到编译器
    这导致的一个结果是, 某些错误原本通常在运行期才能侦测到, 现在可以在编译器找出来
    另一个结果是, 使用TMP的C++代码可能在每一方面都更加高效: 较小的可执行文件, 较短的运行期, 较少的内存要求
    然而, 将工作从运行期转移至编译器的另一个结果是, 编译时间变长了.

    运行高效:
    1. `traits` 引发编译期发生与类型身上的 if-else 计算
    2. 可以预计算出所需要的结果, 从而减少运行期的时间
        比如,阶乘
        ```cpp
        template<unsigned n>
        struct Factorial{
            enum { Value = n * Factorial<n - 1>::Value };
        };

        template<>
        struct Factorial<0> {
            enum { Value = 1 };
        };

        cout << Factorial<5>::Value << endl;	//120
        cout << Factorial<10>::Value << endl;	//3628800
        ```

        反汇编查看, 结果是已经计算出来的: `0x78=120, 0x375F00=3628800`
        ```
        011A100B  |.  6A 78         push    78
        011A100D  |.  FF15 44201A01 call    dword ptr [<&MSVCP140.std::basic>;  MSVCP140.std::basic_ostream<char,std::char_traits<char> >::operator<<

        011A1026  |.  68 005F3700   push    375F00
        011A102B  |.  FF15 44201A01 call    dword ptr [<&MSVCP140.std::basic>;  MSVCP140.std::basic_ostream<char,std::char_traits<char> >::operator<<
        ```
