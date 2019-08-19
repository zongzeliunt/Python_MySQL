#!/usr/bin/python


dividen = -29
divider = 3

def int_to_bin (num):
	bin_list = []
	for i in range (0, 32):
		bin_list.append(0)

	if num < 0:
		num = abs(num)
		bin_list[31] = 1
	i = 30
	while i >= 0:
		if num >= pow(2, i):
			bin_list[i] = 1
			num -= pow(2, i)
		i -= 1
	return bin_list

print int_to_bin (dividen)
print int_to_bin (divider)
