#coding=utf-8

'''
function : deal with the data with calculator
'''

import sys
import time
import Queue
from multiprocessing.managers import BaseManager

class ManagerQuene(BaseManager):
    pass

#由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
ManagerQuene.register('get_task_queue')
ManagerQuene.register('get_result_queue')
#链接网络IP
server_addr = '127.0.0.1'
print("Connect to server %s"  % server_addr)
#验证端口
m = ManagerQuene(address=(server_addr,5000), authkey='abc')
m.connect()
#获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()
#处理从queue中获取的数据，这里是计算
for i in range(10):
    try:
        n = task.get(timeout=10)
        print "run task (%d, %d)" % (n, n)
        r = "%d * %d = %d " %(n,n, n*n)
        result.put(r)
    except Queue.Empty:
        print("task queue is empty..")

print ("worktask exit !")