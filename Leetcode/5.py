def longestPalindrome (s):
	if s == "":
		return ""
	occur_db = {}
	length = len(s)
	for i in range (0, length):
		this_letter = s[i]
		if not this_letter in occur_db:
			this_letter_list = []
		else: 
			this_letter_list = occur_db[this_letter]
		this_letter_list.append(i)
		occur_db[this_letter] = this_letter_list

	recording = 0
	this_start = 0
	this_end = 0
	current_start = 0
	current_end = 0
	pos = 0
	longest_start = 0 
	longest_end = 0 
	while pos < length:	
		this_letter = s[pos]
		this_letter_list = occur_db[this_letter]
		this_letter_current_pos = pos
		this_letter_next_pos = pos
		for number in this_lstter_list:
			if number <= this_start:
				continue
			else:
				this_letter_next_pos = number
				break
		if this_letter_current_pos == this_letter_next_pos and recording == 1:
			


		if recording == 0:
			this_start = this_letter_current_pos 
			this_end = this_letter_next_pos
			current_start = this_letter_current_pos 
			current_end = this_letter_next_pos
			recording = 1
		else:
			if not this_letter_current_pos == current_start + 1 or not this_letter_next_pos == current_end - 1:
				pos = this_end
				recording = 0
			else:
				current_start = this_letter_current_pos 
				current_end = this_letter_next_pos
			



s = "babad"
longestPalindrome(s)
