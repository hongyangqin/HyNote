# 思源笔记docker相关信息

系统环境: `​ubuntu`

镜像版本(`1.4.6`):

```go
$ docker images b3log/siyuan
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
b3log/siyuan        latest              f32030b318bc        12 days ago         102MB
```

先看下启动命令:

```go
$ docker run b3log/siyuan --help
Usage of /opt/siyuan/kernel:
  -accessAuthCode string
        access auth code
  -readonly
        read-only mode
  -resident
        resident memory even if no active session (default true)
  -servePath string
        serve path (default "window.location.hostname+\":6806\"")
  -ssl
        for https and wss
  -wd string
        working directory of SiYuan (default "/opt/siyuan")
  -workspace string
        dir path of the workspace, default to ~/Documents/SiYuan/
```

各个参数的含义:

1. `-accessAuthCode` 授权码, 就是网页打开笔记的时候的验证密码
    ![image.png](assets/image-20211105135356-85tzdzx.png)
2. `-resident` 没用到, 不清楚
3. `-servePath` 网页js访问服务所使用的地址
    使用场景: 配置反向代理之后, 服务所请求的地址被隐藏, 但是由于server并不知道隐藏之后的访问地址是什么, 因此需要通过这个参数配置, 即这里填写的是反向代理之后server的地址
4. `-ssl` 网页js访问`serverPath` 所使用的协议, 为`true` 时, 使用`https`方式访问
5. `-workspace` 指定工作路径, 用于保存数据
    由于容器退出后, 容器内的数据会被清除, 因此, 在使用`docker`的方式部署的时候, 一定要把外部的目录挂载进容器内, 并指定`workspace` 为挂载进来的路径上, 具体挂载参考`docker volume`相关信息

---

# nginx配置反向代理

```go
2021-11-05T05:24:08.76943672Z I 2021/11/05 13:24:08 conf.go:246: local serve path [http://127.0.0.1:6806]
2021-11-05T05:24:09.795849118Z I 2021/11/05 13:24:09 serve.go:68: kernel is booting [http://0.0.0.0:6806]
```

目的: 从上边启动日志可以看出, 思源笔记`kernel` 是固定在`http://0.0.0.0:6806`配置启动, 也无对应的配置项可以设置, **因为采用**`http`**协议, 所有通信过程都是明文可抓取的, 在外网使用场景,** `6806`**端口不能暴露外网下,** 需要通过`nginx`配置反向代理, 并增加`ssl` 加密通信。

nginx配置信息:

```go
server {
        #SSL 访问端口号为 443
        listen 443 ssl; 
        #填写绑定证书的域名
        server_name example.top;

        ssl_certificate /siyuan/1_example.top_bundle.crt;  # pem文件的路径
        ssl_certificate_key /siyuan/2_example.top.key; # key文件的路径

        ssl_session_timeout 5m;
        #请按照以下协议配置
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
        #请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
        ssl_prefer_server_ciphers on;

                location / {
                        proxy_pass http://127.0.0.1:6806;
                        proxy_set_header Host $http_host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
                        proxy_http_version 1.1;
                        proxy_set_header Upgrade $http_upgrade;
                        proxy_set_header Connection "upgrade";
                        proxy_redirect off;
                }
}
```

1. 最终docker启动命令为
    ```go
    docker run -d -p 6806:6806 -v /path/to/workspace/:/siyuan/workspace  b3log/siyuan  -accessAuthCode xxx -workspace /siyuan/workspace -servePath example.top -ssl
    ```

    1. `-d`表式在后台运行
    2. `-p 6806:6806`为nginx代理访问需要, 需要暴露到母机
    3. `-v /path/to/workspace/:/siyuan/workspace`表式挂载外部目录到`/siyuan/workspace`
    4. `-servePath example.top -ssl`表式网页的js会使用`https://example.top`来访问服务

        如果没有`-ssl`则使用`http://example.top`

        ```go
        I 2021/11/05 14:15:26 conf.go:246: local serve path [https://example.top]
        I 2021/11/05 14:15:26 serve.go:68: kernel is booting [http://0.0.0.0:6806]
        ```
2. 关于证书, 可以采用自签名证书, 然后通过`https://ip:port`的方式访问, 也可以直接申请域名, 然后直接使用云服务提供好的签名

# 关于登陆卡在logo转圈圈的页面

卡在这个页面的原因就是`-servePath` 没有配置正确, 把`-servePath` 设置成你当前访问的`ip:port`, 然后根据是否是`https`访问设置`-ssl`参数
