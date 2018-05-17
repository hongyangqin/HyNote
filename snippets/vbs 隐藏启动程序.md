# vbs 隐藏启动程序

使用vsb脚本隐藏启动程序，无任何弹窗显示， 完全后台

```vbs
' invisible.vbs 隐藏启动窗口
CreateObject("Wscript.Shell").Run """" & WScript.Arguments(0) & """", 0, False
```

调用vbs脚本启动被隐藏程序
```bat
wscript.exe "invisible.vbs" "start.bat"
```

## 参考

[windows - Run a batch file in a completely hidden way - Super User](https://superuser.com/questions/62525/run-a-batch-file-in-a-completely-hidden-way?answertab=active#tab-top)

**Solution 1:**

Save this one line of text as file `invisible.vbs`:

> CreateObject("Wscript.Shell").Run """"
> & WScript.Arguments(0) & """", 0,
> False

To run any program or batch file invisibly, use it like this:

> wscript.exe
> "C:\Wherever\invisible.vbs" "C:\Some
> Other Place\MyBatchFile.bat"

To also be able to pass-on/relay a list of arguments use only two double quotes
> CreateObject("Wscript.Shell").Run ""
> & WScript.Arguments(0) & "", 0,
> False

Example: `Invisible.vbs "Kill.vbs ME.exe"`

**Solution 2:**

Use a command line tool to silently launch a process : [Quiet][1], [hidecon][2] or [hideexec][3].


  [1]: http://www.joeware.net/freetools/tools/quiet/index.htm
  [2]: http://code.kliu.org/misc/hidecon/
  [3]: http://code.kliu.org/misc/hideexec/
