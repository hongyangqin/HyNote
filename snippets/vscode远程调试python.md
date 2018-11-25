# vscode 远程调试 python

## 手动同步 + 配置

1. 确保两台电脑有相同的代码
    (这一步先手动上传, 尝试调试功能, 后续再配自动同步)

2. 两台电脑: 安装 `ptvsd`
    ```bash
    python -m pip install --upgrade ptvsd
    ```

3. 远程电脑: 打开防火墙端口

4. 远程电脑: 两种方式进入 "等待绑定" 的状态
    1. 在源文件 `test.py` 中加入以下代码(两台电脑都要加, 因为要保持一致)
        ```python
        import ptvsd

        # Allow other computers to attach to ptvsd at this IP address and port.
        ptvsd.enable_attach(address=('192.168.159.131', 3000), redirect_output=True)

        # Pause the program until a remote debugger is attached
        ptvsd.wait_for_attach()
        ```
        运行 `python test.py`

    2. 通过 `ptvsd` 启动远程进程
        ```bash
        python -m ptvsd --wait --host 192.168.159.131 --port 3000 test.py
        ```
        其中 `192.168.159.131` 是远程电脑的ip地址, `3000` 是端口号

5. vscode 配置 debug 参数 `Python: Attach`
    在 `.vscode` 下创建文件 `launch.json`
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Attach(Remote)",
                "type": "python",
                "request": "attach",
                "port": 3000,
                "host": "192.168.159.131",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/home/hy/python"
                    }
                ],
            }
        ]
    }
    ```
6. 调试
    下断点, `F5` 进行调试

## 自动同步 `vscode-remote-workspace`

前4步的安装一样, 后面配置同步

1. 安装插件 `vscode-remote-workspace`
2. 创建 `.code-workspace` 文件, 添加以下内容(`launch`的配置放在这个文件里面了, 这样就不会在远程的文件夹上创建出 `.vscode` 的配置)
    ```json
    {
        "folders": [{
            "uri": "sftp://hy:admin@192.168.159.131/home/hy/python",
            "name": "My SFTP folder"
        }],
        "launch": {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Attach(Remote)",
                    "type": "python",
                    "request": "attach",
                    "port": 3000,
                    "host": "192.168.159.131",
                    "pathMappings": [
                        {
                            "localRoot": "sftp://hy:admin@192.168.159.131/home/hy/python",
                            "remoteRoot": "/home/hy/python"
                        }
                    ],
                }
            ]
        }
    }
    ```

3. vscode 打开 workspace
    1. 打开 workspace
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-15-27-02.png)
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-15-27-15.png)

    2. 远程进入 "等待绑定状态"
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-16-34-34.png)
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-16-34-52.png)
    也可以在控制台ssh到远程电脑

    3. 启动调试
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-16-35-19.png)

但此方法还有一些不足, 比如在本地不知道这个目录所在的临时文件夹在哪, 比如 无法添加 `.vscode` 文件夹, 因为添加后, 由于目录不在本地, 无法识别(会提示 `Error: No search provider registered for scheme: sftp`, 因此, 很多功能受限, 比如无法搜索, 无法创建task).

至少 在当前插件的版本`v0.37.0`中还没有解决这个问题.

## samba 同步文件夹

1. ubuntu: 安装 `samba`
    ```bash
    sudo apt-get install samba
    ```

2. ubuntu: 配置文件
    ```bash
    sudo cp  /etc/samba/smb.conf  /etc/samba/smb.conf.bak
    sudo echo "[python]
    path = /home/hy/python
    writeable = yes
    browseable = yes
    guest ok = yes" >> /etc/samba/smb.conf
    ```
    <!-- sudo /etc/init.d/samba restart -->

3. windows: 右键开始菜单->运行->`gpedit.msc`->计算机配置-管理模板-网络-lanman工作站-启用不安全的来宾登陆
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-19-17-33.png)

4. windows: 我的电脑->右键:网络->映射网络驱动器->`\\192.168.159.131\python`
    ![](assets/vscodeyuanchengtiaoshipython/2018-11-25-19-18-51.png)

5. 其他操作和最开始的`手动同步 + 配置`一样

6. 添加task, 避免手动ssh进入等待连接状态(预先配置免密登陆)
    创建 `.vscode/task.json`, 并添加以下内容:
    ```json
    {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "start bind",
                "type": "shell",
                "command": "ssh 192.168.159.131 -l hy \"python -m ptvsd --wait --host 192.168.159.131 --port 3000 /home/hy/python/${relativeFile} 1>/dev/null 2>&1\"&"
            }
        ]
    }
    ```
    `launch.json`添加`preLaunchTask`
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                ...
                "preLaunchTask": "start bind"
            }
        ]
    }
    ```

    自此, `F5` 即可直接调试
