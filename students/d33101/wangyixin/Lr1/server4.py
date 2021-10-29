import socket
import threading

conn = socket.socket()
conn.bind(('127.0.0.2', 59498))
conn.listen()
clients = []
names = []

def chat(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        message = client.recv(16384)
        chat(message)


def receive():
    while True:
        client, addr = conn.accept()
        client.send('name'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        clients.append(client)
        names.append(name)

        handle_thread = threading.Thread(target=handle, args=(client,))
        handle_thread.start()

receive()