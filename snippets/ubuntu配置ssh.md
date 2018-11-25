# ubuntu配置ssh

ubuntu 已经预安装了ssh客户端, 只需要安装 `openssh-server` 即可

- 安装 `openssh-server`
    ```bash
    sudo apt-get install openssh-server
    ```

- 免密码
    ```bash
    ssh-keygen -t rsa -C "邮件地址@youremail.com"
    cat rsa.pub >> ~/.ssh/authorized_keys
    ```
