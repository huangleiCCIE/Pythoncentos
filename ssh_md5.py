from ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Cisc0123'):
    try:
        ssh_config = qytang_ssh(ip, username, password,port=22,cmd='show run')
        result_ssh_config = re.split(r'\r\nhostname \S+\r\n', ssh_config)
        config = ssh_config.replace(result_ssh_config[0],'').strip()
        return  config
    except Exception:
        return
#
def qytang_check_diff(ip, username='admin', password='Cisc0123'):
    beforce_md5 = ''
    while True:
        config = qytang_get_config(ip, username, password='Cisc0123')
        a = hashlib.md5()
        a.update(config.encode())
        md5 = a.hexdigest()
        print(md5)
        if not beforce_md5:
            beforce_md5 = md5
        elif beforce_md5 != md5:
            print('MD5 value changed')
            break
        time.sleep(5)


    qytang_check_diff('192.168.88.254', username= 'admin', password= 'Cisc0123')
