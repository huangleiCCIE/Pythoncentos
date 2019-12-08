# print("QYTANG'day "+ '2014-9-28')
#
# word= 'scallywag'
# sub_word= word[2:6]
# print(sub_word)

# language= 'Python'
# new_language= language[1:] + '-' + language[:-5] + "y"
# print(new_language)

# department1 = 'Security'
# department2 = 'Python'
# depart1_m = 'cq_bomb'
# depart2_m = 'qinke'
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456
#
# #方法1
# line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f  The End!' % (department1,depart1_m,COURSE_FEES_SEC)
# line2 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f  The End!' % (department2,depart2_m,COURSE_FEES_Python)
#
# # #方法2
# # line1 ='Department1 name:{0:<10s} Manager:{1:<10s} COURSE FEES:{2:<10.2f}  The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
# # line2 ='Department1 name:{0:<10s} Manager:{1:<10s} COURSE FEES:{2:<10.2f}  The End!'.format(department2,depart2_m,COURSE_FEES_Python)
# #
# # #方法3
# # line1 =f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FEES:{COURSE_FEES_SEC:<10.2f}  The End!'
# # line2 =f'Department1 name:{department2:<10} Manager:{depart2_m:<10} COURSE FEES:{COURSE_FEES_Python:<10.2f}  The End!'
#
# length = len(line1)
# print('='*length)
# print(line1)
# print(line2)
# print('='*length)

# import re
# str1 = 'Port-channel1.189   192.168.189.254 YES  CONFIG  up'
# New_str1=re.match('\s*(\w\S+\d)\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*(\w{1,3})\s*(\w+)\s*(up|down)\s*',str1).groups()

#.group() 返回的是字符串
#.groups() 返回的是元组
#.什么都不加，返回匹配项
# a='接口'
# b='IP地址'
# c='状态'
# Interface=New_str1[0]
# IP=New_str1[1]
# State=New_str1[4]
#
# line= f'{a:<7}:{Interface:<20}\n{b:<7}:{IP:<20}\n{c:<7}:{State:<20}'
# print('-'*50)
# print(line)



