#!/usr/bin/python

import time
import random

"""
now = int(round(time.time()*1000))
#now2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
print now
now2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
print now2
now3 = time.mktime(time.strptime(now2, '%Y-%m-%d %H:%M:%S'))
print now3
"""

sleep_time = 10
spill_num = 100 
time_limit = "2019-08-6 17:55:00"


while (True):
	fl = open("mysubsystem.tsv", "a+")
	now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))

	rand_num_0 = random.uniform(0,10)
	rand_num_1 = random.uniform(0,10)

	spill_num += 1	
	print "now time: " + str(now)
	print "spill_num: " + str(spill_num)
	
	print "device_0: " + str(rand_num_0)
	print "device_1: " + str(rand_num_1)


	time.sleep(sleep_time)

	line = now + " " + str(spill_num) + " " + str(rand_num_0) + " " + str(rand_num_1) + "\n"
	fl.write(line)

	if now > time_limit:
		print "limit"
		break
	fl.close()
