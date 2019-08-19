def is_valid(s):
	if s == "":
		return True
	stack = []
	for i in range (0, len(s)):
		this = s[i]
		if this == "(" or this == "[" or this == "{":
			stack.append(this)
		else:
			if stack == []:
				return False
			top = stack.pop()
			if this == ")" and not top == "(":
				return False
			if this == "]" and not top == "[":
				return False
			if this == "}" and not top == "{":
				return False
			#del(stack[-1])
	if stack == []:
		return True
	return False

s="([])"
print is_valid(s)
