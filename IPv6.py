import re

def full_ipv6(ipv6): #转换为完整的IPv6地址
    ipv6_section = ipv6.split(':') #d对原始地址使用：分段
    ipv6_section_len = len(ipv6.split(':')) #了解原始地址的分段数量

    if ipv6_section.index(''):
        null_location = ipv6_section.index('') #找到空位，这个地方要补0
        ipv6_section.pop(null_location) #把原来的空位弹出去
        add_section = 8 - ipv6_section_len +1 #计算需要补"0000"的个数
        for x in range(add_section):
            ipv6_section.insert(null_location,'0000') #开始补"0000"

        new_ipv6 = []
        for s in ipv6_section:
            if len(s) < 4:
                new_ipv6.append((4 - len(s)) * '0' + s) #对于不够长度的左边补"0"
            else:
                new_ipv6.append(s)
        return ':'.join(new_ipv6) #使用":"连接在一起成为完整的IPv6地址
    else:
        return ipv6


def solicited_node_multicast_address(ipv6): #构建请求节点组播地址
    return 'FF02::1:FF' + full_ipv6(ipv6)[-7:] # -7 包括了一个':'


def mac_to_ipv6_linklocal(mac):  #构建链路本地地址
    mac_value = int(re.sub('[:.-]','',mac),16) #移除多余的字符，空格，冒号，点，减号  十六进制转换为十进制
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    high1 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff
    return 'fe80::{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2,high1,low1,low2)


def ipv6_to_mac(ipv6):   #ipv6转换为MAC地址
    ipv6_address = full_ipv6(ipv6)
    last_4_sections = ipv6_address.split(':')[-4:]
    mac_1 = int(last_4_sections[0][:2],16) ^ 0x02
    mac_2 = int(last_4_sections[0][2:],16)
    mac_3 = int(last_4_sections[1][:2],16)
    mac_4 = int(last_4_sections[2][2:],16)
    mac_5 = int(last_4_sections[3][:2],16)
    mac_6 = int(last_4_sections[3][2:],16)
    return '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac_1,mac_2,mac_3,mac_4,mac_5,mac_6)

def mac_to_eui64(mac,prefix):  #MAC地址转换为EUI64
    mac_value = int(re.sub('[:.-]','',mac),16)
    high1 = mac_value >> 32 & 0xffff ^ 0x0200
    high2 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff
    host_id = '{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high1,high2,low1,low2)
    net = prefix.split('/')[0]
    return net + host_id


if __name__ == '__main__':
    print(full_ipv6('2001::f107:94ac:2717:a736'))  #转换为完整的IPV6地址
    print(solicited_node_multicast_address('2001::f107:94ac:2717:a736')) #构建请求节点组播地址
    print(mac_to_ipv6_linklocal('22:22:22:22:22:22')) #构建链路本地地址
    print(ipv6_to_mac('2001::f107:94ac:2717:a736'))  # ipv6转换为MAC地址
    print(mac_to_eui64(mac='06:b2:4a:00:00:9f',prefix='2001:db8:100::/64')) #窜了一个MAC地址一个前缀，通过eui64，转换为IPV6地址
