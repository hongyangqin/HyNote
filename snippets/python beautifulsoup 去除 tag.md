# python beautifulsoup 去除 tag

采用`soup.extract()`即可从树中去除(同时取出)该`soup`节点

```python
soup = BeautifulSoup(return_data, 'html.parser')
article_a = soup.select('#story')[0]
[x.extract() for x in article_a.findAll('script')]
[x.extract() for x in article_a.findAll('style')]
[x.extract() for x in article_a.findAll('figure')]
```

## 参考

[python - Remove script tags inside p tags using beautifulsoup - Stack Overflow](https://stackoverflow.com/questions/25215922/remove-script-tags-inside-p-tags-using-beautifulsoup?answertab=votes#tab-top)