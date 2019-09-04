import base64
import struct

def file_read (file_name):
	fl_r = open(file_name, "rb")
	fl_w = open("out.mp3", "wb")


	read_count = 0
	#data = fl_r.read(40)
	data = fl_r.read()
	#base64_data = base64.b64encode(data)
	#print len(base64_data)
	print len(data)
	#text = data.decode('utf-8')

	for i in range (0, len(data)):
		#print base64_data[i]
		"""
		old version
		print "data " + str(i)
		testResult = struct.unpack('>B', data[i])
		print testResult[0]
		tmp = 	testResult[0] ^ 0xa3
		print tmp
		print hex(tmp)
		print chr(tmp)	
		"""
		

		#print ord(data[i])
		#tmp = ord(data[i]) ^ 0xa3	
		tmp_0 = ord(data[i])
		#print tmp_0

		tmp_1 = tmp_0 ^ 0xa3
		#print tmp_1
		tmp_2 = chr(tmp_1)
		#print tmp_2
	
		fl_w.write(tmp_2)



	fl_r.close()
	fl_w.close()


file_read("test_music.uc")
