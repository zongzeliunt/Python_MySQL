#!/usr/bin/python

import MySQLdb
import time
import os

"""
command = 'CREATE TABLE mysubsystem ('
command += 'ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,'
command += 'spill INT NOT NULL,'
command += 'device_0 FLOAT NOT NULL,'
command += 'device_1 FLOAT NOT NULL'
command += ')'
"""
debug = 0 
sleep_time = 8 



def mysql_db_connect ():
#{{{
	host = "localhost"
	user = "ares"
	password = ""
	database = "fermilab"
	table = "mysubsystem"
	db = MySQLdb.connect(host, user, password, database)
	print db
	return db
#}}}

def file_read_store(db):
	file_name = "mysubsystem.tsv"
	fl = open(file_name, "r")
	read_count = 0
	last_file_size, last_file_pos = read_config_file()

	print "last_file_size " + str(last_file_size)
	print "last_file pos " + str(last_file_pos)

	fail_count = 0
	while True:
		file_size = get_FileSize(file_name)
		print file_size
		if (float(file_size) <= float(last_file_size)):
			
			print "try fail"
			time.sleep(sleep_time)
			fail_count += 1
			if fail_count == 5:
				break
			continue
		fail_count = 0
		last_file_size = file_size
		fl.seek(int(last_file_pos),os.SEEK_SET)
#######################################################################	
		last_file_pos = one_round_read(fl, db)
#######################################################################	

	write_config_file(last_file_size, last_file_pos)
	fl.close()

def one_round_read(fl, db):
	cursor = db.cursor()
	while (1):
		line = fl.readline().strip()
		if (line == ""):
			break
		line = line.split(" ")
		time_stamp = line[0]			
		time_stamp += " " + line[1]			
		spill = line[2] 
		device_0 = line[3]
		device_1 = line[4]

		command = 'INSERT INTO mysubsystem (ts, spill, device_0, device_1) VALUES('
		command += '"' + time_stamp + '", '
		command += spill + ", "
		command += device_0 + ", "
		command += device_1 + ")"
		if debug == 1:
			print command
		try:
			cursor.execute(command)
			if not debug == 1:
				db.commit()
			print "success"
		except:
			db.rollback()
			print "fail"



	last_file_pos = fl.tell()
	return last_file_pos

#{{{
def read_config_file():
	last_file_size = 0
	last_file_pos = 0
	if not os.path.exists("read_config.txt"):
		return last_file_size, last_file_pos

	fl = open("read_config.txt", "r")
	lines= fl.readlines()
	fl.close()
	if lines == "":
		fl.close()
		return last_file_size, last_file_pos
	line = lines[0] #last_file_size
	line = line.strip()
	line = line.split(" ")
	last_file_size = line[1]
	
	line = lines[1] #last_file_pos
	line = line.strip()
	line = line.split(" ")
	last_file_pos = line[1]
	fl.close()

	return last_file_size, last_file_pos

def write_config_file(last_file_size, last_file_pos):
	fl = open("read_config.txt", "w")
	fl.write("last_file_size " + str(last_file_size) + "\n")
	fl.write("last_file_pos " + str(last_file_pos) + "\n")
	fl.close()

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

def main():
	db = mysql_db_connect ()
	file_read_store(db)

	cursor = db.cursor()
	db.close()	


main()
