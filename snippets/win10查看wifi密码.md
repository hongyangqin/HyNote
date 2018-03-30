# win10查看wifi密码

以管理员身份运行以下命令:

```batch
netsh wlan show profiles % 查看已经保存的wifi名字
netsh wlan show profile name=“连接名” key=clear % 查看某个wifi的密码
netsh wlan show profile * key=clear % 查看所有的wifi密码
```

查看wifi信息

```batch
C:\WINDOWS\system32>netsh wlan show profiles

接口 WLAN 上的配置文件:


组策略配置文件(只读)
---------------------------------
    <无>

用户配置文件
-------------
    所有用户配置文件 : TP-LINK
    所有用户配置文件 : TP-LINK_******
```

查看密码

```batch
C:\WINDOWS\system32>netsh wlan show profile name="TP-LINK" key=clear
...
安全设置
-----------------
    身份验证         : 开放式
    密码                 : 无
    安全密钥               : 不存在
    密钥索引               : 1
...
```

## 参考

[Win10查看已存储WiFi密码的两种方法-系统之家](http://www.xitongzhijia.net/xtjc/20160422/70975.html)