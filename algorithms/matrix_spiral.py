import numpy

n = 6 

matrix = numpy.zeros((n, n), int)

direct = "r"
this = 1
line = 0
col = 0
while True:
	matrix[line][col] = this
	this += 1
	if this == n * n + 1:
		break
	
	if direct == "r":
		if col + 1 == n:
			direct = "d"
			line += 1
		elif matrix[line][col + 1] != 0:
			direct = "d"
			line += 1
		else:	
			col += 1
	elif direct == "d":
		if line + 1 == n:
			direct = "l"
			col -= 1
		elif matrix[line + 1][col] != 0:
			direct = "l"
			col -= 1
		else:	
			line += 1
	elif direct == "l":
		if col - 1 == -1:
			direct = "u"
			line -= 1
		elif matrix[line][col - 1] != 0:
			direct = "u"
			line -= 1
		else:	
			col -= 1
	elif direct == "u":
		if line - 1 == -1:
			direct = "r"
			col += 1
		elif matrix[line - 1][col] != 0:
			direct = "r"
			col += 1
		else:	
			line -= 1


print matrix
