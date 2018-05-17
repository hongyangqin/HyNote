# [Python 获取图片的大小](https://blog.csdn.net/y472360651/article/details/79272927)

了解过Pillow的都知道，Pillow是一个非常强大的图片处理器，这篇文章主要记录一下Pillow对图片信息的获取：

**安装Pillow**
```python
pip install pillow
```

**本地图片**
```python
import os
from PIL import Image

path = os.path.join(os.getcwd(),"23.png")
img = Image.open(path)

print img.format        # PNG
print img.size          # (3500, 3500)
```

**远程图片**
```python
path = "http://h.hiphotos.baidu.com/image/pic/item/c8ea15ce36d3d5397966ba5b3187e950342ab0cb.jpg"

file = urllib2.urlopen(path)
tmpIm = cStringIO.StringIO(file.read())
img = Image.open(tmpIm)

print img.format         # JPEG
print img.size           # (801, 1200)
```