from tensorflow.examples.tutorials.mnist import input_data


import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
import os
import argparse
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#X是一堆784 （28X28）的数据，代表图片
#y是10位长的数据，代表数字0到9。每次只有一位为1

def weight_variable(shape):
#{{{
  """weight_variable generates a weight variable of a given shape."""
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
#}}}

def bias_variable(shape):
#{{{
  """bias_variable generates a bias variable of a given shape."""
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
#}}}

def conv2d(x, W):
#{{{
  """conv2d returns a 2d convolution layer with full stride."""
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
#}}}

def max_pool_2x2(x):
#{{{
  """max_pool_2x2 downsamples a feature map by 2X."""
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')
#}}}

def cal_cross_entropy(y_, y_conv): 
#{{{
	with tf.name_scope('loss'):
		cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv)
	cross_entropy = tf.reduce_mean(cross_entropy)
	return cross_entropy
#}}}

def adam_optimizer(cross_entropy):
#{{{
	with tf.name_scope('adam_optimizer'):
		train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
	return train_step
#}}}

def cal_accuracy(y_conv, y_):
#{{{
	with tf.name_scope('accuracy'):
		correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
		correct_prediction = tf.cast(correct_prediction, tf.float32)
	accuracy = tf.reduce_mean(correct_prediction)
	return accuracy
#}}}


W_conv1 = weight_variable([5, 5, 1, 32])

print (W_conv1)



sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

result = sess.run (W_conv1)

print (result)
print (len(result))


sess.close()












"""
x = tf.placeholder(tf.float32, [None, 784])
#x是28×28×32的图片

y_ = tf.placeholder(tf.float32, [None, 10])

keep_prob = tf.placeholder(tf.float32)

x_image = tf.reshape(x, [-1, 28, 28, 1])
W_conv1 = weight_variable([5, 5, 1, 32])
#b_conv1 就是全0.1
b_conv1 = bias_variable([32])
conv_result = conv2d(x_image, W_conv1)

h_conv1 = tf.nn.relu(conv_result + b_conv1) #output size 28*28*32
h_pool1 = max_pool_2x2(h_conv1)                          #output size 14*14*32


#======================================================
#执行
batch = mnist.train.next_batch(5)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

result = sess.run (W_conv1, feed_dict={x: batch[0]} )

print (result)
print (len(result))


sess.close()
"""
