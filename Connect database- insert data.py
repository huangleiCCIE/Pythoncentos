import sqlite3
import os

#Python字典对象，我们将把它写入SQLite数据库
homework_dict = [{'姓名':'学员1','年龄':37, '作业数':1},
                 {'姓名':'学员2','年龄':33, '作业数':5},
                 {'姓名':'学员3','年龄':32, '作业数':10}]

if os.path.exists('qytanghomework.sqlite'): #如果存在该数据库就删除
    os.remove('qytanghomework.sqlite')

#连接SQlite数据库
conn = sqlite3.connect('qytanghomework.sqlite')
cursor = conn.cursor()

#执行创建表的任务
cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

#读取Python字典数据，并逐条写入SQLite数据库
for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute("insert into qytang_homework_info values (?, ?, ?)",(name,age,homework))  #？表示占位符，（）元组，两个可以对上就可以

conn.commit()

