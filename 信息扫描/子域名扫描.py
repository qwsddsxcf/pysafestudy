import socket,os

with open("zidianlujing", "r") as f:
    yuming = f.readlines()
#D:\hack\字典\字典\挺全的字典集合\subdomainDicts
def pingsaomiaoziyu(zhuyu):

    for i in yuming:
        mingling=f"ping -n 1 -w 100 {i.strip()+'.'+zhuyu}"
        fanhu=os.popen(mingling).read()
        if "TTL=" in fanhu or "正在" in fanhu:
            print(f"发现子域名；{i.strip()+'.'+zhuyu}")
    print("扫描完成")
def socketsaomiaoziyu(zhuyu):
    for i in yuming:
        try:
            ip=socket.gethostbyname(i.strip()+'.'+zhuyu)
            print(f"发现子域名；{i.strip() + '.' + zhuyu},ip为：{ip}")
        except:
            pass
    print("扫描完成")

if __name__ == '__main__':
    #pingsaomiaoziyu("hist.edu.cn")
     socketsaomiaoziyu("hist.edu.cn")