#coding = utf-8

'''
this is multiprocessing pragram
'''

import os
from multiprocessing import  Process

#print 'this is folk ....(%s) ' % os.getpid()  # mac python

#child = os.fork()

#if not child:
#    print 'I am a child process (%s) ,my father is (%s)' % (child.getpid(), child.getppid())
#else:
#    print 'I am a root process (%s),create the child process (%s)' % (child.getpid(), child)


def run_p(name):
    print "Run child pracess name is %s (%s)" % (name, os.getpid())

if __name__ == '__main__':
    print "this is a process %s" % os.getpid()
    p = Process(target=run_p, args=('test',))      #just for send args,create a process instance
    print "child process will start"
    p.start()                                      # start a process
    p.join()                                       # achieve a tongbu deal
    print "Process end"


