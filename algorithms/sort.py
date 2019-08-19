a = [2,1,2]
b = sorted(a, reverse = True)
print b
print b[0]
print b[1]
print b[2]
print len(b)

candidate = 0
for i in range (0, len(b) - 1):
	if b[i] < b[i+1] + b[i+2]:
		candidate = b[i] + b[i+1] +b[i+2]
		break
print candidate
