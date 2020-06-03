import socket
import threading
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8090))

def run():
    global client
    recv = client.recv(1024)
    print(recv.decode("utf8")+'\r\n')

while True:

    t = threading.Thread(target=run)
    t.start()
    data = str(input(""))
    client.send(data.encode("utf8"))

