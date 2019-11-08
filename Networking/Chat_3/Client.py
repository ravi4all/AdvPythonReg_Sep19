import socket
import json

def Main():
    host = '192.168.1.27'
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
        data = mySocket.recv(1000000)

        if isinstance(data,bytes):
            file = open('file_1.jpg', 'wb')
            file.write(data)
            file.close()
        else:
            data = data.decode()
            print('Received from server: ' + data)
        # print(type(data))
        message = input(" -> ")

    mySocket.close()


if __name__ == '__main__':
    Main()