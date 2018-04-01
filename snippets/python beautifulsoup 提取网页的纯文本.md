# python beautifulsoup 提取网页的纯文本

可能存在的情况:

1. 文本内有标签(比如超链接 `<a>`) , 即tag嵌套

    采用`soup.strings`即可提取所有的文本

2. tag不是文本 , 比如 `<script>` , `<style>` , `<figure>`

    采用`soup.extract()`即可从树中去除(同时取出)该`soup`节点
    ```python
    [x.extract() for x in soup.findAll('script')]
    [x.extract() for x in soup.findAll('style')]
    [x.extract() for x in soup.findAll('figure')]
    ```

```python
def get_article_details_help(article_link):
    session = requests.Session()
    cookies = ''
    headers = {
        'Host':'',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    article_a = ''
    while(True):
        try:
            req = session.get(article_link, headers=headers, allow_redirects=False, timeout=10,
            cookies=cookies)
            if req.status_code == 200:
                req.encoding = 'UTF-8'
                return_data = req.text.encode('utf-8')                
                try:
                    soup = BeautifulSoup(return_data, 'html.parser')
                    article_a = soup.select('#story')[0]
                    [x.extract() for x in article_a.findAll('script')]
                    [x.extract() for x in article_a.findAll('style')]
                    [x.extract() for x in article_a.findAll('figure')]
                    article_a = "".join(article_a.strings)
                    break
                except:
                    print('failed "{}"'.format(article_link))
            elif req.status_code == 301:
                article_link = req.headers['Location']
        except:
            print('Timeout "{}"'.format(article_link))
    return article_a
```

## 参考

[python - BeautifulSoup: just get inside of a tag, no matter how many enclosing tags there are - Stack Overflow](https://stackoverflow.com/questions/2957013/beautifulsoup-just-get-inside-of-a-tag-no-matter-how-many-enclosing-tags-there)

[python - Remove script tags inside p tags using beautifulsoup - Stack Overflow](https://stackoverflow.com/questions/25215922/remove-script-tags-inside-p-tags-using-beautifulsoup)