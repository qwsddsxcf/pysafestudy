import requests
# result=requests.get("http://www.gqsoso.com/")
# result.encoding="utf-8"
# print(result.text)
# print(result.headers)

# result=requests.get("http://image.cns.com.cn/xinjiang_editor/transform/20250409/fWRC-heqkzvr4031436.jpg")
# with open("img/1.jpg","wb") as f:
#     f.write(result.content)

#data={"name":"fileToUpload"}
'''
multipart/form-data
此为标准的文件上传格式，py在有file时会默认使用此参数，标准格式如下：
------WebKitFormBoundaryWT2jz2PLQvBdTBBO
Content-Disposition: form-data; name="fileToUpload"; filename="QQ20250316-113916.png"
Content-Type: image/png
常规传递数据时运用列表，出现文件上传时，建议列表中的values是一个元组，如下写法
输出返回值res.text,此为非二进制数据
res.content,二进制数据，用于文件下载，如上
res.headers,返回的数据头
heards参数可自定义，参考下面自定义ua头
cookies返回set-cookie响应头的内容，也可用于请求时携带的参数
'''
#http://test/xiaodi73/1.php
# test=requests.get('http://test/xiaodi73/1.php')
# print(test.cookies)
# heads={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15 Edg/134.0.0.0"}
# files = {
#     'fileToUpload': (
#         'QQ20250316-113916.png',  # 文件名
#         open('img/1.jpg', 'rb'),  # 文件对象
#         'image/png'  # 文件类型
#     )
# }
# data={"hack":"hack"}
# result=requests.post('http://test/xiaodi73/upload.php',files=files,data=data,headers=heads,cookies=test.cookies)
# print(result.text)
'''
以下是使用session自动管理cookie,即用户凭证，将像浏览器一样自动保存发送
'''
sess=requests.Session()
res=sess.get('http://test/xiaodi73/1.php')
print(res.headers)
heads={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15 Edg/134.0.0.0"}
files = {
    'fileToUpload': (
        'QQ20250316-113916.png',  # 文件名
        open('img/1.jpg', 'rb'),  # 文件对象
        'image/png'  # 文件类型
    )
}
res2=sess.post('http://test/xiaodi73/upload.php',files=files,headers=heads)
print(res2.text)
'''
在使用https时忽略证书验证，即不信任的证书
'''
sess.get("https://www.baidu.com",headers=heads,verify=False)