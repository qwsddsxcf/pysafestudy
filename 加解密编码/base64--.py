import base64
'''
编码结果有两种表现形式，一种是原始二进制，一种是字符文本模式
正常变量属于后者（字符串）文件数据属于前者，base64:
将二进制数据，六位为一个转换为英文，+ 补位会转换为=
因此在进行base64编码时先转换为二进制格式，如函数encode()
'''
str="weizhi 黑客"
houstr=base64.b64encode(str.encode())
print(houstr)
print(base64.b64decode(houstr).decode("utf-8"))
'''
b'd2VpemhpIOm7keWuog=='
weizhi 黑客
'''

'''
以下是文件，对文件内容进行编码，再解码转换为图片
'''
with open("2.jpg","rb") as f:
    data=f.read()
    data=base64.b64encode(data)
    print(data)
with open("勒索/4.jpg", "wb") as f:
    f.write(base64.b64decode(data))
