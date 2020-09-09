def func_yield ():
	yield "one"
	yield "two"
	yield "three"

	
g = func_yield()


print(next(g))
print(next(g))
print(next(g))


