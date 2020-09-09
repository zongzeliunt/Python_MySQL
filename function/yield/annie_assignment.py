#yield is same as return
#but next call the function, program execute point is not the beginning of the function, but the next line of last yield.
#in this case, after execute yield zs, the next time call subset, the execute point is yield[x] + zs



print ("hello")

def subset (xs):
	if not xs:
		yield xs
	else:
		x =xs[0]
		ys = xs[1:]
		
		for zs in subset(ys):
			yield zs
			yield [x] + zs

def subset_1 (xs):
	if not xs:
		return [[]]
	else:
		x =xs[0]
		ys = xs[1:]
		return_list = []
		for zs in subset_1(ys):
			return_list.append(zs)
			return_list.append([x] + zs)
		return return_list

test_list = [1,2,3]
print ("subset result")
print (list(subset(test_list)))
print ("subset_1 result")
print (list(subset_1(test_list)))


