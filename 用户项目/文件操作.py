# f=open("txt/1.txt",encoding="utf-8")
# content=f.read(10)
#
# # content=f.readlines()
# print(content)
# f.close()
#
# f=open("txt/1.txt",encoding="utf-8",mode="a")
# f.write(content)
# f.close()

# f=open("txt/2.txt",mode="w",encoding="utf-8")
# f.write("hack for test\n 这是一个演示")
# f.close()

with open("txt/3.csv",mode="r",encoding="utf-8") as f:
    data=f.readlines()
    list=[]
    for i in range(1,len(data)):
        string=data[i].strip()
        infolist=string.split(",")
        username=infolist[0]
        password=infolist[1]
        phone=infolist[2]
        allinfo={"username":username,"password":password,"phone":phone}
        list.append(allinfo)
    print(list)

