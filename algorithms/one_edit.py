def one_edit (a, b):
	log = ""
	short = ""
	if len(b) > len(a):
		log = b
		short = a
	else:
		log = a
		short = b

	print log
	print short

	diff_count = 0
	l_i = 0
	s_i = 0
	while True:
		if s_i == len(short) and l_i != len(log):		
			l_i += 1
			diff_count += 1
		else:
			if log[l_i] != short[s_i]:
				if len(log) == len(short):
					l_i += 1
					s_i += 1
				else:
					l_i += 1
				diff_count += 1
			else:
				l_i += 1
				s_i += 1

		if diff_count == 2:
			return False


		if l_i == len(log) and s_i == len(short):
			break

	return True



print one_edit ("cat", "cats")
print one_edit ("cat", "dog")
print one_edit ("cat", "cut")
print one_edit ("cat", "cast")
print one_edit ("cat", "at")
print one_edit ("cat", "act")
