"""
获取http 请求和响应

Content-Type:image/jpeg 图片
在浏览器上显示一个图片
"""

from socket import *

s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr=s.accept()# 等待链接
print('connect from',addr)
data=c.recv(1024*10)
print(data.decode())
with open("jzmb.jpeg",'rb') as f:
    response="HTTP/1.1 200 OK\r\n"
    response+="Content-Type:image/jpeg\r\n"
    response+="\r\n"
    response=response.encode()+f.read()

c.send(response)
c.close()
s.close()

