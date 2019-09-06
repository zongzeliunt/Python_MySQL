class MyClass1(object):
    def __init__(self):
        self.foo = 'updog'
        MyClass1.foobar = bar

class MyClass2(object):
    def __init__(self):
        self.val = 1
        MyClass2.show_val = show_val

def bar(self):
    print "What's " + self.foo

def show_val(self):
	print "self val is: " + str(self.val)

x = MyClass1()
x.foobar()

y = MyClass2()
y.show_val()
