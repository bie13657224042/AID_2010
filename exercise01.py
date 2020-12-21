from socket import *
from time import sleep,ctime
socket=socket()
socket.bind(("0.0.0.0",8888))
socket.listen(5)
file=open("my.log",'a')
socket.setblocking(False)
while True:
    print("等待接受")
    try:
        connfd,addr=socket.accept()
        print("接受到链接",addr)
    except BlockingIOError as e:
        sleep(3)
        msg="%s : %s\n"%(ctime(),e)
        file.write(msg)
    else:
        data=connfd.recv(1024)
        print(data.decode())
