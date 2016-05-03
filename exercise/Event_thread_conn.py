#coding:utf8

import time
import random
import threading

class MyThread(threading.Thread):
    def __init__(self, threadName, event):
        threading.Thread.__init__(self, name=threadName)
        self.threadEvent = event

    def run(self):
        print "%s is ready" % self.name
        self.threadEvent.wait()
        print "%s run!" % self.name

sinal = threading.Event()
for i in xrange(10):
    t = MyThread(str(i), sinal)
    t.start()

sinal.set()