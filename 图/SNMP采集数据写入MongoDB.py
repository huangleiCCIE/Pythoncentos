import numpy as np
from SNMP.snmpv2_get import snmpv2_get
from SNMP.SNMPV2_GETBULK import snmpv2_getbulk
from datetime import datetime
from pprint import pprint
from pymongo import *
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
import matplotlib.dates as mdate
import matplotlib.ticker as mtick
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
import time


client = MongoClient('mongodb://admin:Cisc0123@192.168.88.2:27017/qytang')
db = client['qytang']

def get_all_info(ip, community_ro):
    # 接口名字列表
    if_name_list = [x[1] for x in snmpv2_getbulk(ip, community_ro, "1.3.6.1.2.1.2.2.1.2", count=25, port=161)]
    # print(if_name_list)

    # 接口速率列表
    if_speed_list = [x[1] for x in snmpv2_getbulk(ip, community_ro, "1.3.6.1.2.1.2.2.1.5", port=161)]
    # print(if_speed_list)

    # 进接口字节数列表
    if_in_bytes_list = [x[1] for x in snmpv2_getbulk(ip, community_ro, "1.3.6.1.2.1.2.2.1.10", port=161)]
    # print(if_in_bytes_list)

    # 出接口字节数列表
    if_out_bytes_list = [x[1] for x in snmpv2_getbulk(ip, community_ro, "1.3.6.1.2.1.2.2.1.16", port=161)]
    # print(if_out_bytes_list)

    name_speed_in_out_list = zip(if_name_list, if_speed_list, if_in_bytes_list, if_out_bytes_list)
    all_info_dict = {}
    if_name_list = []
    for x in name_speed_in_out_list:
        # print(x)
        if x[2] == '0' and x[3] == '0':  #将结果等于0的都不要
            continue
        # print(x)
        all_info_dict[x[0] + '_' + 'speed'] = x[1]
        all_info_dict[x[0] + '_' + 'in_bytes'] = int(x[2])
        all_info_dict[x[0] + '_' + 'out_bytes'] = int(x[3])
        if_name_list.append(x[0])
    all_info_dict.update({'if_name_list':if_name_list})
    # cpmCPUTotal5sec
    cpu_5s = snmpv2_get(ip, community_ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1]
    # cpmCPUMemoryUsed
    mem_u = snmpv2_get(ip, community_ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1]
    # cpmCPUMemoryFree
    mem_f = snmpv2_get(ip, community_ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1]

    all_info_dict.update({'if_name_list': if_name_list})
    all_info_dict['ip'] = ip
    all_info_dict['cpu_5s'] = cpu_5s
    all_info_dict['mem_u'] = mem_u
    all_info_dict['mem_f'] = mem_f
    all_info_dict['record_time'] = datetime.now()

    return all_info_dict

def write_info_to_mongodb(device_info_dict):
    #写入单条数据
    db.deiveinfo.insert_one(device_info_dict)

    #查看并打印secie中的所有数据
    for obj in db.deiveinfo.find():
        pprint(obj, indent=4)

def search_info_from_mongodb(ifname, direction, last_mins):
    if_bytes_list = []
    record_time_list = []
    for obj in db.deiveinfo.find({'record_time': {'$gte': datetime.now() - timedelta(minutes=last_mins)}}):
        if_bytes_list.append(obj[ifname + '_' + direction + '_bytes'])
        record_time_list.append(obj['record_time'])
    # print(if_bytes_list)   #字节
    # print(record_time_list) #时间

    # numpy的diff计算列表的差值
    # np.diff([x for x in range(5)])
    # array([1, 1, 1, 1])
    # 通过这种方式获取两次获取的字节数差值
    diff_if_bytes_list = list(np.diff(if_bytes_list))  #计算字节的差值

    # 计算两次时间对象的秒数的差值，np的多态太牛逼了
    diff_record_time_list = [x.seconds for x in np.diff(record_time_list)]   #计算时间的差值

    # 计算速率
    # *8得到bit数
    # /1000计算Kb
    # / x[1] 计算kbs
    #  round(x, 2)保留两位小数
    # zip把字节差列表和时间差列表 压到一起
    speed_list = list(map(lambda x: round(((x[0]* 8)/(1000* x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list))) #产生速率列表
    record_time_list = record_time_list[1:]   #不要第1位时间   差值计算的第一位是基础值
    return record_time_list, speed_list

def delete_all():
    db.deiveinfo.remove()

def write_db_period(interval=5, seconds=120):   #执行120分钟
    while seconds > 0:
        write_info_to_mongodb(get_all_info('192.168.88.254', 'tcpipro'))
        time.sleep(interval)
        seconds -= interval

def make_linear(ifname, direction, minutes):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S')) # 设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M:%S'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))

    # 把cpu_usage_list的数据,拆分为x轴的时间,与y轴的利用率
    x,y = search_info_from_mongodb(ifname, direction, minutes)
    print(x, y)

    # 添加主题和注释
    plt.title('CPU Monitor, {0} interface, {1} direction, {2} speed(min)'.format(ifname, direction, minutes))
    plt.xlabel('time')
    plt.ylabel('speed(kbps)')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果你有两套数据,完全可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')
    # Y轴限制(0,100)
    # ax.set_ylim(0,100)
    # ax.set_ylim(0,max(y))

    # 保存到图片
    plt.savefig('result1.png')

    # 绘制图形
    plt.show()

if __name__ == "__main__":
    # pprint(get_all_info('192.168.88.254', 'tcpipro'))  #查看读取的内容
    # write_db_period()  #写入数据库
    make_linear('GigabitEthernet1', 'in', 10)   #5分钟入接口G1口的速率
    # print(search_info_from_mongodb('GigabitEthernet1', 'in', 100))
    # delete_all()   #删除数据
