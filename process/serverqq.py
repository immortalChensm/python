import socket
import threading
import os
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8090))
server.listen(5)
print("等待客户端连接中...")

while True:
    client,address = server.accept()
    clientinfo = str(str(address[0]) + ":" + str(address[1]))
    data = client.recv(1024)
    print("客户端[%s]:%s" % (clientinfo, data.decode("utf8")))
    client.send(data)