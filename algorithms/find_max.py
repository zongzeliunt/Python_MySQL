a = [1,3,5,7,8,15,20,17,6,4,2]

def find_max (a):
	print a
	if len (a) == 0:
		return -1
	if len(a) == 1:
		return a[0]

	half_index = len(a) / 2 - 1
	if a[half_index] < a[half_index + 1]:
		return find_max (a[half_index + 1: len(a)])
	else:
		return find_max (a[0: half_index])

print find_max (a)	
