import socket,threading
from scapy.all import *
from scapy.layers.inet import IP, TCP

'''
该代码用于基于tcp的主机端口存活扫描，可指定线程数
通过建立半tcp连接的方式看是否报错来确认端口是否开放tcp连接
'''
def duankousaomiao(ip,start,end):
    '''
    该函数用于扫描端口判断是否存活
    :param ip: 传入要扫描的ip
    :param start: 传入起始
    :param end: 出入结束
    :return:
    '''
    print(f"扫描端口范围：{start,end-1}")
    for i in range(start,end):
        try:
            data=IP(dst=ip)/TCP(dport=i,flags='S')#发送tcp握手中的第一次标志
            fasong=sr1(data,timeout=3,verbose=0)#verbose=0不要输出多于信息
            if fasong[TCP].flags ==0x12:#通过判断返回数据包中的标识是否是第二次握手判断是否成功(sa)
                print(fasong[TCP].flags)
                print(f"端口存活：{i}")
        except:
            pass


def conzhi(ip,start,end,xiancheng):
    '''
    该函数用于控制扫描函数，配置线程数
    :param ip:
    :param start:
    :param end:
    :param xiancheng: 要多少线程进行扫描
    :return:
    '''
    all=end-start+1
    geshu=all//xiancheng#根据指定的线程数来计算每个线程分配多少个端口
    yue=all%geshu

    for i in range(0,xiancheng):
        threading.Thread(target=duankousaomiao,args=(ip,start+i*geshu,start+(i+1)*geshu)).start()
    threading.Thread(target=duankousaomiao,args=(ip,end-yue,end+1)).start()
if __name__ == '__main__':
    conzhi('192.168.161.137',1,999,57)
    #duankousaomiao('192.168.161.131',19,100)
    # data = IP(src="192.168.161.135",dst='192.168.161.131') / TCP(dport=22, flags='S')
    # fasong = sr1(data, timeout=3, verbose=0)