import socket
# socket em localhost:5002
HOST = ''
# NÃO MUDAR, O MESMO QUE EM client.py
PORT = 5002
# cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# coloca ele em localhost:5002
orig = (HOST, PORT)
tcp.bind(orig)
# tranforma em um servidor
tcp.listen(2)
# Sanity check
print(f"Server is running on the port {PORT}")
while True:
    # conexão com o cliente
    con, cli = tcp.accept()
    # Log de conexão
    print('Conectado com', cli)
    while True:
        # recebe mensagem do cliente 
        # (com tamanho máximo de 1024B) 
        msg = con.recv(1024)
        # cliente saiu
        if not msg: break
        # log de mensagens
        print(msg)
    # fecha a conexão e log na tela
    print('Finalizando conexao do cliente', cli)
    con.close()
