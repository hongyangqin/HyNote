# tf.reverse doesn't support tensor with unknown shape

The docs for `tf.reverse()` indicate (perhaps too subtly...) that the `axis` argument must be one-dimensional, so you should instead pass `axis=[0]`. The following code works as intended:

```python
a = tf.placeholder(dtype=tf.int64, shape=[None])
b = tf.reverse(a, axis=[0])
sess = tf.Session()
print sess.run(b, feed_dict={a: [1, 2, 3]})  # Prints "[3, 2, 1]".
```

[tf.reverse doesn't support tensor with unknown shape](https://github.com/tensorflow/tensorflow/issues/11293#issuecomment-313165195)