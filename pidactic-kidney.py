#!/usr/bin/python

import multiprocessing
import random
import time
import math

"""
This version uses multiprocessing.map and 4 times faster than the older version.
"""
#Globals
trials = 10000
radius = 10
threads = multiprocessing.cpu_count()
#trails per thread
tpt = math.ceil( trials / threads )

def walk(rad):
    """Runs multiple trials of a random walk"""

    steps = 0
    for k in range(tpt):
        x = 0
        inside = True
        while inside:
            steps = steps + 1

            #Coin flip
            if bool(random.getrandbits(1)):
                x = x + 1
            else:
                x = x - 1

            if not( -rad < x < rad): #x >= rad or x <= -rad:
                inside = False

    return steps / tpt


if __name__ == '__main__':
    start = time.time()

    jobs = []
    for k in range(threads):
        jobs.append(radius)

    pool = multiprocessing.Pool(threads)

    #Map runs walk(radius) for each "job" and stores the result
    results = pool.map(walk, jobs)

    end = time.time()
    print ("The average number of steps is ", math.ceil(sum(results) / len(results)), " steps")
    print ("This program took ", end - start, " seconds to run")
    print ("There are ", threads, " threads and ", tpt, " trials per thread.")
