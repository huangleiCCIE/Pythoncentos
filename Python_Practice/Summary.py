# import re
# str1 = 'Port-channel1.189   192.168.189.254 YES  CONFIG  up'
# New_str1=re.match('\s*(\w\S+\d)\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# print('接口:'+ New_str1[0])    #\w\S\d 用来匹配各种接口信息
# print('IP:'+ New_str1[1]) #\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 用来匹配IP地址
# [0-9,a-f,A-F]{1,4}\.[0-9,a-f,A-F]{1,4}\.[0-9,a-f,A-F]{1,4}  #用来匹配MAC地址
# \d{1,5} #用来匹配端口


# import re   #接口排序
# port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34',\
# 'eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# port_list.sort(key=lambda x:(int(re.findall('\d+',x)[0]),int(re.findall('\d+',x)[1]),int(re.findall('\d+',x)[2]),\
# int(re.findall('\d+',x)[3])))
# print(port_list)
