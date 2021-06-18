from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# set constants
HOST = ''
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)
QUIT_MSG = "{quit}"

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

clients = {} # empty dictionary for client list

# our 'main' threaded function to accept new clients
def accept_new_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        # send a message for the new connection
        send_msg = 'Type your name and press enter!'
        client.send(send_msg.encode())
        # start the client handler Thread
        Thread(target=handle_client, args=(client,)).start()

# each client has it's own threaded function
def handle_client(client):
    name = client.recv(BUFSIZ).decode()
    # send a welcome message
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(welcome.encode())
    # send a message to everyone else
    msg = "%s has joined the chat!" % name
    broadcast(msg)
    # add new connection to clients
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ).decode()
        # if our connection isn't quitting, broadcast their message to everyone
        if msg != QUIT_MSG:
            send_msg = name+": "+msg
            broadcast(send_msg)
        else:
            # if they quit, bounce the quit message back to them
            client.send(QUIT_MSG.encode())
            # close the connection & delete them from clients
            client.close()
            del clients[client]
            left_msg = "%s has left the chat." % name
            broadcast(left_msg)
            break

# send msg to all clients
def broadcast(msg):
    for sock in clients:
        sock.send(msg.encode())

# start and run our server
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_new_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()