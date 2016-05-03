#coding:utf8

'''
Create on: 2015/11/24
author: YuanRong
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _from_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#通过SMTP发送出去
from_addr = "1076643147@qq.com"#raw_input("From: ")
password = "yr21319937168" #raw_input("Password: ")
#输入SMTP服务器的地址
smtp_server = "smtp.qq.com"#raw_input("SMTP server: ")
#输入收件人的地址
to_addr = "m15575824785@163.com"#raw_input("To: ")

#构建一个简单的纯文本文件
msg = MIMEText("hello, send by python...", 'plain', 'utf-8')
msg['From'] = _from_addr('Pothon爱好者 <%s>' % from_addr)
msg['To'] = _from_addr('qq管理员 <%s>' % to_addr)
msg['Subject'] = "Hello"

import smtplib
#连接服务器的端口 stmp.qq.com
server = smtplib.SMTP(smtp_server, 25)
#打印出和SMTP服务器交互的所有消息
server.set_debuglevel(1)
#登陆SMTP服务器
server.login(from_addr, password)
#发送邮件，一次可以发给多个人，二个参数可以为list，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
