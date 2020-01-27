#!/usr/bin/env python
import sys, time
from curses import wrapper

WAIT = 3 

def main(stdscr):
	"""
	print sys.argv[1]
	while True:
		time.sleep(WAIT)
		localtime = time.asctime( time.localtime(time.time()) )
		print localtime 
	"""
	print stdscr 
	print sys.argv[1]
	stdscr.clear()
    
	titlewindow = stdscr.subwin(1,80,4,0)
		
	titlewindow.addstr(0, 0, "ARES this is page")
	c = stdscr.getch()
	print c

	monitorwindow = stdscr.subwin(15,80,5,0)
	monitor_line_count = 1	
	while True:
		localtime = time.asctime( time.localtime(time.time()) )
		monitorwindow.clear()
		#monitorwindow.erase()
		#monitorwindow.addstr(monitor_line_count, 0, str(monitor_line_count) + " " + localtime)
		monitorwindow.addstr(0, 0, str(monitor_line_count) + " " + localtime)

		monitor_line_count += 1

		monitorwindow.refresh()

		time.sleep(WAIT)
		if monitor_line_count == 10:
			break


wrapper(main)

