import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("0.0.0.0",8090))
server.listen(5)
while True:
    socketClient,socketAddress = server.accept()
    data = socketClient.recv(1024)
    if data:
        print("接收到:"+str(socketClient)+"的数据："+data.decode("utf8")+"\r\n")
        socketClient.send(("您说的是:"+str(data.decode("utf8"))).encode("utf8"))
    else:
        print("没有人连接....")

    #socketClient.close()