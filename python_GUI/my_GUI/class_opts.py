import wx
import function
import os
import sys
sys.path.append('./sub_pages')
import cheatsheet
import step_commands
step_commands = step_commands.step_commands
HORI = 300

def declare_overall_box (self):
#{{{
	#self.box_sizer = wx.BoxSizer(wx.HORIZONTAL)
	self.box_sizer = wx.BoxSizer(wx.VERTICAL)
	#self.box_sizer = wx.WrapSizer()
	self.SetAutoLayout(True)
	self.SetSizer(self.box_sizer)
#}}}


def import_outside_functions(self):
#{{{
	self.OnExit 		=	function.OnExit
	self.OnSelectAll 	= 	function.OnSelectAll
	self.OnButton 		= 	function.OnButton
	self.print_page_0 	=	function.print_page_0
	self.showcheatsheet = 	cheatsheet.showcheatsheet
	
	self.change_combobox_command = change_combobox_command
	self.exe_combobox_command = exe_combobox_command
	



	#self. = function.
#}}}


def generate_status_bar(self):
#{{{
	self.CreateStatusBar() #status bar at the bottom 
	filemenu = wx.Menu() #menu on the top
	menu_page_0 = filemenu.Append(wx.ID_NEW, "&Page0", "Open Page 0")
#	menu_page_0 = filemenu.Append(wx.ID_ANY, "&Page0", "Open Page 0")
	menu_page_1 = filemenu.Append(wx.ID_ANY, "&Page1", "Open Page 1")
	menuExit 	= filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

	# menu bar will include menu
	menuBar = wx.MenuBar()
	menuBar.Append(filemenu, "&Operations")

	
	cheatsheetmenu = wx.Menu()
	cheatsheetpage = cheatsheetmenu.Append(wx.ID_NEW, "&cheatsheet", "View cheatsheet")

	menuBar.Append(cheatsheetmenu, "&Cheatsheet")


	self.SetMenuBar(menuBar)

	self.Bind(wx.EVT_MENU, self.print_page_0, menu_page_0)
	self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
	self.Bind(wx.EVT_MENU, self.showcheatsheet, cheatsheetpage)
#}}}


def add_stepcombobox (self):
	#part 0: combobox:
	combobox=wx.BoxSizer(wx.HORIZONTAL)

	statictext=wx.StaticText(self,label='Select step:')
	combobox.Add(statictext, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)

	list0=[]
	for com in step_commands:
		list0.append(com)

	self.ch1=wx.ComboBox(self, -1, value='C', choices=list0, style=wx.CB_SORT)
	combobox.Add(self.ch1, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
	
	step_exe_button = wx.Button(self, -1, "Execute step" )
	combobox.Add(step_exe_button, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5 )
	self.box_sizer.Add(combobox, 0, wx.ALIGN_LEFT)


	#part 1: commandbox
	
	commandbox=wx.BoxSizer(wx.HORIZONTAL)

	statictext=wx.StaticText(self,label='Command:')
	commandbox.Add(statictext, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)

	self.command_text = wx.TextCtrl(self, -1, 'command', size=(HORI, -1), style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))
	commandbox.Add(self.command_text, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)	
	self.box_sizer.Add(commandbox, 0, wx.ALIGN_LEFT)	
	
	#part 2: explain

	explainbox=wx.BoxSizer(wx.HORIZONTAL)

	statictext=wx.StaticText(self,label='Step explain:')
	explainbox.Add(statictext, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)

	self.explain_text = wx.TextCtrl(self, -1, 'explain', size=(HORI, -1), style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))
	explainbox.Add(self.explain_text, 1, flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)	
	self.box_sizer.Add(explainbox, 0, wx.ALIGN_LEFT)	



	#part 3: operation
	self.Bind(wx.EVT_COMBOBOX, self.change_combobox_command, self.ch1)
	self.Bind(wx.EVT_BUTTON, self.exe_combobox_command, )


def change_combobox_command(self, event):
	combo_box_value = self.ch1.GetValue()
	self.command_text.SetValue(step_commands[combo_box_value][0])
	self.explain_text.SetValue(step_commands[combo_box_value][1])

	#print("select{0}".format(event.GetString()))


def exe_combobox_command(self, event):
	command = self.command_text.GetValue()
	exec(command)






def declare_input_frame (self):
	########## Label ##########


	text_sizer = wx.BoxSizer(wx.HORIZONTAL)
	static_text = wx.StaticText(self, -1, 'Label_0', style=wx.ALIGN_CENTER)
	static_text.SetForegroundColour('red')  
	wx_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
	static_text.SetFont(wx_font)
	text_sizer.Add(static_text, 0, wx.ALIGN_LEFT)	
	input_text = wx.TextCtrl(self, -1, 'input_0', size=(HORI, -1))
	input_text.SetInsertionPoint(0)
	text_sizer.Add(input_text, 0, wx.ALIGN_LEFT)
	self.box_sizer.Add(text_sizer, 0, wx.ALIGN_LEFT)	
	
	text_sizer = wx.BoxSizer(wx.HORIZONTAL)
	static_text_1 = wx.StaticText(self, -1, 'Label_1', style=wx.ALIGN_CENTER)
	static_text_1.SetForegroundColour('red')  
	wx_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
	static_text_1.SetFont(wx_font)
	text_sizer.Add(static_text_1, 0, wx.ALIGN_LEFT)
	input_text_1 = wx.TextCtrl(self, -1, 'input_1', size=(HORI, -1))
	input_text_1.SetInsertionPoint(0)
	text_sizer.Add(input_text_1, 0, wx.ALIGN_LEFT)
	self.box_sizer.Add(text_sizer, 0, wx.ALIGN_LEFT)	
	





	self.area_text = wx.TextCtrl(self, -1, "", size=(HORI, 100), style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))
	self.area_text.SetInsertionPoint(0)
	self.area_text.Bind(wx.EVT_KEY_UP, self.OnSelectAll)
	self.box_sizer.Add(self.area_text)
	
	
	
	
	
	"""
	self.rich_text = wx.TextCtrl(self, -1, u'rich', size=(200, 100),
	                             style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP | wx.TE_RICH2))
	self.rich_text.SetInsertionPoint(0)
	f = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.BOLD, True)  
	self.rich_text.SetStyle(0, self.rich_text.GetLastPosition(), wx.TextAttr("red", "green", f))
	self.box_sizer.Add(self.rich_text)
	"""


def declare_button (self):
	#button
	#self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
	self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
	self.buttons = []

	for i in range (0, 2):
		self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
		self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)    
	
	self.sizer = wx.BoxSizer(wx.VERTICAL)
	#self.sizer.Add(self.control, 1, wx.EXPAND)    	
	self.sizer.Add(self.sizer2, 0, wx.GROW)    
	

	self.box_sizer.Add(self.sizer)

	self.Bind(wx.EVT_BUTTON, self.OnButton, self.buttons[0])
	
	self.Bind(wx.EVT_BUTTON, function.print_warning, self.buttons[1])
