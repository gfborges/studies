from socket import AF_INET, socket, SOCK_STREAM
SERVER = '127.0.0.1'
PORT = 5002
tcp = socket(AF_INET, SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
BUFFSIZ = 1024
if __name__ == '__main__':
    while True:
       msg = tcp.recv(BUFFSIZ).decode()
       print(msg)
