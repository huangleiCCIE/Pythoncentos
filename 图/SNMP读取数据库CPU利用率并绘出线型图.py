import sqlite3
from dateutil import parser
from datetime import datetime, timedelta
from 图.Netflow_线形图 import mat_line

def cpu_read_db(dbname, last_min=1):   #读取数据库的名字和时间
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()  #连接数据库
    now = datetime.now()  #获取当前时间
    before_last_min = now - timedelta(minutes=last_min)  #想获取多少分钟的参数，就获取多少分钟的参数
    cursor.execute("select time, cpu from routerdb where time > '{0}'".format(before_last_min))  #基于时间查询
    yourresults = cursor.fetchall()   #得到结果

    return [[parser.parse(i[0]), i[1]] for i in yourresults]

if __name__ == '__main__':
    # print(cpu_read_db("deviceinfo.sqlite",50))
    mat_line(cpu_read_db("deviceinfo.sqlite", 100))   #读取100分钟内的CPU利用率