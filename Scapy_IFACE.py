import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *
from Get_ifname import get_ifname
import platform


def scapy_iface(os_name):
    if platform.system() == "Linux":
        return os_name
    elif platform.system() == "Windows":
        for x, y in ifaces.items():
            if y.pcap_name is not None:
                if get_ifname(os_name) == ('{' + y.pcap_name.split('{')[1]):
                    return x
                else:
                    pass


if __name__ == '__main__':
    # print(ifaces)  #windows环境下，获得网卡、IP、MAC信息
    print(scapy_iface('VMware Network Adapter VMnet8'))  #查询是否有当前网卡
