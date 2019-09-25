import os
import sys


class base_class:
	def __init__(self):
		self.base_name = "base_class init"
		self.include_all_external_opts()

		self.powerunit = son_class()	
	
	def print_powerunit(self, message):
		print (message) 

	def show_name (self):
		print (name)

	def show_value (self):
		print (value)

	def stop(self):
		print ("base_class stop")

	def include_all_external_opts(self):
		directory = "external_opts"
		if os.path.exists(directory):
			sys.path.append(directory)
			import external_opts
			external_opts.include_all_external_opts(self)
				
class son_class:
	def __init__(self):
		self.value = "this is son class"

	def print_value(self):
		print (self.value)

if __name__ == "__main__":
	STANDALONE_RUN = True
	tb = base_class()
	print (tb.base_name)
	try:
		fire.Fire(tb)
	except:
		raise
	finally:
		tb.stop()	
