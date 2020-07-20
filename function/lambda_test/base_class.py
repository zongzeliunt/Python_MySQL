import os
import ex_opts

class base :
	def __init__ (self, v):
		self.val = v
		self.external_show_class_val = ex_opts.external_show_class_val
	
	def internal_show_class_val(self):
		print (self.val )

if __name__ == '__main__':
	test = base(10)
	test.internal_show_class_val()
	test.external_show_class_val(test)
	#self.Bind(wx.EVT_BUTTON, lambda evt,i=self.step_button_list[i].GetId():self.exe_buttonbox_command(evt, i), self.step_button_list[i])
	g = lambda arg : arg + 2
	print (g(4))

