#https://practice.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers/0
#�ⲻ�����Ž⣬�����ǰѷ�Χ������int���Գ��ܵķ�Χ��
#��������Ȱ�exp������2�Ķ��ٴη���
#���磬���exp��768���Ȱ�ǰ512�����������ֻ����һ��ǰ512��remainder��������


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
