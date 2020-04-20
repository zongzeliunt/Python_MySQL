#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
print (tf.__version__)
print (tf.__path__)
#from tensorflow.examples.tutorials.mnist import input_data

keep_prob = tf.placeholder(tf.float32)
print (keep_prob)
