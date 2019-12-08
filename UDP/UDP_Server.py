import socket
import sys
import struct
import hashlib
import pickle

address = ('192.168.88.1',8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:
    try:
        recv_source_data = s.recvfrom(2048) #能够接收数据的大小

        rdata, addr = recv_source_data  #接收的数据和地址的信息

    # 将头部切出来
        header = rdata[:12]
        uppack_header = struct.unpack('>HHLL',header) #将头部信息从二进制转回字符串
        #取出的内容
        version = uppack_header[0]
        pkt_type = uppack_header[1]
        seq_id = uppack_header[2]
        length = uppack_header[3]

    #数据切出来
        rdata = rdata[12:]
        data = rdata[:length]  #判断数据的大小，长度前面就是数据
        md5_recv = rdata[length:]  #长度后面是MD5值

    #计算MD5值
        m = hashlib.md5()
        m.update(header + data)  #头部和数据放进去算
        md5_value = m.digest()  #得到md5值

    #判断收到的md5值和自己计算数据的md5值是否相等
        if md5_recv == md5_value:
            print('=' * 80)
            print('{0:<30}:{1:<30}'.format('数据源自于',str(addr)))
            print('{0:<30}:{1:<30}'.format('数据序列号', seq_id))
            print('{0:<30}:{1:<30}'.format('数据长度为', length))
            print('{0:<30}:{1:<30}'.format('数据内容为', str(pickle.loads(data))))

    except KeyboardInterrupt:
        sys.exit()


