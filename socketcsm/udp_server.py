import socket
#socket.AF_INET ip协议  有ipv4 ipv6 socket.SOCK_DGRAM SOCK_STREAM  基于数据流传输
udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind(("127.0.0.1",8090))

while True:
    data,addr = udpserver.recvfrom(1024)
    #print("客户端："+data.decode("utf8"))
    #print(data[0].decode("utf8"))
    print("客户端:"+data.decode("utf8"))
    #info = input("请输入东西：")
    #udpserver.sendto(str(info).encode("utf8"),addr)