#coding=utf-8

'''
ThreadLock 主要的作用是为每个线程绑定一个数据库，http请求和用户信息等
'''

import threading
#创建全局变量ThreadLock对象
lock_school = threading.local()  #lock_school 是ThreadLock的一个对象，可以理解为一个dict

def process_Student():
    print "my name is %s (in %s)" % (lock_school.student, threading.current_thread().name)

#绑定lock_student 和线程
def Process_Thread(name):
    lock_school.student = name    #lock_school.student ：一个线程的局部变量，key-student，value-name
    process_Student()

t1 = threading.Thread(target=Process_Thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=Process_Thread, args=('Bob',), name='Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()