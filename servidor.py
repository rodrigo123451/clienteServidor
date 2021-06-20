#servidor
from socket import *
addr = ("localhost", 6666)
srvSock = socket(AF_INET, SOCK_STREAM)
srvSock.bind(addr)
srvSock.listen()
while True:
    cliSock, addr = srvSock.accept()
    print ('...conexion recibida')
    data = cliSock.recv(200)
    cliSock.send(b"Resp: " + data)
    cliSock.close()
srvSock.close()
