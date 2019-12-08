from ping import qytang_ping
from ssh import qytang_ssh
import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if qytang_ping(ip):
            for a in qytang_ssh(ip,username, password,port=22,cmd='show ip int bri').split('\n'):
                result = re.match('([A-Z]\S+\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+\w+\s+\w+',a.strip())
                if result:
                    if_dict[result.groups()[0]] = result.groups()[1]
        device_if_dict[ip] = if_dict
    return  device_if_dict

if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.88.10','192.168.88.11',username='admin',password='Cisc0123'))