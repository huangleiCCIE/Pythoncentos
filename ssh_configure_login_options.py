from ssh import  qytang_ssh
from argparse import ArgumentParser

usage = 'usage: python Simple_SSH_Client.py -i ipaddr -u username -p password -c command'
parser = ArgumentParser(usage=usage)

parser.add_argument('-i', '--ipaddr', dest='ipaddr', help='SSH Server',default='192.168.88.254',type=str)
parser.add_argument('-u', '--username', dest='username', help='SSH Username',default='admin',type=str)
parser.add_argument('-p', '--password', dest='password', help='SSH Password',default='Cisc0123',type=str)
parser.add_argument('-c', '--command', dest='command', help='Shell Command',default='show ip int bri',type=str)

args = parser.parse_args()
print(qytang_ssh(args.ipaddr,args.username,args.password,cmd=args.command))


