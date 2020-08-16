from socket import socket, AF_INET, SOCK_DGRAM
# conexão local (localhost:5002)
SERVER = '127.0.0.1'
PORT = 5002
# criando socket e o destino
udp = socket(AF_INET, SOCK_DGRAM)
dest = (SERVER, PORT)

# aviso sobre como sair 
# nome para msg de input
print('Para sair aperte C-X')
name = input('nome: ') + ': '
msg = input(name)

while msg != '\x18':
    # manda os binários (encode) para dest (localhost:5002)
    udp.sendto(msg.encode(), dest)
    # Pede por uma nova mensagem
    msg = input(name)
