#!/usr/bin/python3

import socket
import random

class webApp:

    def parse(self, request):
        return None

    def process(self, parsedRequest):
        num_aleat = random.randint(1, 100000)
        return ("200 OK", "<html><body><a href='" + str(num_aleat) +
"'>Dame otra</a></body></html>")

    def __init__(self, hostname, port):

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048)
            print(request.decode('utf-8'))
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)
