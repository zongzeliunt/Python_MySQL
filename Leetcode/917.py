
def is_letter (letter):
	if letter >= 'a' and letter <= 'z':
		return 1
	if letter >= 'A' and letter <= 'Z':
		return 1
	return 0


def reverseOnlyLetters(S):
	new_s = "" 
	cur_pos = 0
	cur_can_pos = len(S) - 1
	
	S_rev_letter_list = "" 
	for i in range (0, len(S)):
		if is_letter(S[i]):
			S_rev_letter_list = S[i] + S_rev_letter_list
	
	if len(S_rev_letter_list) == 0:
		return S

	S_rev_list_pos = 0
	for i in range (0, len(S)):
		if is_letter(S[i]) == 0:
			new_s += S[i]
		else:
			new_s += S_rev_letter_list[S_rev_list_pos]
			S_rev_list_pos += 1
	
		
	return new_s

S = "Test1ng-Leet=code-Q!"
print reverseOnlyLetters(S)
