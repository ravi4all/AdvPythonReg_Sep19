import socket

s = socket.socket()
port = 9999
s.connect(('127.0.0.1', port))
data = s.recv(1024)
print(data)
s.close()