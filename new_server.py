import socket

server = ""
port = 5555
#set up our socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(e)
print('Server running, waiting for connection')
s.listen()