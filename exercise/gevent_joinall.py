#coding:utf8

import time
import gevent
from gevent import select

start = time.time()
tic = lambda :'at %1.1f secodes' % (time.time() - start)

def gr1():
    print('Started Polling:' , tic())
    select.select([], [], [], 2)
    print('Ended Polling', tic())

def gr2():
    print('Started Polling:' , tic())
    select.select([], [], [], 2)
    print('End Polling:', tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, at", tic())
    gevent.sleep(1)

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(gr1), gevent.spawn(gr2), gevent.spawn(gr3)])