常用批处理命令.md

1. 获取当前目录，获取脚本所在的目录
	```
	%cd%
	%~dp0
	cd /d %~dp0
	```

2. 获取系统启动目录
	```
	%programdata%\Microsoft\Windows\Start Menu\Programs\Startup
	```

3. 添加到开机启动
	* 复制快捷方式到启动目录
		```
		copy "%~dp0启动本地DNS服务.cmd.lnk" "%programdata%\Microsoft\Windows\Start Menu\Programs\Startup\启动本地DNS服务.cmd.lnk"
		```

	* 直接在开机启动的地方创建快捷方式(不是开始菜单的启动目录)
		```
		//addto-startup.vbs
		Option Explicit
		Dim wsh, fso, ObjShell, BtnCode, ScriptDir, FilePath, link
		/*********************************************
		Set wsh = WScript.CreateObject("WScript.Shell")
		Set fso = CreateObject("Scripting.FileSystemObject")
		/*********************************************
		' 出处
		' https://groups.google.com/forum/#!topic/microsoft.public.scripting.vbscript/Fb-YibxZ2x8
		' https://stackoverflow.com/questions/13296281/permission-elevation-from-vbscript
		'
		If WScript.Arguments.length = 0 Then
			Set ObjShell = CreateObject("Shell.Application")
			ObjShell.ShellExecute "wscript.exe", """" & _
									WScript.ScriptFullName & """" &_
									" RunAsAdministrator", , "runas", 1
			WScript.Quit
		End If
		/*********************************************
		Function CreateShortcut(FilePath)
			Set wsh = WScript.CreateObject("WScript.Shell")
			Set link = wsh.CreateShortcut(wsh.SpecialFolders("Startup") + "\goproxy.lnk")
			link.TargetPath = FilePath
			link.Arguments = ""
			link.WindowStyle = 7
			link.Description = "GoProxy"
			link.WorkingDirectory = wsh.CurrentDirectory
			link.Save()
		End Function
		/*********************************************
		BtnCode = wsh.Popup("是否将 goproxy.exe 加入到启动项？(本对话框 6 秒后消失)", 6, "GoProxy 对话框", 1+32)
		If BtnCode = 1 Then
			ScriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
			FilePath = ScriptDir + "\goproxy-gui.exe"
			If Not fso.FileExists(FilePath) Then
				wsh.Popup "当前目录下不存在 goproxy-gui.exe ", 5, "GoProxy 对话框", 16
				WScript.Quit
			End If
			CreateShortcut(FilePath)
			wsh.Popup "成功加入 GoProxy 到启动项", 5, "GoProxy 对话框", 64
		End If
		```

4. 创建快捷方式
	```
	MKLINK [[/D] | [/H] | [/J]] Link Target

			/D      创建目录符号链接。默认为文件
					符号链接。
			/H      创建硬链接而非符号链接。
			/J      创建目录联接。
			Link    指定新的符号链接名称。
			Target  指定新链接引用的路径
					(相对或绝对)。
	```
	```
	* 这个创建的文件类型是 .symlink（.lnk）文件，和普通的快捷方式不一样
	* 然后第一个参数不写，才能对exe进行创建快捷方式
	mklink "C:\Users\qhy\Desktop\Shadowsocks" "C:\Users\qhy\AppData\tools\Shadowsocks-3.0\Shadowsocks.exe"
	```

5. 禁止程序访问网络
	* 方法是添加防火墙的出站规则
	* 参数解释
		* name 是规则的名字
		* dir 设置为出站规则
		* program 程序路径
		* action block设置为禁止
	```
	netsh advfirewall firewall add rule name="test 666" dir=in program="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" action=block
	```

6. 设置ipv6 ISATAP 隧道
	```
	netsh interface IPv6 ISATAP set router isatap.tsinghua.edu.cn
	netsh interface isatap set state enable
	pause
	```

7. 设置ip和DNS
	```
	::设置ip 子关掩码 网关
	netsh interface ipv4 set address "WLAN" static 125.216.245.243 255.0.0.0 125.216.245.254 1
	netsh interface ipv4 set address "WLAN" static 192.168.1.50 255.0.0.0 192.168.1.1 1
	::设置dns
	netsh interface ipv4 set dnsservers "WLAN" static 127.0.0.1 primary
	::这是备用dns
	netsh interface ipv4 add dnsservers "WLAN" 222.201.130.30
	netsh interface ipv4 add dnsservers "WLAN" 222.201.130.33
	pause
	```

8. 延时一定时间（不精确）
	```
	ping -n 5 127.0.0.1
	```
9. 调用外部程序
	```
	start IDMan.exe
	# 等待进程的结束
	start /wait IDMan.exe
	```
