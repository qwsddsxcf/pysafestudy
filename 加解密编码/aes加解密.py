from Crypto.Cipher import AES
from binascii import b2a_hex
'''
这是aes加密算法过程，要求偏移量，密钥，加密内容大小（二进制计算下）都必须是16字节的倍数
为什么要在二进制下计算，因为len("你好")是2，但是实际二进制占6字节，所以第一步是是对密文的补位
aes有多种加密模式，cbc是最安全的，存在偏移量，加密解密时不能复用同一对象
以下是补全过程
'''
sour="hello weizhi hack 你好"
if len(sour.encode())%16:
    add=16-len(sour.encode())%16
else:
    add=0
sour=sour+(add*'\0')
print(sour)
'''
以下是加密过程
'''
key="weizhihackweizhi".encode('utf-8')
mode=AES.MODE_CBC
vi="weizhihackweizhi".encode('utf-8')

cry=AES.new(key,mode,vi)
miwen=cry.encrypt(sour.encode('utf-8'))
print(b2a_hex(miwen).decode('utf-8'))
'''
以下是解密过程，创建新的解密对象
'''
cry2=AES.new(key,mode,vi)
jiemi=cry2.decrypt(miwen)
print(jiemi.decode('utf-8').rstrip('\0'))#去除\0符
