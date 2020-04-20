def num_comb_gen (base_list, n):
	if n == 1:
		return [base_list + [1]]
	else:
		new_list = []
		for i in range (1, n + 1):
			new_base_list = base_list + [i]
			if not i == n:
				result_list = num_comb_gen(new_base_list, n - i)
				for result in result_list:
					new_list.append(result)
			else:
				new_list.append(new_base_list)
		return new_list

#comb_list = num_comb_gen ([], 4)
#print comb_list


def generateParenthesis (n):
	ans = []
	def find (s = "", left = 0, right = 0):
		if len(s) == 2 * n:
			ans.append(s)
		if left < n:
			find(s + "(", left + 1, right)
		if right < left:
			find(s + ")", left, right + 1)
	find()
	return ans



"""
def generateParenthesis (n):
	result_list = []
	for i in range (n):
    	#wrap number
		result_num_list = num_comb_gen([], n - i)
		print result_num_list
		for result_num in result_num_list:
			if i != 0 and len(result_num) == 1:
				continue
			tmp = ""
			for num in result_num:
				for j in range (num):
					tmp += "("
				for j in range (num):
					tmp += ")"
		
			for k in range (i):
				tmp = "(" + tmp 
			for k in range (i):
				tmp += ")"
			result_list.append(tmp)

	return result_list
"""

n =4 
print generateParenthesis(n)


#["()()()()", "()()(())", "()(())()", "()((()))", "(())()()", "(())(())", "((()))()", "(((())))", "(()()())", "(()(()))", "((())())", "((()()))"]

#["()()()()", "()()(())", "()(())()", "()((()))", "(())()()", "(())(())", "((()))()", "(((())))", "(()()())", "(()(()))", "((())())", "((()()))", "(()())()","(())()()","()(()())"]
