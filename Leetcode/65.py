def isNumber (s):
	allow_list = [" ", "-", "+"]
	for i in range (0, len(s)):
		this_num = s[i]
		if this_num < "9" and this_num > "0":
			allow_list = ["-", "+", "."]
			continue
		if this_num == "e":
			allow_list = [" ", "-", "+", "."]
			
	




s = " 0.1 "
result = isNumber(s) 
print result

