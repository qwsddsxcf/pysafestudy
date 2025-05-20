import string
strdaxie=string.ascii_uppercase
strxiaoxie=string.ascii_lowercase
print(strdaxie)
print(strxiaoxie)
'''
该代码实现对大小写英文字母实现两次自定义加密
两次加密方式分别是凯撒加密（偏移量5），大小写反转
通过string.ascii_lowercase获取大小写字符串
加解密过程数据都是字符串形式
'''
def kaisajiami(sour):
    data=''
    for i in sour:
        if i in strdaxie:
            index=(strdaxie.index(i)+5)%26#防止溢出取余，这对负数也同样适用
            data=data+strdaxie[index]
        elif i in strxiaoxie:
            index=(strxiaoxie.index(i)+5)%26
            data=data+strxiaoxie[index]
        else:
            print("不被允许加密的字符")
    return data

def fanzhuan(sour):
    data=''
    for i in sour:
        if ord(i)>=97 and ord(i)<=122:
            data+=chr(ord(i)-32)
        elif ord(i)>=65 and ord(i)<=90:
            data+=chr(ord(i)+32)
        else:
            print("不被允许的加密字符")
    return data

def jiemikasa(sour):
    data = ''
    for i in sour:
        if i in strdaxie:
            index = (strdaxie.index(i) - 5) % 26
            data = data + strdaxie[index]
        elif i in strxiaoxie:
            index = (strxiaoxie.index(i) - 5) % 26
            data = data + strxiaoxie[index]
        else:
            print("不被允许解密的字符")
    return data


if __name__=='__main__':
    mingwen="weizhihack"
    miwen=fanzhuan(kaisajiami(mingwen))
    print(miwen)
    jiemi=fanzhuan(jiemikasa(miwen))
    print(jiemi)