# flask 跨域访问

```python
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

```

## 参考
[flask 设置headers['Access-Control-Allow-Origin']='*'实现跨域访问 - CSDN博客](https://blog.csdn.net/lovebyz/article/details/52584551)