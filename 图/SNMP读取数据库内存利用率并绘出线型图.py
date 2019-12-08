import sqlite3
from dateutil import parser
from datetime import datetime, timedelta
from 图.Netflow_线形图 import mat_line

def mem_read_db(dbname, last_men=1):
    #连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    #提取时间与CPU利用率信息
    now = datetime.now()
    before_last_min = now - timedelta(minutes=last_men)
    cursor.execute("select time, mem_percent from routerdb where time > '{0}'".format(before_last_min))
    yourresults = cursor.fetchall()

    time_mem_list = [[parser.parse(i[0]),i[1]] for i in yourresults]

    return time_mem_list

if __name__ == '__main__':
    mat_line(mem_read_db('deviceinfo_mem.sqlite', 100))