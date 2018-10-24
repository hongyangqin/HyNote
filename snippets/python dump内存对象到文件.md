# python dump内存对象到文件

## pickle

* dump
    ```python
    pickle.dump(your_object, file, pickle.HIGHEST_PROTOCOL)
    with open("super.file", "wb") as f:
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
    ```

* load
    ```python
    with open("super.file", "rb") as f:
        dump = pickle.load(f)
    ```

## dill

`pickle`对于自定义的结构，在load的时候，需要预先给出该结构的定义，`dill`不用

```python

```


## 参考

* [How to save a python object to disk and retrieve it later?](http://www.albertgao.xyz/2016/12/02/how-to-save-a-python-object-to-disk-and-retrieve-it-later/)