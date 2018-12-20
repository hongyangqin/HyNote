# 转换目录下所有文件的CRLF为LF(`\r\n` $\to$ `\n`)

```bash
find . -type f -print0 | xargs -0 dos2unix
```

[linux - How can I run dos2unix on an entire directory? - Stack Overflow][1]

[1]:https://stackoverflow.com/questions/11929461/how-can-i-run-dos2unix-on-an-entire-directory
