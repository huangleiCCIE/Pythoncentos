#linux环境下
import pyshark
from pymongo import *

client = MongoClient('mongodb://admin:Cisc0123@192.168.1.103:27017/qytang')

db = client['qytang']

db.pktinfo.remove()

#####################最原始操作,信息过量#####################
cap = pyshark.FileCapture('dos.pcap', keep_packets=False)  # 读取pcap文件，数据包被读取后，不在内存中保存，节省内存。


def write_pkt_mongodb(pkt):
    pkt_dict = {}
    for layer in pkt.__dict__.get('layers'):
        pkt_dict.update(layer.__dict__.get('_all_fields'))

    pkt_dict_final = {}
    for key, value in pkt_dict.items():
        pkt_dict_final[key.replace('.', '_')] = value
    print(pkt_dict_final)
    db.pktinfo.insert_one(pkt_dict_final)


# 把函数应用到数据包
cap.apply_on_packets(write_pkt_mongodb)
