class FooBar(object):
    def __init__(self, n):
        self.n = n
        from threading import Semaphore
        self.semfoo = Semaphore(1) 
        self.sembar = Semaphore(0)
        
    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.semfoo.acquire()
            printFoo()
            self.sembar.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.sembar.acquire()
            printBar()
            self.semfoo.release()
