import os,threading
#"192.168.161.131"
from scapy.all import *
from scapy.layers.l2 import ARP

'''
基于arp的多线程IP段存活主机扫描
'''
def ipsaomiao(start,end,ip):
    print(f"正在扫描：{start, end - 1}")
    for i in range(start, end):
       dip=ip+str(i)
       try:
           #print(dip)
           data=ARP(pdst=dip)
           fasong=sr1(data,timeout=1,verbose=0)
           if fasong and ARP in fasong:
               print(fasong[ARP].hwsrc)
               print(f"发现存活主机：{dip}")
       except:
           pass
def conzhi(start,end,ip,xiancheng):
    '''
    需要传入的ip是主机段，即192.168.10.
    指定起始和结束，线程数
    :param start: 起始
    :param end: 结束
    :param ip: 主机段
    :param xiancheng: 线程数
    :return:
    '''
    all=end-start+1
    geshu=all//xiancheng
    yushu=all%geshu

    for i in range(0,xiancheng):
        thread=threading.Thread(target=ipsaomiao,args=(start+i*geshu,start+(i+1)*geshu,ip))
        thread.start()

    threading.Thread(target=ipsaomiao, args=(end-yushu,end+1,ip)).start()


if __name__=="__main__":
    #ipsaomiao(130,150,'192.168.161.')
    conzhi(1,255,"192.168.161.",10)