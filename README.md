# Simple socket-based chat app for python

This mini-project introduces sockets and a very simple client server method.

# Version 1
The first part is to code the server.py and client.py
This gives a server & one client. Both server and client can type messages in and send them back and forth.

# Version 2
This adds threading to the server so that you can have two clients
Still very simple message passing.

# Main constraints
- the other client will only display the last recv'd message - there is no history, so if you type a new message before receiving a reply, that message will over write the one in the list
- only supports two clients
- you have to send a message to see what the other person has typed