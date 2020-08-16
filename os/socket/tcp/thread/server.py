from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from sys import exit
HOST = ''
PORT = 5002
BUFFSIZ = 1024
tcp = socket(AF_INET, SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(3)
ADDRS = {}
CLIENTS = {}

def sendMsg(msg, remetent, prefix=''):
    for con in ADDRS:
        if con != remetent:
            con.send(prefix.encode() + msg)

def connect(tcp):
    con, cli = tcp.accept()
    print('conectado com ', cli)
    ADDRS[con] = cli
    Thread(target=listen, args=(con,)).start()

def listen(con):
    name = con.recv(BUFFSIZ).decode()
    con.send(f'Welcome, {name}!'.encode())
    sendMsg(f'{name} entered the chat'.encode(), con)
    CLIENTS[con] = name
    prefix = f'{name}: '
    while True:
        msg = con.recv(BUFFSIZ)
        if msg == "%exit%": break
        sendMsg(msg, con, prefix)
    con.close()

def close():
    input('Press ENTER to kill server')
    con.close()
    exit(0)

if __name__ == "__main__":
    Thread(target=close).start()
    while True:
        connect(tcp)
