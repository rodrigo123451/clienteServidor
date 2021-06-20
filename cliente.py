Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #cliente
>>> from socket import *
dest = ('localhost', 21567)
cliSock = socket(AF_INET, SOCK_STREAM)
cliSock.connect(dest)
data = input('> ')
cliSock.send(data.encode("utf-8"))
data = cliSock.recv(200)
print(data.decode("utf-8"))
cliSock.close()