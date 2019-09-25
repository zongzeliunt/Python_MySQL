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

	if n % 3 == 0:
		time.sleep (3)

	if n % 3 == 1:
		time.sleep (2)

	if n % 3 == 2:
		time.sleep (1)
	
	print ("this is thread num %s\n" % n)
	time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print time_format
	sm.release()


if __name__ == '__main__':
	sm = Semaphore(3)
	for i in range (10):
		t = threading.Thread (target = run, args=(i,))
		#must be args, not arg. variable must be (i,), not (i) 

		t.start()
	


#以上实验是有以下行为：
#2, 1, 0 三个进程倒着出
#2 release以后3号进程进来
#1 release以后4号进程进来
#0 release以后5号进程进来
#理论上说以上三个进程打出当时时间应该一致，因为：
#2等1秒，1等2秒，0等3秒
#3等3秒，4等2秒，5等1秒
#3，4,5 三个进程都会在程序执行后4秒时打出当时时间的message
#然后，6 的时刻=4+3=7
#7 = 4 + 2
#8 = 4 + 1
#9 是等8 release后开始的，所以9 = 5 （8的时刻）+ 3

#以上就是同步进程操作的例子



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



