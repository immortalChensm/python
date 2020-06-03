import socket


while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("127.0.0.1", 8090))

    data = str(input()).encode("utf8")
    if data.decode("utf8") == 'close':
        client.close()
    if data:
        client.send(data)
    recv = client.recv(1024)
    print("服务器返回的数据："+recv.decode("utf8")+"\r\n")
