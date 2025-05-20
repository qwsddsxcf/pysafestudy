import rsa
from binascii import b2a_hex
'''
这是rsa加密全过程，加密：输入二进制，得到不可解码的二进制
解密：输入不可解码的二进制，得到可解码的二进制数据
b2a_hex函数，让二进制数据输出时已十六进制的格式显示
decode如果参数是十六进制，则只是转换为字符串形式，并不解码
'''
public,private=rsa.newkeys(2048)
print(public,private)
print("=================================")
'''
以上是获取公钥私钥
以下是加密过程
'''
mingwen="hello weizhi hack你好".encode()
miwen=rsa.encrypt(mingwen,public)
print(miwen)
print("===================================")
print(b2a_hex(miwen).decode("utf-8"))
'''
以下是解密过程
'''
jiemi=rsa.decrypt(miwen,private)
print(jiemi.decode("utf-8"))