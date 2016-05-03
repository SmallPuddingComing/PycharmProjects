#coding=utf-8  #plase not add blackkey

'''
many of threading has lock to deal with var changer
'''
#Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
#多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

import  time
import threading
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def loop(n):
    for i in range(100):
        lock.acquire()            #just one thread get a lock
        try:
           change_it(n)           #change the variable
        except EOFError, e:
            print EOFError("now is buys ,variable is change more")
        finally:
            lock.release()       #closs the function of lock


t1 = threading.Thread(target=loop, args=(5,))
t2 = threading.Thread(target=loop, args=(8,))

#start the thread t1 and t2
t1.start()
t2.start()

t1.join()
t2.join()

print  balance

# 这个例子表明如果线程不加锁的话，对于共享的变量的多次修改会有较大的隐患
bb = 0
x1 = bb + 5

x2 = bb + 8
bb = x2

bb = x1
x1 = bb - 5
bb = x1

x2 = bb - 8
bb = x2

print bb
