import socket
import threading
import os
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8090))
server.listen(5)
print("等待客户端连接中...")
userName = {}
def run(client,address):
    clientinfo = str(str(address[0]) + ":" + str(address[1]))
    username = client.recv(1024)

    userName[username.decode("utf8")] = client

    while True:
        msg = client.recv(1024)
        
        group = msg.decode("utf8")
        to = group.split(":")[0]
        content = group.split(":")[1]
        send = str(to)+":"+content
        userName[to].send(send.encode("utf8"))

while True:
    client,address = server.accept()
    weclome = ""

    for who in userName.values():
        weclome+="欢迎进入py世界目前有"+"".join(userName.keys())+",总有"+str(len(userName))+"人连接"

        who.send(weclome.encode("utf8"))
    client.send(weclome.encode("utf8"))
    t = threading.Thread(target=run,args=(client,address))
    t.start()
