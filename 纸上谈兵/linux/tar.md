# 技术|如何在 Linux 中创建和管理归档文件

## 创建归档文件

```
tar -cf a.tar ./dir
tar -czf a.tar.gz ./dir # z使用gzip压缩
tar -cJf a.tar.xz ./dir # z改成J即使用xz压缩
```

## 列出文档内容

```
tar --list
tar -t
```

## 不解压缩的情况删除归档文件内容

```
tar -vf file.tar –- delete xxx
```

## 跳过某些文件或目录

```
tar --exclude `/path/to/dir`
```

## 比较同路径某个文件是否一样
```
root@debian:/home/debian/test# tar -d -f  main.tgz  main.go 
main.go: Mod time differs
main.go: Size differs
```



[技术|如何在 Linux 中创建和管理归档文件](https://linux.cn/article-13126-1.html?utm_source=rss&utm_medium=rss)