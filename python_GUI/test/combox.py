import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None,title="select list",size=(400,130))
        self.Center() 
        panel=wx.Panel(parent=self)
        hbox1=wx.BoxSizer(wx.HORIZONTAL)
        statictext=wx.StaticText(panel,label='select lang')
        list1=['Python','Java',"C++"]
        ch1=wx.ComboBox(panel,-1,value='C',choices=list1,style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX,self.on_combobox,ch1)

        hbox1.Add(statictext,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox1.Add(ch1,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)

        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        statictext=wx.StaticText(panel,label='select sex')
        list2=['M','F']
        ch2=wx.Choice(panel,-1,choices=list2)
        hbox2.Add(statictext,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox2.Add(ch2,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)

        self.Bind(wx.EVT_CHOICE,self.on_choice,ch2)
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox2,1,flag=wx.ALL|wx.EXPAND,border=5)

        panel.SetSizer(vbox)

    def on_combobox(self,event):
        print("select{0}".format(event.GetString()))

    def on_choice(self,event):
        print("select{0}".format(event.GetString()))

class App(wx.App):
    def OnInit(self):
        frame=MyFrame()
        frame.Show()
        return True
    def OnExit(self):
        print("exit")
        return 0

if __name__=='__main__':
    app=App()
    app.MainLoop()
