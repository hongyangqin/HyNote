# python 计算MD5

```python
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
```

## 参考

[python - Generating an MD5 checksum of a file - Stack Overflow](https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file?answertab=active#tab-top)

You can use [hashlib.md5()][1]

Note that sometimes you won't be able to fit the whole file in memory. In that case, you'll have to read chunks of 4096 bytes sequentially and feed them to the Md5 function:

    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


  [1]: http://docs.python.org/library/hashlib.html