import socket
import threading

HEADER = 64
PORT = 5050
Server = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
ADDR = (Server, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message Received".encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {Server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\n[Active connection] {threading.activeCount() -1}")

print("[Starting] server is starting...")
start()

