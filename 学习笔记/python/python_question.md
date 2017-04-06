记录没解决的疑问

1. 'xxxIxxxlovexxxyouxxx' 怎么使用正则匹配
    ```
    a = re.findall("xxx(.*)xxx",s)
    ```
    ```
    ['I', 'you']
    ```
    使用上面这句，只能匹配到 I you ,中间的 love 不能匹配
