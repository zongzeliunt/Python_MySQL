#coding=utf-8
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
def load_mnist(path, kind='train'):
    # 读取文件
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        # 读取magic numer，labels数量
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        print ('label magic : ', magic)
        # 载入label数据
        labels = np.fromfile(lbpath,
                             dtype=np.uint8).reshape(n, 1)
    with open(images_path, 'rb') as imgpath:
        # 读取magic numer，图片数量，图片宽，高
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        print ('image magic : ', magic)
        # 载入图片数据
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(num, rows * cols)
    return images, labels, rows, cols
def show_image():
    images, labels, rows, cols = load_mnist('orig_data/')
    fig, ax = plt.subplots(
        nrows=2,
        ncols=5,
        sharex=True,
        sharey=True, )
    ax = ax.flatten()
    for i in range(10):
        img = images[i].reshape(rows, cols)
        print (labels[i])
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
  show_image()
  # 解析命令行参数，默认没有
  parser = argparse.ArgumentParser()
  # 添加MNIST数据集的下载地址
  parser.add_argument('--data_dir', type=str,
                      default='/tmp/TensorFlow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  # 运行main方法
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
