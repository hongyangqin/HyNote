# python pandas 显示全部行和列

```python
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
print(df)
```

## 参考

- [python - Pretty-print an entire Pandas Series / DataFrame - Stack Overflow](https://stackoverflow.com/questions/19124601/pretty-print-an-entire-pandas-series-dataframe)
