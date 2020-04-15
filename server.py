import socket
import threading  # create multiple threads in one program
import sys

if len(sys.argv) != 2:
    print('Usage: $ python3 server.py [port]')
    quit()
HEADER = 16
PORT = int(sys.argv[1])  # port to listen on
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# What type of IP Address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
users = {}  # holds users in format ADDR: [username, socket obj]


def handle_client(conn, addr):  # thread to handle one client
    global users
    intro = users.get(addr, [addr])[0]
    sendmsg('SERVER', f'{intro} joined the channel')
    del intro
    if addr not in list(users.keys()):
        print(f'[NEW CONNECTION] {addr} connected.')
        send(conn, 'What is your desired username?')
        msg_length = conn.recv(HEADER).decode(FORMAT)
        print(msg_length)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            users[addr] = [msg, conn]
            sendmsg('SERVER', f'{addr} changed name to {users[addr][0]}')
    else:
        print(f'{users[addr][0]} connected')
    username = users.get(addr, ['default', 'default'])[0]
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                sendmsg('SERVER', f'{username} is disconnecting...')
                connected = False
                break
            print(f'[{username}] {msg}')
            sendmsg(username, msg)
    conn.close()


def sendmsg(username, msg):  # sends a message to EVERYONE
    msg = f'[{username}] {msg}'
    for client in users.keys():
        send(users[client][1], msg)


def send(conn, msg):  # sends a message to one client
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)


def start():  # init
    server.listen()
    print(f'[LISTENING] SERVER is listening on {SERVER}')
    while True:
        conn, addr = server.accept()  # waits until new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


print('[STARTING] server is starting...')
start()
