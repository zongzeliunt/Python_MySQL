
class class_base():
	def __init__(self):
		print ("class inialize")
		self.member1 = "member 1"
		self.member2 = "member 2"

def call_member (class_obj, member):
	print(getattr(class_obj,member))


if __name__ == '__main__':
	tb = class_base()
	print (tb.member1)
	print (tb.member2)

	call_member(tb, "member1")

