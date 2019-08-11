# powershellTocmd

## 改变开始菜单右键powershell为cmd

所有设置->个性化->任务栏->取消`当我右键点击"开始"或按下Windows键+x时, 在菜单中将命令行提示符替换为Windos PowerShell`

## shift + 右键 在此处PowerShell窗口

方向: 改注册表`计算机\HKEY_CLASSES_ROOT\Directory\Background\shell\cmd`

修改方式:
1. 显示: `HideBasedOnVelocityId` 改为 `ShowBasedOnVelocityId`
2. 隐藏: `ShowBasedOnVelocityId` 改为 `HideBasedOnVelocityId`

注册表表导出信息:
```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\cmd]
@="@shell32.dll,-8506"
"Extended"=""
"NoWorkingDirectory"=""
"ShowBasedOnVelocityId"=dword:00639bc8

[HKEY_CLASSES_ROOT\Directory\Background\shell\cmd\command]
@="cmd.exe /s /k pushd \"%V\""
```

备注: 

1. 改注册表时会出现`注册表编辑器无法重命名`的错误 -> 修改注册表项`cmd`的权限为完全控制 -> 提示无法保存对xxx权限的更改 -> 修改拥有者为自己(在注册表的shell选项右键 -> 权限 -> 高级 -> 所有者-更改 -> 高级 -> 立即查找 -> 选择自己用户(管理员也可以选择`Administrator`) -> 确定 -> 勾选`替换子容器和对象的所有者` -> 确定 -> `Administrators`的权限为完全控制 -> 修改完后恢复)
2. 带有`"Extended"=""`的是shift+右键的
3. 要以管理权限方式运行, 就把`cmd`名字改成`runas`
4. `默认` 或者 导出信息中的`@="@shell32.dll,-8506"`表示所显示的字符串
    ```
    @shell32.dll,-8506 -> 在此处打开命令窗口(W)
    @shell32.dll,-8508 -> 在此处打开PowerShell窗口(S)
    @shell32.dll,-8509 -> 以管理员身份运行(A)
    @shell32.dll,-50944 -> 以其他用户身份运行(F)
    ```

## 点击文件夹打开命令行

`计算机\HKEY_CLASSES_ROOT\Directory\shell`

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\cmd]
@="@shell32.dll,-8506"
"Extended"=""
"NoWorkingDirectory"=""
"ShowBasedOnVelocityId"=dword:00639bc8

[HKEY_CLASSES_ROOT\Directory\shell\cmd\command]
@="cmd.exe /s /k pushd \"%V\""
```

## 磁盘

`计算机\HKEY_CLASSES_ROOT\Drive\shell\runas`

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Drive\shell\runas]
@="在此处打开命令窗口-管理员"
"Extended"=""
"NoWorkingDirectory"=""
"ShowBasedOnVelocityId"=dword:00639bc8

[HKEY_CLASSES_ROOT\Drive\shell\runas\command]
@="cmd.exe /s /k pushd \"%V\""
```

## 参考

[https://www.jianshu.com/p/a734f1489772](https://www.jianshu.com/p/a734f1489772)