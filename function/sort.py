score = [5, 4, 3, 2, 1]

dic = []
for i in range (len(score)):
	dic.append([i, score[i]])

print dic
dic.sort(key = lambda x:(x[1]), reverse = True)

print dic

new = ["" for i in range (len(score))]



for i in range (len(dic)):
	this = dic[i]
	pos = this[0]
	score = this[1]
	if i == 0:
		new[pos] = "gold"
	elif i == 1:
		new[pos] = "silver"
	elif i == 2:
		new[pos] = "bronze"
	else:
		new[pos] = i + 1

print new
