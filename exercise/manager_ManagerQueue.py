#coding=utf-8

'''
manager many of queue to deal with the process
'''

#此案例为异步处理进程，进程之间网络通信处理任务
#任务管理类

import time
import random
import Queue
from multiprocessing.managers import BaseManager  #任务管理队列的基类

#Create two queue
task_queue = Queue.Queue()
result_queue = Queue.Queue()

class ManagerQueue(BaseManager):
    pass

#resigin queue on web, callable link to queue object
ManagerQueue.register('get_task_queue', callable=lambda: task_queue)
ManagerQueue.register('get_result_queue', callable=lambda: result_queue)
#绑定端口5000，设置验证码‘abc'
manager = ManagerQueue(address=('', 5000), authkey = 'abc')
#启动queue
manager.start()
#获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放进个任务进去
for i in range(10):
    d = random.random(1, 1000)
    print "Put task %s" % d
    task.put(d)

print "workmanager reback the result....."
#从result队列返回计算结果
for  i in range(10):
    t = result.get(timeout = 10)
    print "result is %s" % t

#任务结束，关闭队列管理
manager.shutdown()
print "task work is over"