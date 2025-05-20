import time,os
from collections import Counter
'''
该代码用于实现防御基于tcp的dos攻击，通过
检测cpu负载，tcp连接数量，接收队列，发送队列
判断是否被攻击，并在检测到被攻击后，自动驱动
防火墙进行ip封锁，以实现抗dos攻击
'''
port=80#要防御的tcp端口
cpumax=0.75#cpu预警的阈值
tcpmax=800#tcp预警的阈值
duiliechazhi=20#接收队列的预警差值
def getcpufuzai():
    '''
    该函数用于获取cpu平均负载
    :return:
    '''
    data=os.popen("uptime | awk -F ': ' '{print $2}'|awk -F ',' '{print $1}'").read()
    return data
def gettcplianjieshu():
    '''
    该函数用于获取tcp连接数量
    :return:
    '''
    data=os.popen("netstat -ant | wc -l").read()
    return data

def getrecqsenq():
    '''
    该函数用于获取接收队列，发送队列值
    :return:
    '''
    data=os.popen(f"ss -lnt | grep :{port}").read()
    datashi=data.split()
    return datashi[1],datashi[2]

def getallip():
    '''
    该函数用于获取访问该tcp端口的所有ip
    :return:
    '''
    data=os.popen(f"netstat -ant | grep :{port}").read().split('\n')
    ipshuju=[]
    for i in data:
        try:
            i=i.split()[4]
            i=i.split(':')[0]
            ipshuju.append(i)
        except:
            pass
    return ipshuju
def findgongjiip(shunxu=1):
    '''
    该函数用于获取访问的ip中的攻击者ip
    :param shunxu: 默认只封锁访问次数最多的ip
    :return:
    '''
    ipshuju=getallip()
    dict=Counter(ipshuju)
    attip=dict.most_common(shunxu)
    return attip[0][0]

def conzhifirewalld():
    '''
    该函数用于驱动防火墙封锁ip
    :return:
    '''
    attip=findgongjiip()
    print(f"已经找到攻击ip:{attip},正在驱动防火墙进行自动封锁。。。。")
    data=os.popen(f"sudo firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address={attip} port port={port} protocol=tcp reject'").read()
    os.popen("sudo firewall-cmd --reload")
    if "success" in data:
        print("已经自动防御成功，该ip已被封锁！")
    else:
        print("出现未知错误，封锁失败，请管理员手动处理")


if __name__ == '__main__':
    while True:
        cpufuzai=getcpufuzai().strip()
        tcplianjieshu=gettcplianjieshu().strip()
        recq,sendq=getrecqsenq()
        print(f"cpu平均负载：{cpufuzai}, tcp连接数量：{tcplianjieshu}, 已经接收的recq:{recq}, 已发送未回应的sendq:{sendq}")
        cpu, tcp, duilie = 0, 0, 0
        if float(cpufuzai)>=cpumax:
            print("cpu负载过高！")
            cpu=1
        if float(tcplianjieshu)>=tcpmax:
            print("tcp连接数过高！")
            tcp=1
        if float(recq)>=float(sendq)-duiliechazhi:
            print("发现大量未处理的数据包，网络接收队列拥堵！")
            duilie=1
        all=cpu+tcp+duilie
        if all>=2:
            '''
            当2个值都超过阈值就会进行封锁
            '''
            print("系统疑似正在遭受dos攻击！正在进行自动防御。。。")
            conzhifirewalld()
        cpu,tcp,duilie=0,0,0
        time.sleep(5)