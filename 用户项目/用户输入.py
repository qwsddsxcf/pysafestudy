import 验证函数 as yanzheng
import csv读取 as csv
def input_name():
    name=input("请输入要注册的用户名：")
    if not csv.checkusername(name,"txt/3.csv"):

        if yanzheng.check_name(name):
            print("用户名合法")
            return name
        else:
            print("用户名不合法，请重新输入！")
            input_name()
    else:
        print("用户名已存在")
        input_name()
def input_passwd():
    passwd = input("请输入要注册的密码：")
    if yanzheng.check_passwd(passwd):
        print("密码合法")
        return passwd
    else:
        print("密码不合法，请重新输入！")
        input_passwd()
def input_phone():
    phone = input("请输入要注册的手机号：")
    if yanzheng.check_phone(phone):
        print("手机号合法")
        return phone
    else:
        print("手机号不合法，请重新输入！")
        input_phone()
def input_all():
    username=input_name()
    passwd=input_passwd()
    phone=input_phone()
    return username,passwd,phone


if __name__ == '__main__':
    input_all()