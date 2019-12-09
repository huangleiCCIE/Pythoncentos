# import logging, socketserver, threading, re, os, sqlite3
# from dateutil import parser
# from datetime import datetime
#
# # facility与ID的对应关系的字典
# facility_dict = {0: 'KERN',
#                  1: 'USER',
#                  2: 'MAIL',
#                  3: 'DAEMON',
#                  4: 'AUTH',
#                  5: 'SYSLOG',
#                  6: 'LPR',
#                  7: 'NEWS',
#                  8: 'UUCP',
#                  9: 'CRON',
#                  10: 'AUTHPRIV',
#                  11: 'FTP',
#                  16: 'LOCAL0',
#                  17: 'LOCAL1',
#                  18: 'LOCAL2',
#                  19: 'LOCAL3',
#                  20: 'LOCAL4',
#                  21: 'LOCAL5',
#                  22: 'LOCAL6',
#                  23: 'LOCAL7'}
#
# # severity_level与ID的对应关系的字典
# severity_level_dict = {0: 'EMERG',
#                        1: 'ALERT',
#                        2: 'CRIT',
#                        3: 'ERR',
#                        4: 'WARNING',
#                        5: 'NOTICE',
#                        6: 'INFO',
#                        7: 'DEBUG'}
#
# class SyslogUDPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         data = bytes.decode(self.request[0].strip())  # 读取数据
#
#         #匹配日志中的OSPF-5-ADJCHG字段
#         if 'OSPF-5-ADJCHG' in str(data):
#             ospf_info = re.match(r'.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) on (\w\S+\d+) from (\w+) to (\w+),.*',str(data)).groups()
#             print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
#
#
#         syslog_info_dict = {'device_ip': self.client_address[0]}
#         try:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
#             # print(syslog_info[0]) 提取为整数 例如 185
#             # 185 二进制为 1011 1001
#             # 前5位为facility  >> 3 获取前5位
#             # 后3位为severity_level  & 0b111 获取后3位
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]
#             syslog_info_dict['severity_level'] = int(syslog_info[4])
#             syslog_info_dict['severity_level_name'] = severity_level_dict[int(syslog_info[4])]
#             syslog_info_dict['description'] = syslog_info[5]
#             syslog_info_dict['text'] = syslog_info[6]
#         except AttributeError:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): (\w+): (.*)', str(data)).groups()
#             print(syslog_info[0])
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]
#             # 如果在文本部分解析不了severity_level, 切换到syslog_info[0]去获取
#             # 185 二进制为 1011 1001
#             # 前5位为facility  >> 3 获取前5位
#             # 后3位为severity_level  & 0b111 获取后3位
#             import logging, socketserver, threading, re, os, sqlite3
#             from dateutil import parser
#             from datetime import datetime
#
#             # facility与ID的对应关系的字典
#             facility_dict = {0: 'KERN',
#                              1: 'USER',
#                              2: 'MAIL',
#                              3: 'DAEMON',
#                              4: 'AUTH',
#                              5: 'SYSLOG',
#                              6: 'LPR',
#                              7: 'NEWS',
#                              8: 'UUCP',
#                              9: 'CRON',
#                              10: 'AUTHPRIV',
#                              11: 'FTP',
#                              16: 'LOCAL0',
#                              17: 'LOCAL1',
#                              18: 'LOCAL2',
#                              19: 'LOCAL3',
#                              20: 'LOCAL4',
#                              21: 'LOCAL5',
#                              22: 'LOCAL6',
#                              23: 'LOCAL7'}
#
#             # severity_level与ID的对应关系的字典
#             severity_level_dict = {0: 'EMERG',
#                                    1: 'ALERT',
#                                    2: 'CRIT',
#                                    3: 'ERR',
#                                    4: 'WARNING',
#                                    5: 'NOTICE',
#                                    6: 'INFO',
#                                    7: 'DEBUG'}
#
#             class SyslogUDPHandler(socketserver.BaseRequestHandler):
#                 def handle(self):
#                     data = bytes.decode(self.request[0].strip())  # 读取数据
#
#                     # 匹配日志中的OSPF-5-ADJCHG字段
#                     if 'OSPF-5-ADJCHG' in str(data):
#                         ospf_info = re.match(
#                             r'.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) on (\w\S+\d+) from (\w+) to (\w+),.*',
#                             str(data)).groups()
#                         print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
#
#                     syslog_info_dict = {'device_ip': self.client_address[0]}
#                     try:
#                         syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
#                         # print(syslog_info[0]) 提取为整数 例如 185
#                         # 185 二进制为 1011 1001
#                         # 前5位为facility  >> 3 获取前5位
#                         # 后3位为severity_level  & 0b111 获取后3位
#                         syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#                         syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#                         syslog_info_dict['logid'] = int(syslog_info[1])
#                         syslog_info_dict['time'] = parser.parse(syslog_info[2])
#                         syslog_info_dict['log_source'] = syslog_info[3]
#                         syslog_info_dict['severity_level'] = int(syslog_info[4])
#                         syslog_info_dict['severity_level_name'] = severity_level_dict[int(syslog_info[4])]
#                         syslog_info_dict['description'] = syslog_info[5]
#                         syslog_info_dict['text'] = syslog_info[6]
#                     except AttributeError:
#                         syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): (\w+): (.*)', str(data)).groups()
#                         print(syslog_info[0])
#                         syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#                         syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#                         syslog_info_dict['logid'] = int(syslog_info[1])
#                         syslog_info_dict['time'] = parser.parse(syslog_info[2])
#                         syslog_info_dict['log_source'] = syslog_info[3]import logging, socketserver, threading, re, os, sqlite3
# from dateutil import parser
# from datetime import datetime
#
# # facility与ID的对应关系的字典
# facility_dict = {0: 'KERN',
#                  1: 'USER',
#                  2: 'MAIL',
#                  3: 'DAEMON',
#                  4: 'AUTH',
#                  5: 'SYSLOG',
#                  6: 'LPR',
#                  7: 'NEWS',
#                  8: 'UUCP',
#                  9: 'CRON',
#                  10: 'AUTHPRIV',
#                  11: 'FTP',
#                  16: 'LOCAL0',
#                  17: 'LOCAL1',
#                  18: 'LOCAL2',
#                  19: 'LOCAL3',
#                  20: 'LOCAL4',
#                  21: 'LOCAL5',
#                  22: 'LOCAL6',
#                  23: 'LOCAL7'}
#
# # severity_level与ID的对应关系的字典
# severity_level_dict = {0: 'EMERG',
#                        1: 'ALERT',
#                        2: 'CRIT',
#                        3: 'ERR',
#                        4: 'WARNING',
#                        5: 'NOTICE',
#                        6: 'INFO',
#                        7: 'DEBUG'}
#
# class SyslogUDPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         data = bytes.decode(self.request[0].strip())  # 读取数据
#
#         #匹配日志中的OSPF-5-ADJCHG字段
#         if 'OSPF-5-ADJCHG' in str(data):
#             ospf_info = re.match(r'.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) on (\w\S+\d+) from (\w+) to (\w+),.*',str(data)).groups()
#             print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
#
#
#         syslog_info_dict = {'device_ip': self.client_address[0]}
#         try:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
#             # print(syslog_info[0]) 提取为整数 例如 185
#             # 185 二进制为 1011 1001
#             # 前5位为facility  >> 3 获取前5位
#             # 后3位为severity_level  & 0b111 获取后3位
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]
#             syslog_info_dict['severity_level'] = int(syslog_info[4])
#             syslog_info_dict['severity_level_name'] = severity_level_dict[int(syslog_info[4])]
#             syslog_info_dict['description'] = syslog_info[5]
#             syslog_info_dict['text'] = syslog_info[6]
#         except AttributeError:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): (\w+): (.*)', str(data)).groups()
#             print(syslog_info[0])
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]import logging, socketserver, threading, re, os, sqlite3
# from dateutil import parser
# from datetime import datetime
#
# # facility与ID的对应关系的字典
# facility_dict = {0: 'KERN',
#                  1: 'USER',
#                  2: 'MAIL',
#                  3: 'DAEMON',
#                  4: 'AUTH',
#                  5: 'SYSLOG',
#                  6: 'LPR',
#                  7: 'NEWS',
#                  8: 'UUCP',
#                  9: 'CRON',
#                  10: 'AUTHPRIV',
#                  11: 'FTP',
#                  16: 'LOCAL0',
#                  17: 'LOCAL1',
#                  18: 'LOCAL2',
#                  19: 'LOCAL3',
#                  20: 'LOCAL4',
#                  21: 'LOCAL5',
#                  22: 'LOCAL6',
#                  23: 'LOCAL7'}
#
# # severity_level与ID的对应关系的字典
# severity_level_dict = {0: 'EMERG',
#                        1: 'ALERT',
#                        2: 'CRIT',
#                        3: 'ERR',
#                        4: 'WARNING',
#                        5: 'NOTICE',
#                        6: 'INFO',
#                        7: 'DEBUG'}
#
# class SyslogUDPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         data = bytes.decode(self.request[0].strip())  # 读取数据
#
#         #匹配日志中的OSPF-5-ADJCHG字段
#         if 'OSPF-5-ADJCHG' in str(data):
#             ospf_info = re.match(r'.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) on (\w\S+\d+) from (\w+) to (\w+),.*',str(data)).groups()
#             print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
#
#
#         syslog_info_dict = {'device_ip': self.client_address[0]}
#         try:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
#             # print(syslog_info[0]) 提取为整数 例如 185
#             # 185 二进制为 1011 1001
#             # 前5位为facility  >> 3 获取前5位
#             # 后3位为severity_level  & 0b111 获取后3位
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]
#             syslog_info_dict['severity_level'] = int(syslog_info[4])
#             syslog_info_dict['severity_level_name'] = severity_level_dict[int(syslog_info[4])]
#             syslog_info_dict['description'] = syslog_info[5]
#             syslog_info_dict['text'] = syslog_info[6]
#         except AttributeError:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): (\w+): (.*)', str(data)).groups()
#             print(syslog_info[0])
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]import logging, socketserver, threading, re, os, sqlite3
# from dateutil import parser
# from datetime import datetime
#
# # facility与ID的对应关系的字典
# facility_dict = {0: 'KERN',
#                  1: 'USER',
#                  2: 'MAIL',
#                  3: 'DAEMON',
#                  4: 'AUTH',
#                  5: 'SYSLOG',
#                  6: 'LPR',
#                  7: 'NEWS',
#                  8: 'UUCP',
#                  9: 'CRON',
#                  10: 'AUTHPRIV',
#                  11: 'FTP',
#                  16: 'LOCAL0',
#                  17: 'LOCAL1',
#                  18: 'LOCAL2',
#                  19: 'LOCAL3',
#                  20: 'LOCAL4',
#                  21: 'LOCAL5',
#                  22: 'LOCAL6',
#                  23: 'LOCAL7'}
#
# # severity_level与ID的对应关系的字典
# severity_level_dict = {0: 'EMERG',
#                        1: 'ALERT',
#                        2: 'CRIT',
#                        3: 'ERR',
#                        4: 'WARNING',
#                        5: 'NOTICE',
#                        6: 'INFO',
#                        7: 'DEBUG'}
#
# class SyslogUDPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         data = bytes.decode(self.request[0].strip())  # 读取数据
#
#         #匹配日志中的OSPF-5-ADJCHG字段
#         if 'OSPF-5-ADJCHG' in str(data):
#             ospf_info = re.match(r'.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) on (\w\S+\d+) from (\w+) to (\w+),.*',str(data)).groups()
#             print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
#
#
#         syslog_info_dict = {'device_ip': self.client_address[0]}
#         try:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
#             # print(syslog_info[0]) 提取为整数 例如 185
#             # 185 二进制为 1011 1001
#             # 前5位为facility  >> 3 获取前5位
#             # 后3位为severity_level  & 0b111 获取后3位
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]
#             syslog_info_dict['severity_level'] = int(syslog_info[4])
#             syslog_info_dict['severity_level_name'] = severity_level_dict[int(syslog_info[4])]
#             syslog_info_dict['description'] = syslog_info[5]
#             syslog_info_dict['text'] = syslog_info[6]
#         except AttributeError:
#             syslog_info = re.match(r'^<(\d*)>(\d*): \*(.*): (\w+): (.*)', str(data)).groups()
#             print(syslog_info[0])
#             syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
#             syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
#             syslog_info_dict['logid'] = int(syslog_info[1])
#             syslog_info_dict['time'] = parser.parse(syslog_info[2])
#             syslog_info_dict['log_source'] = syslog_info[3]