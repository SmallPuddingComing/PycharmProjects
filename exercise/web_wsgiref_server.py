#coding:utf8

from wsgiref.simple_server import make_server
from web_design import application

httpd = make_server('', 8999, application)
print "Server HTTP on port 8999...."
#开始监听http的请求
httpd.serve_forever()

