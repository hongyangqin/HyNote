# 创建无名字，只有后缀的文件

## 遇到的问题
在windows下，不输入文件名字直接创建文件是会提示错误滴
![1]

## 解决办法
直接在后缀名后面在加一个点，就可以了 `.atom.`
![2]
![3]

# windows 10 安装 hp1010 打印机驱动
hp1010 并没有提供win10 的安装驱动。也尝试过直接在win10上安装xp的驱动，但是均不成功（大部分时间无法识别，偶尔莫名能打印出来）。
经过百度，得到的解决办法是 在win10上安装 vista 的hp1010驱动就能成功使用。（已验证。）

以下是具体步骤：
1. 下载 vista 的 hp1010驱动，官方的下载地址会出现
    >错误
    >您所请求的网址（URL）无法获取

    这个错误，故选择从驱动精灵的官网下载

2. 解压驱动的压缩包到任意位置

3. 添加打印机 或者 更新打印机驱动
    这里如果之前已经安装过打印机，最好选择更新驱动，尝试过卸载了设备，然后重新扫描的时候，驱动还是原来那个，重新安装也不行。

    * 如果之前没有添加打印机，那么就 `右键开始菜单→控制台→打印机和设备→添加打印机`
        打印机未列出
        ![4]
        通过手动设置添加打印机或网络打印机
        ![5]
        选择正确的端口（USB OR DOT4,都不行的话一个一个尝试）
        ![6]
        从磁盘安装
        ![7]
        浏览→选择驱动解压出来的目录(我这里是1015e)
        ![8]
        选择 1010HB→确定
        ![9]

    * 如果之前已经添加了打印机，那么就 `右键计算机→属性→设备管理器→打印机那一列（不是打印机队列or其他,就是打印机）→选中那一栏的打印机→右键更新驱动`
        `打印机`而不是`打印队列`
        ![10]
        浏览计算机以查找驱动程序软件
        ![11]
        从计算机的设备驱动列表中选取（不要直接浏览，直接浏览可能会出现 `找不到驱动` 或`驱动不是32位` 的奇怪问题）
        ![12]
        然后就是从磁盘安装，和添加打印机的过程是一样的了

## 参考
[32bit下载地址(驱动精)](http://www.drivergenius.com/drv/hotdrivers/ht138.shtml)

[64bit下载地址(动精灵)](http://www.drivergenius.com/drv/hotdrivers/ht139.shtml)

[hp官网社区](http://h30471.www3.hp.com/t5/forums/forumtopicpage/board-id/Install/message-id/39729#M39729)

[12]:assets/windows-7d27a.png
[11]:assets/windows-7e0d4.png
[10]:assets/windows-8abff.png
[9]:assets/windows-9c259.png
[8]:assets/windows-5b2f8.png
[7]:assets/windows-06ad1.png
[6]:assets/windows-b25e3.png
[4]:assets/windows-6a4c1.png
[5]:assets/windows-327ef.png
[1]:assets/windows-f5ce1.png
[2]:assets/windows-04628.png
[3]:assets/windows-2c710.png
