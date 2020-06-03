import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("123.56.12.53",2346))

client.send("hi".encode("utf8"))

data = client.recv(8190)

print(data)