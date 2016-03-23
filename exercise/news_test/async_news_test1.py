#coding:utf8

import gevent
from gevent.event import AsyncResult

a = AsyncResult()

def xiaodi():
    print "xiaodi begin..."
    gevent.sleep(10)
    a.set("hello world")
    print "xiaodi work is over"

def boss():
    print "dage is begin..."
    print a.get() #blocking
    print "I live!"

gevent.joinall([gevent.spawn(xiaodi), gevent.spawn(boss)])


