记录没分类的例子

# 字符串拼接
字符串拼接 & 格式化输出 & 格式化字符串
```
print("Item {0}".format(1))
```
1. 第一个格式化的变量 必须是 {0}
2. {0} 对应 format 第一个参数

# 生成一定范围的连续整数
```
range(1,100)
```
1. 上面的语句 是 作闭右开，即上面的语句 是生成 [1,100) 的整数

# 连接list中的多个字符串 （string.s）
```
l = ['1','2','3']
a = '-'.join(l)
# a = '1-2-3'
```


# 爬虫
## 简单爬取微博的转发
1. 使用cookie登陆，cookie可以直接用 chrome 下 开发者工具抓取
    ![1]
2. 抓取的是手机页面的转发
    ![2]
3. 只是简单抓取转发人 和 转发的内容，图片等没有抓取
    ![3]
4. 数据来源
    1. 发现每一个转发都是在一个 class 为 c 的div块内
        ![4]
    2. 这个 div 下 class 为 nk 的内容为转发的人
        ![5]
    3. class 为 ctt 的 span 的内容为转发的内容
        ![6]
        在 span 内有需要子标签，直接读取子标签的内容即可

5. 代码
    ```
    import requests
    from lxml import etree
    # author：qhy
    # create on：2016年11月11日22:17:36
    # 微博头条爬虫（无登陆功能）

    # 打开网页，这里直接用cookie，
    cookie = {'Cookie':'***'}
    html = requests.get('https://weibo.cn/',cookies = cookie);

    # 使用 xpath 获取所有转发
    selector = etree.HTML(html.content)
    items = selector.xpath('//*[@class="c" and @id]')
    for each in items:
        # 显示每一个转发的内容
        title = each.xpath('div/a[@class="nk"]/text()')[0]
        print('玩家:' + title)
        content = each.xpath('div/span[@class="ctt"]/text()')
        print('内容:' + ','.join(content))
    ```


# 发送邮件
参考：http://python.usyiyi.cn/documents/python_352/library/email-examples.html#email-examples
1. 使用 smtplib 中的 SMTP 来发送
2. 调用 send_message 来发送 MIMEText 封装好的 信息
3. 也可以调用 sendmail 来发送
4. 代码
    ```
    import smtplib
    from email.mime.text import MIMEText
    host = 'smtp.163.com'
    user = '123@163.com'
    pasw = '123'
    SMTP = smtplib.SMTP()

    # 连接smtp服务器
    SMTP.connect(host)
    # 登陆
    SMTP.login(user,pasw)

    # 整理消息
    msg = MIMEText("Testing sending email 内容");
    me = user
    # 收件人，多个用 ; 号隔开
    you = '285571052@qq.com'
    msg['Subject'] = 'Testing sending email 主题'
    msg['From'] = me
    msg['To'] = you

    # 发送消息
    SMTP.send_message(msg)
    SMTP.quit()
    ```

[1]:assets/pythonExample-cd0ff.png
[2]:assets/pythonExample-17184.png
[3]:assets/pythonExample-5210f.png
[4]:assets/pythonExample-dba35.png
[5]:assets/pythonExample-a06d1.png
[6]:assets/pythonExample-c1f3d.png
