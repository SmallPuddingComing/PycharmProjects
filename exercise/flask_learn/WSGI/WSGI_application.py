#coding:utf8

'''
Created on 2016/4/27
learn the WSGI framwork of flask
'''

#method of callobject
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is a python application!']

#class of callobject
class Application(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK', [{'Content-type':'text/plain'}])
        yield "hello world!"



