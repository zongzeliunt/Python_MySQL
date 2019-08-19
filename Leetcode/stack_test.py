stack = []
stack.append("(")
stack.append("(")
stack.append(")")
stack.append("2")

stack.append("4")
for num in stack:
	if num.isdigit():
	
		print str(int(num) + 2)

