def look_say (n):
	

	if n == 1:
		return [1]
	elif n == 2:
		return [1, 1]
	else:
		last_sequence = look_say(n - 1)
		new_sequence = []
		this = last_sequence[0]
		count = 1
		for i in range(1, len(last_sequence)):
			nxt = last_sequence[i]
			if nxt == this:
				count += 1
			else:
				new_sequence.append(count)
				new_sequence.append(this)
				this = last_sequence[i]
				count = 1
	
	new_sequence.append(count)
	new_sequence.append(this)

	return new_sequence
#10:
#1 
#11
#21
#1211
#111221
#312211
#13112221
#1113213211
#31131211131221
#13211311123113112211
print look_say(1)
print look_say(2)
print look_say(3)
print look_say(4)
print look_say(5)
print look_say(6)
print look_say(7)
print look_say(8)
print look_say(9)
print look_say(10)
	   	
