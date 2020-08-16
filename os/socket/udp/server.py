from socket import socket, AF_INET, SOCK_DGRAM
# como o usaremos a rede local HOST é fazio
HOST = ''
# porta que usaremos para passar informação
# A MESMA QUE O ARQ client.py
PORT = 5002
# conexão udp da familia AF _INET (HOST, PORT)
udp = socket(AF_INET, SOCK_DGRAM)
# unindo a conexão com a porta
orig = (HOST, PORT)
udp.bind(orig)
# Sanity check
print(f'Server udp rodando na porta {PORT}')
while True:
    # mesagem e origem da mensagem
    msg, cli = udp.recvfrom(1024)
    # log de transaçãoes
    print(cli, msg)
# fecha a conexão
udp.close()
