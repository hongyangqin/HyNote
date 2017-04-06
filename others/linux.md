目录
<!-- toc -->

- [相关下载地址](#相关下载地址)
- [各种软件安装配置](#各种软件安装配置)
- [其他命令](#其他命令)
- [ubuntu 下 安装 rmp 安装包](#ubuntu-下-安装-rmp-安装包)
- [VMware Workstation 12 Player 下 ubuntu 安装 VMware Tool](#vmware-workstation-12-player-下-ubuntu-安装-vmware-tool)
- [关于密钥环](#关于密钥环)
- [英文设置成中文](#英文设置成中文)
- [dpkg 安装 deb 时，解决 缺少依赖包问题](#dpkg-安装-deb-时解决-缺少依赖包问题)
- [npm设置国内镜像源](#npm设置国内镜像源)
	- [国内优秀npm镜像](#国内优秀npm镜像)
		- [淘宝npm镜像](#淘宝npm镜像)
		- [cnpmjs镜像](#cnpmjs镜像)
	- [使用方法](#使用方法)
- [中文输入法设置](#中文输入法设置)

<!-- tocstop -->

# 相关下载地址
系统国内镜像：http://mirrors.163.com/

# 各种软件安装配置

1. python pip
    ```
    sudo apt-get install python-pip
    ```

2. pycharm
    1. 下载 pycharm 的安装包，并解压到某个目录
    2. 打开bin文件夹
        ![1]
    3. 在这个目录下运行
        ```
        ./pycharm.sh
        ```
        ![22]
    3.3 第一次运行
        ![23]![24]![25]
    4. 启动的时候，选择 create destop entry
        ![2]
    5. 锁定 pycharm 到启动器
        ![3]![26]

3. mega
    1. 到官网下载deb文件
        ![4]
    2. 安装
        ```
        cd 目录
        sudo apt-get install -f ***.deb
        ```

4. java
    0. 直接安装
        ```
        sudo apt install default-fre
        ```
    1. 到官网下载 java
    2. 安装 .rmp
        ```
        sudo alien packagename.rpm
        sudo dpkg -i packagename.deb
        ```

5. eclipse
    1. 安装 java
    2. 下载 并 解压 eclipse
    3. 运行

6. atom
    1. 到 github 上下载 安装包
        ![5]
    2. 安装
        ```
        cd ***
        sudo apt-get install
        ```

# 其他命令
1. 查看本机型号
    ```
    sudo lsb_release -a
    ```

# ubuntu 下 安装 rmp 安装包
1. 安装 alien 和必要的环境
    ```
    sudo apt-get install alien dpkg-dev debhelper build-essential
    ```

2. 把rmp 转换成 deb
    ```
    sudo alien packagename.rpm
    ```

3. 安装 deb
    ```
    sudo dpkg -i packagename.deb
    ```

# VMware Workstation 12 Player 下 ubuntu 安装 VMware Tool
http://jingyan.baidu.com/album/3065b3b6e8dedabecff8a435.html?picindex=13
1. 把 安装包 传入到 ubuntu 中
    ![6]

2. 桌面多了一个vmware-tools-distrib，解压出来

3. 到解压出来的文件夹
    ```
    sudo ./vmware-install.pl
    ```


# 关于密钥环
登陆chrome 的时候会提示创建/输入密钥环
1. 创建的时候直接设置为空
2. 不小心输入了密码
    1. 在 控制台 输入
        ```
        seahorse
        ```
    2. 删除 提示登陆的密钥环
        ![8]
    3. (重新打开chrome创建一个空的即可)创建一个新的密钥欢，**密码设置为空**
        ![7]![9]![10]![11]
    4. 重启

# 英文设置成中文
1. 进入系统设置->languange support->install/remove languange
    ![12]![13]![14]
2. 选择中文简体->apply changes(图片已经安装了，所以为灰色)
    ![15]
3. 最重要的一步，把汉语拖到最上面去
    ![16]
4. 重启系统

# dpkg 安装 deb 时，解决 缺少依赖包问题
1. 安装 deb 文件的时候，缺少依赖包
    ![17]
2. 输入一下命令
    ```
    sudo apt-get -y -f install
    ```
3. 继续安装
    ```
    dpkg -i **.deb
    ```

# npm设置国内镜像源
参考：http://riny.net/2014/cnpm/
## 国内优秀npm镜像
### 淘宝npm镜像
* 搜索地址：http://npm.taobao.org/
* registry地址：http://registry.npm.taobao.org/
### cnpmjs镜像
* 搜索地址：http://cnpmjs.org/
* registry地址：http://r.cnpmjs.org/

## 使用方法
有很多方法来配置npm的registry地址，下面根据不同情境列出几种比较常用的方法。以淘宝npm镜像举例
1. 临时使用
    ```
    npm --registry https://registry.npm.taobao.org install express
    ```
2. 持久使用
    ```
    npm config set registry https://registry.npm.taobao.org
    ```
    验证是否设置成功
    ```
    npm config get registry
    或
    npm info express
    ```

3. 通过cnpm使用
    ```
    npm install -g cnpm --registry=https://registry.npm.taobao.org
    // 使用
    cnpm install express
    ```

# 中文输入法设置
1. 下载搜狗输入法法
2. 直接打开安装(或者命令行)
    ```
    sudo dpkg -i **deb
    ```
3. 设置 fcitx 输入法
    ![18]![19]![20]![21]
4. 重启


[1]:assets/linux-01a07.png
[2]:assets/linux-a8c37.png
[3]:assets/linux-b10e7.png
[4]:assets/linux-db94b.png
[5]:assets/linux-f4746.png
[6]:assets/linux-bdafa.png
[7]:assets/linux-f9e79.png
[8]:assets/linux-96e77.png
[9]:assets/linux-7d32c.png
[10]:assets/linux-e3357.png
[11]:assets/linux-f5b79.png
[12]:assets/linux-d5e9e.png
[13]:assets/linux-5f245.png
[14]:assets/linux-eb8eb.png
[15]:assets/linux-35fb2.png
[16]:assets/linux-df7a8.png
[17]:assets/linux-fc902.png
[18]:assets/linux-fb9ff.png
[19]:assets/linux-c1e4e.png
[20]:assets/linux-f7fa5.png
[21]:assets/linux-03626.png
[22]:assets/linux-8a86b.png
[23]:assets/linux-94805.png
[24]:assets/linux-fef4b.png
[25]:assets/linux-82e5e.png
[26]:assets/linux-3267e.png
