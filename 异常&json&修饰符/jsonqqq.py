import pymysql
import json
from pymysql.cursors import DictCursor

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="password", db="user")
cur = conn.cursor(DictCursor)
sql = "select * from admin"
cur.execute(sql)
data = cur.fetchall()
conn.close()
print(data)
print(type(data))
j=json.dumps(data)
print(j)
print(type(j))
str='[{"id": 1, "username": "xiaodi", "password": "xiaodisec"}, {"id": 2, "username": "hack111", "password": "admin"}, {"id": 3, "username": "test", "password": "test"}, {"id": 4, "username": "wwwww", "password": "wwww"}]'
c=json.loads(str)
print(c)
print(type(c))