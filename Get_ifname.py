import netifaces as ni

import platform


def get_connection_name_from_guid(iface_guids):
    if platform.system() == "Windows":
        import winreg as wr
        # 产生接口名字清单,默认全部填写上'(unknown)'
        iface_names = ['(unknown)' for i in range(len(iface_guids))]
        # 打开"HKEY_LOCAL_MACHINE"
        reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
        # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'
        #
        reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
        for i in range(len(iface_guids)):
            try:
                # 尝试读取每一个接口ID下对应的Name
                reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
                # 如果存在Name,就按照顺序写入iface_names
                iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
            except FileNotFoundError:
                pass
        # 把iface_guids, iface_names 压在一起返回
        return zip(iface_guids, iface_names)


def get_ifname(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        import winreg as wr
        x = ni.interfaces()
        for i in get_connection_name_from_guid(x):
            # 找到名字所对应的接口ID并返回
            if i[1] == ifname:
                return i[0]
    else:
        print('操作系统不支持,本脚本只能工作在Windows或者Linux环境!')


if __name__ == "__main__":
    print(ni.interfaces())   #windows环境下找到所有网卡的唯一ID   linux找到所有网卡的名字
    # print(get_ifname("以太网")) #windows环境下输入一个名字，找到网卡的唯一ID
