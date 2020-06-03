import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("123.56.12.53",2346))

client.send("hi,i am from python client".encode("utf8"))

print(client.recv(4089))

client.close()

