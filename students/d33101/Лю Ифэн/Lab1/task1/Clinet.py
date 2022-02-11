
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 8080))
message = 'Hello , server!'
conn.send(message)
data = conn.recv(1024)
ndata = data.decode('utf-8')
print(ndata)
conn.close()
