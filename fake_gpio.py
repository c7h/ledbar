#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @author: Christoph Gerneth

"""pseudo GPIO-Library for debugging - RasPi not yet delivered ;-)"""

import sys

try:
    import curses
except:
    print "could not find curses-lib"

OUT = "out"
IN = "in"
BOARD = "board"
HIGH = "H"
LOW  = "L"

usedpins = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
	
def setmode(modus):
	sys.stdout.write("setmode auf %s\n" % modus)

def setup(pinNo, mode):
	sys.stdout.write("setup for pin %i: %s\n" % (pinNo, mode) )
	if not pinNo in usedpins:
		usedpins.append(pinNo)

def output(pin, bit):
	'''this is a test'''	
	
#	#test	
#	global counter
	if pin == usedpins[0]:
		sys.stdout.write(bcolors.OKBLUE + bit + bcolors.ENDC)
	if pin == usedpins[1]:
		sys.stdout.write(bcolors.OKGREEN + bit + bcolors.ENDC)
	if pin == usedpins[2]:
		sys.stdout.write(bcolors.FAIL + bit + bcolors.ENDC)

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
