import socket
import math
conn = socket.socket()
conn.connect(("127.0.0.1", 59498))

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

answ = ' '.join([str(a), str(b), str(c)]).encode()
conn.send(answ)

print(conn.recv(16384).decode('utf-8'))

conn.close()