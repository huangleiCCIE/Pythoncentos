#从数据库找到前5的会话
from pymongo import *
import matplotlib.pyplot as plt
import json
import pyshark
from 图.Netflow_柱状图 import mat_zhu_mark
client = MongoClient('mongodb://admin:Cisc0123@192.168.1.103:27017/qytang')
db = client['qytang']
yn_pkt = db.pktinfo.find({'tcp_flags': '0x00000002'})


dos_dict = {}
for x in yn_pkt:
    conn = x.get('ip_src'), x.get('ip_dst'), x.get('tcp_dstport')
    # print(conn)
    counts = dos_dict.get(conn, 0)
    dos_dict[conn] = counts + 1

sorted_dict_key = sorted(dos_dict.keys(), key = lambda  k: dos_dict[k], reverse=True)[:5]
sorted_dict_key_top5 = [f'SRC: {x[0]} DST:{x[1]}, PORT:{x[2]}' for x in sorted_dict_key]
sorted_counts = [dos_dict[x] for x in sorted_dict_key]
print(sorted_dict_key_top5)
print(sorted_counts)

mat_zhu_mark(sorted_counts, sorted_dict_key_top5, '源目地址 端口号 三元组','会话数','连接会话数')

