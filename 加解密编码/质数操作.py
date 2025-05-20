import time,math
def iszhishu(a):
    '''
    该函数用于判断一个数是否为质数，如果是则返回真，否则为假
    通过循环的方式，循环到该数开方后，然后取余看是否被整除
    :param a:
    :return:
    '''
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
def zaojieguo(a):
    '''
    该函数用于传入一个两个质数相乘的数，然后反向查找这两个数（循环查找）
    循环到该数除以2的位置，并且判断该数是否为质数
    找到则输出返回真，否则返回假
    :param a:
    :return:
    '''
    start=time.time()
    for i in range(1,a//2+1):
        for j in range(1,a//2+1):
            if i*j==a and iszhishu(i) and iszhishu(j):
                end=time.time()
                print("找到了：")
                print(i,j)
                print(end-start)
                return True
    print("没有找到")
    return False
if __name__ == '__main__':
    #197*9973
    zaojieguo(1964681)#没有优化前10秒,优化后5

