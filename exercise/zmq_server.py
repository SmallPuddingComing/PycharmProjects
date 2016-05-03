#coding:utf8

'''
实现 zmq的消息队列
过程：
    1、选择传输协议
        四种：inproc/ipc/multicast/tcp
    2、建立基础
        Queue、Rorwarder、streamer
    3、选择通信模式
        req--rep / pub--sub / upstream--downstream / pair
'''

#负载均衡模式 Req_Rep
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5400")

while 1:
    msg = socket.recv()
    print "Got" ,msg
    socket.send(msg)


#PUB-sub模式组合下是松耦合，类似于广播电视台
from random import choice
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5400")

countries = ['N','B','G','P']
events = ['yellow', 'red', 'goal', 'corner', 'foul']

while 1:
    msg = choice(countries) + " " + choice(events)
    print "->", msg





