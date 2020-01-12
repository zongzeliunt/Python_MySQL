import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

"""
fl = open("x_train.txt", "w")
for x in x_train:
	for row in x:
		tmp = ""
		for i in range (len(row)):
			num = row[i]
			if num < 10:
				tmp += "  " + str(num) + " "
			elif num < 100:
				tmp += " " + str(num) + " "
			else:
				tmp += str(num) + " "
	
		fl.write(tmp)
		fl.write ("\n")
fl.close()

fl = open("y_train.txt", "w")
for y in y_train:
	fl.write(str(y) + "\n")
fl.close()
"""
