#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""pseudo GPIO-Library"""

import sys
import curses

OUT = "out"
IN = "in"
BOARD = "board"
HIGH = "H"
LOW  = "L"



def setmode(modus):
	sys.stdout.write("setmode auf %s\n" % modus)

def setup(pinNo, mode):
	sys.stdout.write("setup for pin %i: %s\n" % (pinNo, mode) )

def output(pin, bit):
	#sys.stdout.write("%i : %s\n" % (pin, bit))	
	'''this is a test'''	
	
#	#test	
#	global counter
	if pin == 3:
		sys.stdout.write(bit)
#		if bit == "L":
#			sys.stdout.write("_")
#		else:
#			sys.stdout.write("-")
#		counter += 1 
#
#	if counter == 39:
#		sys.stdout.write("\n")
#		sys.stdout.flush()
#		counter = 0


class CursesWindow:
	'''
	@todo: fertig machen
	'''
	__single = None
	def __init__(self, size):
		if CursesWindow.__single:
			raise CursesWindow.__single
		CursesWindow.__single = self
		self.xsize, self.ysize = size
		self.screen = curses.initscr()
		curses.resizeterm(self.ysize, self.xsize)
		curses.cbreak()
		
	def printbyte(self, bit):
		#@todo: implement method
		pass
	
	def __del__(self):
		'''
		end curses mode and revert to normal stdio-mode
		'''
		curses.nocbreak()
		curses.endwin()
