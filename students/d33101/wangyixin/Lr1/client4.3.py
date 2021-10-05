import socket
import threading

name = input("put your name: ")

conn = socket.socket()
conn.connect(('127.0.0.2', 59498))

def run():
    while True:
        message = conn.recv(16384).decode("utf-8")
        if message == 'name':
            conn.send(name.encode('utf-8'))
        else:
            print(message)

def send():
    while True:
        message = input()
        conn.send(f'{name} : {message}'.encode('utf-8'))

run_thread = threading.Thread(target=run)
run_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()