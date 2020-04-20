
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

import os
import argparse
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



batch = mnist.train.next_batch(5)

print (len(batch))
print (batch[0])
print (len(batch[1]))
print (batch[1])

