import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sk.connect(("www.baidu.com",80))
data = []
sk.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')

while True:
    temp = sk.recv(1024)
    if temp:
        data.append(temp)
    else:
        break

sk.close()
dataStr = (b''.join(data)).decode("utf8")
#print(dataStr)
headers,html = dataStr.split("\r\n\r\n",1)
#print(headers)
print(html)