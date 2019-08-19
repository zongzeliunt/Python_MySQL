#https://practice.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers/0
#这不是最优解，仅仅是把范围控制在int可以承受的范围里
#我想可以先把exp先消灭到2的多少次方内
#比如，这个exp是768，先把前512个乘消灭掉，只留下一个前512的remainder传给后面


input_list = [450,768,517]

base = input_list[0]
exp = input_list[1]
mod = input_list[2]

remainder = 0
while not exp == 0:
	if remainder == 0:
		remainder = base % mod
		exp -= 1 
		continue
	else:
		remainder = (remainder * base) % mod
	exp -= 1


print remainder 
