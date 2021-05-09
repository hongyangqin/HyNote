# 常规套路

设置参数的手段:
1. 导出为公共字段
    ```
    type A struct {
        Field int
    }
    ```
    直接赋值A.Field即可
    不足: 
    1. 使用不方便: 在使用字段前, 需要验证字段是否合法 (是否有效, 是否使用默认值)
        ```
        if A.Field 未设置 {
            设置A.Field默认值(或初始化一个合法对象)
        }
        if A.Field 不合法 {
            中断
        }

        //此时才正常使用A
        ```
    2. 使用不便+1: 字段的类型的零值无法用于区分是否设置时, 需要使用字段的指针类型来加一区分(int -> int*), 并且设置该值时需要创建一个变量(`A.Filed=&3`这句是非法的)
        ```
        type A struct {
            Field *int
        }

        a := 3      //需要创造一个变量用于获取指针
        A.Field=&a  //这不可以通过set方法绕过
        ```
2. 使用Config结构体
    使用方法本质上和1是一样的, 所以遇到的问题也和1一样
3. 使用set方法
    1. 有一些对象的字段希望只在生成的时候配置一次，之后就不能再修改了。这个时候用 Set 就不能很好地保证这一点。
        这个其实可以通过error等报错, 但增加一次方法调用也使得代码逻辑更加复杂啰嗦
        ```
        if err:=s.SetA(a); err != nil {
            //process err
        }
        ```
    2. 有时候我们希望我们提供出去的库的功能是以 interface 来表示的，这样可以更容易地将实现替换掉。在这种情况下使用 Set 模式会大大增加 interface 的方法数量，从而增加替换实现的成本。
        每新增一个字段, 就得在接口所有实现增加对应字段的set方法的实现, 即使该字段只是在某个实现下使用
        ```
        type A interface {
            FuncA error
            SetA error
            SetB error
            ...
        }
        ```


主要看参数的设置, 默认值的设置与区分, 增加参数时的改动


1. 需要知道是否有设置值()否则使用默认值(初始化出合法对象))
    思路1: 如果创建对象时就设置好默认值, 则不需要区分是否已经设置默认值
        如果设置默认值的开销很大, 希望在需要的时候才设置默认值, 则不可走这条路
    思路2: 如果创建对象时未设置默认值, 则需要判断默认值是否设置
        零值无法区分是否设置的状态时, 一般用指针代替(比如`int` -> `int8`)        
2. 每次使用前都需要判断参数的合法性
    思路1: 直接把设置默认值, 判断合法性的都做都放在创建的时候进行, 之后的逻辑都基于参数必定合法有效的状态进行即可
3. 每次增加字段都要增加接口的方法?
    字段应该放在具体的实现里边, 不应该体现在接口上, 所以不推荐这种用法
4. 新增字段的时候尽可能少改动已存在的代码? 
    新增字段必须动作(设置字段的默认值和验证字段的合法性) 应该尽可能放在已有代码之外

# options

```
type MyDialer struct {
	Dialer *net.Dialer
	Timeout time.Duration
	Retry int   //1. 增加字段的定义
}

//2. 增加新字段的options
type retryOpt struct {
	retry int
}

func (o *retryOpt) apply(d *myDialer) {
	d.retry = o.retry
}

func RetryOption(r int) Option {
	return &retryOpt{retry:r}
}

func NewMyDialer(opts ...Option) MyDialer {
	d := &myDialer{
		timeout: time.Second,
		retry: 2,       //2. 设置新增字段默认值
	}
	for _, opt := range opts {
		opt.apply(d)    //3. 通用的修改成用户的值
	}

	if d.dialer == nil {  //跳过非必要的默认对象的构造
		d.dialer = &net.Dialer{}
	}
	return d
}
d := NewMyDialer(RetryOption(5), TimeoutOption(time.Minute), DialerOption(&net.Dialer{
	KeepAlive: 3*time.Second,
})
```

~~但这种方式也有个问题: 每个参数都是独立的option对象, 不同对象的不同配置需要通过flag配置, 则会显得很分散~~
~~(此时用导出字段或Config结构的方式反而更合适)~~

option可以包含不同的字段, 但是含有apply方法的对象可以分别定义

<!-- # 使用Config结构

```
func NewClient(opts ...*options.ClientOptions) (*Client, error) {
    clientOpt := options.MergeClientOptions(opts...)    //合并不同的配置

    client := &Client{}
    client.configure(clientOpt) //让配置生效

    if client.deployment == nil {
        //new deployment
    }

    return client, err
}
``` -->

# 小结

1. 通过定义opts类的方式来扩展函数的参数的数目而不改变函数本身 (用于应对后续函数的参数增加的情况)
2. 尽量用同一段代码解决重复调用的问题, 避免在多处调用(比如opt.apply方法, 比如 多个配置的验证, 配置的修改等)

# 参考资料

https://xie.infoq.cn/article/ce2a09da86ea17b0d573756a9?utm_source=rss&utm_medium=article
https://github.com/uber-go/guide/blob/master/style.md#functional-options
https://kingsamchen.github.io/2020/06/30/golang-options-pattern/
mongo/writeconcern/writeconcern.go 
go.mongodb.org/mongo-driver@v1.3.2/mongo/client.go
https://github.com/grpc/grpc-go/blob/91d8f0c916d76f2a5aac9e846cd7ffcb838db769/clientconn.go#L104