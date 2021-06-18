from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

# set CONSTANTS
HOST = "192.168.0.92"
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect(ADDR)

# set up socket functions

# this function is threaded so it 'listens' for any new messages
# and updates the ktinter msg_list
def receive():
    while True:
        try:
            msg = CLIENT_SOCKET.recv(BUFSIZ).decode()
        except OSError:
            break
        if msg == "{quit}":
            CLIENT_SOCKET.close()
            top.quit()
        msg_list.insert(tkinter.END, msg)

# simple send function, called from <Return> or our 'send' button
def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    CLIENT_SOCKET.send(msg.encode())

# close tkinter
def on_closing(event=None):
    my_msg.set("{quit}")
    send()

# set up tkinter
top = tkinter.Tk()
top.title('My third chat app')

# we use a Frame to group our messages and the scroll bar
messages_frame = tkinter.Frame(top)
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages_frame.pack()

# we need a String Variable to hold our message to send
my_msg = tkinter.StringVar()
my_msg.set('Type here to send.')
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind('<Return>', send) # send on <Return>
entry_field.pack()

# send on button click
send_button = tkinter.Button(top, text='Send', command=send)
send_button.pack()

# close tkinter on 'x' click
top.protocol('WM_DELETE_WINDOW', on_closing)

# begin Threading, and start tkinter
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()