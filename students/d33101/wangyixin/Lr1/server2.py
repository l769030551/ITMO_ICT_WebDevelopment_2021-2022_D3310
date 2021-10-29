import socket
import math

conn = socket.socket()
conn.bind(('127.0.0.1', 59498))
conn.listen()

conn, addr = conn.accept()
data = conn.recv(16384).decode('utf-8')
a, b, c = map(float, data.lstrip().rstrip().split())

def quadratic(a, b, c):
    if a == 0:
        return -c/b
    elif b*b - 4*a*c < 0:
        return None
    elif b*b - 4*a*c == 0:
        return -b/(2*a)
    else:
        return (-b -math.sqrt(b*b - 4*a*c))/(2*a), (-b + math.sqrt(b*b - 4*a*c))/(2*a)

answ = str(quadratic(a, b, c)).encode()
conn.send(answ)

conn.close()

