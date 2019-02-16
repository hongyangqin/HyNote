# pangubox 编译 ipk

设备型号 Newifi 2
固件版本 PandoraBox 18.12 2018-12-14-git-ba60306f2 / LuCI Master (git-18.346.39597-d1ebd59)
内核版本 3.14.79
系统: Linux ubuntu 4.8.0-36-generic #36~16.04.1-Ubuntu SMP Sun Feb 5 09:39:57 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux(`16.04`会有`glibc`版本太低的问题, 直接使用`18.04`省时省力)

1. 安装依赖

    ```bash
    sudo apt-get update
    sudo apt-get install git-core build-essential libssl-dev libncurses5-dev unzip gawk subversion mercurial  ccache bison
    ```

2. [pangubox sdk]

    ```bash
    cd ~
    wget https://downloads.pangubox.com/pandorabox/18.12/targets/ralink/mt7621/PandoraBox-SDK-ralink-mt7621_gcc-5.5.0_uClibc-1.0.x.Linux-x86_64-2018-12-14-git-ba60306f2.tar.xz

    tar -Jxvf PandoraBox-SDK-ralink-mt7621_gcc-5.5.0_uClibc-1.0.x.Linux-x86_64-2018-12-14-git-ba60306f2.tar.xz
    cd PandoraBox-SDK-ralink-mt7621_gcc-5.5.0_uClibc-1.0.x.Linux-x86_64-2018-12-14-git-ba60306f2
    ```

3. 创建包

    ```bash
    git clone https://github.com/scutclient/scutclient.git

    mkdir package/scutclient
    cp scutclient/openwrt/Makefile package/scutclient

    make defconfig
    # make package/scutclient/compile V=s
    ```

    `make defconfig` 提示:
    > scripts/config/conf: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.27' not found (required by scripts/config/conf)

4. 更新 `/lib/x86_64-linux-gnu/libc.so.6`
    升级系统到 `Linux ubuntu 4.18.0-15-generic #16~18.04.1-Ubuntu SMP Thu Feb 7 14:06:04 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux` 之后就包含 `2.27` 版本 (滑稽)
    <!-- - 查看系统glibc支持的版本

        ```bash
        strings /lib/x86_64-linux-gnu/libc.so.6 |grep GLIBC_
        ```

        > GLIBC_2.2.5
        > GLIBC_2.2.6
        > GLIBC_2.3
        > GLIBC_2.3.2
        > GLIBC_2.3.3
        > GLIBC_2.3.4
        > GLIBC_2.4
        > GLIBC_2.5
        > GLIBC_2.6
        > GLIBC_2.7
        > GLIBC_2.8
        > GLIBC_2.9
        > GLIBC_2.10
        > GLIBC_2.11
        > GLIBC_2.12
        > GLIBC_2.13
        > GLIBC_2.14
        > GLIBC_2.15
        > GLIBC_2.16
        > GLIBC_2.17
        > GLIBC_2.18
        > GLIBC_2.22
        > GLIBC_2.23
        > GLIBC_PRIVATE

    - 下载并编译 `glibc 2.27`

        ```bash
        cd ~
        wget https://ftp.gnu.org/gnu/libc/glibc-2.27.tar.gz

        sudo apt-get install bison

        tar -vxf glibc-2.27.tar.gz
        cd glibc-2.27
        mkdir build && cd build/
        ../configure --prefix=/usr/local/glibc-2.27

        make -j4
        sudo make install
        ``` -->

5. 继续步骤3

    <!-- ```bash
    cd ~/PandoraBox-SDK-ralink-mt7621_gcc-5.5.0_uClibc-1.0.x.Linux-x86_64-2018-12-14-git-ba60306f2

    LD_PRELOAD=/usr/local/glibc-2.27/lib/libc-2.27.so make defconfig
    LD_PRELOAD=/usr/local/glibc-2.27/lib/libc-2.27.so make package/scutclient/compile V=s
    ``` -->

6. 在 `bin` 下找到需要的`ipk`包

[pangubox sdk]:https://downloads.pangubox.com/pandorabox/18.12/targets/ralink/mt7621/PandoraBox-SDK-ralink-mt7621_gcc-5.5.0_uClibc-1.0.x.Linux-x86_64-2018-12-14-git-ba60306f2.tar.xz
[pangubox]:https://downloads.pangubox.com
[libc.so.6: version 'GLIBC_2.14' not found报错提示的解决方案 - 散尽浮华 - 博客园]:https://www.cnblogs.com/kevingrace/p/8744417.html
[Ubuntu 使用Openwrt SDK交叉编译ipk包过程全纪录(超多图) - lvshaorong的博客 - CSDN博客]:https://blog.csdn.net/lvshaorong/article/details/52931211
[PandoraBox/LEDE SDK交叉编译OpenWrt ipk安装包的方法 - lvshaorong的博客 - CSDN博客]:https://blog.csdn.net/lvshaorong/article/details/62215033
