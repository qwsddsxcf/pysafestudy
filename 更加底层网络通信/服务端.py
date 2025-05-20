from scapy.all import *
import os
import random
from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from scapy.sendrecv import sr1

def handle_packet(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 9999:
        if pkt[TCP].flags & 0x02:  # SYN
            print(f"收到SYN from {pkt[IP].src}")
            ack_pkt = IP(dst=pkt[IP].src) / TCP(sport=9999, dport=pkt[TCP].sport,
                                                flags="SA", seq=1000, ack=pkt[TCP].seq + 1)
            send(ack_pkt, verbose=0)

        elif pkt[TCP].flags & 0x10:  # ACK
            print(f"连接建立 with {pkt[IP].src}")

        elif pkt.haslayer(Raw):  # 数据
            data = pkt[Raw].load.decode('utf-8')
            print(f"收到数据: {data}")

            # 构造响应
            resp = IP(dst=pkt[IP].src) / TCP(sport=9999, dport=pkt[TCP].sport,
                                             flags="PA", seq=pkt[TCP].ack,
                                             ack=pkt[TCP].seq + len(data)) / b"Server response"
            send(resp, verbose=0)


if __name__ == "__main__":
    print("Scapy服务端监听中...")
    sniff(filter="tcp port 9999", prn=handle_packet)