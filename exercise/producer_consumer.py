#coding:utf8

'''
经典的消费者和生产者的问题，当剩余的产品少于1000，生产者就生成一百，如果剩余的产品多余100时就消费者消费三个
实际处理的是线程之间的相互等待和运行，进行条件变量的控制进行切换
'''

import time
import threading
from Queue import Queue

# class Producer(threading.Thread):
#   '''变量同步机制解决了生产者和消费者的要求
#   '''
#     def run(self):
#         global count
#         while 1:
#             if con.acquire():
#                 if count > 1000:
#                     con.wait()
#                 else:
#                     count += 100
#                     msg = self.name + 'produce 100 , count=' + str(count)
#                     print msg
#                     con.notify()
#                 con.release()
#                 time.sleep(1)
#
# class Consumer(threading.Thread):
#     def run(self):
#         global count
#         while 1:
#             if con.acquire():
#                 if count < 100:
#                     con.wait()
#                 else:
#                     count -= 3
#                     msg = self.name + 'consume 3 , count=' + str(count)
#                     print msg
#                     con.notify()
#                 con.release()
#                 time.sleep(1)
#
# count = 500
# con = threading.Condition()
#
# def test():
#     for i in xrange(2):
#         p = Producer()
#         p.start()
#     for i in xrange(5):
#         c = Consumer()
#         c.start()


class Producer(threading.Thread):
    '''队列同步机制，实现线程之间的切换
    '''
    def run(self):
        global queue
        count = 0
        while 1:
            for i in xrange(100):
                if queue.qsize() > 1000:
                    pass
                else:
                    count += 1
                    msg = '生成产品: ' + str(count)
                    queue.put(msg)
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while 1:
            for i in xrange(3):
                if queue.qsize() < 100:
                    pass
                else:
                    msg = self.name + '消费了 ' + queue.get()
                    print msg
            time.sleep(1)

queue = Queue()

def test():
    for i in xrange(500):
        queue.put('初始化产品 '+str(i))
    for i in xrange(2):
        p = Producer()
        p.start()
    for i in xrange(5):
        c = Consumer()
        c.start()

if __name__ == '__main__':
    test()