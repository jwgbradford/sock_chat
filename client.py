import socket

server = "192.168.0.92"
port = 5555
#set up our socket object 
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

while True:
    data = input('enter your message\n:>')
    conn.send(data.encode())
    print('waiting for reply\n')
    print('received\n', conn.recv(1024).decode())