def longest(s):
	stack = []
	for i in range (0, len(s)):
		previous_num = 0
		this = s[i]
		if this == "(":
			stack.append(this)
		else:
			#this is ")"
			if stack == []:
				stack.append(this)
				continue

			top = stack[-1]
			if top.isdigit():
				if len(stack) == 1:
					stack.append(this)
					continue
				else:
					previous_num = int(top)
					del(stack[-1])
					top = stack[-1]	

			if top == "(":
				#match
				del(stack[-1])
				previous_num += 2
				if stack == []:
					stack.append(str(previous_num))
				else:
					if stack[-1].isdigit():
						stack[-1] = str(int(stack[-1]) + previous_num)
					else:
						stack.append(str(previous_num))
			else:
				#mismatch
				if not previous_num == 0:
					stack.append(str(previous_num))
				stack.append(this)
		print stack
	longest = 0
	for ele in stack:
		if ele == "(" or ele == ")":
			continue
		longest = max(int(ele), longest)
	return longest		
			


s = "((()))())"
#s = ")()())"
print longest(s)
