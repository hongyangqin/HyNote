# tensorflow 实现 next_batch

```python
def next_batch(num, data, labels):
    '''
    Return a total of `num` random samples and labels.

    data = np.array( [ [1,2,3],[4,5,6],[1,1,1],[1,2,3] ] )
    label = np.array( [ [1,0,0],[0,1,0],[0,0,1],[1,0,0] ] )
    d , l = next_batch(2,data , label)
    '''
    idx = np.arange(0, len(data))
    num = min(num, len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = data[idx]
    labels_shuffle = labels[idx]
    return data_shuffle, labels_shuffle
```

[how to implement tensorflow's next_batch for own data](https://stackoverflow.com/a/40995666)