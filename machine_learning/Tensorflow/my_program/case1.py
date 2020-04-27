import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

# 创建一个 常量 op, 返回值 'matrix1' 代表这个 1x2 矩阵.
matrix1 = tf.constant([[3., 3.]])

# 创建另外一个 常量 op, 返回值 'matrix2' 代表这个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)

# 启动默认图.
sess = tf.InteractiveSession()

# 调用 sess 的 'run()' 方法, 传入 'product' 作为该方法的参数，
# 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op)，
# 向方法表明, 我们希望取回矩阵乘法 op 的输出.
result = sess.run(product)

# 返回值 'result' 是一个 numpy `ndarray` 对象.
print(result)
# ==> [[ 12.]]

# 任务完成, 需要关闭会话以释放资源。
sess.close()
