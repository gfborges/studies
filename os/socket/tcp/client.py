import socket
# conexçao com localhost:5002
SERVER = '127.0.0.1'
PORT = 5002
# criando socker tcp
tcp = socket.socket(socket.AF_INET, 
                    socket.SOCK_STREAM)
# criando no locahost:5002 e conectando
dest = (SERVER, PORT)
tcp.connect(dest)
# msg para input
name = input('nome: ') + ': '
# como sair do chat
print('Para sair use C-X')
msg = input(name)
while msg != '\x18':
    # manda mesagem para o server como bytes
    tcp.send(msg.encode())
    msg = input(name)
print("Saindo...")
tcp.close()

