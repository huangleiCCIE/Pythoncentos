# import os
# import re
# ifconfig_result = os.popen('ifconfig ' +'ens33').read()
# print(ifconfig_result)
# sum = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)
# ipv4_add = sum[0]
# netmask = sum[1]
# broadcast = sum[2]
# mac_addr = re.findall('[0-9,a-f,A-F]{1,2}:[0-9,a-f,A-F]{1,2}:[0-9,a-f,A-F]{1,2}:[0-9,a-f,A-F]{1,2}:[0-9,a-f,A-F]{1,2}:\
# [0-9,a-f,A-F]{1,2}',ifconfig_result)[0]
#
# a = 'ipv4_add'
# b = 'netmask'
# c = 'broadcast'
# d = 'mac_addr'
# format_string = '{0:<11s}:{1:<17s}'
# print(format_string.format(a,ipv4_add))
# print(format_string.format(b,netmask))
# print(format_string.format(c,broadcast))
# print(format_string.format(d,mac_addr))
#
# New_ipv4 = ipv4_add.split()
# New_ipv4[0] = '192.168.88.254'
# ipv4_gw=''.join(New_ipv4)
# print('\n我们假设网关IP地址最后一位为254，因此网关IP地址为：'+ipv4_gw +'\n')
#
# ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
# re_ping_result = re.findall('ttl|Unreachable',ping_result)[0]
# if re_ping_result =='ttl':
#     print('网关可达！')
# else:
#     print('网关不可达！')


