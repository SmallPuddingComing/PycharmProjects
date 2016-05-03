#coding:utf8

'''
Created on 2016-4-7
'''
from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for
from flask import abort, render_template, flash

#create our little application
app = Flask(__name__)
#定义模块的配置选线调用from_object（），或者是导入路径应该加载的模块
app.config.from_object(__name__)

#configuration
# print type(app.config)
app.config.update(
DEBUG = True,
SECRET_KEY = 'development key',
USERNAME = 'admin',
PASSWORD = '123456',
DATABASE = 'D:/tmp/flaskr.db')
#加载配置从一个环境变量到一个配置文件，只是快捷方式
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#连接
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

#优雅的连接数据库
@app.before_request
def before_request():
    g.db = connect_db()

#关闭数据库，返回回应
@app.after_request
def after_request(response):
    g.db.close()
    return response

#视图函数把所有的文章以字典的方式传递给show_entries.html模板
@app.route('/')
def show_entries():
    before_request()
    cur = g.db.execute('select title, text from entries order by id desc' )
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print entries
    if entries:
        after_request('ok')
        return render_template('show_entries.html', entries=entries)
    # else:#一条龙服务
    #     after_request('ok')
    #     return redirect(url_for('add_entry', title='hello world', text='i love you !'))
    after_request('ok')

#添加一篇新文章，使用GET进行请求，传说中的一条龙服务
# @app.route('/add', methods=['GET'])
# def add_entry():
#     print type(request.args), request.args
#     # if not session.get('logged_in'):
#     #     abort(401)
#     before_request()
#     g.db.execute('insert into entries (title, text) values (?, ?)',
#                  [request.args.get('title'), request.args.get('text')])
#     g.db.commit()
#     after_request('ok')
#     flash('New entry was sucessfully posted')
#     return redirect(url_for('show_entries'))

#添加一篇新文章,使用POST进行请求。发现test测试不能使用重定向和使用数据库插入数据
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    before_request()
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    after_request('ok')
    flash('New entry was sucessfully posted')
    return redirect(url_for('show_entries'))

#登陆和登出
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # print request, app.config, type(request.form['username']), type(app.config['USERNAME'])
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#注销
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    # init_db()
    app.run(host='127.0.0.1', port=8976)
