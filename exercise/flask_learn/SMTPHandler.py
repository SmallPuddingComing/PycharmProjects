#coding:utf8

'''
Created on 2016/4/26
处理正常异常
'''
from flask import Flask

app = Flask(__name__)

file_handler = None
mail_handler = None
#报错邮件
ADMINS = ['1076643147@qq.com']
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1',
                               'server-error@qq.com',
                               ADMINS, 'YourApplication Failed')
    mail_handler.setLevel(logging.ERROR)
    # app.logger.addHandler(mail_handler)
    #日志格式
    from logging import Formatter
    mail_handler.setFormatter(Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
'''))

#日志文件(FileHandler, RotatingFileHandler, NTEventHandler, SysLogHandler)
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('test.txt', mode='a')
    file_handler.setLevel(logging.WARNING)
    # app.logger.addHandler(file_handler)
    #日志格式 set fmt for logger.Handler
    from logging import Formatter
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s' '[in %(pathname)s:%(lineno)%d]'))


#其他代码库，不建议使用logging一次性配置完所有的日志，因为用到什么就配置什么，运行多个程序的时候不能进行单独的配置
# 通过getLogger（）获取所有日志处理器
from logging import getLogger
loggers = [app.logger, getLogger('sqlalchemy'), getLogger('otherlibrary')]
for logger in loggers:
    logger.addHandler(mail_handler)
    logger.addHandler(file_handler)


