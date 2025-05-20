import socket
soc=socket.socket()
soc.connect(('127.0.0.1',9999))
while True:
    message=input("请输入要发送的消息：")
    soc.send(message.encode())
    dat=soc.recv(10240).decode('utf-8')
    print(dat)