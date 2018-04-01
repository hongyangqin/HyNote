# python 判断文件是否存在

python 判断文件和目录是否存在

```python
import os.path
name = /"etc/password.txt"
# 判断文件
os.path.isfile(name)
# 判断目录
os.path.isdir(name)
# 判断存在
 os.path.exists(name)
```

## 参考

[11.2. os.path — Common pathname manipulations — Python 3.6.5 documentation](https://docs.python.org/3/library/os.path.html?highlight=isdir#os.path.isfile)

[python - How to check whether a file exists? - Stack Overflow](https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists)