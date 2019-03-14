# java提高（15）---java深浅拷贝 - 雨点的名字 - 博客园

> 为什么会有深浅拷贝这个概念? 我觉得主要跟JVM内存分配有关,对于基本数据类型,只存在栈内存,所以它的拷贝不存在深浅拷贝这个概念。而对于对象而言,一个对象的创建会在内存中分配两块空间,一个在栈内存存对象的引用指针,一个在堆内存存放对象。这个时候会有一个问题，你拷贝的只是这个引用指针还是拷贝两块内存一起拷贝,这个时候就会有深浅拷贝一说。

> 基本数据类型的特点：直接存储在栈(stack)中的数据. 引用数据类型的特点：在栈内存存储对象引用，真实的数据存放在堆内存里 引用数据类型在栈中存储了指针，该指针指向堆中该实体的起始地址。当解释器寻找引用值时，会首先检索其在栈中的地址，取得地址后从堆中获得实体。

> 在 Java 中，除了基本数据类型（元类型）之外，还存在 类的实例对象 这个引用数据类型。而一般使用 =号做赋值操作的时候。对于基本数据类型，实际上是拷贝的它的值，但是对于对象而言，其实赋值的只是这个对象的引用，将原对象的引用传递过去，他们实际上还是指向的同一个对象

> 这里可以已经是两个不同的对象了。但是这里需要注意的是,如果对象中含有对象,这个对象还是浅拷贝。

> 弊端: 这里我们Person 类只有一个 Address 引用类型，而 Address 类没有，所以我们只用重写 Address 类的clone 方法，但是如果 Address 类也存在一个引用类型，
那么我们也要重写其clone 方法，这样下去，有多少个引用类型，我们就要重写多少次，如果存在很多引用类型，那么代码量显然会很大，所以这种方法不太合适。 所以还有另一种实现深拷贝方法。

>序列化实现深拷贝
```java
//序列化实现深拷贝
public Object deepClone() throws Exception{
    // 序列化
    ByteArrayOutputStream bos = new ByteArrayOutputStream();
    ObjectOutputStream oos = new ObjectOutputStream(bos);
    oos.writeObject(this);
    // 反序列化
    ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
    ObjectInputStream ois = new ObjectInputStream(bis);
    return ois.readObject();
}
　//因为序列化产生的是两个完全独立的对象，所有无论嵌套多少个引用类型，序列化都是能实现深拷贝的。
```

实现`clone`进行深度拷贝，若对象存在多个引用类型时不合适，一个解决办法是序列化实现深度拷贝

---

- [java提高（15）---java深浅拷贝 - 雨点的名字 - 博客园](http://www.cnblogs.com/qdhxhz/p/10527245.html)
