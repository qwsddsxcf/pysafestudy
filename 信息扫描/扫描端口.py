import socket,threading
'''
该代码用于基于tcp的主机端口存活扫描，可指定线程数
通过建立tcp连接的方式看是否报错来确认端口是否开放tcp连接
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
            s=socket.socket()
            s.settimeout(0.1)
            s.connect((ip,i))
            print(f"端口存活：{i}")
        except:
            pass
        finally:
            s.close()

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
    conzhi('192.168.10.8',1,9999,57)