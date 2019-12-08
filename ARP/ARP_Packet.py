import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *
from 获取win或linux_MAC import  get_mac_address
from Scapy_IFACE import scapy_iface

def gratuitous_arp(ip_address,ifname='ens33'):
    localmac = get_mac_address(ifname)
    gratuitous_arp_pkt = Ether(src=localmac,dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,   #2表示reply
                                                                         hwsrc = localmac,
                                                                         hwdst = localmac,
                                                                         psrc= ip_address,
                                                                         pdst = ip_address
                                                                        )
    sendp(gratuitous_arp_pkt,iface=scapy_iface(ifname),verbose=False)

if __name__ == '__main__':
    gratuitous_arp('192.168.88.8',ifname='ens33')  #给哪个目标地址发reply