# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @author   : thomas_liu
# @motto    : life is short , i use python.

import re
import smtplib, email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def smtp_send_attachment(mailserver, username, password, From, To, Subj, Main_Body, files=None):
    # 使用SSL加密SMTP发送邮件, 此函数发送的邮件有主题,有正文,还可以发送附件
    Tos = To.split(';')  # 把多个邮件接受者通过';'分开
    Date = email.utils.formatdate()  # 格式化邮件时间
    msg = MIMEMultipart()  # 产生MIME多部分的邮件信息
    msg["Subject"] = Subj  # 主题
    msg["From"] = From  # 发件人
    msg["To"] = To  # 收件人
    msg["Date"] = Date  # 发件日期

    part = MIMEText(Main_Body)
    msg.attach(part)  # 添加正文

    if files:  # 如果存在附件文件
        for file in files:  # 逐个读取文件,并添加到附件
            # MIMEXXX决定了什么类型 MIMEApplication为二进制文件
            # 添加二进制文件
            part = MIMEApplication(open(file, 'rb').read())
            # 添加头部信息, 说明此文件为附件,并且添加文件名
            part.add_header('Content-Disposition', 'attachment', filename=file)
            # 把这个部分内容添加到MIMEMultipart()中
            msg.attach(part)

    server = smtplib.SMTP_SSL(mailserver, 465)  # 连接邮件服务器
    server.login(username, password)  # 通过用户名和密码登录邮件服务器
    failed = server.sendmail(From, Tos, msg.as_string())  # 发送邮件
    server.quit()  # 退出会话
    if failed:
        print('Falied recipients:', failed)  # 如果出现故障，打印故障原因！
    else:
        print('邮件已经成功发出！')  # 如果没有故障发生，打印'邮件已经成功发出！'！


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    smtp_send_attachment('smtp.qq.com',
                        '2420800264@qq.com',
                        'rtzeuzgainvgeahj',
                        '2420800264@qq.com',
                        '2420800264@qq.com',
                        '附件测试_主题',
                        '附件测试_正文'
                         # ['Logo.jpg']
                         )
