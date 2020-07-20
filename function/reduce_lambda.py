#reduce function is like this, arg_0 must be a two input function, arg_1 must be a list
#reduce keep giving two data from list into the two input function, use the output as next round's input_0

from functools import reduce


def add(x, y) :            
	return x + y

print (reduce(add, [1,2,3,4,5]))
print (reduce(lambda x, y: x+y, [1,2,3,4,5]))
