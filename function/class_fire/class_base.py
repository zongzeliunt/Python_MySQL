#!/usr/bin/python
import fire


class class_base():
	def __init__(self):
		print "class inialize"
		self.value = 0
		if STANDALONE_RUN:
			print "standalone"
		print "done"
	
	def value_assign (self, val):
		self.value_print()
		self.value = val
		self.value_print()

	def val_print(val):
		print val
	
	def value_print(self):
		print self.value



if __name__ == '__main__':
	STANDALONE_RUN = True
	
	tb = class_base()
	fire.Fire(tb)

