import os
import sys
"""
directory = "external_opts"
if os.path.exists(directory):
	sys.path.append(directory)
	import external_opts
"""

class base_class:
	def __init__(self):
		
		

		self.base_name = "base_class init"

		self.powerunit = son_class()

		self.value = "abc"
		self.value_2 = "123"

		self.external_opt = None	
		#self.external_show_init_value = external_opts.external_show_init_value
	
	def internal_show_init_value (self):
		print ("this is internal")	
		print (self.value)
	


	def internal_show_upper_name (self):
		print (name)

	def stop(self):
		print ("base_class stop")



	def external_show_init_value(self):external_show_init_value(self)
	def external_show_upper_name(self):external_show_upper_name(self)

				
class son_class:
	def __init__(self):
		self.value = "this is son class"

	def print_value(self):
		print (self.value)

if __name__ == "__main__":
	STANDALONE_RUN = True
	exec(open("external_opts/external_opts.py").read())
	external_open_success()
	tb = base_class()
	print (tb.base_name)
	try:
		fire.Fire(tb)
	except:
		raise
	finally:
		tb.stop()	
