import paramiko
import socket

def qytang_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    except paramiko.ssh_exception.AuthenticationException as e:
        print('认证错误',e)
        return
    except socket.timeout as e:
        print('连接超时',e)
        return
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print('SSH请求被管理过滤',e)
        return
    else:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        if 'Line has invalid autocommand' in x:
            print('命令不能被执行！请检查用户权限！')
            return
        else:
            return x
    return x

if __name__ == '__main__':
    print(qytang_ssh('192.168.88.254', 'admin', 'Cisc0123', cmd='show run', port=22))