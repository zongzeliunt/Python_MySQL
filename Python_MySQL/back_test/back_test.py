#/usr/bin/python

import time

while True:
	fl = open("test.txt", "a+")
	now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
	fl.write("now time " + now + "\n")
	fl.close()
	time.sleep(60)
