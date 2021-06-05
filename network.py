import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = "192.168.0.92"
        port = 5555    
        self.client.connect((server, port))

    def send(self, data):
        try:
            self.client.send(data.encode())
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return self.client.recv(1024).decode()
        except socket.error as e:
            print(e)
            return e