这个文件 ，主要记录一些定义的东西的简单声明使用，关于具体应用的实例和技巧，另开文档

# 变量的定义
直接 直接 变量名 = 值
```
a = 1
```

# if-else 语句
```
score = 90
if score >= 90 :
    print("很好")
elif score >= 80 :
    print("良好")
else :
    print("其他")
```
1. 表达式后面 有个冒号
2. if 成立的语句，都要增加要给缩进

# for 循环语句
```
for i in range(1,100):
    print("Item {0}".format(i))
```

1. for 变量名 in 范围
2. for 后面有个冒号
3. for 下的语句 增加一个缩进

# 函数
```
def sayHello():
    print("Hello world")

def max(a,b):
    if a > b:
        return a
    else:
        return b

sayHello()
print( max(2,3) )
```

1. def 函数名（参数列表）
2. def 后面有 冒号
3. 函数内语句整体增加一个缩进
4. 参数的话，直接写参数名字即可


# 类
```
class Hello:
    def __init__(self,name):
        self._name = name;

    def sayHello(self):
        print("Hello {0}".format(self._name));

a = Hello("Qhy");
a.sayHello()
```
1. class 类名
2. class 后面有冒号
3. __init__ 是构造函数，且有两个下划线
4. 有两个参数，第一个参数是self，不用传，只需要传入 第二个开始的参数

## 继承
```
class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print("Hi {0}".format(self._name))

b = Hi("Qhy")
b.sayHi()
```
1. 继承 类名(父类名)
2. 父类名.__init__ 调用 父类的构造方法
3. 调用父类的函数，需要 传递 self 参数

# 引入其他文件 import
```
# mylib.py
class Hello:
    def __init__(self,name):
        self._name = name;

    def sayHello(self):
        print("Hello {0}".format(self._name));

# learning.py
import mylib

a = mylib.Hello("Qhy");
a.sayHello()
```

1. mylib 是引入的名字， 也是命名空间
2. import 文件名，引入文件
3. 文件名.类名 使用引用的文件的东西

## from
省略命名空间
```
from mylib import Hello

a = Hello("Qhy");
a.sayHello()
```

1. from 文件名 import 类名
  这样就不需要使用命名空间来访问 Hello 类

# 正则表达式
```
import re
```
## 符号
1. .:匹配除 换行符 '\n' 之外的任意字符
    可以在方法中增加参数 re.S 来使得 . 能匹配 换行符
2. \*:匹配前一个字符 0 次 或者 无限次，
3. ?:陪陪钱要给字符 0 次 或者 1 次
4. .\*:尽可能地匹配长的字符
5. .\*?:尽可能匹配短的字符
6. ():提取括号内的数据作为返回结果
7. \d+:匹配数字

## 方法
1. findall:匹配所有符合规律的内容
2. Search:匹配并提取抵押给符合规律的内容
3. Sub:替换符合规律的内容，返回替换后的值

## 例子
1. 简单匹配某个字符串
    ```
    import re
    # 提取 I love you
    # 注意:'xxxIxxxlovexxxyou'这句不能匹配到'
    s = 'xxxIxxxxxxlovexxxxxxyouxxx'
    a = re.findall("xxx(.*?)xxx",s)
    print(a)
    ```
    上面的并不能匹配下面的字符串(上面一个匹配只能配到换行)
    ```
    s = '''xxxIxxxxxxlove
    xxxxxxyouxxx'''
    ```
    解决：使用 re.S 第三个参数
    ```
    a = re.findall("xxx(.*?)xxx",s,re.S);
    # output:
    # ['I', 'love\n', 'you']
    ```

2. 提取所有数字
    ```
    s = '12asd123asd54a6s4d6a5s4d98'
    a = re.findall("(\d+)",s)
    print(a)
    ```

3. 替换匹配的字符串
    ```
    i = 666
    old = 'qhyqhyqhqyyhhqyqhhasd page in 1'
    new = re.sub('page in \d+',' page in %d'% i,old);
    # output:
    # qhyqhyqhqyyhhqyqhhasd  page in 666
    ```
    1. 这里 匹配的字符串是 'page in 1' 而不是 '1'
    2. *'page in %d'% i* 用 i 替换 %d (%d 和 C++ 的%d 一样)

 4. 简单用正则爬贴吧帖子作者
    ```
    # 简单爬虫爬贴吧帖子作者
    # 打开网页
    html = requests.get("http://tieba.baidu.com/f?kw=dnf%E5%95%86%E4%BA%BA&ie=utf-8");
    # 正则提取每个帖子的作者
    authors = re.findall("title=\"主题作者: (.*?)\"", html.text,re.S)
    for each in authors:
        print(each)
    ```


# request

## 简单下载文件
```
print('downloading : ' + url)
pic = requests.get(url)
f = open('C:\\Users\\qhy\\Desktop\\456' + str(i) + '.jpg','wb')
f.write(pic.content)
f.close()
```

## 设置 User-Agent
```
# 设置 User-Agent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
html = requests.get("http://jp.tingroom.com/yuedu/yd300p/",headers = headers);
```

## 设置表单 post data
```
# request 表达提交 post data
data = {'data1':'1','data2':2}
html = requests.post(url,data = data)
```

## 设置　Cookie
```
cookie = {'Cookie':'cookie内容'}
html = requests.get('http://weibo.cn/',cookies=cookie);
```
## 遇到的问题
1. ImportError: No module named 'requests'
    ```
    pip install requests
    ```

# 文件操作
## 简单读写
```
f = open("C:\\Users\\qhy\\Desktop\\123.txt")
contend = f.read();
f.close()
f = open('C:\\Users\\qhy\\Desktop\\456' + str(i) + '.jpg','wb')
f.write(pic.content)
f.close()
```

## 遇到的问题
1. 打开文件遇到编码错误 UnicodeDecodeError: 'gbk' codec can't decode byte 0xbe in position 308: illegal multibyte sequence
    解决：打开文件的时候 ，设置编码格式的参数
    ```
    f = open("C:\\Users\\qhy\\Desktop\\123.txt",encoding="UTF-8")
    ```

# XPath
## 安装
在 lxml 库 下
```
pip install lxml
```

## 使用方法
```
from lxml import etree
selector = etree.HTML(网页源代码)
selector.xpath(标题的路径)
# 比如 '//body/li/div[@id="666"]/text()'
# 比如 '//body/li/div[@id="666"]/@title'
# 比如 '@href'
# 比如 '//div/a/@href'
```
1. xpath 的参数 是 标签的路径
2. text() 表示获取标签的内容？
3. 通过在 标签后面 添加 [] 来限制是哪个标签
4. **@id="666"** 表示di 为 **666** 的 div 标签
5. **@title** 表示 返回 的 是 title 属性的值
6. 直接 **@** 表示在当前标签读取
7. 加上 **//** 表示到上级标签再开始取

## 例子
## 一个简答的使用
```
import re
import requests
from lxml import etree
html = '''
<div id = "content">
    <ul id = "useful">
        <li>需要的内容1</li>
        <li>需要的内容2</li>
        <li>需要的内容3</li>
    </ul>
    <ul id = "useless">
        <li>不需要的内容1</li>
        <li>不需要的内容2</li>
        <li>不需要的内容3</li>
    </ul>
    <div id="url">
        <a href="https://www.baidu.com">百度</a>
    </div>
</div>
'''
selector = etree.HTML(html)
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print(each)

content = selector.xpath('//div[@id="url"]/a/@href')
for each in content:
    print(each)

# output :
# 需要的内容1
# 需要的内容2
# 需要的内容3
# https://www.baidu.com
```
## 提取公共前缀名字的值(starts-with)
![1]
```
//div[starts-with(@id,"test")]/text()
```
```
import re
import requests
from lxml import etree
html = '''
<div id="test-1">123</div>
<div id="test-2">456</div>
<div id="test-3">789</div>
'''
selector = etree.HTML(html)
content = selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in content:
    print(each)

# output:
# 123
# 456
# 789
```

## 提取 标签套标签下的内容
![2]
提取标题下的元素，再使用 **string(.)**
```
data = selector.xpath('//div[@id="class3"]')[0]
info = data.xpath('string(.)')
```
```
import re
import requests
from lxml import etree
html = '''
<div id="class3">hell,
    <font color=red>你好</font>
</div>
'''
selector = etree.HTML(html)
content = selector.xpath('//div[@id="class3"]')
for each in content:
    print(each.xpath('string(.)'))

# output:
# hell,
#     你好
```

## 提取某个标签下的所有子标签
```
content = selector.xpath('//div[@id="class3"]')
```
content 的 每个元素还可以继续使用 xpath

## 简单爬取百度贴吧的帖子内容
1. 有的json里面没有date，所以时间还是从网页上爬的好
2. 图片不能爬
```
import requests
from lxml import etree
import json

def show(author,con):
    print(author)
    print(con)
    print('\n')

html = requests.get('http://tieba.baidu.com/p/4847827925')

selector = etree.HTML(html.content)
content = selector.xpath('//*[@id="j_p_postlist"]/div[@data-field]')

for each in content:
    info = json.loads(each.xpath('@data-field')[0])
    author = info['author']['user_name']
    con = each.xpath('div/div/cc/div/text()')
    show(author,con)
```

## 提取含某个属性，不含某个属性的标签
```
div[@class]
div[not(@class)]
```

## 多个条件
用 **and** 连接
```
selector.xpath('//*[@class="c" and @id]')
```

# json

```
from multiprocessing.dummy import pool
dic = json.loads(json内容)
# 返回 dic 字典对象，dic['a']['b'] 这样访问内容
```

# pytesseract
google's Tesseract-OCR ( https://github.com/tesseract-ocr/tesseract ) 的一个封装
用于简答的图像文字识别
地址：https://github.com/madmaze/pytesseract\
## 安装方法
1. 安装 **PIL**
```
pip install PIL
```

2. 安装 **google tesseract-ocr**
    直接到官方的 github 上下载

3. 安装 pytesseract
    直接安装
    ```
    pip install pytesseract
    ```
    下载之后运行setup.py
    ```
    git clone git@github.com:madmaze/pytesseract.git   
    python setup.py install  
    ```
## 使用方法
```
try:
  import Image
except ImportError:
  from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('test.png')))
print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
```
## 遇到的问题
1. FileNotFoundError: [WinError 2] 系统找不到指定的文件。
    ![3]
    这是因为没有安装 **google tesseract-ocr** ，下载安装即可
    环境变量没有 tesseract-ocr

# PIL
## 简单把gif 转换成 jpg
```
img = Image.open('show.gif')
img = img.convert('RGB')
img.save('show.jpg')
```

[1]:assets/pythonNote-56f68.png
[2]:assets/pythonNote-e3b28.png
[3]:assets/pythonNote-251dd.png
