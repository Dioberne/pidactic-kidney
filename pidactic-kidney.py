#!/usr/bin/python

from __future__ import with_statement
from multiprocessing import Process, Value
import multiprocessing
import random
import time

#Globals
trials = 50000
radius = 10
threads = multiprocessing.cpu_count()
#trails per thread 
tpt = trials / threads
#Will be the sum of all trials. Used to determine the actual expectation
expectation = Value('d', 0.0)
lock = multiprocessing.Lock()


def walk():
	"""Runs multiple trials of a random walk"""
	for k in range(tpt):
		x = 0
		inside = True
		steps = 0
		while inside:
			
			steps = steps + 1
			
			flip = random.randint(0,1)	
			
			if flip == 1:
				x = x + 1
			else:
				x = x - 1
			
			if x >= radius or x <= -radius:
				 
				with lock:
					global expectation
					expectation.value =  expectation.value + steps
					# print "We made it ", expectation, " steps!"
				inside = False



def worker(num):
    """Calls the walk. This could probably be avoided"""

    walk()
    #print 'Worker:', num
    return


if __name__ == '__main__':
    start = time.time()
    jobs = []
    for i in range(threads):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    for k in range(threads):
    	p.join()
    print "The average number of steps is ", expectation.value / trials, " steps"
    end = time.time()
    print "This program took ", end - start, " seconds to run"
