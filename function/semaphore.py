#from leetcode #1115
from multiprocessing import Process,Semaphore
import threading
import time

"""
#version 0 
def run (n):
	semaphore.acquire()
	time.sleep(5)
	print ("run the thread %s\n" % n)


	semaphore.release()


if __name__ == '__main__':
	semaphore = threading.BoundedSemaphore(5)
	for i in range (20):
		t = threading.Thread(target=run, args=(i))
		t.start()

while threading.active_count() != 1:
	pass
else:
	print ('---all threads done--')

"""

#version 1 
def run (n):
	sm.acquire()
	#time.sleep(3)
	print ("this is thread num %s\n" % n)
	sm.release()


if __name__ == '__main__':
	sm = Semaphore(3)
	for i in range (10):
		t = threading.Thread (target = run, args=(i,))

		t.start()
	






"""
class FooBar(object):
    def __init__(self, n):
        self.n = n
        from threading import Semaphore
        self.semfoo = Semaphore(1) 
        self.sembar = Semaphore(0)
        
    def foo(self, printFoo):
"""
        #:type printFoo: method
        #:rtype: void
"""
        for i in xrange(self.n):
            self.semfoo.acquire()
            print "Foo"
            self.sembar.release()

    def bar(self, printBar):
"""
        #:type printBar: method
        #:rtype: void
"""
        for i in xrange(self.n):
            self.sembar.acquire()
            print "Bar"
            self.semfoo.release()
"""



