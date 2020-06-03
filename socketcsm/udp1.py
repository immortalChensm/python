import socket
import time
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sk.connect(("127.0.0.1",1234))

while True:
    sk.send("jackcsm is boss".encode("utf8"))
    time.sleep(1)
