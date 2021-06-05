import socket

addr = ""
port = 5555
#set up our socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((addr, port))
except socket.error as e:
    print(e)
s.listen()
print('Server running, waiting for connection')
conn, raddr = s.accept()

while True:
    msg = conn.recv(1024).decode()
    print('Received:', msg)

    data = input('enter your message\n:>')
    conn.send(data.encode())