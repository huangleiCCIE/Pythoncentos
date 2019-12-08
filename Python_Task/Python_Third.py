# import re
# Show = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
# New_Show = re.match('\s*(\d{1,4})\s*([0-9,a-f,A-F]{1,4}\.[0-9,a-f,A-F]{1,4}\.[0-9,a-f,A-F]{1,4})\s*\
# (STATIC|DYNAMIC)\s*(\w\S+\d+)',Show).groups()
# a= 'VLAN ID'
# b= 'MAC'
# c= 'Type'
# d= 'Interface'
# line=f'{a:<11}: {New_Show[0]}\n{b:<11}: {New_Show[1]}\n{c:<11}: {New_Show[2]}\n{d:<11}: {New_Show[3]}'
# print(line)


# import re
# Show = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710,idle 0:01:09,bytes 27575949,flags UIO'
# New_Show = re.match('\s*(\w+)\s*server\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s*localserver\s*(\d{1,3}\.\d{1,3}\
# \.\d{1,3}\.\d{1,3}:\d{1,5}),idle\s*(\d{1,2}):(\d{1,2}):(\d{1,2}),bytes\s*(\d+),flags\s*(\w+)',Show).groups()
# Protocol = 'protocol'
# Server = 'server'
# Localserver = 'localserver'
# Idle = 'idle'
# Bytes = 'bytes'
# Flags = 'flags'
#
# line = f'{Protocol:<20}: {New_Show[0]}\n{Server:<20}: {New_Show[1]}\n{Localserver:<20}: {New_Show[2]}\n{Idle:<20}: \
# { New_Show[3]} 小时 {New_Show[4]}分钟 {New_Show[5]}秒\n{Bytes:<20}: {New_Show[6]}\n{Flags:<20}: {New_Show[7]}'
# print(line)