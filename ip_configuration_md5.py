import hashlib
import sqlite3
import re
import paramiko

def qytang_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password,timeout=5 , compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return  x

def get_config_md5(ip, username='admin', password='Cisc0123'):
    try:
        device_config_raw = qytang_ssh(ip, username, password, 'show run')
        split_result = re.split(r'\r\nhostname \S+\r\n', device_config_raw)
        device_config = device_config_raw.replace(split_result[0], '').strip()

        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        return device_config, md5_value

    except Exception:
        return

#设备信息
device_list = ['192.168.88.254']
username = 'admin'
password = 'Cisc0123'

#将配置和MD5值写入数据库
def write_config_md5_to_db():
    conn = sqlite3.connect('ip_config_md5.sqlite')
    cursor = conn.cursor()
    for device in device_list:    #遍历IP地址
        config_and_md5 = get_config_md5(device, username, password)  #得到的md5值赋值到config_and_md5
        cursor.execute('select * from config_md5 where ip= ?',(device, )) #看一下设备配置是否备份过
        md5_result = cursor.fetchall() #得到结果
        if not md5_result:  #如果没有结果，将ip、配置、md5写入数据库    config_and_md5[0]:配置  config_and_md5[1]:md5值
            cursor.execute('insert into config_md5(ip, config, md5) values (?, ?, ?)',(device,
                                                                                      config_and_md5[0],
                                                                                      config_and_md5[1]))
            conn.commit() #提交

        else: #如果有结果      config_and_md5[1]:MD5值     md5_result[0]:表示在数据库第1个条目  md5_result[2]:md5值
            if config_and_md5[1] != md5_result[0][2]:  #如果md5值不相等
                cursor.execute('update config_md5 set config=?, md5=? where ip =？',(config_and_md5[0],  #更新配置
                                                                                   config_and_md5[1],  #更新MD5
                                                                                   device)) #更新IP
                conn.commit()
            else: #如果相等就继续
                continue
    cursor.execute('select * from config_md5') #查看这个表
    all_result = cursor.fetchall() #得到结果
    for x in all_result:  #遍历这个结果
        print(x[0], x[2])  #打印IP和MD5值
    conn.close() #关闭

if __name__ == '__main__':
    import os
    if os.path.exists('ip_config_md5.sqlite'):
        os.remove('ip_config_md5.sqlite')

    conn = sqlite3.connect('ip_config_md5.sqlite')
    cursor = conn.cursor()

    #执行表的任务
    cursor.execute('create table config_md5 (ip varchar(40), config varchar(99999), md5 varchar(1000))')
    conn.commit()
    conn.close()
    write_config_md5_to_db()