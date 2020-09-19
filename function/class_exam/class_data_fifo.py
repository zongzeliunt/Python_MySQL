class data_1 ():
	def __init__ (self, name , value):
		self.name = name
		self.value = value


class data_store ():
	def __init__ (self, depth = 4):
		self.data_1_fifo = []
		self.depth = depth

	def push (self, data):
		self.data_1_fifo.append(data)
	
	def top (self):
		return self.data_1_fifo[0]

	def pop (self):
		del(self.data_1_fifo[0])

	def empty(self):
		return len(self.data_1_fifo) == 0
	
	def full(self):
		return len(self.data_1_fifo) == self.depth


db = data_store(4)

print (db.empty())
name = 'A'
num = 1
while True:
	
	new_data = data_1 (name, num)
	name = chr(ord(name) + 1)
	num += 1
	db.push(new_data)

	if db.full():
		break

while True:
	top = db.top()
	print (top.name)
	print (top.value)
	db.pop()
	if db.empty():
		break

