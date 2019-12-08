from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
import platform

def get_ip_address(ifname):  #得到IPv4地址
    if platform.system() == 'Linux':
        try:
            return  ifaddresses(ifname)[AF_INET][0]['addr']
        except ValueError:
            return None
    elif platform.system() == 'Windows':
        from windows_网卡唯一码 import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        if not if_id:
            return
        else:
            return ifaddresses(if_id)[AF_INET][0]['addr']
    else:
        print('操作系统不支持，本脚本只能工作在Windows或者linux环境！')

def get_ipv6_address(ifname): #得到IPv6地址
    if platform.system() == 'Linux':
        try:
            return  ifaddresses(ifname)[AF_INET6][0]['addr']
        except ValueError:
            return None
    elif platform.system() == 'Windows':
        from windows_网卡唯一码 import  win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        if not if_id:
            return
        else:
            return ifaddresses(if_id)[AF_INET6][0]['addr']
    else:
        print('操作系统不支持，本脚本只能工作在Windows或者Linux环境！')

if __name__ == '__main__':
    print(get_ip_address('ens33'))
    # print(get_ip_address('以太网'))
    print(get_ipv6_address('ens33'))
    # print(get_ipv6_address('以太网'))