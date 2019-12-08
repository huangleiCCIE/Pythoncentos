from Email.pop3_final import qyt_rec_mail
import time
from Email.day14_smtp_send_attachment import  smtp_send_attachment
import os
from pprint import pprint

while True:
    try:
        for x in qyt_rec_mail('pop.qq.com', '2420800264@qq.com', 'rtzeuzgainvgeahj', save_file=False, delete_email=True):
           if '2420800264@qq.com' in x.get('From') and 'cmd' in x.get('Subject'):
                cmd_exe = x.get('Subject').split(':')[1] #命令格式
                cmd_result = os.popen(cmd_exe).read() #执行命令得到结果
                print(cmd_result)
                smtp_send_attachment('smtp.qq.com',
                                     '2420800264@qq.com',
                                     'rtzeuzgainvgeahj',
                                     '2420800264@qq.com',
                                     '2420800264@qq.com',
                                     f'cmd {cmd_exe} exec result',  #主题
                                     cmd_result)   #显示的是执行的结果

    except KeyboardInterrupt:
        print('接收到管理员的ctrl+c！')
        print('退出程序')
        break
    time.sleep(5)