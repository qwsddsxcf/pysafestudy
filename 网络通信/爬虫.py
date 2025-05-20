import bs4
import requests
from bs4 import BeautifulSoup

'''
爬虫：首先使用request返回内容，选择要解析的格式lxml=>html,然后对返回对象进行操作
获取的是完整的标签，如果是多个返回的是列表中字典形式
方式1：直接调用对象进行单个选取，选取规则是dom树，如：html.head.title
方式2：使用函数数获取单个或全部，find_all,find,直接传入要查找的标签名，可在参数中加入
限制条件（对标签基于对属性的筛选），需要指名参数，如class_='title'，或不指名传入列表{'id':1},
方式3 使用select函数直接等同于css选择 如：div li,类：.user,id:#user
'''
html=requests.get('http://cms15')
html=BeautifulSoup(html.text,'lxml')
print(html.head.meta['charset'])
print("================================")
print(html.head.title.text)
print("================================")
print(html.string)#使用string获取失败，使用text获取全部
print("=================================")
res=html.find_all('a')
for i in res:
    print(i['href'])
print("=================================")
res1=html.find('a')
print(res1['href'])
print("================================")
res2=html.find_all('div',{'id':1},class_='title')
print(res2)
print("================================")
res3=html.select('div span')
print(res3)