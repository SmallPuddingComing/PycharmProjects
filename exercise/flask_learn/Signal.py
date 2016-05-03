#coding:utf8

'''
Created on 2016/4/26
信号订阅机制
Flask信号(signals, or event hooking)
允许特定的发送端通知订阅者发生了什么（既然知道发生了什么，那我们可以知道接下来该做什么了）
Flask钩子(hocking)
用于特定的装饰器，例如request_befor
'''
from flaskr import flaskr
from flask import Flask
from flask import template_rendered
from contextlib import contextmanager

# app = Flask(__name__)

#装饰器基于信号
@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

if __name__ == '__main__':
    #用在单元测试中找出当前渲染的模板和传入模板变量的助手g/request/seesion
    with captured_templates(flaskr.app) as templates:
        rv = flaskr.app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == "show_entries.html"#"index.html"
        # assert len(context['items']) == 10