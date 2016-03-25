#coding:utf8
import gevent
from gevent.event import AsyncResult

class Calc(object):
    def __init__(self):
        self.async = AsyncResult()
        self.mydict = {}
        self.mylist = []

    def calcNumberAuto(self, isFlag=False):
        print "atuo begin..."
        for i in xrange(10):
            self.mydict[i] = i
        if isFlag:
            # self.async = AsyncResult()
            self.mylist.extend(self.async.get(True,10))
            print "get value for aysnc", self.mylist
        mylist = self.mylist
        return mylist

    def calcNumberHandler(self, numList):
        print "handler begin..."
        if numList:
            self.async = AsyncResult()
            self.async.set(numList)
            print "save the list"
            return True
        return False

if __name__ == '__main__':
    c = Calc()
    ulist = [{'name':'lii', 'uid':10002}, {'name':'wu', 'uid':12212}]
    # gevent.joinall([gevent.spawn(c.calcNumberHandler, ulist), gevent.spawn(c.calcNumberAuto, True)])
    if c.calcNumberHandler(ulist):
        print c.calcNumberAuto(True)


