'''
Created on Sep 7, 2012
@author: Christoph Gerneth
'''

from ledbar import *
from time import sleep

def lauflicht(pattern):
    '''
    example usage: Oppa Knightrider Style!
    '''
    LEDBAR_LEN = 20
    b = Ledbar(LEDBAR_LEN, latch_pin=1, clock_pin=2, data_pin=3)

    queue = deque(pattern)
    while True:
        for i in xrange(LEDBAR_LEN):
            queue.rotate()
            b.setPattern(queue)
            sleep(0.2)
            
        for i in xrange(LEDBAR_LEN):
            queue.rotate(-1)
            b.setPattern(queue)
            sleep(0.2)


if __name__ == "__main__":

	# example 1:
    pattern = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    lauflicht(pattern)

	## example 2:
    #x = Statusbar(30, latch_pin=1, clock_pin=2, data_pin=3)
    #x.setPercentage(50)
    
