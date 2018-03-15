# markdown css 样式

```less
html body {
    //图片居中
    img {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    max-width: 80%;
    //display:block;
    //margin: 0 auto;
    //text-align: center;
    }

    //标题编号
    h1 { counter-reset: h2counter; }
    h2 { counter-reset: h3counter; }
    h3 { counter-reset: h4counter; }
    h4 { counter-reset: h5counter; }
    h5 { counter-reset: h6counter; }
    h6 { }
    h2:before {
    counter-increment: h2counter;
    content: counter(h2counter) ".\0000a0\0000a0";
    }
    h3:before {
    counter-increment: h3counter;
    content: counter(h2counter) "."
                counter(h3counter) ".\0000a0\0000a0";
    }
    h4:before {
    counter-increment: h4counter;
    content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) ".\0000a0\0000a0";
    }
    h5:before {
    counter-increment: h5counter;
    content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) ".\0000a0\0000a0";
    }
    h6:before {
    counter-increment: h6counter;
    content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) "."
                counter(h6counter) ".\0000a0\0000a0";
    }
}
```

## 参考

[MarkDown标题自动添加编号 | yanwei.github.io](https://yanwei.github.io/misc/markdown-auto-number-title.html)

[使用css让markdown生成的网页里图片居中 | Trefoil](http://trefoil.github.io/2013/10/23/cssmarkdown.html)