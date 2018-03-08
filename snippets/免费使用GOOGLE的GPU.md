# 免费使用GOOGLE的GPU

1. Google Drive > 右键创建Colaboratory文件（没有就关联更多的应用）

2. 设置后端硬件加速

3. 挂载授权
    1. 安装必要的组件
        ```python
        # Install a Drive FUSE wrapper.
        # https://github.com/astrada/google-drive-ocamlfuse
        !apt-get install -y -qq software-properties-common python-software-properties module-init-tools
        !add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
        !apt-get update -qq 2>&1 > /dev/null
        !apt-get -y install -qq google-drive-ocamlfuse fuse
        ```

    2. google 挂载授权
        ```python
        # Generate auth tokens for Colab
        from google.colab import auth
        auth.authenticate_user()
        # Generate creds for the Drive FUSE library.
        from oauth2client.client import GoogleCredentials
        creds = GoogleCredentials.get_application_default()
        import getpass
        !google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
        vcode = getpass.getpass()
        !echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}
        ```

    3. 挂载drive
        ```python
        # Create a directory and mount Google Drive using that directory.
        !mkdir -p drive
        !google-drive-ocamlfuse drive
        ```
    4. 通过访问`drive`目录访问drive下的文件

4. coding

[Pickle + Drive FUSE example.ipynb - Colaboratory](https://colab.research.google.com/notebook#fileId=1mhRDqCiFBL_Zy_LAcc9bM0Hqzd8BFQS3&scrollTo=c99EvWo1s9-x)

[Google免费GPU使用教程（亲测可用）](http://www.cnblogs.com/infaraway/p/8372881.html)