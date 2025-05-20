import socket,time
soc=socket.socket(type=socket.SOCK_DGRAM)
soc.connect(("192.168.161.142",2425))
id=str(time.time())
name="weizhi"
host="MyHostName"
command=str(0x00000020)
content="test for udp"
message="1.0"+id+":"+name+":"+host+":"+command+":"+content
soc.send(message.encode())