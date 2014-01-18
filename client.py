#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12393                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
name = raw_input("What do you like to be called?  ")
print "Sending name..."
s.send(name)
print "Name sent."
print s.recv(1024)
s.close                     # Close the socket when done
print ("connection closed for server " + str(s))
