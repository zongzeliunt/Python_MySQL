def trapped (s):
	status = "0" #r, e, d
	recording = 0

	if len(s) == 0:
		return 0

	trap_list = []
	tmp_list = []

	previous_num = s[0]
	for i in range (1, len(s)):
		this_num = s[i]
		if status == "0"

		if this_num < previous_num:
			status = "r"
			recording = 1
		tmp_list.append()


s = [0,1,0,2,1,0,1,3,2,1,2,1]
print trapped(s)
