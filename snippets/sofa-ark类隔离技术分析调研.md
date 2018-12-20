# sofa-ark类隔离技术分析调研

怎么我的classpath里的某个包有三四个不同的版本啊，跑的时候到底用的是哪个版本啊？

1. OSGI技术
    使用OSGI技术，用felix、karaf或者Jigsaw这样的容器对jar包进行暴露和隔离。
    而且对于OSGI容器自身就是一个守护进程，他的使用、管理和维护都会有额外的代价。

2. Gradle5.0特性
    使用”java-library”插件之后，”compile”可以被”implementation”和”api”替代。对于组件本身来说，通过”api”或”implementation”引入的包都会被添加到classpath中。而”api”和”implementation”的唯一区别就是，在组件接入方的classpath中(实际上是compileClasspath)，将只会出现通过”api”引入的包，而不会出现通过”implementation”引入的包。

    其实”java-library”做的事情很简单，就是在将jar包上传maven仓库时修改了pom.xml文件中各个依赖包的scope。对于通过”api”引入的依赖来说，scope就是compile；而对于通过”implementation”引入的依赖来说，他的scope就变成了runtime。

    gradle5.0的这个功能对于解决依赖冲突这个问题来说，实在是有点饮鸩止渴，他实际上是将编译期的依赖冲突暂时隐藏了起来，等到运行时再暴露出来。

3. Sofa-ark项目
    sofa-ark项目从概念上其实并没有什么石破天惊的独创，可以说他就是用FatJar技术去实现OSGI的功能。

Sofa-ark项目

...

- [sofa-ark类隔离技术分析调研 | Myths的个人博客][1]

[1]: https://blog.mythsman.com/2018/12/09/1/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
