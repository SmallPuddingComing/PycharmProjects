#coding:utf8

import time
''' create a timer'''

class Timer(object):
    '''calc time'''
    def __init__(self, verbose=True):
        self.varbose = verbose

    def __enter__(self):
        print 'start'
        self.startTime = time.time()

    def __exit__(self, *args):
        self.endTime = time.time()
        self.secs = self.endTime - self.startTime
        self.msecs = self.secs * 1000
        if self.varbose:
            print "use total time %s s"% self.secs

import threading
class Timer_1(threading.Thread):
    ''' control exit time of threading'''
    def __init__(self, fn, sleep=0, args=(), lastDo=True):
        threading.Thread.__init__(self)
        self.fn = fn
        self.args = args
        self.sleep = sleep
        self.lastDo = lastDo
        self.setDaemon(True)#讲一个线程设置为守护线程
        #两个标记符号
        self.fnPlay = False
        self.isPlay = True

    def __do(self):
        self.fnPlay = True
        apply(self.fn, self.args)
        self.fnPlay = False

    def run(self):
        while self.isPlay:
            time.sleep(self.sleep)
            self.__do()

    def stop(self):
        self.isPlay = False
        while True:
            if not self.fnPlay:break
            time.sleep(0.01)

        if self.lastDo:
            self.__do()


def run():
    for i in xrange(1, 10000):
        print "Hello World"


with Timer() as t:
    run()
    print "use total time %s s" %  t.secs#此时这里报错是因为已经退出上下文环境了，变量t无效



