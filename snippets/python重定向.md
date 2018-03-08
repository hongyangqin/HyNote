# python重定向

Redirect stdout to a file in Python

```python 
import sys
sys.stdout = open('file', 'w')
print 'test'
```

```shell 
$ python foo.py > file
```

[Redirect stdout to a file in Python](https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python)