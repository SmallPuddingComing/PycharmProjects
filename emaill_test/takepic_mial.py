#coding:utf8

'''
Create on:2015/11/24
author: YuanRong
'''

from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib

def _from_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),
                       addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#通过SMTP发送出去
from_addr = "m15575824785@163.com"#raw_input("From: ")
password = "yr2015419119" #raw_input("Password: ")
#输入SMTP服务器的地址
smtp_server = "smtp.163.com"#raw_input("SMTP server: ")
#输入收件人的地址
to_addr = "myself_way@sina.cn"#raw_input("To: ")

msg = MIMEMultipart()
msg['Subject'] = Header('For my friend', 'utf-8').encode()
msg['From'] = _from_addr('管理员 <%s>' % from_addr)
msg['To'] = _from_addr('收件人 <%s>' % to_addr)

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('/Users/yuanrong/Desktop/美女照片/bt.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename = 'bt.jpg')
    mime.add.header('Connect-Disposition', 'attachment', filename='bt.jpg')
    mime.add.header('Connect-ID', '<0>')
    mime.add.header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
#server.starttls()
server.set_debuglevel(1)
server.login(smtp_server, password)
server.sendmail(smtp_server, [to_addr], msg.as_string())
server.quit()
