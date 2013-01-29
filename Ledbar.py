#!/usr/bin/env python
#-*- coding:utf-8 -*-

from collections import deque
try:
	import RPI.GPIO as GPIO
except ImportError:
	print "could not find RPI.GPIO..."
	import FakeGPIO as GPIO



class Ledbar(object):
	"""
	a shiftregister control object for raspberry pi
	"""

	def __init__(self, length, latch_pin, clock_pin, data_pin):

		self.latch, self.clock, self.data = latch_pin, clock_pin, data_pin
		#self = [0]*length #initialize array with 0
		self.length = length
		
		#initialize GPIOs
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.latch, GPIO.OUT)
		GPIO.setup(self.clock, GPIO.OUT)
		GPIO.setup(self.data,  GPIO.OUT)
		#every output should be low
		GPIO.output(self.clock, GPIO.LOW)
		GPIO.output(self.latch, GPIO.LOW)
		GPIO.output(self.data,  GPIO.LOW)
		
		self.clear()
		
	def setPattern(self, pattern):
		"""
		push pattern in register memory and display.
		A pattern is an Array containing 0 for LOW and 1 for HIGH
		True or False should work as well.
		"""
		if not len(pattern) > self.length: 		
			for bit in pattern:
				self.push(bit)
			self.flush()
		else:
			raise ValueError("pattern longer than ledbar")
			
	def clear(self):
		"""clear the display an register"""
		for i in xrange(self.length):
			self.push(0)
		self.flush()		
		
	def push(self, bit):
		"""push one bit into register memory"""
		GPIO.output(self.clock, GPIO.HIGH)
		GPIO.output(self.data, (GPIO.HIGH if bit==1 else GPIO.LOW))
		GPIO.output(self.clock, GPIO.LOW)
		GPIO.output(self.data, GPIO.LOW)
	
	def flush(self):
		"""flush output"""
		GPIO.output(self.latch, GPIO.HIGH)
		GPIO.output(self.latch, GPIO.LOW)

	def getLength(self):
		return self.length
	
	

class Statusbar(Ledbar, deque):
	def __init__(self, length, latch_pin, clock_pin, data_pin):
		super(Statusbar, self).__init__(length, latch_pin, clock_pin, data_pin)
		self = [0]*self.length

	def setLeds(self, source):
		if len(source) <= self.getLength()-1:
			self = [0] * self.getLength()
			self[0:len(source)] = source
			self.setPattern(self)
		else:
			raise ValueError("len(source) > len(target)")

	def setPercentage(self, percent):
		#clean dirty values
		if percent >= 100:
			percent = 100
		elif percent < 0:
			percent = 0
		
		# 1 2 3 4 5 6 7 8 9 10
		# 1 1 0 0 0 0 0 0 0 0
		# 20%
		percentPattern = [1]* int(round((float(self.getLength())/100.0 * percent)))
		#self.setLeds(percentPattern)