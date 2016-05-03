#coding:utf8

'''
Create on 2016-4-7
flask 框架的小应用，涉及到路由
发现时默认的端口被占用。自己修改一个端口
'''

from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import abort
from flask import redirect


#类的实例将会是我们的WSGI程序
#实例化类，吧模块和包的名字传给它，这样Flask就会知道它 将要到哪里寻找模板，静态文件之类的东西.
app = Flask(__name__)

#使用route装饰器告诉Flask那个网址将会被触发
@app.route('/')#参数有url和**options，options选择来自（GET.POAT,HEAD）,默认为是监听GET和隐式HEAD
def hello_world():
    return "Hello World!"

#route 的作用就是讲一个函数绑定到一个网址上，
# 还可以构造动态的网址并给函数附加多个规则
@app.route('/')
def index():
    #跳转
    return redirect(url_for('login'))#重定向提前中断一个请求并返回错误码

@app.route('/hello')
def hello():
    return "hello world!"

#变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    #显示该用户的配置文件
    pass

@app.route('/post/int<int:post_id>')
def show_post(post_id):
    #显示给定id，是哟一个整数
    pass

@app.route('/login')
def login():
    abort(401)

#跳转和错误
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#构建URL
with app.test_request_context():
    print url_for('index')#使用url_for构建网址
    print url_for('hello')
    print url_for('login', next='/')
    print url_for('show_user_profile', username='John Doe')
    url_for('static', filename='style.css')
    url_for('page_not_found', error=404)

if __name__ == '__main__':
    #填写需要连接的ip和端口，默认的是127.0.0.1 5000
    app.run(host='127.0.0.1', port=8892, debug=True)
