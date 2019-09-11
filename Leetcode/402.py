num = "1432219"
k = 3

num = "10200"
k = 1

num = "1234567890"
k = 10

#num = "10"
#k=2

#num = "0"
#k=0

#num = "112"
#k=1

#print num[5]
#num = num[0:5] + num[6:length]
#print num

length = len(num)

delete_list = []

if length == 1:
	if k == 0:
		print num
	if k == 1:
		print "0"


i = 0
while k > 0:
	this_bit = num[i]
	next_bit = num[i+1]
	if this_bit > next_bit:
		#delete
		delete_list.append(i)
		k -= 1
	i += 1
	if i >= length - 1:
		break

if k > 0:
	#last numbers are large
	while k > 0:
		#must add to last of delete_list
		delete_list = delete_list + [length - k]
		k -= 1

print delete_list	

if delete_list == []:
	print num


new_num = ""
delete_list_pos = 0
for i in range (0, length):
	if i == delete_list[delete_list_pos]:
		delete_list_pos += 1
		if delete_list_pos == len(delete_list):
			#nothing to delete
			new_num += num[i+1: length]
			break
	else:
		new_num += num[i]

if new_num == "":
	new_num = "0"

if len(new_num) > 1 and new_num[0] == "0": 
	while new_num[0] == "0":
		new_num = new_num[1: len(new_num)]

print new_num
