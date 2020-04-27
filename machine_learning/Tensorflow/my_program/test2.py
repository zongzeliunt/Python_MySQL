import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
import numpy as np

"""
#case 0
#{{{
#matrix1 = tf.constant([[3, 3]])
#matrix2 = tf.constant([[2],[2]])
#np array 类型tf也支持
matrix1 = np.zeros ((2,3), int)
matrix2 = np.zeros ((3,2), int) 

def mul (matrix1, matrix2):
	product = tf.matmul(matrix1, matrix2)
	return product

matrix1[:][:] = [[1,2,3],[4,5,6]]
matrix2[:][:] = [[6,5],[4,3],[2,1]]

sess = tf.Session()
result = sess.run(mul(matrix1, matrix2))
print(result)
sess.close()
#[[20 14]
# [56 41]]

#}}}
"""

#case 1
#{{{
def reshape_test (x):
	x = tf.reshape (x, [-1,3, 3])
	return x
	
x = np.zeros (9, int)
x[:] = [1,2,3,4,5,6,7,8,9]

sess = tf.Session()
x = sess.run (reshape_test(x))
print (x)
sess.close()

#[-1, 3, 3, 1]:
#[
#	[
#		[[1][2][3]]
#		[[4][5][6]]
#		[[7][8][9]]
#	]
#]

#[3, 3]:
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

#[3, 3 ,1]:
#[
#	[[1][2][3]]
#	[[4][5][6]]
#	[[7][8][9]]
#]

#[1, 3, 3]或[-1, 3, 3]:
#[[[1 2 3]
#  [4 5 6]
#  [7 8 9]]]

#}}}





