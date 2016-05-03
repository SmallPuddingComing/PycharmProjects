#coding:utf8

import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:6000")

while 1:
    msg = socket.recv()
    print "Got" ,msg
    socket.send(msg)