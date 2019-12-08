# import  os
# import  re
# import  time
# while True:
#     a = os.popen('netstat -tulnp').read()  #查看服务
#     find = False   #定义一个标杆
#     for tcp80 in a.split('\n'):    #遍历打印服务
#         re_find = re.findall('tcp\s+\d+\s+\d+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:80',tcp80) #找到tcp 80
#         if re_find:      #如果找到，打印HTTP(TCP/80) 服务器已经被打开，find为true，跳出for循环
#             print('HTTP(TCP/80) 服务器已经被打开')
#             find = True
#             break
#         else:   #否则一直打印 ‘等待一秒重新开始监控！’
#             print('等待一秒重新开始监控！')
#         time.sleep(1) #每隔一秒打印一次
#     if find == True:  #如果find为真，跳出while循环
#         break



#
# list1 = ['aaa', 111, (4,5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4,5)]

# # 方法一
# for a in list1:
#     if a in list2:
#         print(str(a) + ' in List1 and List2')
#     else:
#         print(str(a) + ' only in list1')

# 方法二
# def same(l1,l2):   #通过函数找不同
#     for a in l1:
#         if a in l2:
#             print(str(a) + ' in List1 and List2')
#         else:
#             print(str(a) + ' only in list1')
# same(list1,list2)


import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):    #给一个目的IP地址，就会制造一个ICMP包，然后去ping
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip ,True
    else:
        return ip,False

if __name__ == '__main__':
    result = qytang_ping('192.168.88.254')
    if result[1]:
        print(f'{result[0]} 通！')
    else:
        print(print(f'{result[0]} 不通！'))
