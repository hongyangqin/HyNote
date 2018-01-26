# 关于 TensorFlow tf.Session() 和 tf.InteractiveSession() 的区别

Session下不能通过 `Operation.run()` 和 `Tensor.eval()` , 必须通过session调用 `sess.run( Tensor)`

## 参考

[关于 TensorFlow tf.Session() 和 tf.InteractiveSession() 的区别](http://www.yiliao.ai/forum.php?mod=viewthread&tid=17)