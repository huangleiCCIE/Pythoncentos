import os
import sqlite3
from SNMP.snmpv2_get import snmpv2_get
import datetime
import time

def get_info_writedb(ip, rocommunity, dbname, seconds):
    #如果文件存在，删除数据库
    if os.path.exists(dbname):
        os.remove(dbname)

    #连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    #创建数据库
    cursor.execute("create table routerdb(id INTEGER PRIMARY KEY AUTOINCREMENT, time  timestamp, mem_percent int)")

    while seconds > 0:
        #CPU已用
        mem_used = int(snmpv2_get('192.168.88.254', 'tcpipro', '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7', port=161)[1])

        #CPU剩余
        mem_free = int(snmpv2_get('192.168.88.254', 'tcpipro', '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7', port=161)[1])

        #计算利用率        小数点后四位
        mem_percent = round((mem_used / (mem_used + mem_free)),4) * 100

        #记录当前时间
        time_info = datetime.datetime.now()

        #把数据写入数据库
        cursor.execute("insert into routerdb (time, mem_percent) values ('{0}',{1})".format(time_info, mem_percent))

        #每5秒采集一次数据
        time.sleep(5)
        seconds -= 5
        #提交数据库
        conn.commit()

if __name__ == '__main__':
    get_info_writedb('192.168.88.254', 'tcpipro', 'deviceinfo_mem.sqlite', 100)