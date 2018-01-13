免费搭建个人博客-hexo+github
<!--toc-->

- [效果图](#效果图)
- [准备工作](#准备工作)
- [创建github.io仓库](#创建githubio仓库)
- [hexo](#hexo)
	- [安装 hexo](#安装-hexo)
	- [创建 hexo 博客](#创建-hexo-博客)
	- [上传&发布博客 到 githubPage](#上传发布博客-到-githubpage)
		- [编辑 根目录/\_config.yml](#编辑-根目录_configyml)
		- [配置 SSH keys](#配置-ssh-keys)
		- [配置 git](#配置-git)
		- [上传到 github](#上传到-github)
- [发布新博客](#发布新博客)
- [参考](#参考)

<!-- tocstop -->

# 效果图
[hyCodeQ的博客](https://285571052.github.io/index.html)
![1]

# 准备工作
1. 环境:windows 10
2. git
3. nodejs
4. github账号

# 创建github.io仓库
1. github主页->new repository
		![2]
2. repository name 设置为用户名.github.io
    ![3]
3. 进入仓库的setting
    ![4]
4. 点击 Launch automatic page generator->contnue to layouts
    ![5]![6]
5. 点击publish page
    ![7]

# hexo
## 安装 hexo
1. 创建一个文件夹，用来存放hexo 和 博客的文件(git bash here，用cmd也可以)
    ![8]
2. 使用npm安装 hexo(可以先把npm换成国内的镜像源，以加快速度)
    在gitbash 内输入以下命令
    ```
    npm install -g hexo-cli
    npm install hexo --save
    ```
    ![9]  
    ![10]
3. 检查hexo是否安装成功
    ```
    hexo -v
    ```
    ![11]
## 创建 hexo 博客
1. 初始化 hexo
    ```
    hexo init
    ```
    ![12]
2. 安装生成器
    ```
    npm install
    ```
    ![13]
3. 本地运行->浏览器打开 http://localhost:4000
    ```
    hexo s -g
    ```
    ![14]
    ![15]
## 上传&发布博客 到 githubPage
### 编辑 根目录/\_config.yml
![17]
1. 把 url 修改为 刚刚申请到的 githubpage 的地址
    ```
    url: http://285571052.github.io
    ```        
    ![18]
2. 修改 deployer(下面的地址也可以从 github上获取)
    ```
    deploy:
    - type: git
      #285571052改为你的github用户名
      repository: https://github.com/285571052/285571052.github.io.git
      branch: master
    ```
    ![19]
### 配置 SSH keys
1. 生成 SSH Key
    ```
    ssh-keygen -t rsa -C "邮件地址@youremail.com"
    ```
    回车一次，输入密码两次    
    ```
    Enter file in which to save the key (/Users/your_user_directory/.ssh/id_rsa):<直接回车>
    Enter passphrase (empty for no passphrase):<输入加密串>
    Enter same passphrase again:<再次输入加密串>
    ```
    出现下面这个图就成功了
    ![22]
2. 添加SSH Key到GitHub
    1. 在刚刚的界面上找到类似下面的地址
        ```
        C:\Documents and Settings\Administrator.ssh\id_rsa.pub
        ```
    2. 打开 **.pub** 文件，复制里面的key
    3. 登陆github,点击右上角的 Account Settings—->SSH Public keys —-> add添加即可
### 配置 git
1. 设置 git 信息
    ```
    git config --global user.name "你的用户名"
    git config --global user.email "你的邮箱"
    ```

2. 安装 hexo-git 插件
    ```
    npm install hexo-deployer-git --save
    ```
    ![21]
### 上传到 github
```
hexo d -g
```

# 发布新博客
1. 创建新博客(也可以直接复制 .md文件到 sorce\\\_posts\\ 目录)
    ```
    hexo new "文件名字"
    ```
    ![23]

2. 编辑文件
    ![24]

3. 上传到 github
    ```
    hexo d -g
    ```

# 参考
[零基础免费搭建个人博客-hexo+github](http:/hifor.net/2015/07/01/%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%85%8D%E8%B4%B9%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2-hexo-github/)

[1]:assets/免费搭建个人博客-hexo+github-5bbde.png
[2]:assets/免费搭建个人博客-hexo+github-97ff1.png
[3]:assets/免费搭建个人博客-hexo+github-0d11e.png
[4]:assets/免费搭建个人博客-hexo+github-b62ca.png
[5]:assets/免费搭建个人博客-hexo+github-7b38e.png
[6]:assets/免费搭建个人博客-hexo+github-92fbe.png
[7]:assets/免费搭建个人博客-hexo+github-d7af8.png
[8]:assets/免费搭建个人博客-hexo+github-fdc89.png
[9]:assets/免费搭建个人博客-hexo+github-9ba79.png
[10]:assets/免费搭建个人博客-hexo+github-8ef4c.png
[11]:assets/免费搭建个人博客-hexo+github-e13e2.png
[12]:assets/免费搭建个人博客-hexo+github-4b13c.png
[13]:assets/免费搭建个人博客-hexo+github-8027e.png
[14]:assets/免费搭建个人博客-hexo+github-9ba3d.png
[15]:assets/免费搭建个人博客-hexo+github-281b4.png
[16]:assets/免费搭建个人博客-hexo+github-281b4.png
[17]:assets/免费搭建个人博客-hexo+github-db736.png
[18]:assets/免费搭建个人博客-hexo+github-bc2c5.png
[19]:assets/免费搭建个人博客-hexo+github-48184.png
[20]:assets/免费搭建个人博客-hexo+github-07ffe.png
[21]:assets/免费搭建个人博客-hexo+github-61f37.png
[22]:assets/免费搭建个人博客-hexo+github-3ad5f.png
[23]:assets/免费搭建个人博客-hexo+github-e5e56.png
[24]:assets/免费搭建个人博客-hexo+github-a349f.png
