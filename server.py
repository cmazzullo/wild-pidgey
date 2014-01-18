#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12393                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   if c and addr:
       print 'Got connection from ', addr
       c.send('Thank you for connecting')
       break

while True:
    print "Asking client for name..."
    name = c.recv(1024)
    if name:
        c.send("Nice to meet you " + name)
        break

print "about to close..."
c.close()                  # Close the connection
print ("connection closed for " + str(addr))

