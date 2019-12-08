from 获取win或linux_IP import get_ip_address
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp
from pyasn1.codec.ber import decoder
from pysnmp.proto import api

def analysis(info):
    ospf_status_dict = {'1' : 'down',
                        '2' : 'attempt',
                        '3' : 'init',
                        '4' : 'twoWay',
                        '5' : 'exchangeStart',
                        '6' : 'exchange',
                        '7' : 'loading',
                        '8' : 'full'
                        }
    # cbFun函数传进来一个字典result_dict
    # 1.3.6.1.2.1.14.10.1 获取OSPF整体OID摘要信息
    # 1.3.6.1.2.1.14.10.1.6 为OSPF邻居状态改变OID
    # 1.3.6.1.2.1.14.10.1.1 获取OSPF邻居IP地址的OID
    # 1.3.6.1.2.1.14.10.1.3 获取OSPF邻居Router-id的OID
    if '1.3.6.1.2.1.14.10.1.6' in info.keys():
        ospf_nei_ip = info['1.3.6.1.2.1.14.10.1.3']['ipAddress-value']
        ospf_status = info['1.3.6.1.2.1.14.10.1.6']['integer-value']
        print("OSPF Neighbor {0} {1}".format(ospf_nei_ip, ospf_status_dict.get(ospf_status)))

def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):  # 处理Trap信息的函数
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))  # 提取版本信息
        if msgVer in api.protoModules:  # 如果版本兼容
            pMod = api.protoModules[msgVer]
        else:  # 如果版本不兼容，就打印错误
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),  # 对信息进行解码

        )
        print('Notification message from %s:%s: ' % (
            transportDomain, transportAddress  # 打印发送TRAP的源信息
        )
              )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:  # SNMPv1的特殊处理方法,可以提取更加详细的信息
                print('Enterprise: %s' % (
                    pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                )
                      )
                print('Agent Address: %s' % (
                    pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                )
                      )
                print('Generic Trap: %s' % (
                    pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                )
                      )
                print('Specific Trap: %s' % (
                    pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                )
                      )
                print('Uptime: %s' % (
                    pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                )
                      )
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:  # SNMPv2c的处理方法
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)

            result_dict = {}  # 每一个Trap信息,都会整理返回一个字典
            for x in varBinds:  # 打印详细Trap信息
                result = {}
                for x, y in x.items():
                    # print(x, y.prettyPrint())  # 最原始信息打印
                    # 处理信息到字典
                    if x == "name":
                        id = y.prettyPrint()  # 把name写入字典的键
                    else:
                        bind_v = [x.strip() for x in y.prettyPrint().split(":")]
                        for v in bind_v:
                            if v == '_BindValue':
                                next
                            else:
                                result[v.split('=')[0]] = v.split('=')[1]
                result_dict[id] = result
            # 把字典传到分析模块进行分析
            analysis(result_dict)

    return wholeMsg


def snmp_trap_receiver(ifname, port=162):
    if_ip = get_ip_address(ifname)
    transportDispatcher = AsynsockDispatcher()  # 创建实例

    transportDispatcher.registerRecvCbFun(cbFun)  # 调用处理Trap信息的函数

    # UDP/IPv4
    transportDispatcher.registerTransport(
        udp.domainName, udp.UdpSocketTransport().openServerMode((if_ip, port))  # 绑定到本地地址与UDP/162号端口
    )

    transportDispatcher.jobStarted(1)  # 开始工作
    print("SNMP Trap Receiver Started!!!")
    try:
        # Dispatcher will never finish as job#1 never reaches zero
        transportDispatcher.runDispatcher()  # 运行
    except:
        transportDispatcher.closeDispatcher()
        raise

if __name__ == "__main__":
    # WIN解释器,linux有点问题
    snmp_trap_receiver("VMware Network Adapter VMnet8")  #windows

