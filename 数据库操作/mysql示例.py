import pymysql
from pymysql.cursors import DictCursor

# conn=pymysql.connect(host="localhost",user="root",passwd="root",db="user")
# cur=conn.cursor()
# sql="select * from admin"
# cur.execute(sql)
# result=cur.fetchall()
# print(result)
# cur.close()

# conn=pymysql.connect(host="localhost",user="root",passwd="root",db="user")
# cur=conn.cursor(DictCursor)
# sql="select * from admin"
# cur.execute(sql)
# for i in cur.fetchall():
#     print(i["id"],i["username"],i["password"])
# cur.close()

# conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="user")
# cur=conn.cursor(DictCursor)
# sql="update admin set username='hack111' where username='hack';"
# cur.execute(sql)
# conn.commit()
# cur.close()

# conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="user")
# cur=conn.cursor()
# sql="insert into admin(id,username,password) values(3,'test','test');"
# cur.execute(sql)
# conn.commit()
# cur.close()
