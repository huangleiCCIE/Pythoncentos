import paramiko
import re
from 图.饼状图 import mat_bing

def ssh_singlecmd(ip, username, password, cmd):
    try:
        ssh = paramiko.SSHClient() #创建SSH Client
        ssh.load_system_host_keys() #加载系统SSH秘钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #添加新的SSH秘钥
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True) #SSH连接
        stdin, stdout, stderr = ssh.exec_command(cmd) #执行命令
        x = stdout.read().decode() #读取回显
        ssh.close()
        return x

    except Exception as e:
        print('%stErrorn %s' % (ip, e))

def get_netflow_app():
    show_result = ssh_singlecmd('192.168.88.254', 'admin', 'Cisc0123', 'show flow monitor name qytang-monitor cache format table')
    app_name_list = []
    app_bytes_list = []
    for line in show_result.strip().split('\n'):  #将多余的空格去掉
        app_bytes = re.match(r'^((port|layer7) [a-z]+)\s+(\d+)',line)  #提取想要的关键字
        if app_bytes: #如果存在
            app_name_list.append(app_bytes.groups()[0])  #取需要的部分
            app_bytes_list.append(app_bytes.groups()[2])  #取需要的部分
    mat_bing(app_bytes_list, app_name_list)  #x轴的内容，y轴的内容

if __name__ == '__main__':
    get_netflow_app()