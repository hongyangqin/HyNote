# python 打开 保存 json 文件


```python
# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

filename = 'data.json'

# 写 json 文件
with io.open(filename, 'w', encoding='utf-8') as outfile:
    str_ = json.dumps(article_info,indent=4,
        sort_keys=True,separators=(',', ': '),
        ensure_ascii=False)
    outfile.write(to_unicode(str_))

# 读取json文件 , open 的 encoding不能略
with open(filename,encoding='utf-8') as data_file:
    jsondata = json.load(data_file)
```

## 参考

[python - How do I write JSON data to a file? - Stack Overflow](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file)