#coding:utf8

'''
web设计 html的文本编程
'''

def application(environ, start_response):
    start_response('200 0k', [('Content-Type', 'text/html')])
    return '<h1>hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')