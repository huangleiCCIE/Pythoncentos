import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR) # 关闭不必要的报错
from kamene.all import *


class QYTPING:
    def __init__(self,ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):  #制作包类，有源IP和无源IP
        if self.srcip:
            self.pkt = IP(dst=self.ip,src=self.srcip) / ICMP() / (b'a' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b'a' * self.length)

    def one(self):   #ping 一个包判断是否可达
        self.make_pkt()
        result = sr1(self.pkt, timeout=1, verbose = False)
        if result:
            print(self.ip,'可达')
        else:
            print(self.ip,'不可达')

    def ping(self):  #ping 五个包判断是否可达，可达返回！，不可达返回.
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose= False)
            if result:
                print('!',end='',flush=True)
            else:
                print('.',end='',flush=True)
        print()

    def __str__(self):  #如果有源IP，怎样格式化字符串，无源IP，怎样格式化字符串
        if not self.srcip:
            return '<{0} => dstip: {1}, size: {2}>'.format(self.__class__.__name__,self.ip,self.length)
        else:
            return '<{0} => srcip: {1}, dstip: {2}, size: {3}>'.format(self.__class__.__name__,self.srcip,self.ip,self.length)

class NewPing(QYTPING):  #继承QYTPING这个类
    def ping(self):   #直接覆盖之前的类，来做修改
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose= False)
            if result:
                print('+',end='',flush=True)
            else:
                print('?',end='',flush=True)
        print()


if __name__ == '__main__':
    ping = QYTPING('192.168.88.254') #使用类QYTPING，产生实例
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2),word,s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping) #打印类
    print_new('ping one for sure reachable')
    ping.one() #ping 一个包判断可达性
    print_new('ping five')
    ping.ping() #模拟正常ping程序ping五个包，！表示通，.表示不同
    print_new('set payload lenth')
    ping.length = 200 # 设置负载航都
    print(ping) #打印类
    ping.ping() #使用修改长度的包进行ping测试
    print_new('set ping src ip address')
    ping.srcip = '192.168.88.8' #修改源IP地址
    print(ping) #打印类
    ping.ping() #使用修改长度又修改源的包进行ping测试
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.88.254')
    newping.length = 300
    print(newping) #打印类
    newping.ping() #NewPing类自定义过ping()这个方法，'+'表示通，'?'表示不同