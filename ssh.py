import re
def qytang_ssh(ip, username, password, port=22, cmd = 'show run'):   #给ip，用户名，密码，登进去执行show ip int bri
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    return stdout.read().decode()
    # for gw in a.split('\n'):
    #     re_gw = re.match('\w+\d+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+\w+\s+\w+\s+\w+', gw)
    #     if re_gw:
    #         if re_gw.groups()[1] == 'YES':
    #             return re_gw.groups()[0]
    #

#
# def ssh_get_route(ip, username, password):
#     result = qytang_ssh(ip, username, password, cmd ='show ip int bri')
#     for gw in result.split('\n'):
#         re_gw = re.match('\w+\d+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+\w+\s+\w+\s+\w+',gw)
#         if re_gw:
#             if re_gw.groups()[1] == 'YES':
#                 return re_gw.groups()[0]

if __name__ == '__main__':
    # print(qytang_ssh('192.168.88.2', 'root', 'Cisc0123', cmd='pwd'))
    print('网关为：')
    print(qytang_ssh('192.168.88.254','admin','Cisc0123'))

