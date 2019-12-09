from pymongo import *
from datetime import datetime
client = MongoClient('mongodb://admin:Cisc0123@192.168.1.103:27017/qytang')
db = client['qytang']

#写入单条数据
tina = {'name':'tina','department': 'sales', 'age':35, 'location':'Beijing'}
db.secie.insert_one(tina)    #没有secie这个表，创建secie，将tina这条数据插入
for obj in db.secie.find():
    print(obj)
# db.secie.remove()   #删除表
if __name__ == '__main__':
    pass