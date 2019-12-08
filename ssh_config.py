import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient() #创建SSH Client
    ssh.load_system_host_keys() #加载系统SHH秘钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #添加新的秘钥
    ssh.connect(ip, port=22, username=username, password=password,timeout=5, compress=True)  #ssh连接
    chan = ssh.invoke_shell() #激活交互式shell
    time.sleep(1)  #等待网络设备回应
    x = chan.recv(2048).decode()
    if  enable and  '>' in x:
        chan.send('enable'.encode())  #传入enable命令
        chan.send(b'\n')  #换行
        chan.send(enable.encode())  #输入enable密码
        chan.send(b'\n')  # 换行
        time.sleep(wait_time)
    elif not enable and  '>'  in x:
        print('需要配置enable密码！')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(40960).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()

if __name__ == '__main__':
    qytang_multicmd('192.168.88.254',
                    'admin',
                    'Cisc0123',
                    [
                    'terminal length 0',   #敲了这句话，version的内容才能全部显示
                    'show version',
                    'config t',
                    'router ospf 1',
                    'network 192.168.88.0 0.0.0.255 area 0'
                    ],
                    enable = 'Cisc0123',
                    wait_time=1,
                    # verbose =False   #为false 不会显示打印的内容
                    )
