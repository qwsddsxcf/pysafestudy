"""
show_interfaces()显示所有网卡

data = sniff(count=10, filter="icmp", iface="VMware Network Adapter VMnet8")选择要监听的网卡

att=(IP(dst="192.168.161.131")/ICMP()/"hello weizhi hack")创建数据包
send(att,inter=1,count=10)发送数据包，inter时间间隔
ff=sr1(att)发送并接收返回值


data[0].show()展示返回数据
data.summary()展示全部


arp=ARP(psrc="192.168.161.1",pdst="192.168.161.131")
c=sr1(arp)

"""