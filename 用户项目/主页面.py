import 用户输入 as shuru
import csv读取 as csv
def userzhuce():
    username,passwd,phone=shuru.input_all()
    with open("txt/3.csv","a") as f:
        f.write(f"\n{username},{passwd},{phone}")
    print("注册成功！")
    showui()
def userlogin():
    username=input("请输入用户名：")
    passwd=input("请输入密码：")
    userinfo=csv.checkusername(username,"txt/3.csv")
    if userinfo is None:
        print("该用户名不存在！")
        userlogin()
    else:
        if userinfo["passwd"]==passwd:
            print("登录成功！")
            showui()
        else:
            print("密码错误，登陆失败！")
            userlogin()

def changepasswd():
    username = input("请输入用户名：")
    passwd = input("请输入密码：")
    newpasswd=input("请输入要更改的新密码：")
    userinfo = csv.checkusername(username, "txt/3.csv")
    if userinfo is None:
        print("该用户名不存在！")
        changepasswd()
    elif userinfo["passwd"]!=passwd:
        print("密码错误，更改失败！")
        changepasswd()
    else:
        dict = csv.load_csv("txt/3.csv", relu=False)
        for i in dict:
            if i["username"]==username:
                i["passwd"]=newpasswd
                break
        with open("txt/3.csv","w") as f:
            c="username,passwd,phone\n"
            f.write(c)
            for i in dict:
                content=f'{i["username"]},{i["passwd"]},{i["phone"]}'
                f.write(content+"\n")
        print("更改成功！")
        showui()

def showui():
    print("==============迎使用用户管理系统================")
    print("1，用户注册  2，用户登录  3，更改密码  4，退出")
    choice=input("请输入选择：")
    if choice=="1":
        userzhuce()
    elif choice=="2":
        userlogin()
    elif choice=="3":
        changepasswd()
    elif choice=="4":
        exit(0)
    else:
        print("请输入正确的选项！")
        showui()

if __name__=="__main__":
    showui()
