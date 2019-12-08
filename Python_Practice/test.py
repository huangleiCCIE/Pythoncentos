import  re

a = '192.168.1.1 192.168.1.2'

result = re.match('(\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3})',a).groups()
print(result[0])