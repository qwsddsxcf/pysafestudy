import random
import time

from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from scapy.sendrecv import sr1
'''
seq看自己，ack看对方的seq
不要使用同一机器,因为没有使用socket,所以操作系统没有进行记录获得tcb(控制头),会发rst
如果没有记录在后面的每一条连接都是新连接，只有在使用socket时才被操作系统记录
在使用本机ip和127.0.0.1都会进入回环，Scapy 创建的 Raw Socket在底层处理路径中注册自己，因此可以抓住（在送往内核之前）数据包
但是在本地回环的情况下，所有数据包由内核直接决策（触发rst-没有tcb）。Raw Socket无法处理，只能监听
'''
if __name__ == '__main__':
    seq=random.randint(100000,200000)
    data=IP(dst='192.168.217.88')/TCP(sport=4455,dport=9999, flags='S',seq=seq)
    rep=sr1(data,timeout=3,verbose=0)
    ack=rep[TCP].seq+1
    seq1=rep[TCP].ack
    data1=IP(dst='192.168.217.88')/TCP(sport=4455,dport=9999, flags='A',seq=seq1,ack=ack)
    rep1=sr1(data1,timeout=3,verbose=0)

    data2=IP(dst='192.168.217.88')/TCP(sport=4455,dport=9999, flags='PA',seq=seq1,ack=ack)/"hello hack"
    rep2=sr1(data2,timeout=3,verbose=0)
    time.sleep(2)
    print(rep2.show())
'''
一、三次握手（Three‐way Handshake）
假设客户端初始序列号（ISN）为 x，服务器 ISN 为 y。

SYN (客户端 → 服务器)

报文段：SYN, Seq = x

含义：客户端请求建立连接，自己选择一个起始序列号 x。

SYN-ACK (服务器 → 客户端)

报文段：SYN, ACK, Seq = y, Ack = x + 1

含义：

Seq = y：服务器也用自己的 ISN y。

Ack = x + 1：确认客户端的 SYN（SYN 本身也消耗 1 个序列号），告诉客户端“我已经收到了你第一个包”。

ACK (客户端 → 服务器)

报文段：ACK, Seq = x + 1, Ack = y + 1

含义：

Seq = x + 1：客户端的下一个发送序号（握手中自己的 SYN 占用了一个）。

Ack = y + 1：确认服务器的 SYN。

此时，双方连接状态都进入 ESTABLISHED，序列号空间正式打开。

二、数据传输中的 Seq/Ack 变化
假设现在客户端要向服务器发送一段长度为 L1 字节的数据，随后服务器又发送一段长度为 L2 字节的数据。

客户端发送数据段 1

报文段：PSH, ACK, Seq = x + 1, Ack = y + 1, Data = [L1 字节]

含义：客户端从序号 x+1 开始，发送 L1 字节数据。

服务器确认数据段 1

报文段：ACK, Seq = y + 1, Ack = (x + 1) + L1

含义：

Ack = x + 1 + L1：告诉客户端“我已经成功接收到你从 x+1 到 x+L1 的所有数据，下一个期待序列号是 x + 1 + L1。”

Seq = y + 1：还是沿用服务器自己的下一个发送序号（没有新数据时一般不变）。

服务器发送数据段 2

报文段：PSH, ACK, Seq = y + 1, Ack = x + 1 + L1, Data = [L2 字节]

客户端确认数据段 2

报文段：ACK, Seq = x + 1 + L1, Ack = (y + 1) + L2

'''