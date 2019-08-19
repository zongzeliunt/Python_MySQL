#/usr/bin/python
import time
import os

def file_read_open_once():
	file_name = "timer_file.txt"
	print "open once"
	fl = open(file_name, "r")
	read_count = 0
	last_file_pos = 0
	last_file_size = 0
	fail_count = 0
	while (1):
		file_size = get_FileSize(file_name)
		if (file_size <= last_file_size):
			print "try fail"
			time.sleep(1)
			fail_count += 1
			if fail_count == 5:
				break
			continue
		fail_count = 0
		last_file_size = file_size
#######################################################################	
		last_file_pos = one_round_read(fl)
#######################################################################	
	
	fl.close()


def file_read_open_multiple():
	file_name = "timer_file.txt"
	read_count = 0
	last_file_pos = 0
	last_file_size = 0
	fail_count = 0
	while (1):
		file_size = get_FileSize(file_name)
		if (file_size <= last_file_size):
			print "try fail"
			time.sleep(0.2)
			fail_count += 1
			if fail_count == 5:
				break
			continue
		fail_count = 0
		last_file_size = file_size
		fl = open(file_name, "r")
		fl.seek(last_file_pos,os.SEEK_SET)
#######################################################################	
		last_file_pos = one_round_read(fl)
#######################################################################	
	
		fl.close()

#test
#file_read_open_position
#{{{
"""
def file_read_open_position():
	file_name = "timer_file.txt"
	fl = open(file_name, "r")
	read_count = 0

	for i in range (0,3):
		line = fl.readline()
		print line
	print fl.tell()	
	line = fl.read(34)
	print line
	print fl.tell()	
	fl.seek(0, os.SEEK_SET)
	print fl.tell()
	line = fl.read(34)
	print line
	print fl.tell()
	
	fl.seek(102, os.SEEK_SET)
	print fl.tell()
	line = fl.read(34)
	print line
	print fl.tell()

	fl.close()
"""
#}}}

#{{{
def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileSize(filePath):
#	filePath = unicode(filePath,'utf8')
	fsize = os.path.getsize(filePath)
	#this command is converting size into megabyte
#	fsize = fsize/float(1024*1024)
	return round(fsize,2)

def get_FileAccessTime(filePath):
#	filePath = unicode(filePath,'utf8')
	t = os.path.getatime(filePath)
	return TimeStampToTime(t)
def get_FileCreateTime(filePath):
#	filePath = unicode(filePath,'utf8')
	t = os.path.getctime(filePath)
	return TimeStampToTime(t)

def get_FileModifyTime(filePath):
#	filePath = unicode(filePath,'utf8')
	t = os.path.getmtime(filePath)
	return TimeStampToTime(t)
#}}}

def one_round_read(fl):
	while (1):
		line = fl.readline()
		print line
		if (line == ""):
			break
	last_file_pos = fl.tell()
	return last_file_pos

#file_read_open_multiple()
file_read_open_once()
#file_read_open_position()


#print get_FileSize("timer_file.txt")
#print get_FileAccessTime("timer_file.txt")
#print get_FileCreateTime("timer_file.txt")
#print get_FileModifyTime("timer_file.txt")

