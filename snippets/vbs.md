1. 延时
    ```
    Wscript.Sleep 600000
    ```

2. 调用 cmd 文件（隐藏 cmd运行时候的黑窗口）
    ```
    Set ws = CreateObject("Wscript.Shell")
    ws.run "cmd /c unbound_cache -s",vbhide
    ```

3. 判断不能进程是否存在
    ```
    set y=getobject("winmgmts:\\.\root\cimv2")
    Set ws = CreateObject("Wscript.Shell")
    set x=y.execquery("select * from win32_process where name='unbound.exe'")
    for each i in x
         # 存在
         ws.run "cmd /c unbound_cache -s",vbhide
    next
    ```
