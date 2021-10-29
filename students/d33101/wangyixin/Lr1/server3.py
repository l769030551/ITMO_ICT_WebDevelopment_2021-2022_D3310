import socket

conn = socket.socket()
conn.bind(('127.0.0.3', 59498))
conn.listen()

while True:
    conn, addr = conn.accept()
    data = conn.recv(16384)
    response_type = 'HTTP/1.1 200 OK\n'
    headers = 'Content-Type: text/html\n\n'

    with open('Python Socket - Python network programming with sockets.html', 'r') as file:
        body = file.read()
    response = response_type + headers + body
    conn.send(response.encode('utf-8'))
    conn.close()
