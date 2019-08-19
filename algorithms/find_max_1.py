a = [1,2,3,4,5,6,7,5,3,1]
a = [1,3,5,7,8,15,20,17,6,4,2]
a = [1,3,20,17,15,14,13,12,6,4,2]


def find_max (a):
	print a
	length = len(a)
	if length == 0:
		return -1
	if length == 1:
		return a[0]

	mid = length/2 - 1

	print a[mid]
	if a[mid] < a[mid + 1]:
		return find_max(a[mid + 1: length])
		#start from mid + 1
		#finish at length - 1
	else:
		return find_max(a[0: mid + 1])
		#this will include mid	
	


print find_max(a)
