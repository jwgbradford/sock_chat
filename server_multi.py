import socket
from threading import Thread

def threaded_client(conn, user):    
    while True:
        try:
            recv_msg = conn.recv(1024).decode()
            if not recv_msg:
                print("Disconnected")
                break
        except:
            break
        msg_list[user] = recv_msg
        send_msg = msg_list[1 - user]
        conn.send(send_msg.encode())
    print("Lost connection")
    conn.close()

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
msg_list = ["user 1 connected", "user 2 connected"]
user = 0
while True:
    conn, raddr = s.accept()
    x = Thread(target=threaded_client, args=(conn, user))
    x.start()
    user += 1