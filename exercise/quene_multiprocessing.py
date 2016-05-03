#coding=utf-8

'''
many of subprocess connect  each other below the parent process
'''

from multiprocessing import Process, Queue
import os
import time
import random

#writter process
def write_p(q, item):
    for value in item:
       print "put a value %s input %s " % (value, q)
       q.put(value)
       time.sleep(random.random())

#reas process
def read_p(q):
    while True:
        value = q.get(True)
        print "get value is %s" % value


if __name__ == '__main__':
    #create parent process
    q = Queue()
    list_1 = list(raw_input("enter a list :"))
    pw = Process(target=write_p, args=(q, list_1))
    pr = Process(target=read_p, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
