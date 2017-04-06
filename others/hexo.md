<!--toc-->

- [插件](#插件)
	- [增加 RSS](#增加-rss)
	- [生成sitemap](#生成sitemap)
- [主题](#主题)
	- [设置主题](#设置主题)
- [hexo插入图片](#hexo插入图片)
- [为hexo博客添加访问次数统计功能](#为hexo博客添加访问次数统计功能)
- [为Hexo博客添加目录](#为hexo博客添加目录)

<!-- tocstop -->


# 插件
[官方插件目录](https://github.com/hexojs/hexo/wiki/Plugins)

## 增加 RSS
[hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed)
1. 在博客根目录下 使用这个命令
    ```
    npm install hexo-generator-feed --save
    ```
2. 编辑 `_config.yml`
    ```
    feed:
      type: atom
      path: atom.xml
      limit: 20
      hub:
    ```

## 生成sitemap
[hexo-generator-sitemap](https://www.npmjs.com/package/hexo-generator-sitemap)
1. 编辑  `_config.yml`
    ```
    sitemap:
        path: sitemap.xml
    ```
2. 把sitemap的网址提交的google.

# 主题
[主题列表](https://github.com/hexojs/hexo/wiki/Themes)
## 设置主题
编辑 `_config.yml`
```
theme: 主题名
```

# hexo插入图片
1. 图片文件放在 `/source/images/` 目录下
2. 在markdown下引用图片
    ```
    ![1]
    [1]:/images/1.jpg
    ```

# 为hexo博客添加访问次数统计功能
1. 编辑 `themes/你的主题/layout/_partial/footer.ejs`
2. 加入一下内容
    ```html
    <script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
    		<span id="busuanzi_container_page_pv">本文总阅读量<span id="busuanzi_value_page_pv"></span>次</span><br>
    		<span id="busuanzi_container_site_uv">本站访客数<span id="busuanzi_value_site_uv"></span>人次</span><br>
    ```

# 为Hexo博客添加目录
1. 编辑 `\themes\landscape-plus\layout\_partial\article.ejs` 文件
2. 在文件的第23行(`<%- post.content %>`)之前添加一下代码
    ```html
    <!-- 文章目录开始 -->			
         <% if (!index){ %>
           <div id="toc" class="toc-article">
             <strong class="toc-title"><%= __('contents') %></strong>
             <%- toc(page.content) %>
           </div>
         <% } %>
       <!-- 文章目录结束 -->
    ```
3. 编辑 `themes/landscape/source/css/_partial/article.styl` 文件，添加一下内容
    ```css
    #toc {
        font-size: 0.9em;
        line-height: 1.65em;
    	background:#eee;
    	border:1px solid #bbb;
    	border-radius:10px;
    	margin:1.5em 0 0.3em 1.5em;
    	padding:1em 1em 1em 1em;
    	max-width:28%;
        float:right;
    }

    #toc .toc-title {
        font-weight: bold;
        color: #808080;
    	font-size:120%;
    }

    #toc ol.toc {
        margin-left: 0;
        padding: 0.7em 0.7em 0em 0.7em;
        padding-right: 0;
    	margin-top:0em;
    	margin-bottom:0em;
    }

    #toc ol.toc li.toc-item {
        list-style-type: none;
    }

    #toc ol.toc li.toc-item:hover {
        background: none;
    }

    #toc ol.toc a.toc-link {
        color: #808080;
    }
    #toc ol.toc a.toc-link:visited {
        color: #f48385;
    }
    #toc ol.toc a.toc-link:hover {
        color: #88acdb;
        text-decoration: none;
        background: rgba(158,188,226,0.21);
    }
    #toc ol.toc ol.toc-child {
        padding-left: 1.25em;
        margin: 4px 0;
    }
    ```
