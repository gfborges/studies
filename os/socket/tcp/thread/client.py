from socket import socket, AF_INET, SOCK_STREAM

SERVER = '127.0.0.1'
PORT = 5002
BUFFSIZ = 1024
tcp = socket(AF_INET, SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)

def send():
    msgs = ''
    while msgs != '%exit%':
        msgs = input(name+': ')
        tcp.send(msgs.encode())
    tcp.close()

if __name__ == "__main__":
    name = input('Choose a nickname: ')
    tcp.send(name.encode())
    send()

