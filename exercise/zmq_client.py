#coding:utf8

import zmq

#REQ_REP
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://127.0.0.1:6000")
socket.connect("tcp://127.0.0.1:5400")
for i in xrange(10):
    msg = "msg %s" % i
    socket.send(msg)
    print "Sending ", msg
    msg_in = socket.recv()

#SUB_PUB
'''接收'''