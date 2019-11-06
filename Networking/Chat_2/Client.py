import socket
import json

def Main():
    host = 'localhost'
    port = 80

    mySocket = socket.socket()
    mySocket.connect((host, port))

    name = input(" Enter name : ")
    message = ""
    while message != 'q':
        toSend = {"name":name,"message":message}
        toSend = json.dumps(toSend)
        # mySocket.send(message.encode())
        mySocket.send(toSend.encode())
        data = mySocket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" -> ")

    mySocket.close()


if __name__ == '__main__':
    Main()