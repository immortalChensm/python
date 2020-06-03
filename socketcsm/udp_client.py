import socket

udp_cliet = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input("请输入数据")
    udp_cliet.sendto(str(data).encode("utf8"),("127.0.0.1",8090))
    #info = udp_cliet.recv(1024)
    #print("服务器："+info.decode("utf8"))