import socket
import struct
import hashlib
import pickle

def udp_send_data(ip, port, data_list):
    address =(ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ipv4的udp
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        #数据的字典转换为字符串
        send_data = pickle.dumps(x)

        #将头部内容压缩成二进制      版本      包类型    序列号     数据长度
        header = struct.pack('>HHLL',version, pkt_type, seq_id, len(send_data))  #>：网络字节序  H：正数两个字节  L：4字节

        #头部和数据的md5值
        m = hashlib.md5()
        m.update(header + send_data)
        md5_value = m.digest()

        #发送头部+数据+md5值
        s.sendto(header + send_data + md5_value,address)

        #序列号累计+1
        seq_id += 1
    s.close() #关闭udp
if __name__ == '__main__':
    user_data = ['乾颐堂', [1, 'qytang',3],{'qytang':1, 'test':3}]  #发送的数据列表
    udp_send_data('192.168.88.1',8888,user_data)  #ip+端口号+数据