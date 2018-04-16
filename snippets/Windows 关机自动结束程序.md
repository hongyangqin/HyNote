# Windows 关机自动结束程序

![](assets/Windowsguanjizidongjieshuchengxu/2018-04-16-22-59-18.png)

修改一下注册表项:

```
Windows Registry Editor Version 5.00

[HKEY_USERS\.DEFAULT\Control Panel\Desktop]
"AutoEndTasks"="1"
```

## 参考

* [关机总有程序在捣乱 秒杀的方法学下吧](https://mp.weixin.qq.com/s/_TD4sKBV5_vk4VQ8tIjYiA)