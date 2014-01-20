#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12387                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
name = raw_input("What do you like to be called?  ")
print "Sending name..."
s.send(name)
print "Name sent."
print s.recv(1024)

while True:
    closeInput = raw_input("Enter close if you want to close connection:  ")
    if closeInput == "close":
        s.close                     # Close the socket when done
        print ("connection closed for server " + str(s))
        break
