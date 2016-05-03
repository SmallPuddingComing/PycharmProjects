#coding = utf-8

'''
threading
'''

import time
import threading

def loop():
    print "thread %s is Running" % (threading.current_thread())
    n = 0
    while n < 5:
        n = n + 1
        print "thread %s >>> %s"  % (threading.current_thread().name, n)
        time.sleep(1)
    print "thread %s ended" % threading.current_thread()



if __name__ == '__main__':
    print "thread %s is Running" % threading.current_thread().name
    t = threading.Thread(target=loop, name = 'LoopThread')
    t.start()
    t.join()
    print "thread %s is end" % threading.current_thread().name