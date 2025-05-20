import hashlib,time
'''
该代码用于实现md5的爆破实现
'''
def md5jiami(sour):
    '''
    该函数用于md5加密
    :param sour:
    :return:
    '''
    jiami=hashlib.md5(sour.encode()).hexdigest()
    return jiami
def baopomd5():
    '''
    该函数是利用字典的方式爆破md5
    :return:
    '''
    with open('zidianlujing','r') as f:
        list=f.readlines()
        for i in list:
            i=i.strip('\n')
            if "md5zhi"==md5jiami(i):
                print(f"找到密码了：{i}")
                return True
    print("没有找到密码")
    return False


#file:D:\hack\字典\fuzzDicts-master\passwordDict
#2926676d98a979f2d910e03746faec12
if __name__ == '__main__':
    baopomd5()
