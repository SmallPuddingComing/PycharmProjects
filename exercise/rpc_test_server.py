#coding:utf8
'''
把本地函数放到远端去调用
'''


from SimpleXMLRPCServer import SimpleXMLRPCServer, AsyncXMLRPCServer, SimpleXMLRPCRequestHandler

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

def run():
    for i in xrange(1, 10000):
        print ("hello world")

# server = SimpleXMLRPCServer(('127.0.0.1', 8080))
print "Listening on port 8080"
# server.register_multicall_functions()
#
# server.register_function(add, 'add')
# server.register_function(subtract, 'subtract')
# server.register_function(multiply, 'multiply')
# server.register_function(divide, 'divide')
#
# server.serve_forever()

#多线程的支持，作者是自己封装继承了一个类，来自SocketServer.ThreadingMixIn 和 SimpleXMLRPCServer
server1 = AsyncXMLRPCServer(('127.0.0.1', 8080), SimpleXMLRPCRequestHandler)
server1.register_function(add, 'add')
server1.register_function(subtract, 'subtract')
server1.serve_forever()



#测试下rpc和Meaasge之间的差异

