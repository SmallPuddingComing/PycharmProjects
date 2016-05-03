#coding = utf-8

'''
deal the lots of process with the process pool(jinchengchi)
'''

from multiprocessing import Pool
import os
import time
import random

def run_child(name):
    print "Run task %s (%s)" % (name, os.getpid)
    start = time.time()
    time.sleep(3 * random.random())
    end = time.time()
    print "process %s run the time %0.2f" % (name, (end - start))

if __name__ == '__main__':
    print "create a process %s" % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(run_child, args= (i,))
    print "waiting for all subprocess done"
    p.close()
    p.join()
    print "All processes done"

