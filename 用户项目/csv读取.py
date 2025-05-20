def load_csv(filename,set=True,relu=True):
    '''
    函数用于将一个csv格式的文件中的数据转换为列表，元素为字典，第一个参数传递文件路径
    第二个参数默认为真，如果为假，则默认不执行任何操作，并抛出异常，返回值为转换后的列表
    如果以#开头，则忽略该行内容
    :param filename:
    :param set:
    :return:
    '''
    if not set:
        raise Exception("该文件必须是csv格式")
    with open(filename,'r',encoding='utf-8') as f:
        listlines=f.readlines()#读取文件，以换行符为分割转为列表

    listone=listlines[0].strip().split(",")#取出首个元素作为字典的key

    listallinfo=[]#用于装载用户信息的列表

    for i in range(1,len(listlines)):
        if relu and listlines[i].startswith("#"):
            continue
        dictinfo = {}
        listuserinfo=listlines[i].strip().split(",")#首尾区空，并且以，为分隔符分为列表不同元素
        for j in range(len(listone)):
            dictinfo[listone[j]]=listuserinfo[j]#将该字典的键值一一对应
        listallinfo.append(dictinfo)

    return listallinfo

def checkusername(username,filename):
    '''
    函数用于检查要注册的用户名是否已被注册，如果已被注册则返回已注册的用户信息字典，未注册则返回空
    函数调用load_csv(filename,set=True)完成主要功能呢
    :param username:
    :param filename:
    :return:
    '''
    list=load_csv(filename)
    for i in list:
        if username==i['username']:
            return i
    return None

if __name__=='__main__':
    pass
    # list=checkusername("weizhi3")
    # print(list)