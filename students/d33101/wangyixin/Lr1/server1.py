import socket

server = socket.socket()

server.bind(("127.0.0.1", 59498))
server.listen()

conn, addr = server.accept()

print(conn.recv(16384).decode("utf-8"))

conn.send(b'Hello, client\n')
conn.close()
