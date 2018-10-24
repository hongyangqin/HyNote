# latex 超链接

## 页内跳转

问题：使用 `hyperref` 经常失灵
解决：

```latex
\hypertarget{foo}{Your text}
\hyperlink{foo}{Some other text}
% foo 是标记
```

参考：[hyperref - Link to arbitrary part of text? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/a/280464/173047)