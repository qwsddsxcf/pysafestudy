import pymysql
def select(username):
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='password',db='user')
    cur = conn.cursor()
    sql=f"select * from admin where username = '{username}';"
    print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result
def insert(id,username,password):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='user')
    cur = conn.cursor()
    sql = f"insert into admin(id,username,password) values('{id}','{username}','{password}');"
    cur.execute(sql)
    conn.commit()
    conn.close()
def showui():
    username=input("请输入用户名：")
    password=input("请输入密码：")
    result=select(username)
    if len(result)==0:
        insert(4,username,password)
        print("注册成功！")
    else:
        print("该用户已存在！")
        showui()
if __name__=="__main__":
    showui()