def include_all_external_opts(self):
	self.external_print = external_print
	self.external_show_init_value = external_show_init_value	

def external_print ():
	print ("this is from external opt")

def external_show_init_value (self):
	print (self.value)

