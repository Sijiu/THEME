# -*- coding: utf-8 -*-
__author__ = 'wxy'

from QQLogin import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class sendEmail():
    def __init__(self):
        self.user = "ayabishop@sina.com"
        self.pwd = "taotieXY!@"
        self.to = "799235735@qq.com"

        self.sever = "smtp.sina.com"

    def send_qrcodeurl(self, url):
        #使用MIMEText构造符合smtp协议的header及body
        #msg = MIMEText(url)
        print '==============================='


        '''
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'test message'

        msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')
        msgRoot.attach(msgText)

        fp = open('D:\\wangxinyuhhh\\1.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        '''
        url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=501004106&e=0&l=L&s=8&d=72&v=4'
        print url
        msg = MIMEText(url)
        msg["Subject"] = "please pay attention"
        msg["From"]    = self.user
        msg["To"]      = self.to

        stmp = smtplib.SMTP(self.sever, timeout=30)#连接smtp邮件服务器,端口默认是25
        stmp.login(self.user, self.pwd)#登陆服务器
        stmp.sendmail(self.user, self.to, msg.as_string())#发送邮件
        stmp.close()

if __name__ == '__main__':
    se = sendEmail()
    se.send_qrcodeurl("123")