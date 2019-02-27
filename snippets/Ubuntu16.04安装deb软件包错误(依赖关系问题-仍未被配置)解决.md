# Ubuntu16.04安装deb软件包错误(依赖关系问题-仍未被配置)解决

现象: 安装deb软件包过程意外终止, 导致错误

1. 执行命令 `sudo dpkg　-i　XXX.deb`返回依赖关系错误提示
2. 执行 `sudo apt-get -f install` 这条命令将自动安装需要的依赖包．
3. 再次执行命令 `sudo dpkg　-i　XXX.deb` 安装成功

参考:

[Ubuntu16.04安装deb软件包错误(依赖关系问题-仍未被配置)解决 - yucicheung的博客 - CSDN博客]

[Ubuntu16.04安装deb软件包错误(依赖关系问题-仍未被配置)解决 - yucicheung的博客 - CSDN博客]:(https://blog.csdn.net/yucicheung/article/details/79333056)
