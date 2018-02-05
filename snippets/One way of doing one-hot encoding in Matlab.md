# matlab one-hot 编码转换

```matlab
y_one_hot = ind2vec(y')'; // matlab has this built-in function
```

```matlab
[~, loc] = ismember(y, unique(y));
y_one_hot = ind2vec(loc')';
```

```matlab
ystr = cellstr(char('hey', 'hey', 'gurl', 'hey'));
[~, loc] = ismember(ystr, unique(ystr));
y_one_hot = ind2vec(loc')';
array2table(full(y_one_hot), 'VariableNames', unique(ystr))
```

注意 ， 预测结果为精度的话 ， 需要计算最大值的index进行编码修改 ，而不能直接 `Y(Y > 0.5) = 1` , 因为可能存在多个类的概率都大于0.5

[One way of doing one-hot encoding in Matlab](https://gist.github.com/zygmuntz/6939718)