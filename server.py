#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12393                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   s.listen(5)              # Wait for a second client
   c2, addr2 = s.accept()
   if c and addr:
       print '(Client 1: Got connection from ', addr
       c.send('Thank you for connecting')
   if c2 and addr2:
       print '(Client 2: Got connection from ', addr2
       c2.send('Thank you for connecting as well')

while True:
    print "Asking client for name..."
    name = c.recv(1024)
    if name:
        c.send("Nice to meet you " + name)
        break


print "about to close..."
c.close()                  # Close the connection
print ("connection closed for " + str(addr))
