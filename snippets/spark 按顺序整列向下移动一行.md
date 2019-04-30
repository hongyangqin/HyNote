# spark 按顺序整列向下移动一行

`lag` --> `over(window)`

```python
from pyspark.sql.functions import lag, col
from pyspark.sql.window import Window

df = sc.parallelize([(4, 9.0), (3, 7.0), (2, 3.0), (1, 5.0)]).toDF(["id", "num"])
w = Window().partitionBy().orderBy(col("id"))
df.select("*", lag("num").over(w).alias("new_col")).na.drop().show()
```

## 参考

- [python - Spark add new column to dataframe with value from previous row - Stack Overflow](https://stackoverflow.com/questions/34295642/spark-add-new-column-to-dataframe-with-value-from-previous-row)
