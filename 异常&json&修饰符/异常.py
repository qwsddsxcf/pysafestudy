import pymysql
# conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="user")
# cur=conn.cursor()
# sql="select * from users111"
# cur.execute(sql)
#pymysql.err.OperationalError,pymysql.err.ProgrammingError
try:
    conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="user")
    cur=conn.cursor()
    sql = "select * from admin"
    cur.execute(sql)
    print("未出现错误")
except pymysql.err.OperationalError as e:
    print(e)
    print("数据库配置有误")
except pymysql.err.ProgrammingError as e:
    print(e)
    print("sql语句有误")
except:
    print("weizhi")
else:
    print("hhhh")
finally:
    conn.close()
    print("代码执行完成")
