#coding:utf8

'''
Created on 2016-4-7
flask除了request对象之外，还有一个对象是class::flask.session
作用：允许你再不同的请求之间存贮特定的用户信息，在cookies基础上对cookies进行加密
疑惑的地方：在app.run()直接在一个网址上进行了url '/'的调用，那其他的怎么调用？
'''

from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return "Login in as %s" % escape(session['username'])
    return "You are not logged in"

@app.route('/login', methods=['POST'])#['GET', 'POST']
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    redirect(url_for('index'))

app.secret_key = "A0Zr98j/3yX R~XHH!jmNJLWX/,?RT"

if __name__ == '__main__':
    with app.test_request_context():
        print url_for('login', username='John Doe')
        redirect(url_for('index'))
        print url_for('logout')

    app.run(host='127.0.0.1', port=8657)

