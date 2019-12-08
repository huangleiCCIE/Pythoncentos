import netifaces as ni
import winreg as wr

def get_coonection_name_from_guid(iface_guids):
    #接口名字和Windows唯一ID的清单
    iface_dict = {}
    #打开'HKEY_LOCAL_MACHINE'
    reg = wr.ConnectRegistry(None,wr.HKEY_LOCAL_MACHINE)
    # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in iface_guids:
        try:
            #尝试读取每一个接口ID下对应的Name
            reg_subkey = wr.OpenKey(reg_key, i + r'\Connection') #打开拼接后的注册表路径
            #如果存在Name，写入iface_dict字典
            iface_dict[wr.QueryValueEx(reg_subkey,'Name')[0]] = i #读取Name放入印刷的字典
        except FileNotFoundError:
            pass
    return  iface_dict

def win_from_name_get_id(ifname):
    x =ni.interfaces()
    return  get_coonection_name_from_guid(x).get(ifname)

if __name__ == '__main__':
    print(win_from_name_get_id('以太网')) #将windows的网卡名字窜进去，会返回一个网卡唯一ID