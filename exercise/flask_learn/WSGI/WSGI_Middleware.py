#coding:utf8

'''
Created on 2016/4/27
根据url把用户请求调度到不同的application
均衡负载，分发用户的请求
限制请求速率，添加白名单
'''

class IPBlacklistMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ,  start_response):
        ip_add = environ.get("HTTP_HOST").split(':')[0]
        if ip_add not in ('127.0.0.1'):
            return forbidden(start_response)

        return self.app(environ, start_response)

def forbidden(start_response):
    start_response('403 Forbidden', [('content-Type', 'text/plain')])
    return ['Forbidden']

def not_found(start_response):
    start_response('404 Not Found', [('content-Type', 'text/plain')])
    return ['Not Found']

def application(environ, start_response):
    # start_response('200 OK', [('content-Type', 'text/plain')])
    # return ['This is a happy python application!']
    path = environ.get('PATH_INFO', '').lstrip('/')
    mapping = {'dog': dog, 'cat': cat}

    call_back = mapping[path] if path in mapping else not_found
    return call_back(start_response)

def dog(start_response):
    start_response('200 OK', [('content-Type', 'text/plain')])
    return ['This is a dog']

def cat(start_response):
    start_response('200 OK', [('content-Type', 'text/plain')])
    return ['This is a cat']

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    application = IPBlacklistMiddleware(application)
    server = make_server('0.0.0.0', 8080, application)
    server.serve_forever()