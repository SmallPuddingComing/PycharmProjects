#coding:utf8

'''
Created on 2016/4/27
server / Gateway Side
主要是专注于HTTP层面的业务，重点是接收http请求和提交并发，不对 url或method内容做处理。
'''

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is a python application!']

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8080, application)#为environ提供必要的参数，返回一个回调函数start_response
    server.serve_forever()