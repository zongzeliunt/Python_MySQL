from tensorflow.examples.tutorials.mnist import input_data


import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
import os
import argparse
import sys
import dnn
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#X是一堆784 （28X28）的数据，代表图片
#y是10位长的数据，代表数字0到9。每次只有一位为1



x = tf.placeholder(tf.float32, [None, 784])

sess = tf.InteractiveSession()

batch = mnist.train.next_batch(5)
x = batch[0][0]
y_conv = sess.run(dnn.deepnn(x)) 

print (len(y_conv[0]))

sess.close()
