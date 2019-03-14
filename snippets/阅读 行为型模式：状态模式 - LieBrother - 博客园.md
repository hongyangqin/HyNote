# 行为型模式：状态模式 - LieBrother - 博客园

行为型模式：状态模式

```java
public void register() {
    if ("none".equals(state)) {
        System.out.println("游客。注册中。。。");
    }else if ("register".equals(state)) {
        System.out.println("注册用户。不需要再注册。");
    } else if ("apply".equals(state)) {
        System.out.println("授信用户。不需要再注册。");
    } else if ("draw".equals(state)) {
        System.out.println("借款用户。不需要再注册。");
    }
}
```

> 上面代码实现了用户 register (注册)，apply (授信)，draw (借款) 这 3 种行为，每个行为都会根据状态 state 来做权限控制。看起来有点繁琐，扩展性不高，假设新增了一个状态，那么注册、授信、借款这 3 种行为的代码都要修改。下面通过状态模式来解决这个问题。

```java
/**
 * 借款状态
 */
class DrawState implements State {

    @Override
    public void register() {
        System.out.println("借款用户。不需要再注册。");
    }

    @Override
    public void apply() {
        System.out.println("借款用户。不需要再授信。");
    }

    @Override
    public void draw(double money) {
        System.out.println("申请借款【" + money + "】元。申请借款中。。。");
    }
}

class User1 {
    private State state;

    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
    }

    public void register() {
        this.state.register();
    }

    public void apply() {
        this.state.apply();
    }

    public void draw(double money) {
        this.state.draw(money);
    }
}
```

> 我们把状态给抽出来，作为一个接口，因为在每种状态中都可能有注册、授信、借款行为，所以把这 3 个行为作为状态接口的方法，让每个状态子类都实现相应的行为控制。如下代码所示。

> 看上面代码，我们抽象了 State 接口，4 种状态分别用 NoneState (游客)、RegisterState (注册)、ApplyState (授信)、DrawState (借款) 表示。而每个状态都有 3 种行为，它们各自对这些行为进行权限控制。这样子实现可以让权限逻辑分离开，分散到每个状态里面去，如果以后要业务扩展，要新增状态，那就很方便了，只需要再实现一个状态类就可以，不会影响到其他代码。
> 这也是为什么《阿里巴巴 Java 开发手册》里面讲的，当超过 3 层的 if-else 的逻辑判断代码，推荐用状态模式来重构代码。

> 状态模式 很好的减低了代码的复杂性，从而提高了系统的可维护性。在业务开发中可以尝试使用，比如在迭代开发中，业务逻辑越来越复杂，从而不得不使用很多 if-else 语句来实现时，就可以考虑一下是不是可以用 状态模式 来重构，特别是一些有状态流程转换方面的业务。看到这篇文章，想想工作中是不是有些复杂的代码可以重构，赶紧行动起来。

使用大量的if-else来进行状态的判断，不容易维护，把状态的动作交由状态去实现可维护性更好。

---

## 参考

- [行为型模式：状态模式 - LieBrother - 博客园](http://www.cnblogs.com/liebrother/p/10527850.html)
