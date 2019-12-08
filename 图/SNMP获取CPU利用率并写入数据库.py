#使用SNMP读取"cpmCPUTotal5sec"的值, 读取周期为五秒! 把获取的数据写入数据库
#读取数据库, 返回时间和CPU利用率的列表
#根据第二步读取的数据,绘制CPU利用率走势的线性图
import os
import sqlite3
import datetime
import time
from SNMP.snmpv2_get import snmpv2_get

def get_info_writedb(ip, reocommunity, dbname, seconds):
    if os.path.exists(dbname):   #如果存在该数据库，会删除
        os.remove(dbname)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()  #连接数据库

    cursor.execute(r"create table routerdb(id INTEGER PRIMARY KEY AUTOINCREMENT, time timestamp, cpu int)") #创建表，唯一ID，时间，CPU

    while seconds>0:  #如果大于0秒
        cpu_info = snmpv2_get(ip, reocommunity,"1.3.6.1.4.1.9.9.109.1.1.1.1.3.7")[1]  #获得5秒的cpu利用率
        time_info = datetime.datetime.now()  #获取当前时间
        cursor.execute("insert into routerdb (time, cpu) values ('{0}',{1})".format(time_info, int(cpu_info))) #将时间和cpu格式化写入数据库
        time.sleep(5)  #采集一次休息5秒
        seconds -= 5   #每次减5
        conn.commit() #每一次写都提交

if __name__ == '__main__':
    get_info_writedb('192.168.88.254','tcpipro','deviceinfo.sqlite',100)   #获取100分钟内的cpu利用率，每5秒读一次