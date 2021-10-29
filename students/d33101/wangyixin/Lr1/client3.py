import socket

conn = socket.socket()

conn.connect(("127.0.0.3", 59498))
conn.send('html'.encode('utf-8'))

print(conn.recv(16384).decode("utf-8"))

conn.close()