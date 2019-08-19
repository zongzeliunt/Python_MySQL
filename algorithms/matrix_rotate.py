#!/usr/bin/python
import numpy

#matrix = [[1,2,3], [4,5,6], [7,8,9]]
#matrix = [1,2,3, 4,5,6, 7,8,9]
matrix = [1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16]

#transpose
length = len(matrix)
size = int(numpy.sqrt(length))

def swap (a, b):
	tmp = a
	a = b
	b = tmp


print size
for i in range (0, size):
	for j in range (i + 1 , size):
		tmp = matrix[i*size + j]
		matrix[i*size + j] = matrix[j*size + i]
		matrix[j*size + i] = tmp
print matrix

half_line_num = size / 2
for i in range (0, half_line_num):
	#swap line i with line size - 1 - i
	for j in range (0, size):
		tmp = matrix[i*size + j]
		matrix[i*size + j] = matrix[(size - 1 - i) * size + j]
		matrix[(size - 1 - i) * size + j] = tmp

print matrix
	
