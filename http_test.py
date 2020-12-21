"""
获取http 请求和响应
"""


from socket import *

s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr=s.accept()# 等待链接
print('connect from',addr)

data=c.recv(1024*10)
print(data.decode())
response="""HTTP/1.1 200 OK
Content-Type:text/html;charset=utf-8

HEllo World

你好,世界
"""
c.send(response.encode())
c.close()
s.close()