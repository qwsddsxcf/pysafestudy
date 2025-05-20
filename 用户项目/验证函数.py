import re
def check_name(name):
    '''
    检查用户输入的用户名是否符合长度5，12之间，不能以数字开头，只能由数字和字母组成
    正确返回真，错误返回假
    :param name:
    :return:
    '''
    if len(name)<5 or len(name)>12:
        return False
    if name[0]>='0' and name[0]<='9':
        return False
    for i in range(1,len(name)):
        if not((name[i]>='a' and name[i]<='z') or (name[i]>='A' and name[i]<='Z') or (name[i]>='0' and name[i]<='9')):
            return False
    return True
def check_passwd(passwd):
    '''
    检查用户输入的密码是否合法，，密码长度在6，12之间，必须包含一个数字，小写，大写字母
    正确返回真，错误返回假
    :param passwd:
    :return:
    '''
    if len(passwd)<6 or len(passwd)>12:
        return False
    daxie=0
    xiaoxie=0
    shuzi=0
    for i in range(0,len(passwd)):
        if ord(passwd[i]) in range(ord('A'),ord('Z')+1):
            daxie=daxie+1
        if ord(passwd[i]) in range(ord('a'),ord('z')+1):
            xiaoxie=xiaoxie+1
        if ord(passwd[i]) in range(ord('0'),ord('9')+1):
            shuzi=shuzi+1
    if daxie<1 or xiaoxie<1 or shuzi<1:
        return False
    return True
def check_phone(phone):
    '''
    检查用户输入的手机号是否合法，使用正则表达式校验,^$匹配全部，以1开头，第二位3到9，后面用数字9个
    正确返回真，错误返回假
    :param phone:
    :return:
    '''
    rule="^[1][3-9]\d{9}$"
    result=re.match(rule,phone)
    if result:
        return True
    else:
        return False
if __name__ == '__main__':
    def test_function(func,expt,*arg):
        res=func(*arg)
        if res==expt:
            print("测试成功，函数:%s" % func.__name__)
        else:
            print("测试失败，函数：%s" % func.__name__)

    test_function(check_name,True,"123")
    test_function(check_name, True, "12345")
    test_function(check_name, True, "q12345")
    test_function(check_name, True, "qqqqqqq#")
    test_function(check_name, True, "qqqqqqqqqqqqqqqqqq")
    print("====================================")
    test_function(check_passwd,True,"123")
    test_function(check_passwd, True, "123456")
    test_function(check_passwd, True, "as12BAa")
    test_function(check_passwd, True, "as123edf")
    test_function(check_passwd, True, "adcD123")
    print("=====================================")
    test_function(check_phone,True,"11111")
    test_function(check_phone, True, "111111111111111")
    test_function(check_phone, True, "18336132760")
    test_function(check_phone, True, "12312341234")
    test_function(check_phone, True, "2222")
