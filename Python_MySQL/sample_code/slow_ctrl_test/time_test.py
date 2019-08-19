#/usr/bin/python
import time
import os

def timer_file_gen_file_close_version():
	file_name = "timer_file.txt"
	write_count = 0
	if os.path.exists(file_name):
		os.remove(file_name)
	while (1):
		fl = open(file_name, "a+")
		print time.ctime()
		fl.write(time.ctime() + ", " + "event " + str(write_count) + "\n")
		fl.write("	event " + str(write_count) + "," + "hello\n")
		write_count += 1
		if (write_count == 100):
			break			
		time.sleep(0.5)
		fl.close()

def timer_file_gen_no_close_version():
	file_name = "timer_file.txt"
	write_count = 0
	fl = open(file_name, "w")
	while (1):
		print time.ctime() + " " + str(write_count)
		fl.write(time.ctime() + ", " + "event " + str(write_count) + "\n")
		fl.write("	event " + str(write_count) + "," + "hello\n")
		fl.flush() #this is very important! Or receive part cannot read message
		write_count += 1
		if (write_count == 100):
			break			
		time.sleep(0.5)
	fl.close()


timer_file_gen_no_close_version()
#timer_file_gen_file_close_version()
