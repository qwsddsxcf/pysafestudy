import requests,time,threading
sess=requests.session()
data={'q':"tcp111111","searchtype":"title"}
heads={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15 Edg/134.0.0.0",
       "Referer":"http://192.168.161.128/dedecms/uploads/plus/search.php?q=tcp&searchtype=title",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

def test():
    print(threading.current_thread().name)
    for i in range(5):
        print(i)
        time.sleep(1)
def jisuan(fun):
    def wrapper():
        a=time.time()
        fun()
        b=time.time()
        print(f"当前调用的函数为：{fun.__name__},响应时间：{b-a}")
    return wrapper
'''
使用修饰器来计算函数调用用时，修饰器函数第一层函数默认传入修饰器参数
第二层默认传入要修饰的函数，第三层默认传入要修饰的函数参数

'''
@jisuan
def home():
    res=sess.get("http://192.168.161.128/dedecms/uploads")
    if "织梦CMS" in res.text:
        print("访问成功！")
@jisuan
def search():
    res=sess.get("http://192.168.161.128/dedecms/uploads/plus/search.php?q=tcp&searchtype=title",headers=heads)
    if "搜索页_我的网站" in res.text:
        print("搜索成功")
def hack():
    for i in range(500):
        home()
        search()
#q=tcp&searchtype=title
if __name__ == '__main__':
    for i in range(100):
        threading.Thread(target=hack).start()#多线程方式，直接指定函数链式调用start开始