
def fact(n):
	if n <= 2:
		return n
	else:
		return n * fact (n-1)

"""
print fact(1)
print fact(2)
print fact(3)
print fact(4)
print fact(5)
print fact(6)
print fact(7)
print fact(8)
print fact(9)
print fact(10)
"""

for i in range (10):
	print fact(i)
