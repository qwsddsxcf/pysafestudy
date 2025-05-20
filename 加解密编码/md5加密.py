import hashlib
'''
需要加密二进制数据，md5用于表示身份唯一
在输出时转换为十六进制格式
'''
str="weizhi 黑客"
str2="weizhi黑客"
houstr=hashlib.md5(str.encode()).hexdigest()
houstr2=hashlib.md5(str2.encode()).hexdigest()
print(houstr)
print(houstr2)
'''
md5不可逆加密算法
f31fcb96bee4fb4e065153aa0b311cb6
a183bbbfdc574deea31ceed2769065cf

以下是计算文件md5哈希值
'''
with open("2.jpg", 'rb') as f:
    data=f.read()
    md5=hashlib.md5(data).hexdigest()
    print(md5)