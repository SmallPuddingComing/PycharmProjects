#coding:utf8

'''
Creater on:2015/11/25
'''

import smtplib
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.encoders import encode_base64
from email.utils import formataddr, parseaddr

class smtp(object):

    #初始化需要用到的变量
    def set_smtp(self, from_addr, password, to_addr, smtp_server):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server
        self.msg = MIMEMultipart('alternative')#创建兼容性邮件

    #对地址中的昵称进行编码
    def _from_addr(self, str):
        name, addr = parseaddr(str)
        formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8')))

    #添加文本邮件
    def _add_text(self, str):
        self.msg.attach(MIMEText(str, 'plain', 'utf-8'))

        #信件的抬头信息
        self.msg['From'] = self._from_addr('发件人:<%s>' % self.from_addr)
        self.msg['To'] = self._from_addr('收件人：<%s>' % self.to_addr)
        self.msg['Subject'] = Header('主题：', 'utf-8').encode()

    #添加html邮件
    def _add_html(self, str):
        self.msg.attach(MIMEText(str, 'html', 'utf-8'))

    #添加的文件附件
    def _add_file(self, name, type_of_name, type):
        with open(name, 'rb') as f:
            mime = MIMEBase(type, type_of_name, filename=name)#附件的类型， 附件后缀， 附件名

            #头信息
            mime.add_header('Connect-Disposition', 'attachment', filename=name)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')

            mime.set_payload(f.read()) #读入附件的内容
            encode_base64(mime)        #编码64
            self.msg.attach(mime)      #添加附件

    def send_mail(self):
        server = smtplib.SMTP(self.smtp_server, 25)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()


if __name__ == '__main__':
    email = smtp()
    email.set_smtp('m15575824785@163.com', 'yr2015419119', '1076643147@qq.com', 'smtp.163.com')
    email._add_text('Hello!')
    email._add_html('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>',)
    email._add_file('e:/bt.jpg', 'jpg', 'image')#将图片cid:0.png放到同一文件夹
    email.send_mail()


