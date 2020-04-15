import socket
import threading
import sys

if len(sys.argv) != 3:
    print('Usage: $ python3 client.py [server ip] [port]')
HEADER = 16
PORT = int(sys.argv[2])
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = sys.argv[1]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except:
    print('Invalid server')
    quit()


def send(msg):  # send a message
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def receivemsgs():  # thread to receive messages
    global con
    global HEADER
    global FORMAT
    while con:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(msg)


con = True
thread = threading.Thread(target=receivemsgs, args=())
thread.start()
while con:
    msg = input()
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        con = False
